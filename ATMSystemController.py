from ATMCard import ATMCard
from Account import Account
from User import User
from Transaction import Transaction

class ATMSystemController:
    def __init__(self):
    # List of ATM cards
        self.cards = [ATMCard("1234", "Dylan"), ATMCard("7682", "Bobby"), ATMCard("1020", "Dylan")]


    def verify_PIN(card: ATMCard, test_PIN: str) -> bool:
        return card.get_PIN() == test_PIN

    def withdraw_amount(account_type: str, card: ATMCard, amount: int) -> Transaction:
        if account_type == "Chequing":
            account = card.get_user().get_chequing_account()
        elif account_type == "Savings":
            account = card.get_user().get_savings_account()

        if account.get_balance() < amount:
            return ValueError("Insufficient balance")
        
        return account.withdraw(amount)

    def deposit_amount(account_type: str, card: ATMCard, amount: int) -> Transaction:
        if account_type == "Chequing":
            account = card.get_user().get_chequing_account()
        elif account_type == "Savings":
            account = card.get_user()
        if amount <= 0:
            return ValueError("Invalid amount")
        
        return account.deposit(amount)

# These are ui functions
# def print_receipt():
#     pass

# def print_statement():
#     pass

# def PIN_screen():
#     pass

# Testing ATM Card Database
# print(cards[0].get_user().get_chequing_account().get_balance())
# print(self.cards[0].get_user().get_chequing_account().withdraw(100))
# print(self.cards[0].get_user().get_chequing_account().get_balance())
