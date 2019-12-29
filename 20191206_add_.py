matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

def add(m1, m2):
    "Adding 2 matrices together"
    result = []
    for i in range(len(m1)):
        for ii in range(len(m1[i])):
            result.append(m1[i][ii] + m2[i][ii])
    return result

print(add(matrix1, matrix2))
