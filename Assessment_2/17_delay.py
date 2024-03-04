# Python program to delay printing of line from a file using sleep function

import time

filename = 'text_1.txt'
try :
    delay = int(input("Enter the delay in seconds :"))
    with open(filename,"r") as fp :
        time.sleep(delay)
        for line in fp :
            print(line.strip())
        
except ValueError:
    print("Enter seconds as an integer")
except FileNotFoundError:
    print("File not found on path")
except Exception as e :
    print("Error occured",e)