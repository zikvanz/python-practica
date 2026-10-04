# es una coleccion clave valor
# es como el objeto en javascript

diccionario = {"banana": 2.5, "fresa": 3.5}


print(diccionario["banana"])

diccionario["banana"] = 5
print(diccionario)

diccionario["uva"] = 6
print(diccionario)

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

# print(diccionario["higo"]) esto generar un error


# cuando una clave no existe, es mas seguro usar get, ya que no te arroja error
print(diccionario.get("higo"))
# en caso no exista coloca el segundo valor por defecto
print(diccionario.get("higo", "N/A"))
