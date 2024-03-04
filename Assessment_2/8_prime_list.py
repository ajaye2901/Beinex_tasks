#  Write a Python program that takes a list of integers as input and returns a 
# new list with only the numbers that are prime. 

class Prime :
    def __init__(self,Lst) :
        self.Lst = Lst
        self.prime = []

    def check_prime(self) :
        for item in self.Lst :
            if not isinstance(item,int) or item <=1 :
                continue
            for num in range(2,item) :
                if item % num == 0 :
                    break
            else:
                self.prime.append(item)
        return self.prime
    
Lst = ['a',2,3,4,5,6,9,-1,-2]
obj = Prime(Lst)
print(obj.check_prime())