# Tienda - Product Class
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f'El nombre del producto es: {self.name}'


def _run(name, price):
    """
    Make a reporter that can be used when no reporter is specified.
    """
    return Product(name, price)

"""def create_new_product():
    pass

if __name__ == '__main__':  # Ejecuta esto si y solo si el modulo no se importa
    print(f'Prueba uno')
    print(f'Prueba dos')
    print(f'Prueba tres')"""
    