# Write a Python function that takes a list of numbers as input and returns 
# the sum of all the numbers divisible by 3 or 5

def SumThreeFive(Lst) :
    count = 0
    for item in Lst :
        if item <= 0:
            continue
        if item % 3 == 0 or item % 5 == 0 :
            count += item
    return count
try:
    items = input("Enter the list items using commas:").split(",")
    Lst = [int(item) for item in items]
    print(SumThreeFive(Lst))
except ValueError :
    print("Invalid input ")