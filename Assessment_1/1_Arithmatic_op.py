
def Add(a,b) :
    print("Sum = ",a+b)

def Sub(a,b) :
    print("Difference = ",a-b)

def Mul(a,b) :
    print("Product = ",a*b)

def Div(a,b) :
    print("Division = ",a/b)

def Floor(a,b) :
    print("Floor Division = ",a//b)

def Mod(a,b) : 
    print("Reminder = ",a%b)

def Exp(a,b) :
    print("Exponentiation = ",a**b)


def Operations(option) :

    if (option >= 1) and (option <= 7):

        a=float(input("Enter the first no : "))
        b=float(input("Enter the second no : "))

        if option == 1 :
            Add(a,b)
    
        elif option == 2:
            Sub(a,b)
    
        elif option == 3:
            Mul(a,b)

        elif option == 4:
            if b == 0:
                print("The Divisor cannot be Zero. Enter another no")
            else:
                Div(a,b)

        elif option == 5:
            if b == 0:
                print("The Divisor cannot be Zero. Enter another no")
            else:
                Floor(a,b)

        elif option == 6:
            if b == 0:
                print("The Divisor cannot be Zero. Enter another no")
            else:
                Mod(a,b)

        elif option == 7:
            Exp(a,b)
    else:
        print("Choose correct option (1-7)")

print(" \n    Arithmatic Operations           ")

option=int(input("\n  Choose Any option from Below  \n" 
                 
                "\n 1. Addition "
                "\n 2. Subtraction "
                "\n 3. Multiplication "
                "\n 4. Division "
                "\n 5. Floor Division "
                "\n 6. Modulus "
                "\n 7. Exponentiation "
                "\n Option = "))

Operations(option)




