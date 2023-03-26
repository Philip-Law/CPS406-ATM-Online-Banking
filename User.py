from Account import Account

class User:
    def __init__(self, name: str, chequing_balance: int, savings_balance: int):
        self.name = name
        self.accounts = [Account(chequing_balance), Account(savings_balance)]

    def get_name(self):
        return self.name

    def get_account(self, account_type: str) -> Account:
        if account_type == 'Chequing':
            return self.accounts[0]
        elif account_type == 'Savings':
            return self.accounts[1]