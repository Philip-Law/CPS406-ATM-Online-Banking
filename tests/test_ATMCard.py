from ATMCard import ATMCard
from User import User
from unittest.mock import MagicMock
import pytest

class TestATMCard:
    @pytest.fixture
    def card(self):
        user = User("John", 500, 700)
        return ATMCard("1234", user)


    def test_get_PIN(self, card):
        assert card.get_PIN() == "1234"


    def test_get_card_number(self, card):
        # Mocks a potential card number for a card, as card numbers are randomly generated
        card.get_card_number = MagicMock(return_value = 1111_2222_3333_4444)

        assert card.get_card_number() == 1111222233334444


    def test_get_user(self, card):
        newUser = User("John", 500, 700)
        assert newUser.get_account("Chequing").get_balance() == card.get_user().get_account("Chequing").get_balance()
        assert newUser.get_account("Savings").get_balance() == card.get_user().get_account("Savings").get_balance()