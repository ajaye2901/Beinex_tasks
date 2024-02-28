# 9.Write a Python program that prompts the user to enter their age. 
# Define a custom exception called InvalidAgeError that is raised when the entered age is less than 0 or greater than 150. 
# Handle the InvalidAgeError exception and display an appropriate error message.

class Invalid_age_error(Exception) :

    def __init__(self, age : int) :
        self.age = age

    def __str__(self) -> str:
        return "Invalid age. Age must be in between 0 and 150"
    
def age_check(age) :

    if age < 0 or age > 150 :
        raise Invalid_age_error(age)
    
    print("Age :")

try :
    age = int(input("Enter the age :"))
    age_check(age)

except ValueError:
    print("Age must be an integer. Please enter an integer")
except Invalid_age_error as e :
    print(e)
