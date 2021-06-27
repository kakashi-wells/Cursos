matrix1 = [[1,2,3],[7,8,9],[13,14,15]]
matrix2 = [[4,5,6],[10,11,12],[16,17,18]]

matrix3 = [[1,2,3],[7,8,9],[13,14,15]]


for rowPosition, value in enumerate(matrix1):
    for coluPosition, value2 in enumerate(value):
        matrix3[rowPosition][coluPosition]=value2+matrix2[rowPosition][coluPosition]
print(matrix3)