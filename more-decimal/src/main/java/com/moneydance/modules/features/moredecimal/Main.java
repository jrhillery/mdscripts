/*
 * Created on May 3, 2020
 */
package com.moneydance.modules.features.moredecimal;

import com.infinitekind.moneydance.model.CurrencyType;
import com.moneydance.apps.md.controller.FeatureModule;

/**
 * Module used to change the number of decimal places in a Moneydance security.
 */
public class Main extends FeatureModule {
	private MoreDecimalWindow decimalWindow = null;
	private DecimalChanger decimalChanger = null;

	/**
	 * Register this module to be invoked via the extensions menu.
	 *
	 * @see com.moneydance.apps.md.controller.FeatureModule#init()
	 */
	public void init() {
		getContext().registerFeature(this, "domoredecimal", null, getName());

	} // end init()

	/**
	 * This is called when this extension is invoked.
	 *
	 * @see com.moneydance.apps.md.controller.FeatureModule#invoke(java.lang.String)
	 */
	public void invoke(String uri) {
		System.err.println(getName() + " invoked with uri [" + uri + ']');
		showWindow();

		this.decimalChanger = new DecimalChanger(this.decimalWindow,
			getContext().getCurrentAccountBook());

	} // end invoke(String)

	/**
	 * Change the specified security to a new number of decimal places.
	 */
	void changeDecimals() {
		try {
			synchronized (this.decimalChanger) {
				this.decimalWindow.clearText();
				this.decimalChanger.forgetChanges();
				CurrencyType origSecurity = this.decimalWindow.getSecurity();
				int newDecimals = this.decimalWindow.getNewDecimals();
				this.decimalChanger.changeDecimals(origSecurity, newDecimals);
			}
			this.decimalWindow.enableCommitButton(this.decimalChanger.isModified());
		} catch (Throwable e) {
			handleException(e);
		}

	} // end changeDecimals()

	/**
	 * This is called when the commit button is selected.
	 */
	void commitChanges() {
		try {
			synchronized (this.decimalChanger) {
				this.decimalChanger.commitChanges();
			}
			this.decimalWindow.disableActions();
		} catch (Throwable e) {
			handleException(e);
		}

	} // end commitChanges()

	private void handleException(Throwable e) {
		this.decimalWindow.addText(e.toString());
		this.decimalWindow.enableCommitButton(false);
		e.printStackTrace(System.err);

	} // end handleException(Throwable)

	public void cleanup() {
		closeWindow();

	} // end cleanup()

	public String getName() {

		return "More Decimal";
	} // end getName()

	/**
	 * Show our window.
	 */
	private synchronized void showWindow() {
		if (this.decimalWindow == null) {
			this.decimalWindow = new MoreDecimalWindow(this,
				getContext().getCurrentAccountBook().getCurrencies());
			this.decimalWindow.setVisible(true);
		} else {
			this.decimalWindow.setVisible(true);
			this.decimalWindow.toFront();
			this.decimalWindow.requestFocus();
		}

	} // end showWindow()

	/**
	 * Close our window and release resources.
	 */
	synchronized void closeWindow() {
		if (this.decimalWindow != null)
			this.decimalWindow = this.decimalWindow.goAway();

		if (this.decimalChanger != null)
			this.decimalChanger = this.decimalChanger.releaseResources();

	} // end closeWindow()

} // end class Main
