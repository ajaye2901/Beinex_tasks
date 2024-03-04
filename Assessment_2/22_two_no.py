
try :
    first_value = int(input("Enter first Number :"))
    second_value = int(input("Enter second Number :"))
    div = first_value / second_value
    print(div)

except ValueError as e :
    print("Please input intger only",e)
except ZeroDivisionError as e :
    print("Second Number Should Not Be Zero")
except Exception as e :
    print(e)