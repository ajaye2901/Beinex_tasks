# 5. Implement a program that reads a text file and counts the occurrences of each word, ignoring case sensitivity. 

try :
    with open('text.txt',"r") as fp :
        contents = fp.readlines()
        count_dict={}
        words_in_lines = [line.split() for line in contents]
        for line in words_in_lines :
            for words in line :
                words=words.lower()
                if words not in count_dict :
                    count_dict[words] = 1
                    count = 1
                else :
                    count_dict[words] += 1
        print(count_dict)

except FileNotFoundError as e :
    print(e)
except Exception as e :
    print(e)