""" Main for Decorator's Challenge """
# __doc__ (Main file for little app for Decorator´s Challenge)

from app.decorators.decorator import decorator_validate_int
from app.models.filters import Filters
from app.models.info import Info

value_1 = 2  # pylint: disable=C0103
value_2 = 5  # pylint: disable=C0103
CFG_USE_INPUTS = True
filters = Filters()

# Func w/decorator docstring


@decorator_validate_int
def add(a, b):  # pylint: disable=C0103,C0116
    return a + b


if __name__ == '__main__':
    try:
        check = 'y'  # pylint: disable=C0103
        while check.lower() == 'y':
            if CFG_USE_INPUTS:
                value_1 = filters.data_type(input('Inserta el primer valor: '))
                value_2 = filters.data_type(
                    input('Inserta el segundo valor: '))

            print(f'El resultado es: {add(value_1, value_2)}')

            check = input('¿Repetir operación? (Y) para repetir: ')
    except TypeError as error:
        print(
            'Error de Tipo: Operación de Tipo no soportada al sumar' +
            f'2 variables de distinto tipo.\nType Error: {error}')
    finally:
        print('\n'+('-'*49)+'\n')
        view_credits = input(
            '¿Quiere ver los créditos del Challenge? ' +
            'Ingrese (Y) para verlos, o cualquier tecla para omitir: ')

        if view_credits.lower() == 'y':
            print('\n')
            Info().show_credits(True)
