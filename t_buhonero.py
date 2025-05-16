class objeto():
    def __init__(self, nombre, p_compra):
        self.nombre = nombre
        self.p_compra = p_compra
        self.p_venta = p_compra*0.75
    
    #lista = ["Granada", "Vendas","Balas"]
    #cantidad = [3,2,4]
    def inv_buhonero(self,inventario, cantidades):
        indice = inventario.index(self)# Toma el numero de indice del objeto actual en la lista del inventario(inventario es una lista)
        print(f"{self.nombre}   x   {cantidades[indice]}    ({self.p_compra} $)") #cantidad[indice] toma el indice obtenido anteriormente y lo usa como referencia al valor de cantidad que es el mismo de inventario(cantidad tmb es una lista)

    def inv_leon(self,inventario, cantidades):
        indice = inventario.index(self)# Toma el numero de indice del objeto actual en la lista del inventario
        print(f"{self.nombre}   x   {cantidades[indice]}    ({self.p_venta} $)") 

# inventario = [objeto2, objeto1, objeto3]
# cantidad = [3,2, 10]

# objeto3.inv_buhonero(inventario, cantidad)

class arma(objeto):
    def __init__(self, nombre, p_compra, daño, vel_recarga, cadencia, capacidad):
        super().__init__(nombre, p_compra)
        self.daño = daño
        self.vel_recarga = vel_recarga
        self.cadencia = cadencia
        self.capacidad = capacidad

    def inv_buhonero(self, inventario, cantidades):
        print(self.nombre, self. p_compra)

        print(" Daño     Vel.Recarga     Cadencia       Capacidad")
        print(" "+"|"*self.daño + "-"*(6-self.daño), end="      ")
        print(" "+"|"*self.vel_recarga + "-"*(3-self.vel_recarga), end="           ")
        print(" "+"|"*self.cadencia + "-"*(3-self.cadencia), end="          ")
        print(" "+"|"*self.capacidad + "-"*(6-self.capacidad))

    # precio = 10000 - 8000 (1-daño/5)
    def inv_mejora(self):
        print("Mejorar", self.nombre)

        print("1.-Daño          " + "|"*self.daño + "-"*(6-self.daño), end="    ")
        print(10000 - 8000 *(1-self.daño/5), "$")

        print("2.-Vel. Recarga  " + "|"*self.vel_recarga + "-"*(3-self.vel_recarga),end="       ")
        print(10000 - 8000 *(1-self.vel_recarga/2), "$")
        
        print("3.-Cadencia      " + "|"*self.cadencia + "-"*(3-self.cadencia),end="       ")
        print(10000 - 8000 *(1-self.cadencia/2), "$")

        print("4.-Capacidad     " + "|"*self.capacidad + "-"*(6-self.capacidad),end="    ")
        print(10000 - 8000 *(1-self.capacidad/5), "$")

class leon():
    def __init__(self, inventario, cantidades, dinero ):
        self.inventario = inventario
        self.cantidades = cantidades
        self.dinero = dinero

    def vender(self, buhonero):
        bandera = False
        while bandera == False:
            n = 1
            print("--------------INVENTARIO--------------")
            print("\nDinero: ", self.dinero)
            for item in self.inventario:
                print(f"{n}.-", end=" ")
                item.inv_leon(self.inventario, self.cantidades)
                n += 1
                print("\n")
            print(len(self.inventario) + 1, "Volver")
            opcion = int(input("Vender: "))

            if opcion == len(self.inventario) + 1:
                bandera = True
                break
            obj = self.inventario[opcion-1]
            indice = self.inventario.index(obj)

            self.dinero += obj.p_venta
            self.cantidades[indice] -= 1

            posee = False
            for i in buhonero.inv_tienda:
                if i == obj:
                    buhonero.cantidades[buhonero.inv_tienda.index(i)] += 1
                    posee = True
                    break
            # Estas acciones deben estar fuera del for
            if not posee:
                buhonero.inv_tienda.append(obj)
                buhonero.cantidades.append(1)
            if self.cantidades[indice] == 0:
                self.inventario.remove(obj)
                self.cantidades.pop(indice)
            # Termina la venta y vuelve a mostrar el inventario

