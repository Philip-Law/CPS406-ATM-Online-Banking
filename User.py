from Account import Account

class User:
    def __init__(self, name: str, chequing_balance: int, savings_balance: int):
        self.name = name
        self.accounts = [Account(chequing_balance), Account(savings_balance)]

    def get_chequing_account(self):
        return self.accounts[0]
    
    def get_savings_account(self):
        return self.accounts[1]