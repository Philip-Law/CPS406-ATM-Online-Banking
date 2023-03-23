from User import User
from Account import Account
import pytest

@pytest.fixture
def user():
    return User("Justin", 500, 700)


# Make a way for accounts / users to be equal?

def test_get_chequing_account(user):
    chequing = Account(500)
    assert chequing.get_balance() == user.get_chequing_account().get_balance()


def test_get_savings_account(user):
    savings = Account(700)
    assert savings.get_balance() == user.get_savings_account().get_balance()