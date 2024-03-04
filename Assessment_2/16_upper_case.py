# Count the total number of uppercase characters in a file in Python

try :
    filename = 'text_1.txt'
    with open(filename,"r") as fp :
        count = 0
        for words in fp:
            for chara in words :
                if chara.isupper() :
                    count += 1
        print("Uppercase characters =",count)

except FileNotFoundError as e :
    print("File not found")
except Exception as e:
    print("Error occured",e)


