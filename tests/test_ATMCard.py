from ATMCard import ATMCard
from User import User
import pytest

@pytest.fixture
def card():
    user = User("John", 500, 700)
    return ATMCard("1234", user)


def test_get_PIN(card):
    assert card.get_PIN() == "1234"


def test_get_card_number(card):
    assert card.get_card_number() >= 1000000000000000 and card.get_card_number() <= 9999999999999999


def test_get_user(card):
    newUser = User("John", 500, 700)
    assert newUser.get_chequing_account().get_balance() == card.get_user().get_chequing_account().get_balance()
    assert newUser.get_savings_account().get_balance() == card.get_user().get_savings_account().get_balance()