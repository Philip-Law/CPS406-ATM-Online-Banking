from ATMSystemController import ATMSystemController
from ATMCard import ATMCard
from Account import Account
from User import User
from Transaction import Transaction
from datetime import date

import pytest
@pytest.fixture
def control():
    return ATMSystemController()

@pytest.fixture
def card():
    user = User("Joe", 500, 1000)
    return ATMCard("1234", user)

@pytest.fixture
def card2():
    user = User("John", 200, 400)
    return ATMCard("3080", user)


def test_verify_PIN(control, card, card2):
    assert True == control.verify_PIN(card, "1234")
    assert False == control.verify_PIN(card, "9999")

    assert True == control.verify_PIN(card2, "3080")
    assert False == control.verify_PIN(card2, "3081")
    

def test_withdraw_amount(control, card, card2):
    wAction = Transaction(date.today, "Withdraw", 60, "10000001")
    assert control.withdraw_amount("Chequing", card, 60) == wAction

    wAction = Transaction(date.today, "Withdraw", 400, "10000002")
    assert control.withdraw_amount("Savings", card2, 400) == wAction

    # Checks for raised error when withdrawing an invalid amount
    with pytest.raises(ValueError):
        control.withdraw_amount("Chequing", card, -300)

    # Checks for raised error when withdrawing an amount more than balance
    with pytest.raises(ValueError):
        control.withdraw_amount("Savings", card2, 1)


def test_deposit_amount(control, card, card2):
    dAction = Transaction(date.today, "Deposit", 200, "10000003")
    assert control.deposit_amount("Savings", card, 200) == dAction

    dAction = Transaction(date.today, "Deposit", 600, "10000004")
    assert control.deposit_amount("Chequing", card2, 600) == dAction

    # Checks for error when depositing an invalid amount
    with pytest.raises(ValueError):
        control.deposit_amount("Savings", card2, -999)