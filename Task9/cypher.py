# Create a class named Cypher. The purpose of that class is to receive an input string of characters and convert it to 
# another cypher string. Use a constructor to receive the input. You can also read the input from user. But don’t use 
# input() inside the constructor. 
# The class must have a class method to do the string conversion. And an instance method to invoke the classmethod 
# from within it.
# • Use the below conversion logic:
# • Iterate over each character in the string, and if the character is a digit increment it by one (0->1, 1-
# >2, ... 9 should be replaced with 0)
# • if the character is an alphabet then shift the character by 2 positions (use chr() and ord() built-ins for 
# this) (a->c, b->d, ... y->a, z->b) If the character is in upper case convert it to lower and vice versa
# • The returned string must be of same length as the input. 
# No need to implement the reversing algorithm but will be a plus if available.
# 1) create an object for the Cypher class with the string.
# 2) call the instance method, which should internally call the classmethod you prepared for the conversion, pass the 
# string data to classmethod and do the conversion.
# No need to consider special characters for now.
# Expected output for the string "ABcD1293Z" is "cdEf2304b


class Cypher :

    def __init__(self,msg) -> None:
        self.msg = msg

    @classmethod

    def convert(cls,msg) : 

        conv_msg = ""

        for i in msg :

            if i.isdigit() :
                conv_msg = conv_msg  + str((int(i) + 1) % 10)

            elif i.isalpha() :
                if i.islower() :
                    shift = chr((ord(i) - ord('a') + 2) % 26 + ord('a')) 
                    shift = shift.upper()
                else:
                    shift = chr(((ord(i) - ord('A') + 2) % 26) + ord('A'))
                    shift = shift.lower()
                conv_msg += shift

            else:
                conv_msg += i
        return conv_msg
    
msg=input("Enter your message : ")

print(Cypher.convert(msg))