class buhonero():
    def __init__(self, inv_tienda, cantidades):
        self.inv_tienda = inv_tienda
        self.cantidades = cantidades

    def vender(self, leon):
        bandera = False
        while bandera == False:
            n = 1
            print("--------------Tienda--------------")
            print("\nDinero: ", leon.dinero)
            for item in self.inv_tienda:
                print(f"{n}.-", end=" ")
                item.inv_buhonero(self.inv_tienda, self.cantidades)
                n += 1
                print("\n")
            print(len(self.inv_tienda) + 1, "Volver")
            opcion = int(input("Comprar: "))

            if opcion == len(self.inv_tienda) + 1:
                bandera = True
                break
            obj = self.inv_tienda[opcion-1]
            indice = self.inv_tienda.index(obj)

            if leon.dinero >= obj.p_compra:
                leon.dinero -= obj.p_compra
                posee = False
                for i in leon.inventario:
                    if i == obj:
                        leon.cantidades[leon.inventario.index(i)] += 1
                        self.cantidades[indice] -= 1
                        posee = True
                        break
                if not posee:
                    leon.inventario.append(obj)
                    leon.cantidades.append(1)
                    self.cantidades[indice] -= 1
                if self.cantidades[indice] == 0:
                    self.inv_tienda.remove(obj)
                    del self.cantidades[indice]
            else:
                print("No tienes suficiente dinero")
                return
    def mejorar(self, leon):
        bandera = False
        while bandera == False:
            n = 1
            print("--------------MEJORAR--------------")
            print("\nDinero: ", leon.dinero)
            for i in leon.inventario:
                if isinstance(i, arma):
                    print(f"{n}.-", end=" ")
                    i.inv_buhonero(leon.inventario, leon.cantidades)
                    print("\n")
                    n += 1
                    print("\n")
            print(len(self.inv_tienda) + 1, "Volver")   
            opcion = int(input("Mejorar: "))
        
            if opcion == n + 1:
                bandera = True
                break

            num_arma = 0
            for i in leon.inventario:
                if isinstance(i, arma) == True:
                    num_arma += 1
                if isinstance(i, arma) == True and num_arma == opcion - 1:
                    mejora = 0
                    while mejora != 5:
                        print("\n-----------------MEJORAR--------------")
                        print("\nDinero: ", leon.dinero)                    
                        i.inv_mejora()
                        print("\n5.-Volver")
                        mejora = int(input("Mejorar: "))
                        if mejora == 5:
                            break

                        if mejora == 1:
                            if i.daño < 6:
                                precio = 10000 - 8000 *(1-i.daño/5)
                                if leon.dinero >= precio:
                                    i.daño += 1
                                    leon.dinero -= precio
                                else:
                                    print("No tienes suficiente dinero")
                            else:
                                print("No puedes mejorar mas")
                        elif mejora == 2:
                            if i.vel_recarga < 3:
                                precio = 10000 - 8000 *(1-i.vel_recarga/2)
                                if leon.dinero >= precio:
                                    i.vel_recarga += 1
                                    leon.dinero -= precio
                                else:
                                    print("No tienes suficiente dinero")
                            else:
                                print("No puedes mejorar mas")
                        elif mejora == 3:
                            if i.cadencia < 3:
                                precio = 10000 - 8000 *(1-i.cadencia/2)
                                if leon.dinero >= precio:
                                    i.cadencia += 1
                                    leon.dinero -= precio
                                else:
                                    print("No tienes suficiente dinero")
                            else:
                                print("No puedes mejorar mas")
                        elif mejora == 4:
                            if i.capacidad < 6:
                                precio = 10000 - 8000 *(1-i.capacidad/5)
                                if leon.dinero >= precio:
                                    i.capacidad += 1
                                    leon.dinero -= precio
                                else:
                                    print("No tienes suficiente dinero")
                            else:
                                print("No puedes mejorar mas")
                        else:
                            print("No puedes mejorar mas")
                        # Se verifica si el jugador tiene suficiente dinero para mejorar el arma
                            

def tienda_buhonero(leon, buhonero):
    seleccion = 0
    while seleccion != 4:
        print("\n------------------TIENDA--------------\n\n")
        print(" [1.-Comprar] [2.-Mejorar] [3.-Vender] ")
        print("                            [4.-Salir] \n\n")
        seleccion = int(input("Seleccion: ")) 

        if seleccion == 1:
            print("\n\n")
            buhonero.vender(leon)
        elif seleccion == 2:
            print("\n\n")
            buhonero.mejorar(leon)
        elif seleccion == 3:
            print("\n\n")
            leon.vender(buhonero)
        else:
            print("Opcion no valida")

Rifle = arma("Rifle", 12000, 5, 3, 2, 6)  
Escopeta = arma("Escopeta", 8000, 6, 2, 1, 4)
Granada = objeto("Granada", 1500)
Hierba = objeto("Hierba Verde", 500)
Municion = objeto("Munición", 1000)
Spray = objeto("Spray", 2000)

inventario = [Rifle, Escopeta, Granada, Hierba, Municion, Spray]
inv_tienda = [Rifle, Escopeta, Granada, Hierba, Municion, Spray]
cantidad_tienda = [1, 1, 5, 3, 50, 2]
cantidades = [1, 1, 5, 3, 50, 2]

Leon = leon(inventario,cantidades,20000)
Buhonero = buhonero(inv_tienda, cantidad_tienda)

tienda_buhonero(Leon, Buhonero)