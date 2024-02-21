"""· Write a Python program to create a file where all letters of English alphabet 
are listed by specified number of letters on each line."""


a="abcdefghijklmnopqrstuvwxyz"
n=4
f=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\4_alphabet.txt",'w')

for i in range(0,len(a),n):
    s=a[i:i+n]
    f.write(s+'\n')