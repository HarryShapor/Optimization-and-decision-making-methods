def _create_tableau(n, m, c, A, b):
    tableau = [[0.0 for _ in range(n + m + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            tableau[i][j] = A[i][j]
    for i in range(m):
        tableau[i][n + i] = 1.0
    for i in range(m):
       tableau[i][-1] = b[i]
    for j in range(n):
        tableau[-1][j] = -c[j]
    return tableau

def _find_pivot_column(tableau):
    last_row = tableau[-1][:-1]
    min_val = min(last_row)
    if min_val < 0:
        return last_row.index(min_val)
    return None


def _find_pivot_row(tableau, pivot_col, m):
    ratios = []
    for i in range(m):
        if tableau[i][pivot_col] > 0:
            ratio = tableau[i][-1] / tableau[i][pivot_col]
            ratios.append((ratio, i))
    if ratios:
        return min(ratios, key=lambda x: x[0])[1]
    return None


def _pivot(pivot_row, pivot_col,tableau, basis):
    pivot_value = tableau[pivot_row][pivot_col]
    for j in range(len(tableau[0])):
        tableau[pivot_row][j] /= pivot_value
    for i in range(len(tableau)):
        if i != pivot_row:
            factor = tableau[i][pivot_col]
            for j in range(len(tableau[0])):
                tableau[i][j] -= factor * tableau[pivot_row][j]
    basis[pivot_row] = pivot_col

def round_solution(solution, A, b):
    rounded_solution = [round(x) for x in solution]

    for i in range(len(A)):
        used = sum(A[i][j] * rounded_solution[j] for j in range(len(rounded_solution)))
        if used > b[i]:
            while used > b[i] and any(x > 0 for x in rounded_solution):
                max_ratio = 0
                max_index = 0
                for j in range(len(rounded_solution)):
                    if rounded_solution[j] > 0:
                        ratio = A[i][j] / rounded_solution[j]
                        if ratio > max_ratio:
                            max_ratio = ratio
                            max_index = j
                
                rounded_solution[max_index] -= 1
                used = sum(A[i][j] * rounded_solution[j] for j in range(len(rounded_solution)))
    
    return rounded_solution

def solve(A, b, c):
    m = len(A)
    n = len(A[0])
    basis = list(range(n, n + m))
    tableau = _create_tableau(n, m, c, A, b)
    while True:
        pivot_col = _find_pivot_column(tableau)
        if pivot_col is None:
            break
        pivot_row = _find_pivot_row(tableau,pivot_col, m)
        if pivot_row is None:
            print("Задача неограниченна")
            return None
        _pivot(pivot_row, pivot_col, tableau, basis)
    solution = [0.0] * n
    for i, j in enumerate(basis):
        if j < n:
            solution[j] = tableau[i][-1]
    return solution

def main():
    c = [5.7, 12.6]

    A = [
        [0.21, 0.35],
        [0.41, 0.54]
    ]

    b = [80, 45]

    solution = solve(A, b, c)
    if solution is not None:
        rounded_solution = round_solution(solution, A, b)
        
        print("Оптимальное решение (целые числа):")
        print(f"Количество столов: {rounded_solution[0]}")
        print(f"Количество шкафов: {rounded_solution[1]}")

        max_profit = sum(c[i] * rounded_solution[i] for i in range(len(rounded_solution)))
        print(f"Максимальный доход: {max_profit:.2f}")

        used_coniferous = A[0][0] * rounded_solution[0] + A[0][1] * rounded_solution[1]
        used_deciduous = A[1][0] * rounded_solution[0] + A[1][1] * rounded_solution[1]
        
        print("\nИспользование древесины:")
        print(f"Хвойные породы: {used_coniferous:.2f} м³ (из {b[0]} м³)")
        print(f"Лиственные породы: {used_deciduous:.2f} м³ (из {b[1]} м³)")
        remaining_coniferous = b[0] - used_coniferous
        remaining_deciduous = b[1] - used_deciduous
        
        print("\nОстаток древесины:")
        print(f"Хвойные породы: {remaining_coniferous:.2f} м³")
        print(f"Лиственные породы: {remaining_deciduous:.2f} м³")


if __name__ == "__main__":
    main()