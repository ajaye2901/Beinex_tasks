def matrix1_elements(row,column,matrix):
    for i in range(row):
        l=[]
        for j in range(column):
            item=int(input("Enter the element : "))
            l.append(item)
        matrix.append(l)
    return matrix

def matrix_multiplication(matrix1,matrix2,row1,column1,column2) : 

    result=[[0 for row in range(column2)] for column in range(row1)]

    for i in range(row1):
        for j in range(column2):
            for k in range(column1):
                result[i][j]+=matrix1[i][k]*matrix2[k][j]
    return result



row1 = int(input("Enter the no of rows of Matrix 1 : "))
column1 = int(input("Enter the no of columns of Matrix 1 : "))

matrix_1=[]
print(matrix1_elements(row1,column1,matrix_1))

row2 = int(input("Enter the no of rows of Matrix 2 : "))
column2 = int(input("Enter the no of columns of Matrix 2 : "))

matrix_2=[]
print(matrix1_elements(row2,column2,matrix_2))

if column1 != row2:
    print("Cannot Multiply")
else:
    print(matrix_multiplication(matrix_1,matrix_2,row1,column1,column2))
    
