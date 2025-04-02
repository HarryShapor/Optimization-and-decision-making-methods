def sort(arr):
    for i in range(len(arr)-1):
        indexMin = i
        for j in range(i,len(arr)):
            if (arr[j] > arr[indexMin]):
                indexMin = j
        if (indexMin != i):
            arr[i], arr[indexMin] = arr[indexMin], arr[i]
    return arr
def printContainers(matr):
    print("Контейнеры:")
    for i in range(len(matr)):
        print(f'{i+1}: ', end="")
        for j in range(len(matr[i])):
            print(f' {matr[i][j]}', end="\t")
        print(f'\tобщий вес = {sum(matr[i])}')

def first_fit_decreasing():
    n = int(input(("Введите количество предметов:")))
    maxW = int(input(("Введите максимальный вес контейнера:")))
    arrW = []
    for i in range(n):
        wi = float(input(f'Введите вес {i + 1} предмета: '))
        arrW.append(wi)
    arrContainer = []
    arrContainer.append([])
    arrX = []
    while (len(arrX) < n):
        for j in range(n):
            for l in range(len(arrContainer)):
                if (j not in arrX):
                    if ((sum(arrContainer[l]) + arrW[j]) <= maxW):
                        arrContainer[l].append(arrW[j])
                        arrX.append(j)
                        break
                    elif(l < len(arrContainer)-1):
                        continue
                    else:
                        arrContainer.append([])
                        break
    printContainers(arrContainer)

def sort_first_fit_decreasing():
    n = int(input(("Введите количество предметов:")))
    maxW = int(input(("Введите максимальный вес контейнера:")))
    arrW = []
    for i in range(n):
        wi = float(input(f'Введите вес {i + 1} предмета: '))
        arrW.append(wi)
    arrW = sort(arrW)
    arrContainer = []
    arrContainer.append([])
    arrX = []
    while (len(arrX) < n):
        for j in range(n):
            for l in range(len(arrContainer)):
                if (j not in arrX):
                    if ((sum(arrContainer[l]) + arrW[j]) <= maxW):
                        arrContainer[l].append(arrW[j])
                        arrX.append(j)
                        break
                    elif (l < len(arrContainer) - 1):
                        continue
                    else:
                        arrContainer.append([arrW[j]])
                        arrX.append(j)
                        break
    printContainers(arrContainer)

print("Первый подходящий по убыванию:")
first_fit_decreasing()
print("Первый подходящий по убыванию (отсортированный):")
sort_first_fit_decreasing()