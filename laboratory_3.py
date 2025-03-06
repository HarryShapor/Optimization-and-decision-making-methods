
def transport_problem():
    '''Метод северо-западного угла для решения транспортной задачи.'''
    countStorage = int(input("Введите количество складов: "))
    stocks_in_warehouses = []
    for i in range(countStorage):
        stocks_in_warehouses.append(float(input(f'Введите запас на {i+1} складе:  ')))
    countConsumers = int(input("Введите количество потребителей: "))
    consumer_need = []
    for i in range(countConsumers):
        consumer_need.append(float(input(f'Введите потребность {i+1} потребителя:  ')))
    matrixC = []
    for i in range(countStorage):
        matrixC.append([])
        for j in range(countConsumers):
            matrixC[i].append(float(input(f'Введите стоимость доставки {i+1} склада и {j+1} потребителя:  ')))
    if (sum(stocks_in_warehouses) != sum(consumer_need)):
        return "Потребности не соответствуют запасам!"
    # countStorage = 3
    # countConsumers = 3
    # stocks_in_warehouses = [10,20,30]
    # consumer_need = [15,20,25]
    # matrixC = [[5,3,1], [3,2,4], [4,1,2]]
    stroka = "\t\t "
    for i in range(countConsumers):
        stroka += "Потребитель " + str(i+1) + "\t"
    print(f'Исходная таблица транспортной задачи:')
    stroka += "Запасы на складах"
    print(stroka)
    stroka = ""
    for i in range(countStorage):
        stroka += "Склад " + str(i+1) + "\t\t\t"
        for j in range(countConsumers):
            stroka += str(matrixC[i][j]) + "\t\t\t\t"
        stroka +=  str(stocks_in_warehouses[i]) + "\t\t"
        print(stroka)
        stroka = ""
    stroka = "Потребности \t"
    for i in range(countConsumers):
        stroka += str(consumer_need[i]) + "\t\t\t"
    stroka += str(sum(consumer_need))
    print(stroka)
    matrixTransport = [[0] * countConsumers for _ in range(countStorage)]

    sumC = 0
    i = 0
    j = 0
    while(i < countStorage):
        while(j < countConsumers):
            if (stocks_in_warehouses[i] > consumer_need[j]):
                sumC += consumer_need[j] * matrixC[i][j]
                matrixTransport[i][j] = consumer_need[j]
                stocks_in_warehouses[i] -= consumer_need[j]
                if (stocks_in_warehouses[i] == 0):
                    i += 1
                j += 1
            else:
                sumC += stocks_in_warehouses[i]  * matrixC[i][j]
                matrixTransport[i][j] = stocks_in_warehouses[i]
                consumer_need[j] -= stocks_in_warehouses[i]
                if (consumer_need[j] == 0):
                    j += 1
                i += 1
    stroka = "\t\t\t"
    print(f'Опорный план:')
    for i in range(countConsumers):
        stroka += "Потребитель " + str(i + 1) + "\t"
    print(stroka)
    stroka = ""
    for i in range(countStorage):
        stroka += "Склад " + str(i + 1) + "\t\t\t"
        for j in range(countConsumers):
            stroka += str(matrixTransport[i][j]) + "\t\t\t\t"
        print(stroka)
        stroka = ""
    print(f'Минимальная стоимость доставки  {sumC}')

transport_problem()

# while(True):
#     pass