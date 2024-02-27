class Add :
    def __call__(self, *args,**kwargs) :
        return sum(*args)

add = Add()

total = add([1,2,3,4,5,6])

print(total)
