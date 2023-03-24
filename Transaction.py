class Transaction:
    transaction_number = 10000000

    @classmethod
    def update_transaction_number(cls):
        cls.transaction_number += 1
        return str(cls.transaction_number)


    def __init__(self, date: str, action_type: str, amount: int, id=None):
        if id == None:
            self.id = self.update_transaction_number()
        else:
            self.id = id
            
        self.date = date
        self.action_type = action_type
        self.amount = amount


    def get_id(self):
        return self.id
    
    def get_date(self):
        return self.date

    def get_action_type(self):
        return self.action_type
    
    def get_amount(self):
        return self.amount
    
    def __eq__(self, __o: object) -> bool:
        return self.id == __o.get_id() and self.date == __o.get_date() and self.action_type == __o.get_action_type() and self.amount == __o.get_amount()