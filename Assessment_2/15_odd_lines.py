# Copy odd lines of one file to another file in Python
file_1 = "text.txt"
file_2 = "text_1.txt"

try :
    with open(file_1,"r") as fp:
        line_no = 1
        contents = ''

        for line in fp.readlines() :
            if line_no % 2 != 0 :
                contents+=line
            line_no += 1

    if contents:    
        with open(file_2,'w') as fp2 :
            fp2.write(contents)
            print("Successfull")
    else:
        print("File is empty")

except FileNotFoundError as e :
    print("File not found",e)
except Exception as e :
    print("Error occured",e)


