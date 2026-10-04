# 2. datetime
# Escribe una función dias_hasta(fecha_str) que reciba una fecha en formato "DD/MM/YYYY" y devuelva cuántos días faltan para esa fecha desde hoy.
# Si la fecha ya pasó, devuelve un número negativo.
# from datetime import datetime
# def dias_hasta(fecha_str):
#     date_objetive = datetime.strptime(fecha_str, "%d/%m/%Y").date()
#     date_today = datetime.today().date()
#     return (date_objetive - date_today).days
# print(dias_hasta("19/07/2026"))


# 3. os y pathlib
# Escribe una función listar_pythons(carpeta) que reciba una ruta y devuelva una lista con los nombres de todos los archivos .py en esa carpeta.
# from pathlib import Path
# def listar_pythons(carpeta):
#     ruta = Path(carpeta)
#     return [archivo.name for archivo in ruta.glob("*.py")]
# print(listar_pythons("/home/jin/Desktop/python"))


# 4. JSON
# Escribe dos funciones: guardar_contactos(contactos, archivo) que guarde una lista de diccionarios en un JSON, y cargar_contactos(archivo) que la lea de vuelta.
# Si el archivo no existe, cargar_contactos debe devolver una lista vacía.
from json import dump, load


def guardar_contactos(contactos, archivo):
    # ruta='/home/jin/Desktop'
    with open("contactos.json", "w") as archivo:
        dump(contactos, archivo)


def cargar_contactos(archivo):
    with open("contactos.json", "r") as archivo:
        contactos = load(archivo)
    return contactos


contactos = [{"name": "jean", "phone": 967733601}, {"name": "jose", "phone": 967733641}]
guardar_contactos(contactos, "contactos")
print(cargar_contactos("contactos"))
