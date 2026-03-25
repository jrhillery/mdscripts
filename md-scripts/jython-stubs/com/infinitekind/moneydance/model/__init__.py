# encoding: utf-8
# module __init__.py
class AbstractTxn(object):
    # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/AbstractTxn.class
    BANK_TRANSACTION_TYPE = None
    ITEM_KEY_ID = None
    ITEM_KEY_TIMESTAMP = None
    ITEM_TYPE_KEY = None
    PRINT_CHECKNUM_PREFIX = None
    PRINT_CHECKNUM_SUFFIX = None
    SECURITY_SUBTYPES_ITEM_TYPE = None
    SPLIT_TRANSACTION_TYPE = None
    STATUS_CLEARED = None
    STATUS_RECONCILING = None
    STATUS_UNRECONCILED = None
    TAG_FITID_PREFIX = None
    TAG_FI_ID = None
    TAG_INVST_SPLIT_EXP = None
    TAG_INVST_SPLIT_FEE = None
    TAG_INVST_SPLIT_INC = None
    TAG_INVST_SPLIT_SEC = None
    TAG_INVST_SPLIT_TYPE = None
    TAG_INVST_SPLIT_XFR = None
    TAG_INVST_TXN_TYPE = None
    TAG_IS_NEW_TXN = None
    TAG_ONLINE_PMT_ID = None
    TAG_QIF_IMPORT_SESSION = None
    TAG_QIF_INVST_ACTION = None
    TAG_RECON_ASOFDT = None
    TAG_RECON_DATE = None
    TAG_SPLIT_ADDED = None
    TAG_SPLIT_AMOUNT = None
    TAG_SPLIT_CALC = None
    TAG_SPLIT_PAIR = None
    TRANSFER_TYPE_BANK = None
    TRANSFER_TYPE_BUYSELL = None
    TRANSFER_TYPE_BUYSELLXFR = None
    TRANSFER_TYPE_DIVIDEND = None
    TRANSFER_TYPE_DIVIDENDXFR = None
    TRANSFER_TYPE_MISCINCEXP = None
    TRANSFER_TYPE_SHORTCOVER = None

    class ClearedStatus(object):
        # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/AbstractTxn$ClearedStatus.class
        CLEARED = None
        RECONCILING = None
        UNRECONCILED = None
    
        class EnumDesc(object):
        
            def bootstrapArgs(self, ):
                pass
        
            def bootstrapArgsList(self, ):
                pass
        
            def bootstrapMethod(self, ):
                pass
        
            def constantName(self, ):
                pass
        
            def constantType(self, ):
                pass
        
            def equals(self, Object=None):
                pass
        
            def getClass(self, ):
                pass
        
            @staticmethod
            def of(ClassDesc=None, String1=None):
                pass
        
            @staticmethod
            def ofCanonical(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            @staticmethod
            def ofNamed(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            def resolveConstantDesc(self, Lookup=None):
                pass
        
            def toString(self, ):
                pass
    
        def compareTo(self, Enum=None):
            pass
    
        def describeConstable(self, ):
            pass
    
        def equals(self, Object=None):
            pass
    
        def getClass(self, ):
            pass
    
        def getDeclaringClass(self, ):
            pass
    
        def name(self, ):
            pass
    
        def ordinal(self, ):
            pass
    
        @staticmethod
        def statusForByte(byte=None):
            pass
    
        @staticmethod
        def statusForString(String=None):
            pass
    
        def toString(self, ):
            pass
    
        @staticmethod
        def valueOf(Class=None, String1=None):
            pass
    
        @staticmethod
        def values():
            pass

    def __init__(self, AccountBook=None):
        pass

    def addParameters(self, Map=None):
        pass

    def addTags(self, Map=None):
        pass

    @staticmethod
    def decodeKeywordList(String=None):
        pass

    def deleteItem(self, ):
        pass

    def doesParameterExist(self, String=None):
        pass

    def duplicate(self, ):
        pass

    @staticmethod
    def encodeKeywordList(List=None):
        pass

    def equals(self, Object=None):
        pass

    def getAccount(self, ):
        pass

    def getAccountParameter(self, String=None, String1=None, Account2=None):
        pass

    def getAddress(self, ):
        pass

    def getAddressParameter(self, String=None, String1=None, AddressBookEntry2=None):
        pass

    def getAttachmentKeys(self, ):
        pass

    def getAttachmentTag(self, String=None):
        pass

    def getBook(self, ):
        pass

    def getBooleanParameter(self, String=None, boolean1=None):
        pass

    def getCheckNumAsInt(self, ):
        pass

    def getCheckNumAsLong(self, ):
        pass

    def getCheckNumber(self, ):
        pass

    def getClass(self, ):
        pass

    def getClearedStatus(self, ):
        pass

    def getCurrencyParameter(self, String=None, String1=None, String2=None, CurrencyType3=None):
        pass

    def getDateEntered(self, ):
        pass

    def getDateInt(self, ):
        pass

    def getDatePostedOnline(self, ):
        pass

    def getDescription(self, ):
        pass

    def getDoubleParameter(self, String=None, double1=None):
        pass

    def getFIID(self, ):
        pass

    def getFiTxnId(self, int=None):
        pass

    def getIntParameter(self, String=None, int1=None):
        pass

    def getKeywords(self, ):
        pass

    def getLongParameter(self, String=None, long1=None):
        pass

    def getOldTxnID(self, ):
        pass

    def getOriginalItem(self, ):
        pass

    def getOriginalOnlineTxn(self, ):
        pass

    def getOtherTxn(self, int=None):
        pass

    def getOtherTxnCount(self, ):
        pass

    def getParameter(self, String=None, String1=None):
        pass

    def getParameterCount(self, ):
        pass

    def getParameterKeys(self, ):
        pass

    def getParentTxn(self, ):
        pass

    def getPreference(self, String=None, String1=None):
        pass

    def getPreferenceBoolean(self, String=None, boolean1=None):
        pass

    def getPreferenceDouble(self, String=None, double1=None):
        pass

    def getPreferenceInt(self, String=None, int1=None):
        pass

    def getPreferenceIntArray(self, String=None):
        pass

    def getPreferenceLong(self, String=None, long1=None):
        pass

    def getPreferenceStringList(self, String=None):
        pass

    def getPreferenceSublist(self, String=None):
        pass

    def getPreferenceSubset(self, String=None):
        pass

    def getStatus(self, ):
        pass

    def getStatusChar(self, ):
        pass

    def getStringListParameter(self, String=None):
        pass

    def getSyncInfo(self, ):
        pass

    def getSyncItemType(self, ):
        pass

    def getSyncTimestamp(self, ):
        pass

    def getTags(self, ):
        pass

    def getTaxDateInt(self, ):
        pass

    def getTransferType(self, ):
        pass

    def getUUID(self, ):
        pass

    def getValue(self, ):
        pass

    def hasAttachments(self, ):
        pass

    def hasBeenSynced(self, ):
        pass

    def hasKeywordSubstring(self, String=None, boolean1=None):
        pass

    def isDirty(self, ):
        pass

    def isNew(self, ):
        pass

    def isTransferTo(self, Account=None):
        pass

    def itemWasUpdated(self, SyncRecord=None):
        pass

    def itemWillSync(self, SyncRecord=None):
        pass

    def loadFromStorage(self, Map=None):
        pass

    @staticmethod
    def makeSyncableItem(AccountBook=None, SyncRecord1=None):
        pass

    def needsToBePrinted(self, ):
        pass

    def removeAttachmentTag(self, String=None):
        pass

    def removeParameter(self, String=None):
        pass

    def resetDirty(self, ):
        pass

    def setAccount(self, Account=None):
        pass

    def setAccountParameter(self, String=None, String1=None, Account2=None):
        pass

    def setAddress(self, AddressBookEntry=None):
        pass

    def setAddressParameter(self, String=None, String1=None, AddressBookEntry2=None):
        pass

    def setAttachmentTag(self, String=None, File1=None):
        pass

    def setClearedStatus(self, ClearedStatus=None):
        pass

    def setCurrencyParameter(self, String=None, String1=None, String2=None, CurrencyType3=None):
        pass

    def setDescription(self, String=None):
        pass

    def setDirty(self, ):
        pass

    def setEditingMode(self, ):
        pass

    def setFIID(self, String=None):
        pass

    def setFiTxnId(self, int=None, String1=None):
        pass

    def setIsNew(self, boolean=None):
        pass

    def setKeywords(self, List=None):
        pass

    def setOriginalOnlineTxn(self, OnlineTxn=None):
        pass

    def setParameter(self, String=None, boolean1=None):
        pass

    def setParameterNoNotify(self, String=None, String1=None):
        pass

    def setPreference(self, String=None, boolean1=None):
        pass

    def setStatus(self, byte=None):
        pass

    def syncItem(self, ):
        pass

    def toString(self, ):
        pass

    def wasDownloaded(self, ):
        pass

class Account(object):
    # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/Account.class
    ITEM_KEY_ID = None
    ITEM_KEY_TIMESTAMP = None
    ITEM_TYPE_KEY = None
    MONEYBOT_ID_KEY = None
    PARAM_INCLUDE_IN_NET_WORTH = None
    PARAM_QIF_TXNID = None
    PARAM_TAX_RELATED = None
    PARAM_VAT_ACCT = None
    PARAM_VAT_ACCTID = None
    PARAM_VAT_APPLIES = None
    PARAM_VAT_PCT = None
    SECURITY_SUBTYPES_ITEM_TYPE = None
    SPLIT_ACCOUNT_ID = None
    SYNCABLE_TYPE_VALUE = None

    class AccountType(object):
        # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/Account$AccountType.class
        ASSET = None
        BANK = None
        CREDIT_CARD = None
        EXPENSE = None
        INCOME = None
        INVESTMENT = None
        LIABILITY = None
        LOAN = None
        ROOT = None
        SECURITY = None
    
        class EnumDesc(object):
        
            def bootstrapArgs(self, ):
                pass
        
            def bootstrapArgsList(self, ):
                pass
        
            def bootstrapMethod(self, ):
                pass
        
            def constantName(self, ):
                pass
        
            def constantType(self, ):
                pass
        
            def equals(self, Object=None):
                pass
        
            def getClass(self, ):
                pass
        
            @staticmethod
            def of(ClassDesc=None, String1=None):
                pass
        
            @staticmethod
            def ofCanonical(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            @staticmethod
            def ofNamed(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            def resolveConstantDesc(self, Lookup=None):
                pass
        
            def toString(self, ):
                pass
    
        def code(self, ):
            pass
    
        def compareCodeTo(self, AccountType=None):
            pass
    
        def compareTo(self, Enum=None):
            pass
    
        def describeConstable(self, ):
            pass
    
        def equals(self, Object=None):
            pass
    
        def filter(self, ):
            pass
    
        def getClass(self, ):
            pass
    
        def getDeclaringClass(self, ):
            pass
    
        def name(self, ):
            pass
    
        def ordinal(self, ):
            pass
    
        def syncID(self, ):
            pass
    
        def toString(self, ):
            pass
    
        @staticmethod
        def typeForCode(int=None):
            pass
    
        @staticmethod
        def typeForSyncID(String=None):
            pass
    
        @staticmethod
        def valueOf(Class=None, String1=None):
            pass
    
        @staticmethod
        def values():
            pass

    class BalanceType(object):
        # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/Account$BalanceType.class
        CLEARED = None
        CONFIRMED = None
        CURRENT = None
        NORMAL = None
        UNCONFIRMED = None
    
        class EnumDesc(object):
        
            def bootstrapArgs(self, ):
                pass
        
            def bootstrapArgsList(self, ):
                pass
        
            def bootstrapMethod(self, ):
                pass
        
            def constantName(self, ):
                pass
        
            def constantType(self, ):
                pass
        
            def equals(self, Object=None):
                pass
        
            def getClass(self, ):
                pass
        
            @staticmethod
            def of(ClassDesc=None, String1=None):
                pass
        
            @staticmethod
            def ofCanonical(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            @staticmethod
            def ofNamed(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            def resolveConstantDesc(self, Lookup=None):
                pass
        
            def toString(self, ):
                pass
    
        def compareTo(self, Enum=None):
            pass
    
        def describeConstable(self, ):
            pass
    
        def equals(self, Object=None):
            pass
    
        def getClass(self, ):
            pass
    
        def getDeclaringClass(self, ):
            pass
    
        def name(self, ):
            pass
    
        def ordinal(self, ):
            pass
    
        def toString(self, ):
            pass
    
        @staticmethod
        def valueOf(Class=None, String1=None):
            pass
    
        @staticmethod
        def values():
            pass

    class DebtPaymentSpec(object):
        # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/Account$DebtPaymentSpec.class
        CLEARED_BALANCE = None
        CURRENT_BALANCE = None
        FIXED = None
        PERCENTAGE_OF_CLEARED_BALANCE = None
        PERCENTAGE_OF_CURRENT_BALANCE = None
    
        class EnumDesc(object):
        
            def bootstrapArgs(self, ):
                pass
        
            def bootstrapArgsList(self, ):
                pass
        
            def bootstrapMethod(self, ):
                pass
        
            def constantName(self, ):
                pass
        
            def constantType(self, ):
                pass
        
            def equals(self, Object=None):
                pass
        
            def getClass(self, ):
                pass
        
            @staticmethod
            def of(ClassDesc=None, String1=None):
                pass
        
            @staticmethod
            def ofCanonical(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            @staticmethod
            def ofNamed(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            def resolveConstantDesc(self, Lookup=None):
                pass
        
            def toString(self, ):
                pass
    
        def compareTo(self, Enum=None):
            pass
    
        def describeConstable(self, ):
            pass
    
        def equals(self, Object=None):
            pass
    
        def getClass(self, ):
            pass
    
        def getDeclaringClass(self, ):
            pass
    
        def getIDString(self, ):
            pass
    
        def name(self, ):
            pass
    
        def ordinal(self, ):
            pass
    
        def toString(self, ):
            pass
    
        @staticmethod
        def valueForString(String=None):
            pass
    
        @staticmethod
        def valueOf(Class=None, String1=None):
            pass
    
        @staticmethod
        def values():
            pass

    def __init__(self, AccountBook=None):
        pass

    def addParameters(self, Map=None):
        pass

    def addTags(self, Map=None):
        pass

    def adjustStartBalance(self, long=None):
        pass

    def balanceIsNegated(self, ):
        pass

    def canDownloadTxns(self, ):
        pass

    def checkedInitialTransfer(self, ):
        pass

    def compareFullPathToAccount(self, Account=None):
        pass

    def compareToAccount(self, Account=None):
        pass

    @staticmethod
    def decodeKeywordList(String=None):
        pass

    def deleteItem(self, ):
        pass

    def doesParameterExist(self, String=None):
        pass

    def downloadedTxnsUpdated(self, ):
        pass

    def dumpAccounts(self, ):
        pass

    def duplicate(self, ):
        pass

    @staticmethod
    def encodeKeywordList(List=None):
        pass

    def ensureAccountStructure(self, ):
        pass

    def equals(self, Object=None):
        pass

    def getAPR(self, ):
        pass

    def getAPRPercent(self, ):
        pass

    def getAccountByName(self, String=None, AccountType1=None):
        pass

    def getAccountDescription(self, ):
        pass

    def getAccountIsInactive(self, ):
        pass

    def getAccountName(self, ):
        pass

    def getAccountNum(self, ):
        pass

    def getAccountOrParentIsInactive(self, ):
        pass

    def getAccountParameter(self, String=None, String1=None, Account2=None):
        pass

    def getAccountType(self, ):
        pass

    def getAddress(self, ):
        pass

    def getAddressParameter(self, String=None, String1=None, AddressBookEntry2=None):
        pass

    def getAllAccountNames(self, ):
        pass

    def getAnnualFee(self, ):
        pass

    def getBalance(self, BalanceType=None):
        pass

    def getBankAccountNumber(self, ):
        pass

    def getBankName(self, ):
        pass

    def getBankingFI(self, ):
        pass

    def getBillPayFI(self, ):
        pass

    def getBondType(self, ):
        pass

    def getBook(self, ):
        pass

    def getBooleanParameter(self, String=None, boolean1=None):
        pass

    def getBroker(self, ):
        pass

    def getBrokerPhone(self, ):
        pass

    def getCalcPmt(self, ):
        pass

    def getCardExpirationMonth(self, ):
        pass

    def getCardExpirationYear(self, ):
        pass

    def getCardNumber(self, ):
        pass

    def getCheckNumTags(self, String=None):
        pass

    def getClass(self, ):
        pass

    def getClearedBalance(self, ):
        pass

    def getComment(self, ):
        pass

    def getCompounding(self, ):
        pass

    def getConfirmedBalance(self, ):
        pass

    def getCreationDate(self, ):
        pass

    def getCreationDateInt(self, ):
        pass

    def getCreditLimit(self, ):
        pass

    def getCurrencyChoice(self, ):
        pass

    def getCurrencyParameter(self, String=None, String1=None, String2=None, CurrencyType3=None):
        pass

    def getCurrencyType(self, ):
        pass

    def getCurrentBalance(self, ):
        pass

    def getDebtPaymentAmount(self, ):
        pass

    def getDebtPaymentProportion(self, ):
        pass

    def getDebtPaymentSpec(self, ):
        pass

    def getDefaultAccount(self, AcctFilter=None, String1=None):
        pass

    def getDefaultCategory(self, ):
        pass

    def getDefaultTransferAccount(self, ):
        pass

    def getDepth(self, ):
        pass

    def getDividend(self, ):
        pass

    def getDoubleParameter(self, String=None, double1=None):
        pass

    def getDownloadedTxns(self, ):
        pass

    def getEscrow(self, ):
        pass

    def getEscrowAccount(self, ):
        pass

    def getEscrowPayment(self, ):
        pass

    def getExchange(self, ):
        pass

    def getFaceValue(self, ):
        pass

    def getFixedMonthlyPaymentAmount(self, ):
        pass

    def getFullAccountName(self, ):
        pass

    def getHideOnHomePage(self, ):
        pass

    def getIndentedName(self, ):
        pass

    def getInitialPrincipal(self, ):
        pass

    def getInitialTransfer(self, ):
        pass

    def getInstitutionName(self, ):
        pass

    def getIntParameter(self, String=None, int1=None):
        pass

    def getInterestAccount(self, ):
        pass

    def getInterestRate(self, ):
        pass

    def getInvestAccountNumber(self, ):
        pass

    def getInvstCommissionAcct(self, ):
        pass

    def getKeywords(self, ):
        pass

    def getLongParameter(self, String=None, long1=None):
        pass

    def getMaturity(self, ):
        pass

    def getMonth(self, ):
        pass

    def getNextCheckNumber(self, ):
        pass

    def getNextCheckNumberLong(self, ):
        pass

    def getNumPayments(self, ):
        pass

    def getNumYears(self, ):
        pass

    def getOFXAccountKey(self, ):
        pass

    def getOFXAccountMsgType(self, ):
        pass

    def getOFXAccountNumber(self, ):
        pass

    def getOFXAccountType(self, ):
        pass

    def getOFXBankID(self, ):
        pass

    def getOFXBillPayAccountNumber(self, ):
        pass

    def getOFXBillPayAccountType(self, ):
        pass

    def getOFXBillPayBankID(self, ):
        pass

    def getOFXBranchID(self, ):
        pass

    def getOFXBrokerID(self, ):
        pass

    def getOnlinePayees(self, ):
        pass

    def getOnlinePayments(self, ):
        pass

    def getOptionPrice(self, ):
        pass

    def getOriginalItem(self, ):
        pass

    def getParameter(self, String=None, String1=None):
        pass

    def getParameterCount(self, ):
        pass

    def getParameterKeys(self, ):
        pass

    def getParentAccount(self, ):
        pass

    def getParentAtDepth(self, int=None):
        pass

    def getPath(self, ):
        pass

    def getPaymentSchedule(self, ):
        pass

    def getPaymentsPerYear(self, ):
        pass

    def getPermanentAPR(self, ):
        pass

    def getPoints(self, ):
        pass

    def getPreference(self, String=None, String1=None):
        pass

    def getPreferenceBoolean(self, String=None, boolean1=None):
        pass

    def getPreferenceDouble(self, String=None, double1=None):
        pass

    def getPreferenceInt(self, String=None, int1=None):
        pass

    def getPreferenceIntArray(self, String=None):
        pass

    def getPreferenceLong(self, String=None, long1=None):
        pass

    def getPreferenceStringList(self, String=None):
        pass

    def getPreferenceSublist(self, String=None):
        pass

    def getPreferenceSubset(self, String=None):
        pass

    def getPreferredSortAscending(self, boolean=None):
        pass

    def getPreferredSortOrder(self, int=None):
        pass

    def getPreferredTwoLines(self, boolean=None):
        pass

    def getPut(self, ):
        pass

    def getRateChangeDate(self, ):
        pass

    def getReconcilingBalance(self, ):
        pass

    def getRecursiveBalance(self, ):
        pass

    def getRecursiveClearedBalance(self, ):
        pass

    def getRecursiveCurrentBalance(self, ):
        pass

    def getRecursiveReconcilingBalance(self, ):
        pass

    def getRecursiveStartBalance(self, ):
        pass

    def getRecursiveUserBalance(self, ):
        pass

    def getRecursiveUserClearedBalance(self, ):
        pass

    def getRecursiveUserCurrentBalance(self, ):
        pass

    def getRecursiveUserReconcilingBalance(self, ):
        pass

    def getRecursiveUserStartBalance(self, ):
        pass

    def getReminder(self, ):
        pass

    def getRootAccount(self, ):
        pass

    def getSecuritySubType(self, ):
        pass

    def getSecurityType(self, ):
        pass

    def getStartBalance(self, ):
        pass

    def getStrikePrice(self, ):
        pass

    def getStringListParameter(self, String=None):
        pass

    def getSubAccount(self, int=None):
        pass

    def getSubAccountCount(self, ):
        pass

    def getSubAccounts(self, AcctFilter=None):
        pass

    def getSyncInfo(self, ):
        pass

    def getSyncItemType(self, ):
        pass

    def getSyncTimestamp(self, ):
        pass

    def getTaxCategory(self, ):
        pass

    def getUUID(self, ):
        pass

    def getUnconfirmedTxnCount(self, ):
        pass

    def getUserBalance(self, ):
        pass

    def getUserClearedBalance(self, ):
        pass

    def getUserConfirmedBalance(self, ):
        pass

    def getUserCurrentBalance(self, ):
        pass

    def getUserReconcilingBalance(self, ):
        pass

    def getUserStartBalance(self, ):
        pass

    def getUsesAverageCost(self, ):
        pass

    def hasBeenSynced(self, ):
        pass

    def hasExpiringRate(self, ):
        pass

    def hasKeywordSubstring(self, String=None, boolean1=None):
        pass

    def indexOf(self, Account=None):
        pass

    def isAncestorOf(self, Account=None):
        pass

    def isDeductible(self, ):
        pass

    def isDescendantOf(self, Account=None):
        pass

    def isDirty(self, ):
        pass

    def isLeafNode(self, ):
        pass

    def isOnlineBankingCandidate(self, ):
        pass

    def isOnlineBillpayCandidate(self, ):
        pass

    def isOnlineEnabled(self, ):
        pass

    def isRegisterAccount(self, ):
        pass

    def isTaxRelated(self, ):
        pass

    def isTaxable(self, ):
        pass

    def itemWasUpdated(self, SyncRecord=None):
        pass

    def itemWillSync(self, SyncRecord=None):
        pass

    @staticmethod
    def makeAccount(AccountBook=None, AccountType1=None, Account2=None):
        pass

    @staticmethod
    def makeSyncableItem(AccountBook=None, SyncRecord1=None):
        pass

    def migrateFromOldDownloadedTxns(self, ):
        pass

    def notifyAccountModified(self, ):
        pass

    def removeParameter(self, String=None):
        pass

    def setAPR(self, double=None):
        pass

    def setAPRPercent(self, double=None):
        pass

    def setAccountDescription(self, String=None):
        pass

    def setAccountIsInactive(self, boolean=None):
        pass

    def setAccountName(self, String=None):
        pass

    def setAccountParameter(self, String=None, String1=None, Account2=None):
        pass

    def setAccountType(self, AccountType=None):
        pass

    def setAddress(self, AddressBookEntry=None):
        pass

    def setAddressParameter(self, String=None, String1=None, AddressBookEntry2=None):
        pass

    def setAnnualFee(self, long=None):
        pass

    def setBankAccountNumber(self, String=None):
        pass

    def setBankName(self, String=None):
        pass

    def setBankingFI(self, OnlineService=None):
        pass

    def setBillPayFI(self, OnlineService=None):
        pass

    def setBondType(self, int=None):
        pass

    def setBroker(self, String=None):
        pass

    def setBrokerPhone(self, String=None):
        pass

    def setCalcPmt(self, boolean=None):
        pass

    def setCardExpirationMonth(self, int=None):
        pass

    def setCardExpirationYear(self, int=None):
        pass

    def setCardNumber(self, String=None):
        pass

    def setCheckNumTags(self, String=None):
        pass

    def setCheckedInitialTransfer(self, ):
        pass

    def setComment(self, String=None):
        pass

    def setCompounding(self, CompoundingType=None):
        pass

    def setCreationDate(self, long=None):
        pass

    def setCreditLimit(self, long=None):
        pass

    def setCurrencyChoice(self, String=None):
        pass

    def setCurrencyParameter(self, String=None, String1=None, String2=None, CurrencyType3=None):
        pass

    def setCurrencyType(self, CurrencyType=None):
        pass

    def setDebtPaymentAmount(self, long=None):
        pass

    def setDebtPaymentProportion(self, double=None):
        pass

    def setDebtPaymentSpec(self, DebtPaymentSpec=None):
        pass

    def setDeductible(self, boolean=None):
        pass

    def setDefaultAccount(self, String=None, Account1=None):
        pass

    def setDefaultCategory(self, Account=None):
        pass

    def setDefaultTransferAccount(self, Account=None):
        pass

    def setDirtyFlag(self, ):
        pass

    def setDividend(self, long=None):
        pass

    def setEditingMode(self, ):
        pass

    def setEscrow(self, boolean=None):
        pass

    def setEscrowAccount(self, Account=None):
        pass

    def setEscrowPayment(self, long=None):
        pass

    def setExchange(self, String=None):
        pass

    def setFaceValue(self, long=None):
        pass

    def setFixedMonthlyPaymentAmount(self, long=None):
        pass

    def setHasExpiringRate(self, boolean=None):
        pass

    def setHideOnHomePage(self, boolean=None):
        pass

    def setIncludeInNetWorth(self, boolean=None):
        pass

    def setInitialPrincipal(self, long=None):
        pass

    def setInitialTransfer(self, AbstractTxn=None):
        pass

    def setInstitutionName(self, String=None):
        pass

    def setInterestAccount(self, Account=None):
        pass

    def setInterestRate(self, double=None):
        pass

    def setInvestAccountNumber(self, String=None):
        pass

    def setKeywords(self, List=None):
        pass

    def setMaturity(self, long=None):
        pass

    def setMonth(self, int=None):
        pass

    def setNumPayments(self, int=None):
        pass

    def setNumYears(self, int=None):
        pass

    def setOFXAccountKey(self, String=None):
        pass

    def setOFXAccountMsgType(self, int=None):
        pass

    def setOFXAccountNumber(self, String=None):
        pass

    def setOFXAccountType(self, String=None):
        pass

    def setOFXBankID(self, String=None):
        pass

    def setOFXBillPayAccountNumber(self, String=None):
        pass

    def setOFXBillPayAccountType(self, String=None):
        pass

    def setOFXBillPayBankID(self, String=None):
        pass

    def setOFXBranchID(self, String=None):
        pass

    def setOFXBrokerID(self, String=None):
        pass

    def setOnlinePayees(self, OnlinePayeeList=None):
        pass

    def setOnlinePayments(self, OnlinePaymentList=None):
        pass

    def setOptionPrice(self, double=None):
        pass

    def setParameter(self, String=None, boolean1=None):
        pass

    def setParameterNoNotify(self, String=None, String1=None):
        pass

    def setParentAccount(self, Account=None):
        pass

    def setPaymentsPerYear(self, int=None):
        pass

    def setPermanentAPR(self, double=None):
        pass

    def setPoints(self, double=None):
        pass

    def setPreference(self, String=None, boolean1=None):
        pass

    def setPreferredSortAscending(self, boolean=None):
        pass

    def setPreferredSortOrder(self, int=None):
        pass

    def setPreferredTwoLines(self, boolean=None):
        pass

    def setPut(self, boolean=None):
        pass

    def setRateChangeDate(self, int=None):
        pass

    def setReminder(self, boolean=None):
        pass

    def setSecuritySubType(self, String=None):
        pass

    def setSecurityType(self, SecurityType=None):
        pass

    def setStartBalance(self, long=None):
        pass

    def setStrikePrice(self, long=None):
        pass

    def setTaxCategory(self, String=None):
        pass

    def setTaxRelated(self, boolean=None):
        pass

    def setTaxable(self, boolean=None):
        pass

    def setUsesAverageCost(self, boolean=None):
        pass

    def shouldBeIncludedInNetWorth(self, ):
        pass

    def sortAccounts(self, ):
        pass

    def syncItem(self, ):
        pass

    def toString(self, ):
        pass

class AccountBook(object):
    # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/AccountBook.class
    DROPBOX_SYNC_UUID = None

    @staticmethod
    def accountBookForFolder(File=None):
        pass

    def addAccountListener(self, AccountListener=None):
        pass

    def addFileListener(self, MDFileListener=None):
        pass

    def addListener(self, AccountBookListener=None):
        pass

    def cleanUp(self, ):
        pass

    def cleanupDeletedAttachments(self, ):
        pass

    def doInitialLoad(self, boolean=None):
        pass

    def equals(self, Object=None):
        pass

    @staticmethod
    def fakeAccountBook():
        pass

    def getAccountByNum(self, int=None):
        pass

    def getAccountByUUID(self, String=None):
        pass

    def getAccountByUUIDOrLegacyNumber(self, String=None):
        pass

    def getAddresses(self, ):
        pass

    def getAttachmentsFolder(self, ):
        pass

    @staticmethod
    def getBookFileForName(File=None, String1=None):
        pass

    def getBudgets(self, ):
        pass

    def getCheckpointFiles(self, ):
        pass

    def getCheckpointsFolder(self, ):
        pass

    def getClass(self, ):
        pass

    def getCurrencies(self, ):
        pass

    def getCurrencyByUUID(self, String=None):
        pass

    def getEncryptedTemporaryFolder(self, ):
        pass

    def getFileUUID(self, ):
        pass

    def getItemForID(self, String=None):
        pass

    def getItemsWithType(self, String=None):
        pass

    def getLastModified(self, ):
        pass

    def getLocalStorage(self, ):
        pass

    def getMemorizedItems(self, ):
        pass

    def getName(self, ):
        pass

    def getOnlineInfo(self, ):
        pass

    def getPublicMetaData(self, ):
        pass

    def getRecalcBalances(self, ):
        pass

    def getReminders(self, ):
        pass

    def getRootAccount(self, ):
        pass

    def getRootAccountFile(self, ):
        pass

    def getRootFolder(self, ):
        pass

    def getSyncer(self, ):
        pass

    def getTemporaryFolder(self, ):
        pass

    def getTransactionSet(self, ):
        pass

    def getUndoManager(self, ):
        pass

    @staticmethod
    def getUnusedFileNameWithBase(File=None, String1=None):
        pass

    @staticmethod
    def getUnusedFriendlyFileInBase(File=None):
        pass

    def hasCompletedInitialSync(self, ):
        pass

    def hasLoggedChanges(self, ):
        pass

    def initializeAccounts(self, Account=None):
        pass

    def initializeNewEmptyAccounts(self, String=None):
        pass

    @staticmethod
    def isValid(AccountBook=None):
        pass

    @staticmethod
    def isValidBookFile(String=None):
        pass

    @staticmethod
    def isValidBookName(File=None, String1=None):
        pass

    def logModifiedItem(self, MoneydanceSyncableItem=None):
        pass

    def logModifiedItems(self, List=None):
        pass

    def logRemovedItem(self, MoneydanceSyncableItem=None):
        pass

    def logRemovedItems(self, List=None):
        pass

    def moveToFolder(self, File=None):
        pass

    def notifyAccountModified(self, Account=None):
        pass

    def pauseSyncing(self, ):
        pass

    def performPostLoadVerification(self, ):
        pass

    def refreshAccountBalances(self, ):
        pass

    def refreshAccountBalancesAsync(self, ):
        pass

    def registerAttachmentForDeletion(self, String=None):
        pass

    def registerNewItemWithoutSyncing(self, SyncableItem=None):
        pass

    def removeAccountListener(self, AccountListener=None):
        pass

    def removeFileListener(self, MDFileListener=None):
        pass

    def removeListener(self, AccountBookListener=None):
        pass

    def resetLoggedChanges(self, ):
        pass

    def resumeSyncing(self, ):
        pass

    def save(self, ):
        pass

    def saveTrunkFile(self, ):
        pass

    def scheduleQueuePurgeInMillisecondsFromNow(self, long=None):
        pass

    def setFinishedInitialLoad(self, boolean=None):
        pass

    def setLocalStorage(self, LocalStorage=None):
        pass

    def setPublicMetaData(self, StreamTable=None):
        pass

    def setRecalcBalances(self, boolean=None):
        pass

    def setUndoManager(self, UndoManagerInterface=None):
        pass

    def startSyncing(self, SyncFolder=None, SyncDelegate1=None, boolean2=None):
        pass

    def stopSyncing(self, ):
        pass

    @staticmethod
    def stripNonFilenameSafeCharacters(String=None):
        pass

    def toString(self, ):
        pass

    def unregisterAttachmentForDeletion(self, String=None):
        pass

class ParentTxn(object):
    # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/ParentTxn.class
    BANK_TRANSACTION_TYPE = None
    ITEM_KEY_ID = None
    ITEM_KEY_TIMESTAMP = None
    ITEM_TYPE_KEY = None
    PRINT_CHECKNUM_PREFIX = None
    PRINT_CHECKNUM_SUFFIX = None
    SECURITY_SUBTYPES_ITEM_TYPE = None
    SPLIT_TRANSACTION_TYPE = None
    STATUS_CLEARED = None
    STATUS_RECONCILING = None
    STATUS_UNRECONCILED = None
    SYNCABLE_TYPE_VALUE = None
    TAG_FITID_PREFIX = None
    TAG_FI_ID = None
    TAG_INVST_SPLIT_EXP = None
    TAG_INVST_SPLIT_FEE = None
    TAG_INVST_SPLIT_INC = None
    TAG_INVST_SPLIT_SEC = None
    TAG_INVST_SPLIT_TYPE = None
    TAG_INVST_SPLIT_XFR = None
    TAG_INVST_TXN_TYPE = None
    TAG_IS_NEW_TXN = None
    TAG_ONLINE_PMT_ID = None
    TAG_QIF_IMPORT_SESSION = None
    TAG_QIF_INVST_ACTION = None
    TAG_RECON_ASOFDT = None
    TAG_RECON_DATE = None
    TAG_SPLIT_ADDED = None
    TAG_SPLIT_AMOUNT = None
    TAG_SPLIT_CALC = None
    TAG_SPLIT_PAIR = None
    TRANSFER_TYPE_BANK = None
    TRANSFER_TYPE_BUYSELL = None
    TRANSFER_TYPE_BUYSELLXFR = None
    TRANSFER_TYPE_DIVIDEND = None
    TRANSFER_TYPE_DIVIDENDXFR = None
    TRANSFER_TYPE_MISCINCEXP = None
    TRANSFER_TYPE_SHORTCOVER = None

    class ClearedStatus(object):
        # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/AbstractTxn$ClearedStatus.class
        CLEARED = None
        RECONCILING = None
        UNRECONCILED = None
    
        class EnumDesc(object):
        
            def bootstrapArgs(self, ):
                pass
        
            def bootstrapArgsList(self, ):
                pass
        
            def bootstrapMethod(self, ):
                pass
        
            def constantName(self, ):
                pass
        
            def constantType(self, ):
                pass
        
            def equals(self, Object=None):
                pass
        
            def getClass(self, ):
                pass
        
            @staticmethod
            def of(ClassDesc=None, String1=None):
                pass
        
            @staticmethod
            def ofCanonical(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            @staticmethod
            def ofNamed(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            def resolveConstantDesc(self, Lookup=None):
                pass
        
            def toString(self, ):
                pass
    
        def compareTo(self, Enum=None):
            pass
    
        def describeConstable(self, ):
            pass
    
        def equals(self, Object=None):
            pass
    
        def getClass(self, ):
            pass
    
        def getDeclaringClass(self, ):
            pass
    
        def name(self, ):
            pass
    
        def ordinal(self, ):
            pass
    
        @staticmethod
        def statusForByte(byte=None):
            pass
    
        @staticmethod
        def statusForString(String=None):
            pass
    
        def toString(self, ):
            pass
    
        @staticmethod
        def valueOf(Class=None, String1=None):
            pass
    
        @staticmethod
        def values():
            pass

    def __init__(self, AccountBook=None):
        pass

    def addParameters(self, Map=None):
        pass

    def addSplit(self, SplitTxn=None):
        pass

    def addTags(self, Map=None):
        pass

    @staticmethod
    def decodeKeywordList(String=None):
        pass

    def deleteItem(self, ):
        pass

    def doesParameterExist(self, String=None):
        pass

    def duplicate(self, ):
        pass

    def duplicateAsNew(self, ):
        pass

    @staticmethod
    def encodeKeywordList(List=None):
        pass

    def equals(self, Object=None):
        pass

    def getAccount(self, ):
        pass

    def getAccountParameter(self, String=None, String1=None, Account2=None):
        pass

    def getAddress(self, ):
        pass

    def getAddressParameter(self, String=None, String1=None, AddressBookEntry2=None):
        pass

    def getAttachmentKeys(self, ):
        pass

    def getAttachmentTag(self, String=None):
        pass

    def getBook(self, ):
        pass

    def getBooleanParameter(self, String=None, boolean1=None):
        pass

    def getCheckNumAsInt(self, ):
        pass

    def getCheckNumAsLong(self, ):
        pass

    def getCheckNumber(self, ):
        pass

    def getClass(self, ):
        pass

    def getClearedStatus(self, ):
        pass

    def getCurrencyParameter(self, String=None, String1=None, String2=None, CurrencyType3=None):
        pass

    def getDateEntered(self, ):
        pass

    def getDateInt(self, ):
        pass

    def getDatePostedOnline(self, ):
        pass

    def getDescription(self, ):
        pass

    def getDoubleParameter(self, String=None, double1=None):
        pass

    def getFIID(self, ):
        pass

    def getFiTxnId(self, int=None):
        pass

    def getIntParameter(self, String=None, int1=None):
        pass

    def getInvestTxnType(self, ):
        pass

    def getKeywords(self, ):
        pass

    def getLongParameter(self, String=None, long1=None):
        pass

    def getMemo(self, ):
        pass

    def getOldTxnID(self, ):
        pass

    def getOriginalItem(self, ):
        pass

    def getOriginalOnlineTxn(self, ):
        pass

    def getOtherTxn(self, int=None):
        pass

    def getOtherTxnCount(self, ):
        pass

    def getParameter(self, String=None, String1=None):
        pass

    def getParameterCount(self, ):
        pass

    def getParameterKeys(self, ):
        pass

    def getParentTxn(self, ):
        pass

    def getPreference(self, String=None, String1=None):
        pass

    def getPreferenceBoolean(self, String=None, boolean1=None):
        pass

    def getPreferenceDouble(self, String=None, double1=None):
        pass

    def getPreferenceInt(self, String=None, int1=None):
        pass

    def getPreferenceIntArray(self, String=None):
        pass

    def getPreferenceLong(self, String=None, long1=None):
        pass

    def getPreferenceStringList(self, String=None):
        pass

    def getPreferenceSublist(self, String=None):
        pass

    def getPreferenceSubset(self, String=None):
        pass

    def getSplit(self, int=None):
        pass

    def getSplitCount(self, ):
        pass

    def getStatus(self, ):
        pass

    def getStatusChar(self, ):
        pass

    def getStringListParameter(self, String=None):
        pass

    def getSyncInfo(self, ):
        pass

    def getSyncItemType(self, ):
        pass

    def getSyncTimestamp(self, ):
        pass

    def getTags(self, ):
        pass

    def getTaxDateInt(self, ):
        pass

    def getTransferType(self, ):
        pass

    def getUUID(self, ):
        pass

    def getValue(self, ):
        pass

    def hasAttachments(self, ):
        pass

    def hasBeenSynced(self, ):
        pass

    def hasKeywordSubstring(self, String=None, boolean1=None):
        pass

    def indexOfSplit(self, SplitTxn=None):
        pass

    def isDirty(self, ):
        pass

    def isNew(self, ):
        pass

    def isTransferTo(self, Account=None):
        pass

    def itemWasUpdated(self, SyncRecord=None):
        pass

    def itemWillSync(self, SyncRecord=None):
        pass

    def loadFromStorage(self, Map=None):
        pass

    @staticmethod
    def makeParentTxn(AccountBook=None, int1=None, int2=None, long3=None, String4=None, Account5=None, String6=None, String7=None, long8=None, byte9=None):
        pass

    @staticmethod
    def makeSyncableItem(AccountBook=None, SyncRecord1=None):
        pass

    def needsToBePrinted(self, ):
        pass

    def removeAttachmentTag(self, String=None):
        pass

    def removeParameter(self, String=None):
        pass

    def removeSplit(self, SplitTxn=None):
        pass

    def resetDirty(self, ):
        pass

    def setAccount(self, Account=None):
        pass

    def setAccountParameter(self, String=None, String1=None, Account2=None):
        pass

    def setAddress(self, AddressBookEntry=None):
        pass

    def setAddressParameter(self, String=None, String1=None, AddressBookEntry2=None):
        pass

    def setAttachmentTag(self, String=None, File1=None):
        pass

    def setCheckNumber(self, String=None):
        pass

    def setClearedStatus(self, ClearedStatus=None):
        pass

    def setCurrencyParameter(self, String=None, String1=None, String2=None, CurrencyType3=None):
        pass

    def setDateEntered(self, long=None):
        pass

    def setDateInt(self, int=None):
        pass

    def setDescription(self, String=None):
        pass

    def setDirty(self, ):
        pass

    def setEditingMode(self, ):
        pass

    def setFIID(self, String=None):
        pass

    def setFiTxnId(self, int=None, String1=None):
        pass

    def setInvestTxnType(self, InvestTxnType=None):
        pass

    def setIsNew(self, boolean=None):
        pass

    def setKeywords(self, List=None):
        pass

    def setMemo(self, String=None):
        pass

    def setOriginalOnlineTxn(self, OnlineTxn=None):
        pass

    def setParameter(self, String=None, boolean1=None):
        pass

    def setParameterNoNotify(self, String=None, String1=None):
        pass

    def setPreference(self, String=None, boolean1=None):
        pass

    def setStatus(self, byte=None):
        pass

    def setTaxDateInt(self, int=None):
        pass

    def setTransferType(self, String=None):
        pass

    def syncItem(self, ):
        pass

    def toMultilineString(self, ):
        pass

    def toString(self, ):
        pass

    def wasDownloaded(self, ):
        pass

class Reminder(object):
    # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/Reminder.class
    BASIC_REMINDER_TYPE = None
    ITEM_KEY_ID = None
    ITEM_KEY_TIMESTAMP = None
    ITEM_TYPE_KEY = None
    LAST_DAY_OF_MONTH = None
    MONTHLY_EVERY = None
    MONTHLY_EVERY_FOURTH = None
    MONTHLY_EVERY_OTHER = None
    MONTHLY_EVERY_SIXTH = None
    MONTHLY_EVERY_THIRD = None
    REPEAT_BY_DAY_OF_MONTH = None
    REPEAT_BY_DAY_OF_WEEK = None
    REPEAT_BY_EVERY_YEAR = None
    REPEAT_BY_NDAYS = None
    REPEAT_BY_NONE = None
    SECURITY_SUBTYPES_ITEM_TYPE = None
    SYNCABLE_TYPE_VALUE = None
    TXN_REMINDER_TYPE = None
    WEEKLY_EVERY = None
    WEEKLY_EVERY_FIFTH = None
    WEEKLY_EVERY_FIRST = None
    WEEKLY_EVERY_FOURTH = None
    WEEKLY_EVERY_LAST = None
    WEEKLY_EVERY_SECOND = None
    WEEKLY_EVERY_THIRD = None

    class Type(object):
        # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/Reminder$Type.class
        NOTE = None
        TRANSACTION = None
    
        class EnumDesc(object):
        
            def bootstrapArgs(self, ):
                pass
        
            def bootstrapArgsList(self, ):
                pass
        
            def bootstrapMethod(self, ):
                pass
        
            def constantName(self, ):
                pass
        
            def constantType(self, ):
                pass
        
            def equals(self, Object=None):
                pass
        
            def getClass(self, ):
                pass
        
            @staticmethod
            def of(ClassDesc=None, String1=None):
                pass
        
            @staticmethod
            def ofCanonical(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            @staticmethod
            def ofNamed(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                pass
        
            def resolveConstantDesc(self, Lookup=None):
                pass
        
            def toString(self, ):
                pass
    
        def code(self, ):
            pass
    
        def compareTo(self, Enum=None):
            pass
    
        def describeConstable(self, ):
            pass
    
        def equals(self, Object=None):
            pass
    
        def getClass(self, ):
            pass
    
        def getDeclaringClass(self, ):
            pass
    
        def name(self, ):
            pass
    
        def ordinal(self, ):
            pass
    
        def toString(self, ):
            pass
    
        @staticmethod
        def typeForCode(int=None):
            pass
    
        @staticmethod
        def valueOf(Class=None, String1=None):
            pass
    
        @staticmethod
        def values():
            pass

    def __init__(self, AccountBook=None):
        pass

    def addParameters(self, Map=None):
        pass

    def addTags(self, Map=None):
        pass

    @staticmethod
    def decodeKeywordList(String=None):
        pass

    def deleteItem(self, ):
        pass

    def doesParameterExist(self, String=None):
        pass

    def duplicate(self, ):
        pass

    @staticmethod
    def encodeKeywordList(List=None):
        pass

    def equals(self, Object=None):
        pass

    def getAccountParameter(self, String=None, String1=None, Account2=None):
        pass

    def getAddress(self, ):
        pass

    def getAddressParameter(self, String=None, String1=None, AddressBookEntry2=None):
        pass

    def getAutoCommitDays(self, ):
        pass

    def getBook(self, ):
        pass

    def getBooleanParameter(self, String=None, boolean1=None):
        pass

    def getClass(self, ):
        pass

    def getCurrencyParameter(self, String=None, String1=None, String2=None, CurrencyType3=None):
        pass

    def getDateAcknowledgedInt(self, ):
        pass

    def getDescription(self, ):
        pass

    def getDoubleParameter(self, String=None, double1=None):
        pass

    def getId(self, ):
        pass

    def getInitialDateInt(self, ):
        pass

    def getIntParameter(self, String=None, int1=None):
        pass

    def getKeywords(self, ):
        pass

    def getLastDateInt(self, ):
        pass

    def getLongParameter(self, String=None, long1=None):
        pass

    def getMemo(self, ):
        pass

    def getNextOccurance(self, int=None):
        pass

    def getOriginalItem(self, ):
        pass

    def getParameter(self, String=None, String1=None):
        pass

    def getParameterCount(self, ):
        pass

    def getParameterKeys(self, ):
        pass

    def getPastDueDates(self, Calendar=None):
        pass

    def getPreference(self, String=None, String1=None):
        pass

    def getPreferenceBoolean(self, String=None, boolean1=None):
        pass

    def getPreferenceDouble(self, String=None, double1=None):
        pass

    def getPreferenceInt(self, String=None, int1=None):
        pass

    def getPreferenceIntArray(self, String=None):
        pass

    def getPreferenceLong(self, String=None, long1=None):
        pass

    def getPreferenceStringList(self, String=None):
        pass

    def getPreferenceSublist(self, String=None):
        pass

    def getPreferenceSubset(self, String=None):
        pass

    def getRateAdjustmentOption(self, ):
        pass

    def getReminderType(self, ):
        pass

    def getRepeatDaily(self, ):
        pass

    def getRepeatMonthly(self, ):
        pass

    def getRepeatMonthlyModifier(self, ):
        pass

    def getRepeatWeeklyDays(self, ):
        pass

    def getRepeatWeeklyModifier(self, ):
        pass

    def getRepeatYearly(self, ):
        pass

    def getStringListParameter(self, String=None):
        pass

    def getSyncInfo(self, ):
        pass

    def getSyncItemType(self, ):
        pass

    def getSyncTimestamp(self, ):
        pass

    def getTags(self, ):
        pass

    def getTransaction(self, ):
        pass

    def getUUID(self, ):
        pass

    def hasBeenAcknowledged(self, Date=None):
        pass

    def hasBeenAcknowledgedInt(self, int=None):
        pass

    def hasBeenSynced(self, ):
        pass

    def hasKeywordSubstring(self, String=None, boolean1=None):
        pass

    def isLoanReminder(self, ):
        pass

    def itemWasUpdated(self, SyncRecord=None):
        pass

    def itemWillSync(self, SyncRecord=None):
        pass

    @staticmethod
    def makeSyncableItem(AccountBook=None, SyncRecord1=None):
        pass

    def occursOnDate(self, Calendar=None):
        pass

    def removeParameter(self, String=None):
        pass

    def setAccountParameter(self, String=None, String1=None, Account2=None):
        pass

    def setAcknowledgedInt(self, int=None):
        pass

    def setAddress(self, AddressBookEntry=None):
        pass

    def setAddressParameter(self, String=None, String1=None, AddressBookEntry2=None):
        pass

    def setAutoCommitDays(self, int=None):
        pass

    def setCurrencyParameter(self, String=None, String1=None, String2=None, CurrencyType3=None):
        pass

    def setDescription(self, String=None):
        pass

    def setEditingMode(self, ):
        pass

    def setId(self, long=None):
        pass

    def setInitialDateInt(self, int=None):
        pass

    def setKeywords(self, List=None):
        pass

    def setLastDateInt(self, int=None):
        pass

    def setLoan(self, boolean=None):
        pass

    def setMemo(self, String=None):
        pass

    def setParameter(self, String=None, boolean1=None):
        pass

    def setParameterNoNotify(self, String=None, String1=None):
        pass

    def setPreference(self, String=None, boolean1=None):
        pass

    def setRateAdjustmentOption(self, RateAdjustmentOption=None):
        pass

    def setReminderType(self, Type=None):
        pass

    def setRepeatDaily(self, int=None):
        pass

    def setRepeatMonthly(self, int=None, int1=None):
        pass

    def setRepeatWeekly(self, int=None, int1=None):
        pass

    def setRepeatYearly(self, boolean=None):
        pass

    def setTransaction(self, ParentTxn=None):
        pass

    def syncItem(self, ):
        pass

    def toString(self, ):
        pass

class ReminderSet(object):
    # source:jar:file:/~/Documents/Prog/moneydance-devkit-5.1/lib/moneydance-dev.jar!/com/infinitekind/moneydance/model/ReminderSet.class

    def __init__(self, AccountBook=None):
        pass

    def addReminder(self, Reminder=None):
        pass

    def addReminderListener(self, ReminderListener=None):
        pass

    def autoCommitReminders(self, ):
        pass

    def equals(self, Object=None):
        pass

    def getAccountBook(self, ):
        pass

    def getAllReminders(self, ):
        pass

    def getClass(self, ):
        pass

    def getEventsInDay(self, Calendar=None):
        pass

    def getOverdueItems(self, Calendar=None):
        pass

    def getRemindersOnDay(self, Calendar=None):
        pass

    def removeReminder(self, Reminder=None):
        pass

    def removeReminderListener(self, ReminderListener=None):
        pass

    def toString(self, ):
        pass

