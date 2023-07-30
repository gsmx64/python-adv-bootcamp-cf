# Corto circuito de operadores lógicos


def division(a, b):
    return a / b


if division(1, 3) > 0 and division(1, 0) > 0:
    print("Esto terminó bien")
else:
    print("BOOM!")
