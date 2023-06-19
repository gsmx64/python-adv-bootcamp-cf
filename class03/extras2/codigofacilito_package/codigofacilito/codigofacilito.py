from codigofacilito.workshops import unreleased
import logging

"""
INFO -> 10
DEBUG -> 20
WARNING -> 30
ERROR -> 40
CRITICAL -> 50
"""

logging.basicConfig(level=logging.WARNING)

#if __name__ == '__main__':
def main():
    logging.debug('>>> Estamos comenzando la ejecución del paquete.')
    
    workshops = unreleased()
    logging.debug(workshops)
    logging.debug(type(workshops))
    
    logging.debug('>>> Estamos finzalizando la ejecución del paquete.')


#print(f'El valor de main para workshop es {__name__}')
    