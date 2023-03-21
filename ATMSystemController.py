from ATMCard import ATMCard
from Account import Account
from User import User
from Transaction import Transaction

test = [ATMCard(1234, "Dylan"), ATMCard(7682, "Bobby"), ATMCard(1020, "Dylan")]


# Testing ATM Card Database
print(test[0].get_user().get_chequing_account().get_balance())
print(test[0].get_user().get_chequing_account().withdraw(100))
print(test[0].get_user().get_chequing_account().get_balance())