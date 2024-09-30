/*
 * Created on May 10, 2020
 */
package com.moneydance.modules.features.moredecimal;

import static com.infinitekind.moneydance.model.Account.AccountType.INVESTMENT;
import static com.moneydance.modules.features.moredecimal.MoreDecimalWindow.baseMessageBundleName;
import static java.time.format.FormatStyle.MEDIUM;

import java.math.BigDecimal;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.ResourceBundle;

import com.infinitekind.moneydance.model.AbstractTxn;
import com.infinitekind.moneydance.model.Account;
import com.infinitekind.moneydance.model.AccountBook;
import com.infinitekind.moneydance.model.AccountUtil;
import com.infinitekind.moneydance.model.CurrencyType;
import com.infinitekind.moneydance.model.ParentTxn;
import com.infinitekind.moneydance.model.SplitTxn;
import com.infinitekind.moneydance.model.TransactionSet;
import com.leastlogic.moneydance.util.MdUtil;

/**
 * Module used to change the number of decimal places for a Moneydance security.
 */
public class DecimalChanger {
	private MoreDecimalWindow decimalWindow;
	private Locale locale;
	private AccountBook book;
	private TransactionSet txnSet;

	private CurrencyType security = null;
	private int newDecimalPlaces = 0;
	private int rightMovePlaces = 0;
	private int numAcnts = 0;
	private ArrayList<TransactionHandler> changeTxns = new ArrayList<>();
	private ResourceBundle msgBundle = null;

	private static final DateTimeFormatter dateFmt = DateTimeFormatter.ofLocalizedDate(MEDIUM);

	/**
	 * Sole constructor.
	 *
	 * @param decimalWindow
	 * @param accountBook Moneydance account book
	 */
	public DecimalChanger(MoreDecimalWindow decimalWindow, AccountBook accountBook) {
		this.decimalWindow = decimalWindow;
		this.locale = decimalWindow.getLocale();
		this.book = accountBook;
		this.txnSet = accountBook.getTransactionSet();

	} // end (MoreDecimalWindow, AccountBook) constructor

	/**
	 * Change the specified security to a new number of decimal places.
	 *
	 * @param security
	 * @param newDecimalPlaces
	 */
	public void changeDecimals(CurrencyType security, int newDecimalPlaces) {
		this.security = security;
		this.newDecimalPlaces = newDecimalPlaces;
		this.rightMovePlaces = newDecimalPlaces - security.getDecimalPlaces();
		String securityName = security.getName();

		if (this.rightMovePlaces == 0) {
			// No changes needed. %s already has %d decimal places.
			writeFormatted("MDC02", securityName, newDecimalPlaces);
		} else {
			boolean allAccountsGood = true;
			List<Account> invAccounts = MdUtil.getAccounts(this.book, INVESTMENT);

			for (Account investAcnt : invAccounts) {
				Account securityAcnt = MdUtil.getSubAccountByName(investAcnt, securityName);

				if (securityAcnt != null) {
					allAccountsGood &= saveAccntToChanges(securityAcnt, investAcnt);
				}
			} // end for

			if (!allAccountsGood) {
				forgetChanges();
			}
		}

	} // end changeDecimals(CurrencyType, int)

	/**
	 * @param securityAccount
	 * @param investAccount
	 * @return true when all transactions can change decimals as requested
	 */
	private boolean saveAccntToChanges(Account securityAccount, Account investAccount) {
		boolean accountGood = false;
		int txnDate = 0;
		try {
			int txnCount = 0;
			List<AbstractTxn> txnLst = this.txnSet.getTxnsForAccount(securityAccount);

			for (AbstractTxn txn : txnLst) {
				if (txn instanceof SplitTxn) {
					txnDate = txn.getDateInt();
					saveTxnToChange((SplitTxn) txn, securityAccount, txnDate);
					++txnCount;
				} else {
					// WARNING: Found unexpected transaction in %s: %s.
					writeFormatted("MDC03", securityAccount.getFullAccountName(), txn);
				}
			} // end for
			// Verified and staged %d relevant transactions in %s account.
			writeFormatted("MDC04", txnCount, investAccount.getAccountName());
			++this.numAcnts;
			accountGood = true;
		} catch (ArithmeticException e) {
			// expect exception came from longValueExact call
			// %s with %d decimal places for security %s on %s.
			String txnDateStr = MdUtil.convDateIntToLocal(txnDate).format(dateFmt);
			writeFormatted("MDC05", e.getMessage(), this.newDecimalPlaces,
				securityAccount.getFullAccountName(), txnDateStr);
		}

		return accountGood;
	} // end saveAccntToChanges(Account, Account)

