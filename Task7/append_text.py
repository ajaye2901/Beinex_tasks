"""· Write a Python program to append text to a file and display the text."""

s = input("Enter the text : ")

f=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\1_read.txt",'a+')
f.write("\n"+s)
f.close()


f=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\1_read.txt",'r')
print(f.read())
f.close()





