from User import User
from random import randint

class ATMCard:
    def __init__(self, cardPIN, owner_name):
        self.card_PIN = cardPIN
        self.card_number = randint(1000000000000000, 9999999999999999)
        self.owner = User(owner_name, randint(100, 5000), randint(100, 5000))

    def get_PIN(self):
        return self.card_PIN
    
    def get_card_number(self):
        return self.card_number
    
    def get_user(self):
        return self.owner
    
    def verify_card_number(self, check_number):
        return self.card_number == check_number