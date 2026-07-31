class ExpenseManager:
    def __init__(self):
        self.categories = {}

    # create
    def add_category(self, category):
        if self._category_exists(category):
            print(f"Ошибка: Категория '{category}' уже существует!")
            return

        self.categories[category] = []

    def add_expense(self, category, name, price):
        if not self._category_exists(category):
            print(f"Ошибка: Категории '{category}' не существует!")
            return

        self.categories[category].append({"name": name, "price": price})

    # read
    def get_expenses(self, category):
        if not self._category_exists(category):
            print(f"Ошибка: Категории '{category}' не существует!")
            return

        return self.categories[category]

    def calculate_total(self, category):
        if not self._category_exists(category):
            print(f"Ошибка: Категории '{category}' не существует!")
            return

        total_price = 0.0
        for expense in self.categories[category]:
            total_price += expense["price"]
        return total_price

    # delete
    def remove_expense(self):
        pass

    def remove_category(self):
        pass

    # debug
    def get_info(self):
        return self.categories

    def _category_exists(self, category):
        return category in self.categories
