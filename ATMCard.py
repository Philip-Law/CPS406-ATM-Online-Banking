from User import User
from random import randint

class ATMCard:
    def __init__(self, cardPIN: str, owner: User):
        # Initialize an ATM card object with a card PIN, a random 16-digit card number, and an owner object of class User
        self.card_PIN = cardPIN
        self.card_number = randint(1000000000000000, 9999999999999999)
        self.owner = owner

    def get_PIN(self):
        # Returns the PIN associated with this card
        return self.card_PIN
    
    def get_card_number(self):
        # Returns the 16-digit card number associated with this card
        return self.card_number
    
    def get_user(self):
        # Returns the owner object of class User associated with this card
        return self.owner
