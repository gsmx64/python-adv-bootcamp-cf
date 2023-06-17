# El __main__.py es opcional

# Código viejo, movido a ecommerce.py
"""from ecommerce import Products
from ecommerce import ShoppingCar

if __name__ == '__main__':
        
    product1 = Product('product1', 100)
    product2 = Product('product2', 150)

    shopping_car = ShoppingCar()
    shopping_car.add_product(product1)
    shopping_car.add_product(product2)

    print(shopping_car.total)"""
    
# Código OK!
from ecommerce.ecommerce import main

# OK!
# python -m ecommerce
if __name__ == '__main__':
    main()
