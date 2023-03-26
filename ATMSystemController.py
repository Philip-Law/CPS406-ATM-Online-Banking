from ATMCard import ATMCard
from Account import Account
from User import User
from Transaction import Transaction

class ATMSystemController:
    def __init__(self):
        # List of ATM cards
        self.cards = [ATMCard("1234", User("Dixie Normous", 5000, 4000)), 
        ATMCard("7682", User("Phuc Yu", 1000, 10)), ATMCard("1020", User("Sal Ami", 4200, 590)), 
        ATMCard("3976", User("Yoshie Takeshita", 4080, 1080)), ATMCard("2396", User("Jack Daniels", 1998, 1875))]

    def get_cards(self):
        return self.cards

    def verify_PIN(card: ATMCard, test_PIN: str) -> bool:
        return card.get_PIN() == test_PIN

    def find_card(self, name: str, card_number: int, card_pin: str) -> ATMCard:
        for card in self.cards:
            if card.get_user().get_name() == name and card.get_card_number() == card_number and card_pin == card.get_PIN():
                return card

    def withdraw_amount(self, account_type: str, card: ATMCard, amount: int) -> Transaction:
        account = card.get_user().get_account(account_type)

        if account.get_balance() < amount or amount <= 0:
            raise ValueError("Invalid Amount")
        
        return account.withdraw(amount)

    def deposit_amount(self, account_type: str, card: ATMCard, amount: int) -> Transaction:
        account = card.get_user().get_account(account_type)

        if amount <= 0:
            raise ValueError("Invalid Amount")
        
        return account.deposit(amount)

# Testing ATM Card Database
# print(cards[0].get_user().get_chequing_account().get_balance())
# print(self.cards[0].get_user().get_chequing_account().withdraw(100))
# print(self.cards[0].get_user().get_chequing_account().get_balance())
