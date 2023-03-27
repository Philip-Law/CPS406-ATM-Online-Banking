class Transaction:

    def __init__(self, id: str, date: str, action_type: str, amount: int):
        # Intialize instance variables
        self.id = id
        self.date = date
        self.action_type = action_type
        self.amount = amount

    def get_id(self):
        # Get transaction id
        return self.id
    
    def get_date(self):
        # Get transaction date
        return self.date

    def get_action_type(self):
        # Get transaction type
        return self.action_type
    
    def get_amount(self):
        # Get transaction amount
        return self.amount
    
    def __eq__(self, __o: object) -> bool:
        # Equal function for Transaction
        return self.id == __o.get_id() and self.date == __o.get_date() and self.action_type == __o.get_action_type() and self.amount == __o.get_amount()
