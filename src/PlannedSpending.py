# Look at all spending reminders to see what's planned
from datetime import date, timedelta
from decimal import Decimal

from com.infinitekind.moneydance.model import AbstractTxn, Account, AccountBook, ParentTxn, Reminder, ReminderSet
from typing import List, Optional

from Configure import Configure


class PlannedReminder(object):
    ONE_DAY = timedelta(days=1)

    def __init__(self, reminder):
        # type: (Reminder) -> None
        self.reminder = reminder  # type: Reminder
        self.annualTotal = None  # type: Optional[Decimal]
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
        if not self.annualTotal:
            self.annualTotal = Decimal(0)
            curDate = date.today()
            endDate = date(curDate.year + 1, curDate.month, curDate.day)

            while curDate < endDate:
                if self.reminder.occursOnDate(curDate):
                    self.annualTotal += self.spendTotal

                curDate += PlannedReminder.ONE_DAY
            # end while

        return self.annualTotal
    # end getAnnualTotal()

    def __str__(self):
        return "{} spend {}".format(
            self.reminder.getDescription(), self.spendTotal)
    # end __str__()

# end class PlannedReminder


Configure.logToSysErr()

if "moneydance" in globals():
    global moneydance
    accountBook = moneydance.getCurrentAccountBook()  # type: AccountBook
    root = accountBook.getRootAccount()  # type: Account
    reminderSet = accountBook.getReminders()  # type: ReminderSet
    reminders = reminderSet.getAllReminders()  # type: List[Reminder]
    reminders.sort(key=lambda reminder: reminder.getDescription())
    plannedSpending = []  # type: List[PlannedReminder]

    for remind in reminders:
        planned = PlannedReminder(remind)

        if planned.isSpending():
            plannedSpending.append(planned)
    # end for
    print "Number of spending reminders:", len(plannedSpending), "- annual spending for each:"
    plannedSpending.sort(key=lambda spend: spend.getAnnualTotal(), reverse=True)

    for planned in plannedSpending:
        print "{:>8} {}".format(
            planned.getAnnualTotal(), planned.reminder.getDescription())
    # end for
