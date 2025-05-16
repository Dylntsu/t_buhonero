from math import pi
# class celular():
#     def __init__(self,marca, camara,memoria):
#         self.marca = marca
#         self.camara = camara
#         self.memoria = memoria

#     def mostrarCaracteristicas(self):
#         print("Marca: " + self.marca)
#         print("Camara: " + str(self.camara))
#         print("Memoria: " + str(self.memoria))

#     def encender():
#         print("Telefono Encendido")

# Iphone = celular("iphone", 12, 128)
# Samsung = celular("Samsung", 35, 240)

# Samsung.mostrarCaracteristicas()

class auto():
    def __init__(self,color,placa,marca,precio):
        self.color = color
        self.placa = placa
        self.precio = precio    
        self.marca = marca

    def mostrarAtributos(self):
        print(f"El color de tu auto es {self.color}")
        print(f"La marca de tu auto es {self.marca}")
        print(f"La placa de tu auto es {self.placa}")
        print(f"El precio de tu auto es {self.precio}")

        if self.precio > 500000:
            print("Wow, tu auto es realmente caro")
    
    def calcularImpuesto(self):
        print(f"El impuesto de tu auto es de {self.precio * 0.01} pesos mexicanos")

# lambo = auto("azul","chi-123-45-11","BMW",600000)

# lambo.mostrarAtributos()
class estudiante():
    def __init__(self, nombre, codigo, asignatura, nota1,nota2,nota3,nota4):
        self.nombre = nombre
        self.codigo = codigo
        self.asignatura = asignatura
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def mostrarDatos(self):
        print("Estudiante:", self.nombre)
        print("codigo:", self.codigo)
        print("asignatura:", self.asignatura)
        print("Nota 1:", self.nota1)
        print("Nota 2:", self.nota2)
        print("Nota 3:", self.nota3)
        print("Nota 4:", self.nota4)

    def promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

        if promedio >= 3:
            print(f"El estudiante {self.nombre} aprobó la materia con un promedio de {promedio}")
        else:
            print(f"Reprobaste pa, tu pinche promedio fue de {promedio}, que pendejo")

# jorge = estudiante("Jorge", "5123125", "Matematicas", 4,5,5,3)

# jorge.mostrarDatos()
# jorge.promedio()

# Ejercicio 3

class producto():
    def __init__(self, nombre, precio):
        self.precio = precio
        self.nombre = nombre

    def datos(self):
        print(f"{self.nombre}: {self.precio}")

class comida(producto):
    def __init__(self, nombre, precio, caducidad):
        super().__init__(nombre, precio,)
        self.caducidad = caducidad

    def datos(self):
        print(f"{self.nombre}: {self.precio}")
        print(f"Caducidad: {self.caducidad}")

class herramientas(producto):
    def __init__(self, nombre, precio, material):
        super().__init__(nombre, precio)
        self.material = material
        
    def datos(self):
        print(f"{self.nombre}: {self.precio}")
        print(f"Material: {self.material}")

class aseo(producto):
    def __init__(self, nombre, precio, uso):
        super().__init__(nombre, precio)
        self.uso = uso
    
    def datos(self):
        print(f"{self.nombre}: {self.precio}")
        print("Uso: {self.uso}")

class tienda():
    def __init__(self, inventario):
        self.inventario = inventario
    
    def comida(self):
        
        for item in self.inventario:
            if isinstance(item,comida) == True:
                item.datos()
    
    def herramientas(self):
        for item in self.inventario:
            if isinstance(item,herramientas) == True:
                item.datos()

    def aseo(self):
        for item in self.inventario:
            if isinstance(item,aseo) == True:
                item.datos()
                print("\n")

manzana = comida("Manzana", 3000, "22/03/24")
pera = comida("Pera", 4000, "25/03/24")
chocolate = comida("Chocolate", 2500, "12/07/24")
martillo = herramientas("Martillo", 45000, "Metal")
destornillador = herramientas("Destornillador", 37000, "Metal y plástico")
detergente = aseo("Detergente", 7000, "1 tapa de detergente por cada 5 litros de agua")

inventario = [manzana, destornillador, detergente, chocolate, martillo, pera]

Tiendita = tienda(inventario)

# Tiendita.comida()
# Tiendita.herramientas()
# Tiendita.aseo()

#Ejercicio 4

