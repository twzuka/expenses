import sys
import json


commands = {"add", "add-category", "list", "total", "help"}

FILE_NAME = "data.json"


def check_len(string, length):
    return len(string) <= length


def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        data = {}
    return data


def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def print_commands():
    print("--- СПИСОК ВСЕХ КОМАНД ---")
    print("1. Добавить расход: «python expenses.py add <стоимость> <категория> <название>»")
    print("2. Добавить категорию: «python expenses.py add-category <категория>»")
    print("3. Показать все расходы: «python expenses.py list [категория]»")
    print("4. Показать сумму расходов: «python expenses.py total  [категория]»")


def add_category(category):
    if not check_len(category, 20):
        print("Ошибка: название категории слишком длинное! Максимум 20 символов.")
        sys.exit(1)

    low_category = category.lower()
    data = load_data()
    
    if low_category not in data:
        data[low_category] = []
        save_data(data)
    else:
        print(f"Ошибка: Категория '{category}' уже существует!")


def add(price, category, item_name):
    if not check_len(category, 20):
        print("Ошибка: название категории слишком длинное! Максимум 20 символов.")
        sys.exit(1)

    if not check_len(item_name, 30):
        print("Ошибка: название расхода слишком длинное! Максимум 30 символов.")
        sys.exit(1)

    low_category = category.lower()

    try:
        int_price = int(price)
        
        if int_price < 0:
            print(f"Ошибка: Число {int_price} отрицательное!")
            sys.exit(1)
            
    except ValueError:
        print("Ошибка: Введено не число!")
        sys.exit(1)
        
    data = load_data()
    
    if low_category in data:
        data[low_category].append([int_price, item_name])
        save_data(data)
    else:
        print(f"Ошибка: Категории {category} не существует!")


def list_expenses(argument):
    data = load_data()

    if not argument or not argument.strip():
        print("--- ПОЛНЫЙ СПИСОК РАСХОДОВ ---")
        
        for cat, exp in data.items():
            print(f"Категория: {cat.capitalize()}")
            
            for item in exp:
                print(f"-- {item[1]}: {item[0]} руб.")
                
    else:
        category_lower = argument.lower()
        
        if category_lower in data:
            print(f"--- РАСХОДЫ ПО КАТЕГОРИИ: {category_lower.capitalize()} ---")
            
            for item in data[category_lower]:
                print(f"-- {item[1]}: {item[0]} руб.")
                
        else:
            print(f"Ошибка: Категории '{argument}' не существует.")


def total_expenses(argument):
    data = load_data()

    if not argument or not argument.strip():
        print("--- ПОЛНАЯ СУММА РАСХОДОВ ---")

        all_total = 0

        for cat, exp in data.items():
            total = 0

            for item in exp:
                total += int(item[0])

            all_total += total

            print(f"Категория {cat.capitalize()}: {total} руб.")

        print(f"--- Общий итог: {all_total} руб. ---")
        
    else:
        low_category = argument.lower()

        if low_category in data:
            total = 0

            for item in data[low_category]:
                total += int(item[0])

            print(f"--- Всего по категории {low_category.capitalize()}: {total} руб. ---")
            
        else:
            print(f"Ошибка: Категории '{argument}' не существует.")


args = sys.argv

if len(args) > 1:
    command = args[1]

    if command not in commands:
        print(f"Ошибка: Неизвестная команда: '{command}'!")
        sys.exit(1)
        
    elif command == "add":
        if len(args) == 5:
            add(args[2], args[3], args[4])
        else:
            print("Ошибка: Команда 'add' требует 3 аргумента: стоимость, категория и название.")
            sys.exit(1)
            
    elif command == "add-category":
        if len(args) == 3:
            add_category(args[2])
        else:
            print("Ошибка: Команда 'add-category' требует 1 аргумент: название категории.")
            sys.exit(1)
            
    elif command == "list":
        obj = args[2] if len(args) == 3 else None
        list_expenses(obj)
        
    elif command == "total":
        obj = args[2] if len(args) == 3 else None
        total_expenses(obj)
        
    elif command == "help":
        print_commands()
        
else:
    print("Ошибка: Неизвестная команда!")
    print("Для вывода всех команд используйте 'help'")
