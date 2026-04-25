import sys, json

commands = {"add", "add-category", "list", "total", "help"}

FILE_NAME = "data.json"


def start():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def help():
    print("--- СПИСОК ВСЕХ КОМАНД ---")
    print(
        "1. Добавить расход: «python expenses.py add <стоимость> <категория> <название>»"
    )
    print("2. Добавить категорию: «python expenses.py add-category <категория>»")
    print("3. Показать все расходы: «python expenses.py list [категория]»")
    print("4. Показать сумму расходов: «python expenses.py total  [категория]»")


def add_category(cat):
    data = start()
    if cat not in data:
        data[cat] = []
        save(data)
    else:
        print("Ошибка: категория уже существует!")


def add(price, cat, name):
    try:
        int_price = int(price)
    except ValueError:
        print("Ошибка: введено не число!")
        return
    data = start()
    if cat in data:
        data[cat].append([int_price, name])
        save(data)
    else:
        print("Ошибка: такой категории не существует!")
        return


def list_cat(cat_arg):
    data = start()

    if not cat_arg or not cat_arg.strip():
        print(f"--- ПОЛНЫЙ СПИСОК РАСХОДОВ ---")
        for cat, exp in data.items():
            print(f"Категория: {cat}")
            for item in exp:
                print(f"-- {item[1]}: {item[0]} руб.")
    elif cat_arg in data:
        print(f"--- РАСХОДЫ ПО КАТЕГОРИИ: {cat_arg} ---")
        for item in data[cat_arg]:
            print(f"-- {item[1]}: {item[0]} руб.")
    else:
        print(f"Ошибка: категории '{cat_arg}' не существует.")


def total_exp(cat_arg):
    data = start()

    if not cat_arg or not cat_arg.strip():
        print("--- ПОЛНАЯ СУММА РАСХОДОВ ---")
        for cat, exp in data.items():
            total = 0
            for item in exp:
                total += int(item[0])
            print(f"Категория {cat}: {total} руб.")
    elif cat_arg in data:
        total = 0
        for item in data[cat_arg]:
            total += int(item[0])
        print(f"--- Всего по категории {cat_arg}: {total} руб. ---")


args = sys.argv
if len(args) > 1:
    if args[1] in commands:
        if args[1] == "add" and len(sys.argv) == 5:
            add(args[2], args[3], args[4])
        elif args[1] == "add-category" and len(sys.argv) == 3:
            add_category(args[2])
        elif args[1] == "list":
            list_cat(args[2] if len(sys.argv) == 3 else None)
        elif args[1] == "total":
            total_exp(args[2] if len(sys.argv) == 3 else None)
        elif args[1] == "help" and len(sys.argv) == 2:
            help()
        else:
            print("Ошибка: Неизвестная команда!")
else:
    help()
