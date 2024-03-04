# 1. Read and Print the Contents of a Text File

try :   
    with open("text.txt","r") as fp :
        print(fp.read())
        
except FileNotFoundError as e:
    print("File not Found.",e)