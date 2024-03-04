# 3. Search for a String in a Text File

try :
    with open("text.txt","r") as fp :
        contents = fp.readlines()
        for line in contents :
            line = line.lower()
            if "hello" in line.strip() :
                print("string found") 
                break
        else:
            print("sting not found")

except FileNotFoundError as e :
    print(e)