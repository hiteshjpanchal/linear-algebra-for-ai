#code1
#code to find average of numbers in a list
numbers = [12, 13, 17, 23, 39, 40]
sum = 0
for num in numbers:
    sum = sum + num
average = sum / len(numbers)
print("avarage of numbers in the list is", average)


#code2
#Transpose of a matrix
a = [[1,2,3], 
     [4,5,6],
     [7,8,9]]
rows = len(a)
cols = len(a[0])
transpose = [[0 for _ in range(rows)] for _ in range(cols)] #Created empty matrix with swapped dimensions
for i in range(rows):
  for j in range(cols):
    print(i,j)
    transpose[j][i] = a[i][j]  #this will swap raws and columns
print(transpose)  # this will print transpose of a


#code3 matrix multiplication
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]   # Matrix A
b = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]   # Matrix B
rows_a = len(a)   #raw of matrix a
cols_a = len(a[0]) #column of matrix a
rows_b = len(b)    #row of matrix b
cols_b = len(b[0]) #column of matric b
result = []   #empty result 3 * 3
for i in range(rows_a):
    row = []
    for j in range(cols_b):
        row.append(0)  #put 0 in each raw
    result.append(row)  #put that raw in result matrix
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a): 
            result[i][j] = result[i][j] + a[i][k] * b[k][j]
print(result)