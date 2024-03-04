# 2. Count the Number of Lines, Words, and Characters in a Text File

def WordCount(contents) :
    words = contents.split("\n")
    print("words = ",len(words))
    char_counts = 0
    for word in words :
        for char in word :
            char_counts += 1
    print("characters = ",char_counts)

try : 
    with open("text.txt","r") as fp :
        print("lines = ",len(fp.readlines()))
        fp.seek(0)
        contents = fp.read()
        WordCount(contents)

except FileNotFoundError as e :
    print("File not Found.",e)