# 1. Clase básica
# Crea una clase Rectangulo con atributos ancho y alto. Agrega métodos area() y perimetro(), y un __str__ que muestre "Rectángulo 5x3 | Área: 15 | Perímetro: 16".
# class Rectangulo:
#     def __init__(self, ancho, alto):
#         self.ancho = ancho
#         self.alto = alto

#     def area(self):
#         return self.ancho * self.alto

#     def perimetro(self):
#         return 2 * (self.ancho + self.alto)

#     def __str__(self):
#         return f"Rectángulo {self.ancho}x{self.alto} | Área: {self.area()} | Perímetro: {self.perimetro()}"

# o1 = Rectangulo(5, 3)
# print(o1)


# 2. Encapsulamiento
# Crea una clase CuentaBancaria con saldo privado. Métodos: depositar(monto), retirar(monto) (valida que no exceda el saldo), y una @property saldo.
# Agrega un __str__ que muestre el saldo actual.
# class CuentaBancaria:
#     def __init__(self, saldo):
#         self.__saldo = saldo

#     def depositar(self, monto):
#         self.__saldo += monto

#     def retirar(self, monto):
#         if monto > self.__saldo:
#             print("Saldo insuficiente")
#         else:
#             self.__saldo -= monto

#     @property
#     def saldo(self):
#         return self.__saldo

#     def __str__(self):
#         return f"Saldo actual: {self.__saldo}"

# cuenta=CuentaBancaria(1000)
# cuenta.depositar(500)
# print(cuenta)
# cuenta.retirar(2000)
# print(cuenta)


# 3. Herencia
# Crea una clase base Vehiculo con atributos marca y velocidad_max. Hereda dos clases: Auto (agrega num_puertas) y Moto (agrega tipo: "deportiva", "touring").
# Ambas deben tener un método descripcion().
# class Vehiculo:
#     def __init__(self, marca, velociadad_max):
#         self.marca = marca
#         self.velocidad_max = velociadad_max


# class Auto(Vehiculo):
#     def __init__(self, marca, velocidad_max, num_puertas):
#         super().__init__(marca, velocidad_max)
#         self.num_puertas = num_puertas

#     def descripcion(self):
#         return f"Auto {self.marca} | Velocidad máxima: {self.velocidad_max} km/h | Puertas: {self.num_puertas}"


# class Moto(Vehiculo):
#     def __init__(self, marca, velocidad_max, tipo):
#         super().__init__(marca, velocidad_max)
#         self.tipo = tipo

#     def descripcion(self):
#         return f"Moto {self.marca} | Velocidad máxima: {self.velocidad_max} km/h | Tipo: {self.tipo}"


# auto = Auto("Toyota", 180, 4)
# moto = Moto("Honda", 200, "deportiva")

# print(auto.descripcion())
# print(moto.descripcion())


# 4. @classmethod y @staticmethod
# Agrega a Rectangulo del ejercicio 1:
# Un @classmethod cuadrado(cls, lado) que cree un rectángulo con ancho y alto iguales
# Un @staticmethod es_valido(ancho, alto) que devuelva True si ambos son positivos
# class Rectangulo:
#     def __init__(self, ancho, alto):
#         self.ancho = ancho
#         self.alto = alto

#     def area(self):
#         return self.ancho * self.alto

#     def perimetro(self):
#         return 2 * (self.ancho + self.alto)

#     def __str__(self):
#         return f"Rectángulo {self.ancho}x{self.alto} | Área: {self.area()} | Perímetro: {self.perimetro()}"

#     @classmethod
#     def cuadrado(cls, lado):
#         return cls(lado, lado)

#     @staticmethod
#     def es_valido(ancho, alto):
#         return ancho > 0 and alto > 0


# o1 = Rectangulo(5, 3)
# print(o1)

# o2 = Rectangulo.cuadrado(4)
# print(o2)

# print(Rectangulo.es_valido(5, 3))
# print(Rectangulo.es_valido(-1, 3))


# 5. Integrador
# Crea un sistema simple de inventario con una clase Inventario que contenga una lista de Producto.
# Métodos: agregar(producto), buscar(nombre), listar_por_categoria(categoria), producto_mas_caro().


class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} | Precio: {self.precio} | Categoría: {self.categoria}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def listar_por_categoria(self, categoria):
        return [
            producto for producto in self.productos if producto.categoria == categoria
        ]

    def producto_mas_caro(self):
        if not self.productos:
            return None
        return max(self.productos, key=lambda p: p.precio)


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)

    def aplicar_descuento(self, porcentaje):
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        return total - descuento

    def resumen_compra(self):
        resumen = "Resumen de Compra:\n"
        for producto in self.productos:
            resumen += f"{producto}\n"
        resumen += f"Total: {self.calcular_total()}\n"
        return resumen


inventario = Inventario()
carrito = Carrito()
inventario.agregar_producto(Producto("Laptop", 1500, "Electrónica"))
inventario.agregar_producto(Producto("Smartphone", 800, "Electrónica"))
inventario.agregar_producto(Producto("Camiseta", 20, "Ropa"))

carrito.agregar_producto(Producto("Laptop", 1500, "Electrónica"))
carrito.agregar_producto(Producto("Camiseta", 20, "Ropa"))
carrito.agregar_producto(Producto("Smartphone", 800, "Electrónica"))

for producto in inventario.listar_por_categoria("Electrónica"):
    print(producto)

print(inventario.producto_mas_caro())
print(carrito.resumen_compra())
print(f"Total con descuento del 10%: {carrito.aplicar_descuento(10)}")

# 6. Desafío
# Extiende el sistema del ejercicio 5: agrega una clase Carrito que permita agregar productos, calcular el total, aplicar un descuento global y generar un resumen de compra.
