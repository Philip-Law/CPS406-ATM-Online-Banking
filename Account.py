from Transaction import Transaction
from random import randint
from datetime import date

class Account:
    # Starting transaction id
    transaction_id = 10000000

    @classmethod
    def generate_transaction_id(cls):
        # Generate transaction id for every transaction made in account
        cls.transaction_id += 1
        return str(cls.transaction_id)

    def __init__(self, balance: int):
        # Intialize balance and list of transactions
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount: int):
        # Deposit amount to account
        self.balance += amount
        transaction = Transaction(Account.generate_transaction_id(), date.today(), "Deposit", amount)
        self.transaction_history.append(transaction)
        return transaction

    def withdraw(self, amount: int):
        # Withdraw amount to account
        self.balance -= amount
        transaction = Transaction(Account.generate_transaction_id(), date.today(), "Withdraw", amount)
        self.transaction_history.append(transaction)
        return transaction

    def get_balance(self):
        # Get balance of account
        return self.balance
    
    def get_transaction_history(self):
        # Get list of transaction_history
        return self.transaction_history
    
    def add_transaction(self, new_transaction: Transaction):
        # Add transaction to transaction_history list
        self.transaction_history.append(new_transaction)
