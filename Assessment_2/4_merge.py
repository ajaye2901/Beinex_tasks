# 4. Merge Multiple Text Files into One

file_path = ['text_1.txt','text_2.txt','text_3.txt']
try :
    with open(r'text.txt',"w+") as fp1 :
        for file in file_path :
            with open(file,'r') as fp2:
                contents = fp2.read()
                fp1.write(contents)
                
except FileNotFoundError as e :
    print(e)