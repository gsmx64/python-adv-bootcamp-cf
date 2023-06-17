# Tienda - ShoppingCar Class
class ShoppingCar:

    def __init__(self):
        self.total = 0
        self.products = []

    def add_product(self, product):
        self.products.append(product)

        self.total = self.total + product.price

# Código OK! - Agregado instanciador
def _run():
    """
    Make a reporter that can be used when no reporter is specified.
    """
    return ShoppingCar()
