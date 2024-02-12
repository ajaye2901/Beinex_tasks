"""Define a function that accepts roll number and returns whether the student is present or absent. """


def attendence(roll_no):

    l=[1,2,3,4,6,7,8,9,11,13,14,15] # nos from 1 to 15

    if roll_no in l:
        return True
    else :
        return False
    
roll_no = int(input("Enter the roll no : "))

if attendence(roll_no) == True:
    print("Student is present")
else:
    print("Student is not present")