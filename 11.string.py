# Escribe una función es_palindromo(texto) que devuelva True si el texto es igual al leerlo al revés (ignorando mayúsculas y espacios).
# Ej: es_palindromo("Anita lava la tina") → True.
# def es_palindromo(texto):
#     text_parsed = texto.strip().lower()
#     return text_parsed == text_parsed[::-1]
# print(es_palindromo(" Ana"))

# Dado producto = "Laptop" y precio = 2599.999,
# imprime: "El producto Laptop cuesta $2,600.00" (precio redondeado a 2 decimales, con separador de miles).
# producto = "Laptop"
# precio = 2599.999
# print(f"El producto {producto} cuesta ${precio:.2f}")


# Tienes esta línea de texto: "Ana Torres;28;Lima".
# Escribe código que la separe y construya un diccionario {"nombre": ..., "edad": ..., "ciudad": ...} (la edad como int, no como string).
# def toDict(texto):
#     texto_parsed = texto.split(";")
#     diccionario = {
#         "nombre": texto_parsed[0].strip(),
#         "edad": int(texto_parsed[1].strip()),
#         "ciudad": texto_parsed[2].strip(),
#     }
#     return diccionario
# texto = "Ana Torres;28;Lima"
# print(toDict(texto))


# Escribe una función validar_password(password) que devuelva True solo si la contraseña tiene al menos 8 caracteres,
# al menos un número y al menos una mayúscula.
# def validar_password(password):
#     passStripped = password.strip()
#     return (
#         len(passStripped) >= 8
#         and any(el.isdigit() for el in passStripped)
#         and any(el.isupper() for el in passStripped)
#     )
# print(validar_password("   hola1123W"))


# Tienes esta lista con datos sucios:
# pythonemails = ["  Ana@Mail.com ", "LUIS@mail.COM", " eva@mail.com"]
# Normalízalos para que todos queden en minúsculas y sin espacios.
# def normalizar(emails):
#     return [email.strip().lower() for email in emails]
# pythonemails = ["  Ana@Mail.com ", "LUIS@mail.COM", " eva@mail.com"]
# print(normalizar(pythonemails))


# Escribe una función generar_slug(titulo) que convierta un título en un "slug" para URL: todo en minúsculas, espacios reemplazados por guiones, sin caracteres especiales (solo letras, números y guiones).
# Ej: generar_slug("¡Hola Mundo! Bienvenidos 2024") → "hola-mundo-bienvenidos-2024".


def generar_slug(texto):
    text_parsed = "".join(
        word.lower() for word in texto if word.isalnum() or word.isspace()
    )
    print(text_parsed)
    return "-".join(text_parsed.split(" "))


print(generar_slug("¡Hola Mundo! Bienvenidos 2024"))
