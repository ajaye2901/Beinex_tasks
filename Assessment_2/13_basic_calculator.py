# Implement a program that simulates a basic calculator, allowing users to perform arithmetic operations 
# (addition, subtraction, multiplication, division) on two numbers.

class Calculator :

    @staticmethod
    def Add(first,second) :
        Sum = first + second
        return Sum
    @staticmethod
    def Difference(first,second) :
        Diff = first - second
        return Diff
    @staticmethod
    def Product(first,second) :
        Pro = first * second
        return Pro
    @staticmethod
    def Division(first,second) :
        if second == 0 :
            raise ZeroDivisionError
        Div = first / second
        return Div

def Operations(option) :
    if (option >= 1) and (option <= 4):

        first = float(input("Enter the first no : "))
        second = float(input("Enter the second no : "))

        if option == 1:
            print("Sum =",Calculator.Add(first,second))
        elif option == 2:
            print("Difference =",Calculator.Difference(first,second))
        elif option == 3:
            print("Product =",Calculator.Product(first,second))
        elif option == 4:
            print("Division =",Calculator.Division(first,second))
    elif option == 5:
            print("Exiting")
            exit()
    else:
        print("Choose correct Option ")
while True :
    print(" \n    Arithmatic Operations           ")
    option=int(input("\n  Choose Any option from Below  \n"        
                "\n 1. Addition "
                "\n 2. Subtraction "
                "\n 3. Multiplication "
                "\n 4. Division "
                "\n 5. Exit "
                "\n Option = "))
    try :
        Operations(option)
    except ValueError :
        print("Enter a numeric Value")
    except ZeroDivisionError :
        print("This no cannot be zero")