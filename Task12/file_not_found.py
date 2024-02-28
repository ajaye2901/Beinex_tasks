# 2.Create a program that opens a file and reads its contents. 
# Use a try-except block to handle the FileNotFoundError exception and display a custom error message if the file does not exist.

try : 
    with open(r"C:\Users\ajuaj\Desktop\Beinex\Task12\text_1.txt","r") as fp :
        fp.read()
        print("file found and readed")
    fp.close()

except FileNotFoundError :
    print("Error!! File not found")
