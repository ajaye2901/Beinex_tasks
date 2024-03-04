#7. Write a function that takes a list of numbers as input and returns the second-largest number.

def SecondLarge(Lst) :
    if len(Lst)<2 :
        return "List contain less than two elements"
    elif len(set(Lst)) == 1 :
        return "All elements are same"
    else:
        large = Lst[0]
        sec_large = -1
        for item in Lst:
            if item > large:
                sec_large,large = large,item
            elif sec_large < item < large:
                sec_large = item
        return f"Second largest element is {sec_large}"
            
Lst = [5,6,3,9,8]
print(SecondLarge(Lst))