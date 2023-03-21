class Transaction:
    def __init__(self, id, date, action_type, amount):
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