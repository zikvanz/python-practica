# # importar todo el modulo
# import modulo_math
# print(modulo_math.restar(5, 1))

# # importar solo lo que necesitas
# from modulo_math import restar, sumar
# print(sumar(1, 5))

# # importar con alias
# import modulo_math as mate
# print(mate.sumar(1, 5))

# # importar todo
# # evitar esto, ya que no se sabe de donde viene el metodo importado
# from modulos.modulo_math import *
# print(sumar(1, 5))


from modulo_calculadora import dividir

print(dividir(1, 5))
