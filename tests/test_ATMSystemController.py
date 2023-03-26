from ATMSystemController import ATMSystemController
from ATMCard import ATMCard
from Account import Account
from User import User
from Transaction import Transaction
from datetime import date

from unittest.mock import patch
import pytest


class TestATMSystemController:
    # Defines instances of ATMSystemController and ATMCard which will be used in each test
    @pytest.fixture
    def control(self):
        return ATMSystemController()

    @pytest.fixture
    def card(self):
        user = User("Jane Doe", 500, 1000)
        return ATMCard("1234", user)


    def test_verify_PIN(self, control, card):
        assert True == control.verify_PIN(card, "1234")
        assert False == control.verify_PIN(card, "9999")
        

    def test_withdraw_amount(self, control, card):
        # Mocks the "generate_transaction_id" method in Account to return a set value
        with patch.object(Account, "generate_transaction_id", return_value="12345678"):
            # Creates and tests if the withdraw_amount() method returns the expected Transaction
            wAction = Transaction("12345678", date.today(), "Withdraw", 60)
            assert control.withdraw_amount("Chequing", card, 60) == wAction


    def test_withdraw_invalid_amount(self, control, card):
        # Checks for a raised error when withdrawing an invalid amount
        with pytest.raises(ValueError):
            control.withdraw_amount("Chequing", card, -300)

        # Checks for a raised error when withdrawing an amount more than balance
        with pytest.raises(ValueError):
            control.withdraw_amount("Savings", card, 1001)


    def test_deposit_amount(self, control, card):
        # Mocks the "generate_transaction_id" method in Account to return a set value
        with patch.object(Account, "generate_transaction_id", return_value="12345678"):
            # Creates and tests if the withdraw_amount() method returns the expected Transaction
            dAction = Transaction("12345678", date.today(), "Deposit", 200)
            assert control.deposit_amount("Savings", card, 200) == dAction


    def test_deposit_invalid_amount(self, control, card):
        # Checks for a raised error when depositing an invalid amount
        with pytest.raises(ValueError):
            control.deposit_amount("Savings", card, -999)