# class figuras():
#     def __init__(self,figura):
#         self.figura = figura
    
#     def calcArea(self):
#         pass

#     def calcPerimetro(self):
#         pass

# class rectangulo(figuras):
#     def __init__(self, figura, lado1, lado2):
#         super().__init__(figura)
#         self.lado1 = lado1
#         self.lado2 = lado2

#     def calcArea(self):
#         return self.lado1 * self.lado2
    
#     def calcPerimetro(self):
#         return 2*self.lado1 + 2*self.lado2
    
#     def datos(self):
#         print(self.figura)
#         print(f"Lado 1: {self.lado1}, lado 2: {self.lado2}")
#         print(f"AREA: {self.calcArea()}")
#         print(f"PERIMETRO: {self.calcPerimetro()}")

# class triangulo(figuras):
#     def __init__(self, figura, base, altura):
#         super().__init__(figura)
#         self.base = base
#         self.altura = altura

#     def calcArea(self):
#         return (self.base * self.altura) / 2
    
#     def calcPerimetro(self):
#         hipotenusa = (self.base**2 + self.altura**2)**(1/2)
#         return self.base + self.altura + hipotenusa
    
#     def datos(self):
#         print(self.figura)
#         print(f"Base: {self.base}, Altura: {self.altura}")
#         print(f"AREA: {self.calcArea()}")
#         print(f"PERIMETRO: {self.calcPerimetro()}")

# class circulo(figuras):
#     def __init__(self, figura,radio):
#         super().__init__(figura)
#         self.radio = radio 

#     def calcArea(self):
#         return pi*self.radio**2
    
#     def calcPerimetro(self):
#         return 2*pi*self.radio

#     def datos(self):
#         print(self.figura)
#         print(f"Radio: {self.radio}")
#         print(f"AREA: {self.calcArea()}")
#         print(f"PERIMETRO: {self.calcPerimetro()}")

# # circ = circulo("Circulo",2)

# circ.datos()

class libro():
    def __init__(self,titulo, autor, ISBN, estado):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.estado = estado
    
    def datos(self):
        print(self.titulo)
        print(self.autor)
        print(self.ISBN)
        if self.estado == True:
            print("Libro disponible")
        else:
            print("libro tomado")

class biblioteca():
    def __init__(self,libros): #libros es una lista de varios obejtos libro
        self.libros = libros

    def buscar_libro(self,nombre):
        for libro in self.libros: # Se itera en la lista libros para buscar el libro
            if nombre.upper() == libro.titulo.upper():
                print("Libro encontrado!")
                libro.datos()
    
    def prestados(self):
        print("LIBROS PRESTADOS")
        for libro in self.libros:
             if libro.estado == False:
              libro.datos()
              print("\n")

class persona():
    def __init__(self,nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.lib_prestados = []
    
    def prestar(self, biblioteca):
        print("LIBROS DISPONIBLES")
        for libro in biblioteca.libros:
            if libro.estado == True:
                libro.datos()
                print("\n")

        seleccion = input("Nombre del libro: ")
        for libro in biblioteca.libros:
            if seleccion.upper() == libro.titulo.upper():
                self.lib_prestados.append(libro)
                libro.estado = False
                print("\nLibro prestado correctamente!\n")
                break

    def devolver(self):
        print("LIBROS PRESTADOS")
        for libro in self.lib_prestados:
            libro.datos()
            print("\n")

        seleccion = input("Nombre del libro a devolver: ")
        for libro in self.lib_prestados:
            if seleccion.upper() == libro.titulo.upper():
                libro.estado = True
                del self.lib_prestados[self.lib_prestados.index(libro)]
                break



misery = libro("Misery", "Stephen King", "9788466345682", True)
it = libro("It", "Stephen King", "9780450411434", False)
cien_anos = libro("Cien años de soledad", "Gabriel García Márquez", "9780307474728", True)
don_quijote = libro("Don Quijote de la Mancha", "Miguel de Cervantes", "9788491050413", False)
el_principito = libro("El Principito", "Antoine de Saint-Exupéry", "9780156012195", True)

libros = [misery, it, cien_anos, don_quijote, el_principito]

jorge = persona("Jorge","124151515")

biblio = biblioteca(libros)

biblio.prestados()

jorge.prestar(biblio)

jorge.devolver()

biblio.prestados()