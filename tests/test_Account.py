from Account import Account
from Transaction import Transaction
from datetime import date
import pytest

class TestAccount:

    def test_deposit(self):
        acc = Account(5000)
        acc.deposit(1000)

        assert acc.get_balance() == 6000

        acc.deposit(100)
        assert acc.get_balance() == 6100


    def test_withdraw(self):
        acc = Account(100)
        acc.withdraw(90)
        assert acc.get_balance() == 10

        acc.withdraw(10)
        assert acc.get_balance() == 0

        errorAction = Transaction("3", date.today(), "Withdraw", 1000)
        with pytest.raises(ValueError):
            acc.withdraw(1)

        assert errorAction not in acc.get_transaction_history()


    # Combine w/ withdraw?
    def test_get_transaction_history(self):
        acc = Account(100)
        acc.withdraw(90)
        wAction = Transaction("1", date.today(), "Withdraw", 90)       #(Not working yet!!!!)
        #assert wAction in acc.get_transaction_history()


        # Suggest: NOT random transaction ID? Small chance it could choose the same one
            # Also DEFINE EQUALS for Transactions                       (Test if it exists in history)
        acc.deposit(100)
        dAction = Transaction("2", date.today(), "Deposit", 100)
        #assert dAction in acc.get_transaction_history()


    def test_add_transaction(self):
        acc = Account(100)

        # Suggest: Check if transaction being added is INVALID
        newAction = Transaction("1", date.today(), "Deposit", 100)

        acc.add_transaction(newAction)
        assert acc.get_transaction_history()[0].get_amount() == 100