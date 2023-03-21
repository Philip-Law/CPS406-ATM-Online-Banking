from Transaction import Transaction
from random import randint
from datetime import date

class Account:
    def __init__(self, balance: int):
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(randint(10000000, 99999999), date.today(), "Deposit", amount)
        self.transaction_history.append(transaction)
        return transaction

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        transaction = Transaction(randint(10000000, 99999999), date.today(), "Withdraw", amount)
        self.transaction_history
        return transaction

    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history