# Look at all spending reminders to see what's planned
from datetime import date, timedelta
from decimal import Decimal

from com.infinitekind.moneydance.model import AbstractTxn, Account, AccountBook, ParentTxn, Reminder, ReminderSet
from typing import Dict, List

from Configure import Configure


class ReminderGroup(object):
    """Class to hold a group of planned reminders that have the same core description"""

    ONE_DAY = timedelta(days=1)

    def __init__(self, description):
        # type: (str) -> None
        self.descCore = description  # type: str
        self.annualTotal = Decimal(0)
    # end __init__(str)

    def addReminder(self, reminder, spendAmt):
        # type: (Reminder, Decimal) -> None
        annualTotal = Decimal(0)
        curDate = date.today()
        endDate = date(curDate.year + 1, curDate.month, curDate.day)

        while curDate < endDate:
            if reminder.occursOnDate(curDate):
                annualTotal += spendAmt

            curDate += self.ONE_DAY
        # end while
        self.annualTotal += annualTotal
    # end addReminder(Reminder, Decimal)

# end class ReminderGroup


class ReminderAccessor(object):
    """Class to retrieve and aggregate planned reminders"""

    def __init__(self, accountBook):
        # type: (AccountBook) -> None
        self.accountBook = accountBook
        self.reminderGroups = {}  # type: Dict[str, ReminderGroup]
    # end __init__(AccountBook)

    def getReminderGroupForDesc(self, description):
        # type: (str) -> ReminderGroup

        if description not in self.reminderGroups:
            self.reminderGroups[description] = ReminderGroup(description)

        return self.reminderGroups[description]
    # end getReminderGroupForDesc(str)

    def getPlannedSpending(self):
        # type: () -> List[ReminderGroup]
        reminderSet = self.accountBook.getReminders()  # type: ReminderSet
        reminders = reminderSet.getAllReminders()  # type: List[Reminder]

        for remind in reminders:
            txn = remind.getTransaction()  # type: ParentTxn
            numSplits = txn.getOtherTxnCount()  # type: int

            for i in range(numSplits):
                other = txn.getOtherTxn(i)  # type: AbstractTxn
                spendAmt = self.getSpendValue(other)  # type: Decimal

                if spendAmt > 0:
                    desc = [self.getDescriptionCore(remind)]  # type: List[str]

                    if numSplits > 1:
                        desc.append(": ")
                        desc.append(other.getDescription())

                    self.getReminderGroupForDesc("".join(desc)).addReminder(remind, spendAmt)
            # end for splits
        # end for reminders

        return list(self.reminderGroups.values())
    # end getPlannedSpending()

    @staticmethod
    def getSpendValue(other):
        # type: (AbstractTxn) -> Decimal
        otherAcc = other.getAccount()  # type: Account

        if otherAcc.getAccountType() == Account.AccountType.EXPENSE:
            decimalPlaces = otherAcc.getCurrencyType().getDecimalPlaces()

            return Decimal(other.getValue()).scaleb(-decimalPlaces)
        else:
            return Decimal(0)
    # end getSpendValue(AbstractTxn)

    @staticmethod
    def getDescriptionCore(remind):
        # type: (Reminder) -> str
        """Get the core portion of our reminder's description."""
        description = remind.getDescription()
        descLen = len(description)

        # remove the trailing 2 characters when ends in <blank><char>
        if descLen > 2 and description[descLen - 2] == " ":
            description = description[:descLen - 2]

        return description
    # end getDescriptionCore(Reminder)

# end class ReminderAccessor


Configure.logToSysErr()

if "moneydance" in globals():
    global moneydance
    reminderAcc = ReminderAccessor(moneydance.getCurrentAccountBook())
    plannedSpending = reminderAcc.getPlannedSpending()
    print "{} spending reminders; annual spending for each:".format(
        len(plannedSpending))
    plannedSpending.sort(key=lambda spend: spend.annualTotal, reverse=True)

    for reminderGroup in plannedSpending:
        print "{:>8} {}".format(
            reminderGroup.annualTotal, reminderGroup.descCore)
    # end for
