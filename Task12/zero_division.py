# 3.Write a program that calculates the division of two numbers entered by the user. Use a try-except block to handle the
#  ZeroDivisionError exception and display an appropriate error message if the user tries to divide by zero.

first_no = float(input("Enter first no :"))
second_no = float(input("Enter the second no :"))

try :
    div = first_no / second_no
    print(f"{first_no} divided by {second_no} is ",div)

except ZeroDivisionError :
    print("Divisor/second no cannot be zero. Enter a valid input")
