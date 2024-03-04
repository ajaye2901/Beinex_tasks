# Create a class named Notes for handling text-based file operations. Class should contain methods 
# "write", "read" and then "append" as instance methods or class methods. (Can contain any other methods if you wish) 
# Use a single file for saving the notes. You can set the file name as a constant somewhere in the program (Or as a class variable).
# write method should create the if it doesn't exist, Then it should overwrite the older contents 
# with the user input if the user plans to overwrite the file. read method should read the whole file 
# contents and return it. If the file doesn't exist, then it should return "No notes found" append method should take the 
# user input value and it must add the value to the end of the file. It must not overwrite the file. 
# Now create a program to utilize this class. The program should repeatedly ask the user for these 4 choices : 
# 1 - Write Note (Overwrite existing). 
# 2 - Add more Notes (Append). 
# 3 - Read Notes. 
# 4 – Exit

class Notes :
    def __init__(self,filename) :
        self.filename = filename

    def WriteNote(self) :
        try :
            with open(self.filename,"w") as fp :
                self.content = input("Enter the content :")
                fp.write(self.content)
            return "File Writing done"
        except Exception as e :
            print("Error occured",e)
    
    def AddNotes(self) :
        try :
            with open(self.filename,"a") as fp :
                self.content = input("Enter the content :")
                fp.write("\n"+self.content)
            return "File writing done"
        except Exception as e :
            print("Error occured",e)
    
    def ReadFile(self) :
        try :
            with open(self.filename,"r") as fp :
                self.content = fp.read()
            return self.content
        except FileNotFoundError :
            print("No notes Found")
        except Exception as e :
            print("Error occured",e)

filename = 'text.txt'
obj = Notes(filename)

def Operations(option) :
    if option == 1 :
        print(obj.WriteNote())
    elif option == 2 :
        print(obj.AddNotes())
    elif option == 3 :
        print(obj.ReadFile())
    elif option == 4 :
        print("Exiting...")
        exit()
    else :
        print("Choose correct option")

while True :
    print("\n File Operations")
    try :
        options = int(input("Choose any option below \n"
                        "1. Write Note (Overwriting Existing) \n"
                        "2. Add More Notes (Append) \n"
                        "3. Read Notes \n"
                        "4. Exit \n"
                        "Option = ")) 
        Operations(options)
    except ValueError :
        print("Enter a nuemeric value")