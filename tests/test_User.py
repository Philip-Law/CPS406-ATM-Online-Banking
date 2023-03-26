from User import User
from Account import Account
import pytest

class TestUser:
    @pytest.fixture
    def user(self):
        return User("Justin", 500, 700)


    def test_get_chequing_account(self, user):
        chequing = Account(500)
        assert chequing.get_balance() == user.get_account("Chequing").get_balance()


    def test_get_savings_account(self, user):
        savings = Account(700)
        assert savings.get_balance() == user.get_account("Savings").get_balance()