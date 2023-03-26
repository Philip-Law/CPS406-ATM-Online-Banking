from Account import Account
from Transaction import Transaction
from datetime import date

from unittest.mock import patch
import pytest

class TestAccount:
    def test_get_balance(self):
        acc = Account(2000)
        assert acc.get_balance() == 2000


    def test_deposit(self):
        # Tests deposit 2 times to make sure the balance is updated properly
        acc = Account(5000)

        acc.deposit(1000)
        assert acc.get_balance() == 6000

        acc.deposit(100)
        assert acc.get_balance() == 6100


    def test_withdraw(self):
        # Tests withdraw 2 times to make sure the balance is updated properly
        acc = Account(100)

        acc.withdraw(90)
        assert acc.get_balance() == 10

        acc.withdraw(10)
        assert acc.get_balance() == 0


    def test_withdraw_error(self):
        # Tests when an amount more than balance is withdrawn
        acc = Account(0)

        with pytest.raises(ValueError):
            acc.withdraw(1)


    def test_deposit_adds_transaction_to_history(self):
        acc = Account(1000)

        # Mocks the generate_transaction_id method in Account to return a set ID
        with patch.object(Account, "generate_transaction_id", return_value="12345678"):
            acc.deposit(500)

            # Creates expected transaction and checks if it's within the Account's history
            dAction = Transaction("12345678", date.today(), "Deposit", 500)
            assert dAction in acc.get_transaction_history()


    def test_withdraw_adds_transaction_to_history(self):
        acc = Account(500)

        # Mocks the transaction id generation in the Account class
        with patch.object(Account, "generate_transaction_id", return_value="12345678"):
            acc.withdraw(500)

            # Creates expected transaction and checks if it's within the Account's history
            wAction = Transaction("12345678", date.today(), "Withdraw", 500)
            assert wAction in acc.get_transaction_history()


            # Withdraws an invalid amount from an account and checks to see if no transaction was created
            errorAction = Transaction("12345678", date.today(), "Withdraw", 1)
            with pytest.raises(ValueError):
                acc.withdraw(1)
            
            assert errorAction not in acc.get_transaction_history()


    def test_add_transaction(self):
        acc = Account(100)

        # Adds a Transaction to an Account and checks if it's within its history
        newAction = Transaction("10000004", date.today(), "Deposit", 100)

        acc.add_transaction(newAction)
        assert acc.get_transaction_history()[0] == newAction