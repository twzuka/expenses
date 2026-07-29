class ExpenseManager:
    def __init__(self):
        self.categories = {}

    # создание
    def add_category(self, category):
        self.categories[category] = []

    def add_expense(self, name, price, category):
        self.categories[category].append({"name": name, "price": price})

    # получение
    def get_expenses(self, category):
        return self.categories[category]

    def calculate_total(self, category):
        total_price = 0.0
        for expense in self.categories[category]:
            total_price += expense["price"]
        return total_price

    # изменение
    def remove_expense(self):
        pass

    def remove_category(self):
        pass

    # отладка
    def get_info(self):
        return self.categories
