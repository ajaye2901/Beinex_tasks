# Create a Python library with the function to input the values with expectation handling and demonstrate with the example.

def input_values(num) :
    try :
        value = float(num)
        return value

    except ValueError as e :
        return "Enter a Number !!" , e
        
