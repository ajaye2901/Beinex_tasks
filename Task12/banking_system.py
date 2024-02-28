# 10.Write a Python program that simulates a banking system. 
# Implement a class called BankAccount with methods to initialize an account with a starting balance, 
# withdraw funds, and handle a custom exception called NegativeBalanceError when the account balance goes below zero.

class NegativeBalanceError(Exception) :
    def __init__(self, balance : float) :
        self.balance = balance
    
    def __str__(self) -> str:
        return "Negative Balance, Can't withdraw"

class BankAccount :
    def __init__(self,balance = 500) :
        self.balance = balance
    
    def update_balance(self,amount) :
        if amount > self.balance :
            raise NegativeBalanceError(self.balance)
        else :
            self.balance -= amount
            print("Withdraw Successfull. Remaining balance",self.balance)

try :
    amount = float(input("Enter the amount you want to withdraw :"))
    bank = BankAccount()
    bank.update_balance(amount)

except ValueError :
    print("Enter a numeric value")
except NegativeBalanceError as e:
    print(e)

