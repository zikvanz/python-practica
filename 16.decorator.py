# def mi_decorador(func):
#     def wrapper(*args, **kwargs):
#         print("antes")
#         resultado = func(*args, **kwargs)
#         print("despues")
#         return resultado

#     return wrapper

# @mi_decorador
# def saludar(nombre):
#     print(f"hola {nombre}")

# saludar("nombre")

# Escribe un decorador log_llamada que imprima el nombre de la función y los argumentos cada vez que se llama. Ej: llamando saludar con args=('Ana',) kwargs={}.


# def log_llamada(func):
#     def wrapper(*args, **kwargs):
#         print(f"llamando a  {func.__name__} con args={args}  kwargs={kwargs}")
#         resultado = func(*args, **kwargs)
#         return resultado

#     return wrapper

# @log_llamada
# def saludar(nombre):
#     return


# saludar("jean")


# Escribe un decorador cache_simple que guarde el resultado de una función en un diccionario y, si se llama con los mismos argumentos, devuelva el valor guardado sin ejecutar la función de nuevo.


# def cache_simple(func):
#     register = {}

#     def wrapper(*args, **kwargs):
#         key = (tuple(sorted(args)), tuple(kwargs.items()))
#         if key in register:
#             return register[key]
#         resultado = func(*args, **kwargs)
#         register[key] = resultado
#         print(register)
#         return resultado

#     return wrapper


# @cache_simple
# def sumar(a, b):
#     return a + b


# print(sumar(1, 5))
# # print(sumar(1, 8))
# print(sumar(1, 5))


# Escribe un generador fibonacci() que produzca la secuencia de Fibonacci indefinidamente (0, 1, 1, 2, 3, 5, 8...). Usa next() para obtener los primeros 8 valores.
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# generador = fibonacci()
# impresor = [next(generador) for _ in range(8)]
# print(impresor)


# Escribe un generador primos() que produzca números primos indefinidamente. Obtén los primeros 10.
# def es_primo(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# def primos():
#     n = 2
#     while True:
#         if es_primo(n):
#             yield n
#         n += 1
# gen = primos()
# impresor = [next(gen) for _ in range(10)]
# print(impresor)


# Escribe una función procesar_ventas(ventas) decorada con medir_tiempo que reciba una lista de diccionarios {"producto": str, "monto": float}
# y use un generador interno para filtrar solo las ventas mayores a 1000 y calcule el total.

# import time


# def medir_tiempo(func):
#     def wrapper(*args, **kwargs):
#         inicio = time.time()
#         resultado = func(*args, **kwargs)
#         print(f"{func.__name__} tardo {time.time() -inicio:.4f}s")
#         return resultado

#     return wrapper


# def ventas_mayores(ventas, minimo):
#     for venta in ventas:
#         if venta["monto"] > minimo:
#             yield venta


# @medir_tiempo
# def procesar_ventas(ventas):
#     counter = 0
#     for venta in ventas_mayores(ventas, 1000):
#         counter = counter + venta["monto"]
#     return counter


# ventas = [
#     {"producto": "Laptop", "monto": 3500},
#     {"producto": "Mouse", "monto": 50},
#     {"producto": "Monitor", "monto": 1200},
#     {"producto": "Teclado", "monto": 80},
#     {"producto": "Silla", "monto": 1500},
# ]

# print(procesar_ventas(ventas))


# Escribe un generador leer_csv_lazy(archivo) que lea un CSV línea por línea sin cargarlo todo en memoria,
# y devuelva cada fila como diccionario usando la primera línea como cabecera.
# Pruébalo creando un CSV de ejemplo primero.


def leer_csv_lazy(archivo):
    with open(archivo, encoding="utf-8") as f:
        cabecera = f.readline().strip().split(",")
        for linea in f:
            valores = linea.strip().split(",")
            yield dict(zip(cabecera, valores))


import csv

with open("ventas.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["producto", "monto", "categoria"])
    writer.writerows(
        [
            ["Laptop", "3500", "Tecnología"],
            ["Mouse", "50", "Tecnología"],
            ["Silla", "400", "Hogar"],
            ["Mesa", "600", "Hogar"],
        ]
    )

for fila in leer_csv_lazy("ventas.csv"):
    print(fila)
