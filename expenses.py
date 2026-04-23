import sys, json

commands = {"add", "add-category", "list", "total"}

FILE_NAME = "data.json"


def start():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_category(cat):
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if cat not in data:
        data[cat] = []

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


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
    
