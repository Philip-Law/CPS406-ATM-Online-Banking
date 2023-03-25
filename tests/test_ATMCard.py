from ATMCard import ATMCard
from User import User
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def card():
    user = User("John", 500, 700)
    return ATMCard("1234", user)


def test_get_PIN(card):
    assert card.get_PIN() == "1234"


def test_get_card_number(card):
    # Mocks a potential card number for a card, as card numbers are randomly generated
    card.get_card_number = MagicMock(return_value = 1111_2222_3333_4444)

    assert card.get_card_number() == 1111222233334444


def test_get_user(card):
    newUser = User("John", 500, 700)
    assert newUser.get_chequing_account().get_balance() == card.get_user().get_chequing_account().get_balance()
    assert newUser.get_savings_account().get_balance() == card.get_user().get_savings_account().get_balance()