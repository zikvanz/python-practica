empleados = [
    {"nombre": "Ana", "departamento": "Ventas", "salario": 3000},
    {"nombre": "Luis", "departamento": "IT", "salario": 4500},
    {"nombre": "Eva", "departamento": "Ventas", "salario": 3200},
    {"nombre": "Carlos", "departamento": "IT", "salario": 5000},
]


# def totalSalaryDepartment(empleados):
#     depTotals = {}
#     for emp in empleados:
#         departamento = emp["departamento"]
#         depTotals[departamento] = depTotals.get(departamento, 0) + emp["salario"]
#     return depTotals
# print(totalSalaryDepartment(empleados))


# def getEmployeeWithSalaryOver(salary, empleados):
#     return [emp["nombre"] for emp in empleados if emp["salario"] >= salary]
# print(getEmployeeWithSalaryOver(4000, empleados))

# numeros = [4, 8, 15, 16, 23, 42]
# print([num for num in numeros if num % 2 == 0])


# def getDivision(a, b):
#     return a // b, a % b
# print(getDivision(5, 2))


# inventario = {"manzanas": 50, "peras": 30, "uvas": 0}
# def onlyStock(fruits):
#     fruits = fruits.items()
#     print(fruits)
#     return [k for k, v in fruits if v > 0]
# print(onlyStock(inventario))


# evento1 = ["ana@mail.com", "luis@mail.com", "eva@mail.com"]
# evento2 = ["eva@mail.com", "carlos@mail.com", "luis@mail.com"]
# tupla1 = set(evento1)
# tupla2 = set(evento2)
# print(tupla1 & tupla2)
# print(tupla1 - tupla2)


productos = [
    {"nombre": "Laptop", "precio": 3500, "categoria": "Tecnología"},
    {"nombre": "Mouse", "precio": 50, "categoria": "Tecnología"},
    {"nombre": "Silla", "precio": 400, "categoria": "Hogar"},
    {"nombre": "Mesa", "precio": 600, "categoria": "Hogar"},
]

# categorias = {}
# for product in productos:
#     categoria = product["categoria"]
#     if categoria not in categorias:
#         categorias[categoria] = []
#     categorias[categoria].append({"nombre": product["nombre"]})
# print(categorias)

categorias = {}
for product in productos:
    categoria = product["categoria"]
    categorias[categoria] = (
        categorias.get(categoria, 0)
        if categorias.get(categoria, 0) > product["precio"]
        else product["precio"]
    )
print(categorias)
