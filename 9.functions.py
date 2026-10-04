# def suma(a: int, b: int) -> int:
#     return a + b

# a = 1
# b = 2

# print(f"{a}+{b}={suma(a,b)}")


# def saludar(nombre, saludo="Hola"):
#     return f"{saludo}, {nombre}!"
# print(f"{saludar('jin','hola')}")
# print(f"{saludar(saludo='saludos',nombre='Jin')}")

# con type hint, es solo documentacion
# def saludar(nombre: str, saludo: str = "Hola") -> str:
#     return f"{saludo}, {nombre}!"
# print(f"{saludar('jin','hola')}")
# print(f"{saludar(saludo='saludos',nombre='Jin')}")


# # funciones lambda es lo mismo que arrow functions en js
# saludar = lambda nombre: f"hola {nombre}"
# print(saludar("jean"))

# # con parametors
# saludar = lambda nombre, apellido: f"hola {nombre} {apellido}"
# print(saludar("jean", "palomino"))

# las funciones lambda generalmente para funciones map, filter, sort etc
# numeros = [1, 5, 3, 1, 4]
# ordenados = sorted(numeros, key=lambda x: -x)
# print(ordenados)


# # args recoge todo en una tupla
# def sumar(*numeros):
#     return sum(numeros)
# print(sumar(1, 2, 3))


# # kargs recoge argumentos nombrados en un diccionario
# def mostrar(edad=12, nombre="jean"):
#     return f"{nombre} tiene {edad} anios"
# print(mostrar(nombre="juan", edad=12))


# # combinar *args y *kargs
# def mostrar(a, b, *args, **kwargs):
#     print(f"{a} {b}")
#     print(f"args {args}")
#     print(f"kwargs {kwargs}")
# mostrar(1, 2, 3, 2, 5, x=9, y=19)


# # crear_tarjeta(titulo, descripcion="Sin descripción", severidad="info")
# # [INFO] Título: Sin descripción
# def crear_tarjeta(titulo, descripcion="Sin descripción", severidad="info"):
#     print(f"[{severidad.upper()}] {titulo}:{descripcion}")
# crear_tarjeta("Titulito", severidad="severidad", descripcion="descripcioncita")


# def configurar(activo: bool = True, opciones: dict = None):
#     if opciones is None:
#         opciones = {}
#     opciones["activo"] = activo
#     return opciones
# print(configurar())  # {activo:true}
# print(configurar(False, {"tema": "oscuro"}))  # {"tema": "oscuro",activo:False}

# componentes = [
#     {"nombre": "Button", "usos": 45},
#     {"nombre": "Tag", "usos": 12},
#     {"nombre": "Alert", "usos": 28},
# ]
# ordenado = sorted(componentes, key=lambda x: -x["usos"])
# print(ordenado)

# <Button class="btn btn-primary" disabled="True" id="submit-btn">
# def crear_componente(component, *clases, **propiedades):
#     clases_str = " ".join(clases)
#     propiedades_str = " ".join(f'{k}="{v}"' for k, v in propiedades.items())
#     return f"<{component} class='{clases_str}' {propiedades_str} "
# print(crear_componente("Button", "btn", "btn-primary", disabled=True, id="submit-btn"))

# duplicar = lambda x: x * 2
# incrementar = lambda x: x + 1
# def componer(*funciones):
#     def funcion_compuesta(valor):
#         for funcion in funciones:
#             valor = funcion(valor)
#         return valor
#     return funcion_compuesta
# pipeline = componer(duplicar, incrementar)
# print(pipeline(5))  # primero duplica (10), luego incrementa (11) -> 11


# Escribe una función es_primo(n) que devuelva True si el número es primo, False si no.
# def es_primo(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(es_primo(5))


# Escribe una función crear_email(nombre, apellido, dominio="empresa.com")
# que devuelva un string con formato nombre.apellido@dominio en minúsculas. Ej: crear_email("Ana", "Torres") → "ana.torres@empresa.com".
# def crear_email(nombre, apellido, dominio="empresa.com"):
#     return f"{nombre}.{apellido}@{dominio}".lower()
# print(crear_email("jean",'Palomino'))


# Escribe una función promedio(*notas) que reciba cualquier cantidad de notas y devuelva el promedio.
# Si no recibe ninguna nota, debe devolver 0 (evita la división por cero).
# def promedio(*notas):
# return sum(notas) / len(notas)
# print(promedio(1, 2, 3, 4))


# Escribe una función armar_query(**filtros) que reciba pares clave-valor y devuelva un string tipo SQL WHERE.
# Ej: armar_query(nombre="Ana", edad=28) → "nombre='Ana' AND edad=28".
# def armar_query(**filtros):
#     query = " AND ".join([f"{k}={v}" for k, v in filtros.items()])
#     return query
# print(armar_query(nombre="Ana", edad=28))

# Ordénala de mayor a menor precio usando sort() y una lambda como key.
# productos = [
#     {"nombre": "Laptop", "precio": 3500},
#     {"nombre": "Mouse", "precio": 50},
#     {"nombre": "Teclado", "precio": 150},
# ]
# ordenados = sorted(productos, key=lambda x: x["precio"], reverse=True)
# print(ordenados)


# Escribe una función resumen_ventas(*ventas, **opciones) que:
# Reciba ventas como diccionarios {"producto": str, "monto": float}
# Calcule el total de todas las ventas
# Si recibe opciones["impuesto"] (ej: 18), aplique ese porcentaje de impuesto al total
# Devuelva un diccionario {"total_ventas": N, "total_con_impuesto": M}


def resumen_ventas(*ventas, **opciones):
    suma = sum([x["monto"] for x in ventas])
    total_con_impuesto = suma * (1 + opciones.get("impuesto", 0) / 100)
    return {"total_ventas": suma, "total_con_impuesto": total_con_impuesto}


print(
    resumen_ventas(
        {"producto": "laptop", "monto": 200},
        {"producto": "cocina", "monto": 100},
        impuesto=50,
    )
)
