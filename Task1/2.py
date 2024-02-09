"""Python Program to replicate bank transaction: min balance 500, ask user to the amount to withdraw, 
print the balance amount after withdrawal, if user enters an amount greater than balance: print:: insufficient balance. 
if balance is below 500 print an alert message : your account balance is "available_balance",
 Please  keep your account balance above Rs.500 to avoid unwanted charges."""

def Bank(Initial_amt,withdraw_amt) :

    if Initial_amt<withdraw_amt:
        print("Insufficient Balance")
    
    else:
        current_amt=Initial_amt-withdraw_amt
        if current_amt<500:
            print("Available balance is ",current_amt,"Please  keep your account balance above Rs.500 to avoid unwanted charges.")
        else:
            print("Withdraw Successfull","Remaining Balance is",current_amt)
            # print("Remaining Balance is",current_amt)


Initial_amt=float(input("Enter Your Initial Amount : "))
withdraw_amt=float(input("Enter the Amount You Want to withdraw : "))

Bank(Initial_amt,withdraw_amt)

