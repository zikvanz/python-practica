def sumar(a, b):
    return a + b


# Es el patrón estándar para que un archivo pueda funcionar tanto como módulo importable como script ejecutable directamente.
# Lo vas a ver en casi todo proyecto Python.
if __name__ == "main":
    # este bloque solo se ejecuta solo si ejecutas el archivo directamente
    # si se importa desde otro archivo no se ejecutara
    print(sumar(4, 2))
