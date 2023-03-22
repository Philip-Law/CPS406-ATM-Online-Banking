from Transaction import Transaction

class TestTransaction:
    def test_get_id(self):
        withdrawAction = Transaction("401", "03/22/2023", "withdraw", 500)
        assert withdrawAction.get_id() == "401"

    def test_get_date(self):
        withdrawAction = Transaction("401", "03/22/2023", "withdraw", 500)
        assert withdrawAction.get_date() == "03/22/2023"

    def test_get_action(self):
        withdrawAction = Transaction("401", "03/22/2023", "withdraw", 500)
        assert withdrawAction.get_action_type() == "withdraw"
    
    def test_get_amount(self):
        withdrawAction = Transaction("401", "03/22/2023", "withdraw", 500)
        assert withdrawAction.get_amount() == 500