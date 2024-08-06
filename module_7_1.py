from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        self.__file_name = 'products.txt'
        product_name = open(self.__file_name, 'r')

        return product_name.read()

    def add(self, *products):
        __file_name = 'products.txt'

        for product_name in products:
            self.get_products()
            if str(product_name.name) not in __file_name:
                product_name = open(__file_name, 'a')
                product_name.write(str(Product(*products).name))
                product_name.write('\n')


            if str(product_name.name) in __file_name:
                print(f'Продукт {Product(*products).name.name} уже есть в магазине')
                product_name.close()
                break



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  #__str__

s1.add(p1, p2, p3)

print(s1.get_products())