	/**
	 * @param sTxn
	 * @param securityAccount
	 * @param txnDate
	 */
	private void saveTxnToChange(SplitTxn sTxn, Account securityAccount, int txnDate)
			throws ArithmeticException {
		// verify shares fits with new decimals
		BigDecimal shares = BigDecimal.valueOf(sTxn.getValue());
		shares = shares.movePointRight(this.rightMovePlaces);
		long newShares = shares.longValueExact();

		// verify balance fits with new decimals
		BigDecimal balance = BigDecimal.valueOf(
			AccountUtil.getBalanceAsOfDate(this.book, securityAccount, txnDate));
		balance.movePointRight(this.rightMovePlaces).longValueExact();

		// good to go; save for commit
		this.changeTxns.add(new TransactionHandler(sTxn, newShares));

	} // end saveTxnToChange(SplitTxn, Account, int)

	/**
	 * Commit any changes to Moneydance.
	 */
	public void commitChanges() {
		// Change the specified security to the new number of decimal places.
		this.security.setEditingMode();
		this.security.setDecimalPlaces(this.newDecimalPlaces);
		this.security.syncItem();

		for (TransactionHandler txnHandler : this.changeTxns) {
			// change this transaction to the new number of decimal places
			txnHandler.applyUpdate();
		} // end for

		// Changed a total of %d transaction%s in %d account%s.
		// Security %s now has %d decimal places
		int txns = this.changeTxns.size();
		writeFormatted("MDC08", txns, sUnless1(txns), this.numAcnts, sUnless1(this.numAcnts),
			this.security.getName(), this.newDecimalPlaces);

		forgetChanges();

	} // end commitChanges()

	/**
	 * @param num
	 * @return the letter 's' unless num is 1
	 */
	private static String sUnless1(int num) {

		return num == 1 ? "" : "s";
	} // end sUnless1(int)

	/**
	 * Class to hold on to, and perform, a transaction change (security and share
	 * balance).
	 */
	private static class TransactionHandler {
		private SplitTxn txn;
		private long newShares;

		/**
		 * Sole constructor.
		 *
		 * @param txn
		 * @param newShares
		 */
		public TransactionHandler(SplitTxn txn, long newShares) {
			this.txn = txn;
			this.newShares = newShares;

		} // end (SplitTxn, long) constructor

		/**
		 * Change the share balance.
		 */
		public void applyUpdate() {
			ParentTxn pTxn = this.txn.getParentTxn();
			pTxn.setEditingMode();
			this.txn.setAmount(this.newShares, this.txn.getAmount());
			pTxn.syncItem();

		} // end applyUpdate()

	} // end class TransactionHandler

	/**
	 * Clear out any pending changes.
	 */
	public void forgetChanges() {
		this.numAcnts = 0;
		this.changeTxns.clear();

	} // end forgetChanges()

	/**
	 * @return True when we have uncommitted changes in memory
	 */
	public boolean isModified() {

		return (this.numAcnts != 0) || !this.changeTxns.isEmpty();
	} // end isModified()

	/**
	 * Release any resources we acquired.
	 *
	 * @return null
	 */
	public DecimalChanger releaseResources() {
		// nothing to release

		return null;
	} // end releaseResources()

	/**
	 * @return Our message bundle
	 */
	private ResourceBundle getMsgBundle() {
		if (this.msgBundle == null) {
			this.msgBundle = MdUtil.getMsgBundle(baseMessageBundleName, this.locale);
		}

		return this.msgBundle;
	} // end getMsgBundle()

	/**
	 * @param key The resource bundle key (or message)
	 * @return Message for this key
	 */
	private String retrieveMessage(String key) {
		try {

			return getMsgBundle().getString(key);
		} catch (Exception e) {
			// just use the key when not found
			return key;
		}
	} // end retrieveMessage(String)

	/**
	 * @param key The resource bundle key (or message)
	 * @param params Optional array of parameters for the message
	 */
	private void writeFormatted(String key, Object... params) {
		this.decimalWindow.addText(String.format(this.locale, retrieveMessage(key), params));

	} // end writeFormatted(String, Object...)

} // end class DecimalChanger
