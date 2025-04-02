'''Задача о рюкзаке'''
def selectionSort(arr):
    arrIndex = [i for i in range(len(arr))]
    for i in range(len(arr)):
        indexMin = i
        for j in range(len(arr)):
            if (arr[j] < arr[indexMin]):
                indexMin = j
        if (indexMin != i):
            arr[j], arr[indexMin] = arr[indexMin], arr[j]
            arrIndex[j], arrIndex[indexMin] = arrIndex[indexMin], arrIndex[j]
        print(f'arr = {arr}')
    return arrIndex
def the_backpack_problem():
    n = int(input(("Введите количество предметов:")))
    maxW = int(input(("Введите максимальный вес рюкзака:")))
    arrW = []
    arrP = []
    arrP_W = []
    for i in range(n):
        pi = float(input(f'Введите стоимость {i+1} предмета: '))
        wi = float(input(f'Введите вес {i+1} предмета: '))
        arrW.append(wi)
        arrP.append(pi)
        arrP_W.append(pi/wi)
    sumW = sum(arrW)
    print(f'Суммарный вес всех предметов равен {sumW}')
    arrIndex = selectionSort(arrP_W)
    arrX = [0 for _ in range(n)]
    U = 0
    for i in range(n):
        if ((U + arrW[arrIndex[i]]) < maxW):
            U += arrW[arrIndex[i]]
            arrX[i] = 1
    sumP = 0
    sumW_Pack = 0
    str_taken = "В рюкзак взяты: "
    str_not_taken = "В рюкзак не взяты: "
    for i in range(n):
        if (arrX[i] == 1):
            str_taken += str(arrIndex[i]+1) + ", "
            sumP += arrP[arrIndex[i]]
            sumW_Pack += arrW[arrIndex[i]]
        else:
            str_not_taken += str(arrIndex[i] + 1) + ", "
    print(str_taken[:-2])
    print(str_not_taken[:-2])
    print(f'Суммарная стоимость предметов в рюкзаке = {sumP}')
    print(f'Суммарный вес предметов в рюкзаке = {sumW_Pack}')

# the_backpack_problem()
#
# while True:
#     pass