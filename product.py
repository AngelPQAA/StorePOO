class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def view(self):
        print(f'name: {self.name} \nprice: {self.price} \nstock: {self.stock}')






