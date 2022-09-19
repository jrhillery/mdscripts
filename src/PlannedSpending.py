# Look at all spending reminders to see what's planned
from datetime import date, timedelta
from decimal import Decimal

from com.infinitekind.moneydance.model import AbstractTxn, Account, AccountBook, ParentTxn, Reminder, ReminderSet
from typing import Dict, List, Optional

from Configure import Configure


class PlannedReminder(object):
    ONE_DAY = timedelta(days=1)

    def __init__(self, reminder):
        # type: (Reminder) -> None
        self.reminder = reminder  # type: Reminder
        self.spendTotal = Decimal(0)  # type: Decimal
        txn = reminder.getTransaction()  # type: ParentTxn
        numSplits = txn.getOtherTxnCount()  # type: int

        for i in range(numSplits):
            other = txn.getOtherTxn(i)  # type: AbstractTxn
            otherAcc = other.getAccount()  # type: Account

            if otherAcc.getAccountType() == Account.AccountType.EXPENSE:
                decimalPlaces = otherAcc.getCurrencyType().getDecimalPlaces()
                self.spendTotal += Decimal(other.getValue()).scaleb(-decimalPlaces)
        # end for
    # end __init__(Reminder)

    def isSpending(self):
        # type: () -> bool
        return self.spendTotal > 0
    # end isSpending()

    def getAnnualTotal(self):
        # type: () -> Decimal
        annualTotal = Decimal(0)
        curDate = date.today()
        endDate = date(curDate.year + 1, curDate.month, curDate.day)

        while curDate < endDate:
            if self.reminder.occursOnDate(curDate):
                annualTotal += self.spendTotal

            curDate += PlannedReminder.ONE_DAY
        # end while

        return annualTotal
    # end getAnnualTotal()

    def getDescriptionCore(self):
        # type: () -> str
        """Get the core portion of our reminder's description."""
        description = self.reminder.getDescription()
        descLen = len(description)

        # remove the trailing 2 characters when ends in <blank><char>
        if descLen > 2 and description[descLen - 2] == " ":
            description = description[:descLen - 2]

        return description
    # end getDescriptionCore()

    def __str__(self):
        return "{} spend {}".format(
            self.reminder.getDescription(), self.spendTotal)
    # end __str__()

# end class PlannedReminder


class ReminderGroup(object):
    """Class to hold a group of planned reminders that have the same core description"""

    def __init__(self, description):
        # type: (str) -> None
        self.descCore = description  # type: str
        self.reminders = []  # type: List[PlannedReminder]
        self.annualTotal = None  # type: Optional[Decimal]
    # end __init__(str)

    def getAnnualTotal(self):
        # type: () -> Decimal
        if not self.annualTotal:
            self.annualTotal = Decimal(0)

            for reminder in self.reminders:
                self.annualTotal += reminder.getAnnualTotal()

        return self.annualTotal
    # end getAnnualTotal()

# end class ReminderGroup


Configure.logToSysErr()

if "moneydance" in globals():
    global moneydance
    accountBook = moneydance.getCurrentAccountBook()  # type: AccountBook
    root = accountBook.getRootAccount()  # type: Account
    reminderSet = accountBook.getReminders()  # type: ReminderSet
    reminders = reminderSet.getAllReminders()  # type: List[Reminder]
    reminderGroups = {}  # type: Dict[str, ReminderGroup]

    for remind in reminders:
        planned = PlannedReminder(remind)

        if planned.isSpending():
            desc = planned.getDescriptionCore()

            if desc not in reminderGroups:
                reminderGroups[desc] = ReminderGroup(desc)

            reminderGroups[desc].reminders.append(planned)
    # end for
    plannedSpending = list(reminderGroups.values())
    print "Number of spending reminders: {}; annual spending for each:".format(
        len(plannedSpending))
    plannedSpending.sort(key=lambda spend: spend.getAnnualTotal(), reverse=True)

    for reminderGroup in plannedSpending:
        print "{:>8} {}".format(
            reminderGroup.getAnnualTotal(), reminderGroup.descCore)
    # end for
