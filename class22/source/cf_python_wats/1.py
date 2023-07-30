# Funcionamiento de Threads como demonios

from threading import Thread
import time


def imprimir():
    for i in range(10):
        print(i)
        time.sleep(0.5)


thr = Thread(target=imprimir, daemon=True)
thr.start()

# thr.join() # así se espera a que termine el thread
print("Fin del programa")
