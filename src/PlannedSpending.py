# Look at all spending reminders to see what's planned
from datetime import date, timedelta

from com.infinitekind.moneydance.model import AbstractTxn, Account, AccountBook, ParentTxn, Reminder, ReminderSet
from typing import List, Optional

from Configure import Configure


class PlanedReminder(object):

    def __init__(self, reminder):
        # type: (Reminder) -> None
        self.reminder = reminder  # type: Reminder
        self.annualTotal = None  # type: Optional[int]
        self.spendTotal = 0  # type: int
        txn = reminder.getTransaction()  # type: ParentTxn
        numSplits = txn.getOtherTxnCount()  # type: int

        for i in range(numSplits):
            other = txn.getOtherTxn(i)  # type: AbstractTxn
            otherAcc = other.getAccount()  # type: Account

            if otherAcc.getAccountType() == Account.AccountType.EXPENSE:
                self.spendTotal += other.getValue()
        # end for
    # end __init__(Reminder)

    def isSpending(self):
        # type: () -> bool
        return self.spendTotal > 0
    # end isSpending()

    def getAnnualTotal(self):
        if not self.annualTotal:
            self.annualTotal = 0
            curDate = date.today()
            endDate = date(curDate.year + 1, curDate.month, curDate.day)

            while curDate < endDate:
                if self.reminder.occursOnDate(curDate):
                    self.annualTotal += self.spendTotal

                curDate += timedelta(days=1)
            # end while

        return self.annualTotal
    # end getAnnualTotal()

    def __str__(self):
        return "{} spend {}".format(
            self.reminder.getDescription(), self.spendTotal)
    # end __str__()

# end class PlanedReminder


Configure.logToSysErr()

if "moneydance" in globals():
    global moneydance
    accountBook = moneydance.getCurrentAccountBook()  # type: AccountBook
    root = accountBook.getRootAccount()  # type: Account
    reminderSet = accountBook.getReminders()  # type: ReminderSet
    reminders = reminderSet.getAllReminders()  # type: List[Reminder]
    reminders.sort(key=lambda reminder: reminder.getDescription())
    plannedSpending = []  # type: List[PlanedReminder]

    for remind in reminders:
        planned = PlanedReminder(remind)

        if planned.isSpending():
            plannedSpending.append(planned)
    # end for
    print "Number of spending reminders:", len(plannedSpending)
    plannedSpending.sort(key=lambda spend: spend.getAnnualTotal(), reverse=True)

    for planned in plannedSpending:
        print planned, "annual", planned.getAnnualTotal()
    # end for
