try :
    value = int(input("Enter a value :"))
    print(value)

except ValueError as e :
    print("Invalid Input..Please Input Integer Only..")
except Exception as e :
    print(e)