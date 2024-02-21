"""· Write a Python program to read a random line from a file."""

import random

f2=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\2_copy.txt","r")
contents=f2.readlines()
f2.close()

if contents:
    print(random.choice(contents))

else:
    print("File is empty")

