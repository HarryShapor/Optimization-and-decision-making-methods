class ManeuveringSystem:
    def __init__(self, initial_state, target_state):
        self.initial_state = initial_state
        self.target_state = target_state
        self.visited_states = set()
    def apply_rule(self, state, i, j):
        """
        Применяет правило перестановки Le1e2e3 => Le1e3e2
        i - индекс начала второй группы
        j - индекс начала третьей группы
        """
        if i >= j or j >= len(state):
            return None
        e1 = state[:i]
        e2 = state[i:j]
        e3 = state[j:]
        return e1 + e3 + e2
    
    def get_possible_moves(self, state):
        """Генерирует все возможные состояния после одного маневра"""
        moves = []
        for i in range(len(state)):
            for j in range(i+1, len(state)+1):
                new_state = self.apply_rule(state, i, j)
                if new_state and new_state not in self.visited_states:
                    moves.append((new_state, i, j))
        return moves

    
    def forward_search(self):
        """Прямой вывод - от начального состояния к целевому"""
        queue = [(self.initial_state, [])]  # (состояние, путь)
        self.visited_states = set([self.initial_state])
        while queue:
            current_state, path = queue.pop(0)
            
            if current_state == self.target_state:
                return path
            
            possible_moves = self.get_possible_moves(current_state)
            for new_state, i, j in possible_moves:
                self.visited_states.add(new_state)
                new_path = path + [(current_state, i, j, new_state)]
                queue.append((new_state, new_path))
        
        return None
    
    def backward_search(self):
        """Обратный вывод - от целевого состояния к начальному"""
        queue = [(self.target_state, [])]  # (состояние, путь)
        self.visited_states = set([self.target_state])
        
        while queue:
            current_state, path = queue.pop(0)
            if current_state == self.initial_state:
                # Нужно инвертировать путь, так как идем от цели к началу
                return [(step[3], step[1], step[2], step[0]) for step in reversed(path)]
            possible_moves = self.get_possible_moves(current_state)
            for new_state, i, j in possible_moves:
                self.visited_states.add(new_state)
                new_path = path + [(new_state, i, j, current_state)]
                queue.append((new_state, new_path))
        
        return None
    
    @staticmethod
    def print_solution(path, method_name):
        """Выводит найденное решение"""
        print(f"\n{method_name}:")
        if not path:
            print("Решение не найдено!")
            return
        
        print(f"Найдено решение с {len(path)} маневрами:")
        for step_num, (initial, i, j, result) in enumerate(path, 1):
            print(f"Шаг {step_num}: {initial} => {result} (i={i}, j={j})")


def simulate_maneuver(vector, i, j):
    """
    Имитирует процесс реализации продукционного правила для вектора V
    с заданными индексами i и j
    """
    if i < 0 or j < 0 or i >= j or j >= len(vector):
        print("Ошибка: недопустимые значения индексов")
        return None
    
    e1 = vector[:i]
    e2 = vector[i:j]
    e3 = vector[j:]
    result = e1 + e3 + e2
    
    print(f"Исходный вектор: {vector}")
    print(f"Разбиение: e1={e1}, e2={e2}, e3={e3}")
    print(f"Результат применения правила: {result}")
    
    return result


def solve_task1():
    """Решение задачи 1 - прямой вывод"""
    initial_state = "ABCDEFG"
    target_state = "DEBCFGA"

    system = ManeuveringSystem(initial_state, target_state)
    solution = system.forward_search()
    system.print_solution(solution, "Задача 1 (прямой вывод)")


def solve_task2():
    """Решение задачи 2 - обратный вывод"""
    initial_state = "ABCDEFG"
    target_state = "CADEFGB"
    
    system = ManeuveringSystem(initial_state, target_state)
    solution = system.backward_search()
    system.print_solution(solution, "Задача 2 (обратный вывод)")


def solve_task3():
    """Решение задачи 3 - имитация применения правила"""
    print("\nЗадача 3:")
    vector = input("Введите начальный порядок вагонов (например, ABCDEFG): ")
    
    try:
        i = int(input("Введите индекс i (начало второй группы): "))
        j = int(input("Введите индекс j (начало третьей группы): "))
        simulate_maneuver(vector, i, j)
    except ValueError:
        print("Ошибка: индексы должны быть целыми числами")


def solve_task4():
    """Решение задачи 4 - прямой вывод для произвольных состояний"""
    print("\nЗадача 4:")
    initial_state = input("Введите начальный порядок вагонов (V): ")
    target_state = input("Введите целевой порядок вагонов (W): ")
    if len(initial_state) != len(target_state):
        print("Ошибка: начальный и целевой порядок должны иметь одинаковую длину.")
        return
        
    if not initial_state or not target_state:
        print("Ошибка: порядок вагонов не может быть пустым.")
        return
    system = ManeuveringSystem(initial_state, target_state)
    solution = system.forward_search()
    system.print_solution(solution, f"Задача 4 (прямой вывод: {initial_state} -> {target_state})")


def main():
    print("Программа для решения задачи о маневрировании локомотива")
    print("Реализует продукционное правило: Le1e2e3 => Le1e3e2")
    
    while True:
        print("\nВыберите задачу:")
        print("1. Задача 1 - прямой вывод (ABCDEFG -> DEBCFGA):")
        print("2. Задача 2 - обратный вывод (ABCDEFG -> CADEFGB):")
        print("3. Задача 3 - имитация процесса продукционного правила:")
        print("4. Задача 4 - прямой вывод для произвольных состояний (V -> W):")
        print("0. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            solve_task1()
        elif choice == "2":
            solve_task2()
        elif choice == "3":
            solve_task3()
        elif choice == "4":
            solve_task4()
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main() 