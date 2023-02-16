import utils
from product import Product


class Store:
    name = 'Mascotas para todos'
    product_list = []

    def start(self):
        self.product_list.append(Product('Arena', 15000, 10))
        self.product_list.append(Product('Max Cat', 144800, 5))
        self.product_list.append(Product('Collar de gato', 5000, 9))
        self.product_list.append(Product('Dog Chow', 4000, 30))

        self.show_menu()

    def show_menu(self):

        while True:
            print(f'****************************\n{self.name.upper()} \n**************************** ')

            option = utils.validate_number('Seleccione una opción: \n'
                                           '1. Mostrar todos los productos. \n'
                                           '2. Agregar un producto. \n'
                                           '3. Eliminar un producto. \n'
                                           '0. Salir.\n')

            match option:
                case 0:
                    break
                case 1:
                    self.show_all_products()
                case 2:
                    self.add_product()
                case 3:
                    self.delete_product()
                case _:
                    print('Opción no encontrada')

    def show_all_products(self):
        print(f'Hay {len(self.product_list)} products')
        for product in self.product_list:
            product.view()

    def add_product(self):
        print('Agregue el Producto:')

        name = input('Ingrese el nombre: ')
        price = utils.validate_number('Ingrese el valor: ')
        stock = utils.validate_number('Ingrese la cantidad: ')

        new_product = Product(name, price, stock)
        self.product_list.append(new_product)

        print(f'El producto que se agregó:')
        new_product.view()

    def delete_product(self):

        product_to_delete = input('ingrese el nombre del producto a eliminar: ')
        product_found = False
        index = 0

        for i, product in enumerate(self.product_list):
            if product.name.upper() == product_to_delete.upper():
                product_found = True
                index = i
                break

        if product_found:
            self.validate_delete(self.product_list[index], index)
        else:
            print('El producto no se encuentra registrado')

    def validate_delete(self, product, index):

        stock_to_delete = utils.validate_number(f'Ingrese la cantidad a eliminar, hay: {product.stock}')

        if stock_to_delete > product.stock:
            print(f'No hay suficiente cantidad para eliminar, udidades disponibles: {product.stock}' )
        elif stock_to_delete == product.stock:
            del self.product_list[index]
            print('El producto se ha eliminado correctamente')
        else:
            product.stock = product.stock - stock_to_delete
            print(f'Las unidades se han eliminado correctamente, quedan: {product.stock}')

