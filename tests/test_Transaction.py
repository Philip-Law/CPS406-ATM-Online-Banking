from Transaction import Transaction
import pytest

class TestTransaction:
    # Defines an instance of Transaction which will be used in each test
    @pytest.fixture
    def withdrawAction(self):
        return Transaction("401", "2023-03-23", "Withdraw", 500)

    def test_get_id(self, withdrawAction):
        assert withdrawAction.get_id() == "401"

    def test_get_date(self, withdrawAction):
        assert withdrawAction.get_date() == "2023-03-23"

    def test_get_action(self, withdrawAction):
        assert withdrawAction.get_action_type() == "Withdraw"

    def test_get_amount(self, withdrawAction):
        assert withdrawAction.get_amount() == 500

    def test_eq(self, withdrawAction):
        assert withdrawAction == Transaction("401", "2023-03-23", "Withdraw", 500)