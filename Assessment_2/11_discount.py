# Write a Python function called calculate_discounted_price that takes the  original price of an item and a discount percentage 
# as input. The function should return the discounted price after applying the discount. Ensure that the function handles the case 
# where the discount percentage is negative and raises a custom exception called InvalidDiscountError with an 
# appropriate error message. 

class InvalidDiscountError(Exception) :
    def __init__(self,discount) :
        self.discount = discount
    
    def __str__(self) -> str:
        return "Discount cannot be a megative value"

class Discount :
    def __init__(self,price,discount):
        self.price = price
        self.discount = discount

    def calculate_discounted_price(self) :
        if self.discount < 0 :
            raise InvalidDiscountError(self.discount)
        else :
            final_price = self.price - (self.price*(self.discount/100))
            return final_price

try :
    price = float(input("Enter the price of the item :"))
    discount = int(input("Enter the discount percentage :"))
    obj = Discount(price,discount)
    print("Price after discount :",obj.calculate_discounted_price())

except ValueError :
    print("Enter correct input")
except InvalidDiscountError as e :
    print(e)  