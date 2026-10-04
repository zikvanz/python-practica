# coleccion que no permite duplicados
# se usa cuando no quieres duiplicados en una lista
#  se usa para saber mas rapido si un elemento existe en una lista
set1 = {1, 5, 2, 4, 1}
set2 = set([1, 5, 2, 1, 4, 2])

print(set1)
print(set2)

set1.add(9)
print(set1)

set1.remove(2)
print(set1)

print(10 in set1)

# operaciones de conjuntos
# union
print({1, 2, 3} | {2, 3, 4})

# interseccion
print({1, 2, 3} & {2, 3, 4})

# diferencia
print({1, 2, 3} - {2, 3, 4})
