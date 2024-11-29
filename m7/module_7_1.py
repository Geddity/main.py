import os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self, __file_name='products.txt'):
        self.file_name = __file_name

    def get_products(self):
        with open(self.file_name, 'r') as file:
            products = file.read()
        return products

    def add(self, *products):
        existing_products = set()

        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                for line in file:
                    product_info = line.strip().split(',')
                    if len(product_info) == 3:
                        name, weight, category = product_info
                        existing_products.add((name.strip(), float(weight.strip()), category.strip()))

        for product in products:
            name, weight, category = str(product).split(',')
            if (name.strip(), float(weight.strip()), category.strip()) not in existing_products:
                with open(self.file_name, 'a') as file:
                    file.write(f"{product}\n")

            else:
                existing_products.add((name.strip(), float(weight.strip()), category.strip()))
                print(f"Продукт {name} уже есть в магазине")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())