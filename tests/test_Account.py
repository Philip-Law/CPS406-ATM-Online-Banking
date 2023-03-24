from Account import Account
from Transaction import Transaction
from datetime import date
import pytest

class TestAccount:

    def test_deposit_history(self):
        acc = Account(5000)
        acc.deposit(1000)

        assert acc.get_balance() == 6000

        acc.deposit(100)
        assert acc.get_balance() == 6100

        dAction = Transaction(date.today(), "Deposit", 100, "10000002")
        assert dAction in acc.get_transaction_history()


    def test_withdraw_history(self):
        acc = Account(100)
        acc.withdraw(90)
        assert acc.get_balance() == 10

        wAction = Transaction(date.today(), "Withdraw", 90, "10000003")
        assert wAction in acc.get_transaction_history()

        acc.withdraw(10)
        assert acc.get_balance() == 0

        errorAction = Transaction(date.today(), "Withdraw", 1, "10000003")
        with pytest.raises(ValueError):
            acc.withdraw(1)

        assert errorAction not in acc.get_transaction_history()


    def test_add_transaction(self):
        acc = Account(100)

        newAction = Transaction(date.today(), "Deposit", 100, "10000004")

        acc.add_transaction(newAction)
        assert acc.get_transaction_history()[0].get_amount() == 100