from Transaction import Transaction
import pytest

@pytest.fixture
def withdrawAction():
    return Transaction("401", "2023-03-23", "Withdraw", 500)

def test_get_id(withdrawAction):
    assert withdrawAction.get_id() == "401"

def test_get_date(withdrawAction):
    assert withdrawAction.get_date() == "2023-03-23"

def test_get_action(withdrawAction):
    assert withdrawAction.get_action_type() == "Withdraw"

def test_get_amount(withdrawAction):
    assert withdrawAction.get_amount() == 500