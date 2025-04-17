def solve_furniture_problem():
    c = [5.7, 12.6]
    A = [
        [0.21, 0.41],
        [0.35, 0.54]
    ]
    b = [80, 45]
    m = len(A)
    n = len(c)
    tableau = []
    tableau.append([-x for x in c] + [0])
    for i in range(m):
        tableau.append(A[i] + [b[i]])
    while True:
        min_val = float('inf')
        pivot_col = -1
        for j in range(n):
            if tableau[0][j] < min_val:
                min_val = tableau[0][j]
                pivot_col = j
        if (min_val >= 0):
            pivot_col = -1
        if pivot_col == -1:
            break
        min_ratio = float('inf')
        pivot_row = -1
        for i in range(1, m + 1):
            if tableau[i][pivot_col] > 0:
                ratio = tableau[i][-1] / tableau[i][pivot_col]
                if ratio < min_ratio:
                    min_ratio = ratio
                    pivot_row = i
        if pivot_row == -1:
            print("Задача не имеет решения")
            return None
        pivot_value = tableau[pivot_row][pivot_col]
        for j in range(len(tableau[pivot_row])):
            tableau[pivot_row][j] /= pivot_value
        for i in range(len(tableau)):
            if i != pivot_row:
                factor = tableau[i][pivot_col]
                for j in range(len(tableau[i])):
                    tableau[i][j] -= factor * tableau[pivot_row][j]
    solution = [0] * n
    for j in range(n):
        column = [tableau[i][j] for i in range(len(tableau))]
        if sum(1 for x in column if abs(x) < 1e-10) == len(column) - 1:
            for i in range(1, len(tableau)):
                if abs(tableau[i][j] - 1) < 1e-10:
                    solution[j] = tableau[i][-1]
                    break
    if solution:
        print("Оптимальное решение найдено.")
        print(f"Количество столов: {solution[0]:.0f} шт.")
        print(f"Количество шкафов: {solution[1]:.0f} шт.")
        profit = sum(c[i] * solution[i] for i in range(len(solution)))
        print(f"Максимальная прибыль: {profit:.0f} руб.")

        used_resources = [sum(A[i][j] * solution[j] for j in range(len(solution))) for i in range(len(A))]
        print("\nИспользование ресурсов:")
        print(f"Использовано хвойной древесины: {used_resources[0]:.1f} куб.м из {b[0]} куб.м")
        print(f"Использовано лиственной древесины: {used_resources[1]:.1f} куб.м из {b[1]} куб.м")
    else:
        print("Решение не найдено!")

if __name__ == "__main__":
    solve_furniture_problem()
    while True:
        pass