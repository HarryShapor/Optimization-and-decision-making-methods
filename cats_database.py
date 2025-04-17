class Cat:
    def __init__(self, name, short_hair, long_hair, size_small, size_large, fluffy_tail, blue_eyes, active):
        self.name = name
        self.characteristics = [
            1 if short_hair == "Да" else 0,
            1 if long_hair == "Да" else 0,
            1 if size_small == "Да" else 0,
            1 if size_large == "Да" else 0,
            1 if fluffy_tail == "Да" else 0,
            1 if blue_eyes == "Да" else 0,
            1 if active == "Да" else 0
        ]

def create_cats_database():
    cats = [
        Cat("Персидская", "Нет", "Да", "Нет", "Да", "Да", "Да", "Нет"),
        Cat("Сиамская", "Да", "Нет", "Да", "Нет", "Нет", "Да", "Да"),
        Cat("Мейн-кун", "Нет", "Да", "Нет", "Да", "Да", "Нет", "Да"),
        Cat("Британская короткошерстная", "Да", "Нет", "Нет", "Да", "Нет", "Да", "Нет"),
        Cat("Шотландская вислоухая", "Да", "Нет", "Да", "Нет", "Да", "Да", "Нет"),
        Cat("Бенгальская", "Да", "Нет", "Нет", "Да", "Да", "Нет", "Да"),
        Cat("Русская голубая", "Да", "Нет", "Да", "Нет", "Да", "Да", "Да"),
        Cat("Рэгдолл", "Нет", "Да", "Нет", "Да", "Да", "Да", "Да"),
        Cat("Абиссинская", "Да", "Нет", "Да", "Нет", "Нет", "Нет", "Да"),
        Cat("Сфинкс", "Да", "Нет", "Да", "Нет", "Нет", "Да", "Да")
    ]
    return cats

def print_cats_table(cats):
    # Заголовки столбцов
    headers = ["№", "Название породы", "Короткошерстная", "Длинношерстная", 
              "Размер <4кг", "Размер >6кг", "Пушистый хвост", "Голубые глаза", "Активный"]
    
    # Ширина столбцов
    col_widths = [3, 25, 15, 15, 12, 12, 15, 13, 10]
    
    # Печать заголовка
    header_line = ""
    separator_line = ""
    for width in col_widths:
        header_line += "+" + "-" * width
        separator_line += "+" + "-" * width
    header_line += "+"
    separator_line += "+"
    
    print(header_line)
    header_row = "|"
    for header, width in zip(headers, col_widths):
        header_row += f"{header:<{width}}|"
    print(header_row)
    print(separator_line)
    
    # Печать данных
    for i, cat in enumerate(cats, 1):
        row = f"|{i:<3}|{cat.name:<25}|"
        for char in cat.characteristics:
            value = "Да" if char == 1 else "Нет"
            row += f"{value:<15}|"
        print(row)
        print(separator_line)

def print_characteristics_table(cats):
    print("\nТаблица характеристик пород (в бинарном виде):\n")
    headers = ["Характеристики"] + [str(i) for i in range(1, len(cats) + 1)]
    characteristics = [
        "Короткошерстная",
        "Длинношерстная",
        "Размер <4кг",
        "Размер >6кг",
        "Пушистый хвост",
        "Голубые глаза",
        "Активный"
    ]

    print("+", "-" * 20, "+", "-" * (len(cats) * 4 - 1), "+", sep="")
    print("|{:<20}|".format("Характеристики"), end="")
    for i in range(len(cats)):
        print("{:^3}|".format(i + 1), end="")
    print()
    print("+", "-" * 20, "+", "-" * (len(cats) * 4 - 1), "+", sep="")

    for i, char in enumerate(characteristics):
        print("|{:<20}|".format(char), end="")
        for cat in cats:
            print("{:^3}|".format(cat.characteristics[i]), end="")
        print()
    print("+", "-" * 20, "+", "-" * (len(cats) * 4 - 1), "+", sep="")

    print("|{:<20}|".format("Порода"), end="")
    for i in range(len(cats)):
        print("{:^3}|".format(i + 1), end="")
    print()
    print("+", "-" * 20, "+", "-" * (len(cats) * 4 - 1), "+", sep="")

def find_cat_breed():
    questions = [
        "Кошка короткошерстная?",
        "Кошка длинношерстная?",
        "Размер кошки меньше 4 кг?",
        "Размер кошки больше 6 кг?",
        "У кошки пушистый хвост?",
        "У кошки голубые глаза?",
        "Кошка активная?"
    ]
    
    user_answers = []
    print("\nОтветьте на следующие вопросы (да/нет):")
    
    for question in questions:
        while True:
            answer = input(f"{question} ").lower()
            if answer in ['да', 'нет']:
                user_answers.append(1 if answer == 'да' else 0)
                break
            else:
                print("Пожалуйста, ответьте 'да' или 'нет'")
    cats = create_cats_database()
    matching_breeds = []
    
    for cat in cats:
        if user_answers == cat.characteristics:
            matching_breeds.append(cat.name)
    
    print("\nРезультаты поиска:")
    if matching_breeds:
        print("Подходящие породы:")
        for breed in matching_breeds:
            print(f"- {breed}")
    else:
        print("Извините, нет данных")

def main():
    cats = create_cats_database()
    print("\nТаблица пород кошек и их характеристик:\n")
    print_cats_table(cats)
    print_characteristics_table(cats)
    
    while True:
        choice = input("\nХотите определить породу кошки? (да/нет): ").lower()
        if choice == 'да':
            find_cat_breed()
        elif choice == 'нет':
            break
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'")

if __name__ == "__main__":
    main() 