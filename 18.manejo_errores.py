# 1. Básico
# Escribe una función dividir_seguro(a, b) que maneje ZeroDivisionError y TypeError (si los argumentos no son números), devolviendo None en caso de error e imprimiendo un mensaje descriptivo.


# def dividir_seguro(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Error: División por cero.")
#         return None
#     except TypeError:
#         print("Error: Ambos argumentos deben ser números.")
#         return None


# print(dividir_seguro(10, 2))  # Debería devolver 5.0
# print(dividir_seguro(10, 0))  # Debería imprimir un mensaje de error y devolver None
# print(dividir_seguro(10, "a"))  # De


# 2. Validación con raise
# Escribe una función validar_email(email) que lance ValueError si el email no contiene @ o no tiene al menos un punto después del @. Si es válido, devuelve True.


# def validar_email(email):
#     if "@" not in email or "." not in email.split("@")[-1]:
#         raise ValueError("Email inválido: debe contener '@' y un dominio válido.")
#     return True


# 3. Excepciones personalizadas
# Crea una jerarquía de excepciones para un sistema bancario:
# BancoError (base)
# SaldoInsuficienteError
# CuentaBloqueadaError
# Úsalas en una clase Banco con métodos depositar y retirar.
# import json


# class BancoError(Exception):
#     pass


# class SaldoInsuficienteError(BancoError):
#     def __init__(self):
#         super().__init__("saldo insuficuente")


# class CuentaBloqueadaError(BancoError):
#     def __init__(self):
#         super().__init__("cuenta bloqueda")


# class Banco:
#     def __init__(self, saldo, is_cuenta_bloqueada):
#         self.saldo = saldo
#         self.is_cuenta_bloqueada = is_cuenta_bloqueada

#     def depositar(self, monto):
#         self.saldo += monto

#     def retirar(self, monto):
#         if monto > self.saldo:
#             raise SaldoInsuficienteError()
#         self.saldo -= monto


# banco = Banco(2000)
# banco.depositar(1000)
# print(banco.saldo)
# try:
#     banco.retirar(10000)
# except SaldoInsuficienteError as e:
#     print(f"errorcito {e}")

# print(banco.saldo)


# 4. finally y recursos
# Escribe una función leer_config(ruta) que lea un archivo JSON. Usa try/except/finally para manejar FileNotFoundError y json.JSONDecodeError, y garantiza que siempre imprima "operación finalizada" al terminar.

# import json


# def leer_config(ruta):
#     try:
#         with open(ruta, "r", encoding="utf-8") as archivo:
#             contenido = json.load(archivo)
#             print(f"{contenido}")
#     except FileNotFoundError as e:
#         print(f"error not found {e}")
#     except json.JSONDecodeError as e:
#         print(f"error file invalid {e}")
#     finally:
#         print("operación finalizada")

# leer_config("/home/jin/Documents/datos.json")


# 5. Integrador
# Crea un sistema de pedidos donde:
# PedidoError es la excepción base
# ProductoAgotadoError y PedidoInvalidoError heredan de ella
# Una clase SistemaPedidos procesa una lista de pedidos y maneja cada error apropiadamente sin detener el procesamiento del resto.
# import json


# class PedidoError(Exception):
#     pass


# class ProductoAgotadoError(PedidoError):
#     def __init__(self):
#         super().__init__("producto agotado")


# class PedidoInvalidoError(PedidoError):
#     def __init__(self):
#         super().__init__("pedido invalido")


# class SistemaPedidos:
#     def __init__(self):
#         self.productos = [
#             {"id": 1, "nombre": "laptop", "stock": 5},
#             {"id": 2, "nombre": "mouse", "stock": 3},
#         ]

#     def pedir(self, pedidos):
#         for pedido in pedidos:
#             is_producto_founded = False
#             for producto in self.productos:
#                 if pedido["nombre"] == producto["nombre"]:
#                     is_producto_founded = True
#                     if producto["stock"] >= pedido["cantidad"]:
#                         producto["stock"] -= pedido["cantidad"]
#                     else:
#                         raise ProductoAgotadoError()
#             if is_producto_founded == False:
#                 raise PedidoInvalidoError()


# sistema = SistemaPedidos()
# try:
#     sistema.pedir([{"nombre": "laptops", "cantidad": 1}])
# except ProductoAgotadoError as e:
#     print(e)
# except PedidoInvalidoError as e:
#     print(e)

# print(sistema.productos)


# 6. Desafío
# Escribe un decorador manejo_errores(logger=print) que capture cualquier excepción en la función decorada, la registre usando logger, y devuelva None en vez de explotar. Pruébalo con varias funciones que fallen de distintas formas.


import logging


def manejo_errores(func):
    def wrapper(*args, **kwargs):
        try:
            resultado = func(*args, **kwargs)
            return resultado
        except Exception as e:
            logging.exception(f"{e}")

    return wrapper


@manejo_errores
def dividir(a, b):
    return a / b


print(f"{dividir(1,0)}")
