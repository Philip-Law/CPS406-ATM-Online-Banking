from User import User
from random import randint

class ATMCard:
    def __init__(self, cardPIN: str, owner: User):
        self.card_PIN = cardPIN
        self.card_number = randint(1000000000000000, 9999999999999999)
        self.owner = owner

    def get_PIN(self):
        return self.card_PIN
    
    def get_card_number(self):
        return self.card_number
    
    def get_user(self):
        return self.owner