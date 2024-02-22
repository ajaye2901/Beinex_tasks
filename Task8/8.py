"""8) show class method, static method and instance method with simple example."""

#instance method

class Add_1:

    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b

    def add(self) :
        return self.a+self.b
    
obj = Add_1(10,20)

print(obj.add())


#Class method

class Add_2 :
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b

    @classmethod
    
    def sum_1(cls,a,b) :
        return a+b

print(Add_2.sum_1(10,20))

#static method

class add_3 :
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b

    @staticmethod

    def sum_2(a,b):
        return a+b
    
print(add_3.sum_2(10,20))




        