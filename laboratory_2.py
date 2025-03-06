import statistics
def method_arg_ballov():
    '''Метод средних баллов, для оценки рангов проектов экспертами'''
    experts = int(input("Введите количество экспертов"))
    projects = int(input("Введите количество проектов"))
    matr = []
    matr_sum_ballov = []
    matr_rank = []
    for i in range(projects):
        print(f'Введите оценки {i+1} проекта:')
        matr.append([])
        s = 0
        for j in range(experts):
            matr[i].append(int(input(f'Оценка {j+1} эксперта:')))
            s += matr[i][j]
        matr_sum_ballov.append(s)
        matr_rank.append([i+1,s/experts])
    for i in range(len(matr_rank)):
        print(f'Проект {matr_rank[i][0]} имеет среднее арифметическое рангов = {matr_rank[i][1]}')
    for i in range(1,len(matr_rank)):
        if (matr_rank[i-1][1] > matr_rank[i][1]):
            matr_rank[i-1], matr_rank[i] = matr_rank[i], matr_rank[i-1]
    for i in range(1,len(matr_rank)):
        if (matr_rank[i-1][1] == matr_rank[i][1]):
            matr_rank[i].append((i+i-1)/2)
            matr_rank[i-1].append((i + i-1) / 2)
        else:
            matr_rank[i].append(i)
            if (i == 1):
                matr_rank[i-1].append(i-1)
    for i in range(len(matr_rank)):
        print(f'Проект {matr_rank[i][0]} имеет итоговый ранг по среднему арифметическому = {matr_rank[i][2]+1}')
    return matr

def method_medians_ranks(matr):
    '''Метод медианных рангов'''
    matr_median = []
    for i in range(len(matr)):
        matr[i].sort()
        matr_median.append(statistics.median(matr[i]))
    for i in range(len(matr_median)):
        print(f'Проект {i} имеет медианный ранг = {matr_median[i]}')
    for i in range(1, len(matr_median)):
        if (matr_median[i - 1] == matr_median[i]):
            matr_median[i] = ((matr_median[i] + matr_median[i - 1]) / 2)
            matr_median[i - 1] = ((matr_median[i] + matr_median[i - 1]) / 2)
    for i in range(len(matr_median)):
        print(f'Проект {i} имеет итоговый ранг по медианам = {matr_median[i]}')
matr1 = method_arg_ballov()
method_medians_ranks(matr1)

while(True):
    pass