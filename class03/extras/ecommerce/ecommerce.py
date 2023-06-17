# El __main__.py es opcional
'''from ecommerce import Cupon
from ecommerce import Products
from ecommerce import ShoppingCar'''

from ecommerce import cupon as c
from ecommerce import product as p
from ecommerce import shopping_car as sc


#if __name__ == '__main__':
    
def main(prog=None, args=None):     
    '''product1 = Product('product1', 100)
    product2 = Product('product2', 150)'''
    
    product1 = p._run('product1', 100)
    product2 = p._run('product2', 150)

    '''shopping_car = ShoppingCar()
    shopping_car.add_product(product1)
    shopping_car.add_product(product2)'''
    
    shopping_car = sc._run()
    shopping_car.add_product(product1)
    shopping_car.add_product(product2)

    print(shopping_car.total)

