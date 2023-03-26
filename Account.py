from Transaction import Transaction
from random import randint
from datetime import date

class Account:
    transaction_id = 10000000

    @classmethod
    def generate_transaction_id(cls):
        cls.transaction_id += 1
        return str(cls.transaction_id)

    def __init__(self, balance: int):
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(Account.generate_transaction_id(), date.today(), "Deposit", amount)
        if self.balance <= 0:
            raise ValueError("Invalid Deposit")
        self.transaction_history.append(transaction)
        return transaction

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        transaction = Transaction(Account.generate_transaction_id(), date.today(), "Withdraw", amount)
        self.transaction_history.append(transaction)
        return transaction

    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history
    
    
    def add_transaction(self, new_transaction: Transaction) -> None:
        self.transaction_history.append(new_transaction)