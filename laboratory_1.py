
def expert_assessments(matr_R, matr_el):
    '''Метод экспертных оценок'''
    matr_Z = []
    for i in range(len(matr_R)):
        matr_Z.append(matr_R[i] / sum(matr_R))
    matr_W = []
    for i in range(len(matr_el[0])):
        S = 0
        for j in range(len(matr_el)):
            S += matr_el[j][i] * matr_Z[j]
        matr_W.append(S)
    k = 0
    max_el = matr_W[0]
    for i in range(len(matr_W)):
        print(f'Вес цели {i+1} = {matr_W[i]}')
        if (max_el < matr_W[i]):
            max_el = matr_W[i]
            k = i
    print(f'Лучшая альтернатива - {k+1} с оценкой {max_el}')
    return k

matr_R = [6, 9]
matr = [[0.6, 0.18, 0.19], [0.2, 0.7, 0.12]]
expert_assessments(matr_R, matr)








