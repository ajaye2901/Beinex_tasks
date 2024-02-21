"""· Write a Python program that takes a text file as input and returns the number of words of a given text file. 
Note: Some words can be separated by a comma with no space."""


f=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\3_words.txt","r")

words=f.read()

f.close()

words=words.replace(",",'')
words=words.split() 

print("No of words in the file is ",len(words))


