lst_1 = [1,2,4,5,9,6]
lst_2 = [1,4,0,3]

lst_3=[]

for i in lst_1:
    for j in lst_2:
        if i==j :
            lst_3.append(i)
print(lst_3)