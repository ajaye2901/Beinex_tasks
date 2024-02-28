# 5.Write a program that opens a file, reads its contents, and writes the contents to a new file. 
# Use a try-except-finally block to ensure that the file is closed even if an exception occurs during the file operations.

try :
    with open(r"C:\Users\ajuaj\Desktop\Beinex\Task12\text_1.txt","r+") as file_1 :
        contents = file_1.read() 

    try :
        with open(r"C:\Users\ajuaj\Desktop\Beinex\Task12\text_2.txt","w+") as file_2 :
            file_2.write(contents)
    
    except FileNotFoundError:
        print("Can't find the file that to be written check path again")

except FileNotFoundError:
    print("Can't find the file check path ")

finally :
    file_1.close()
    file_2.close()

