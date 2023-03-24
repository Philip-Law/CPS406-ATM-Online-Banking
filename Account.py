from Transaction import Transaction
from random import randint
from datetime import date

class Account:
    def __init__(self, balance: int):
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(date.today(), "Deposit", amount)
        if self.balance <= 0:
            raise ValueError("Invalid Deposit")
        self.transaction_history.append(transaction)
        return transaction

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        transaction = Transaction(date.today(), "Withdraw", amount)
        self.transaction_history.append(transaction)
        return transaction

    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history
    
    
    def add_transaction(self, new_transaction: Transaction) -> None:
        if new_transaction.get_amount() <= 0:
            raise ValueError("Invalid Transaction balance")
        
        self.transaction_history.append(new_transaction)
