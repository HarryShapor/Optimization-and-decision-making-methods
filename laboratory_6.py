'''Симплексный метод решение задачи линейного программирования'''


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]} \t\t\t', end="")
        print()

def the_simplex_method():
    matr_X = [[0.21,0.35],[0.41,0.54]]
    row = [5.7,12.6]
    column = [80,45]

    simplex_table = [["базис",'Bi']]
    x = len(matr_X)
    for i in range(len(matr_X)-1):
        simplex_table.append([])
        simplex_table[i].append(len(matr_X)+i+1) #xi
        simplex_table[i].append(column[i]) #Bi
        for j in range(len(matr_X[0])):
            simplex_table[i].append(matr_X[i][j])
        if (x == len(matr_X)+i+1):
            simplex_table[i].append(1)
            x += 1
        else:
            simplex_table[i].append(0)
        simplex_table[i].append(0)


    print_matrix(simplex_table)

the_simplex_method()