# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas

# Dada la siguiente clase:

class Camion:

    patentes_usadas = set()   
    
    def __init__(self, patente:str, marca:str, carga:str, anio:int, modelo:str):
        self.patente = self.validar_patente(patente)
        self.marca = self.validar_cadena(marca)
        self.carga = self.validar_cadena(carga)
        self.anio = self.validar_entero(anio)
        self.modelo = self.validar_cadena(modelo)

    def __str__(self):
        return f"Camión: #{self.patente} \nMarca: {self.marca} \nCarga: {self.carga} \nAño: {self.anio}  \nModelo: {self.modelo}"
    
    
#(b)# def __eq__(self, otro):
    #     if not isinstance(otro, Camion):
    #         raise TypeError('El objeto debe ser una instancia de la clase Camion.')
    #     return (self.patente == otro.patente 
    #             and self.marca == otro.marca 
    #             and self.carga == otro.carga 
    #             and self.anio == otro.anio 
    #             and self.modelo == otro.modelo)
    
#(c)#   
    def __eq__(self, otro):
        if not isinstance(otro, Camion):
            raise TypeError('El objeto debe ser una instancia de la clase Camion.')
        return (self.patente == otro.patente)

#(d)#
    def validar_patente (self, patente):
        if patente in Camion.patentes_usadas:
            raise ValueError(f'La patente {patente} ya está asignada a otro camion.')
        else:
            Camion.patentes_usadas.add(patente)
        return patente
    
    def validar_cadena(self, cadena: str):
        if not isinstance(cadena, str):
            raise TypeError('El texto ingresado debe ser una cadena.')
        if len(cadena) == 0:
            raise ValueError('El texto ingresado no puede ser vacío.')
        
    def validar_entero(self, entero:int):
        if not isinstance(entero, int):
            raise TypeError('El texto ingresado debe ser un número entero.')
        if len(entero) == 0:
            raise ValueError('El texto ingresado no puede ser vacío')
        
# a. Indicá qué devuelven las siguientes expresiones. Analizalo con tus compañeros y 
# luego ejecutá las instrucciones en la máquina para comprobar tu respuesta.

# furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
# furgon2 = furgon1
# furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
# furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

# print(furgon1 == furgon2) # True pq analiza porque al no haber eq analiza la igualdad por id
# print(furgon1 is furgon2) # True pq is compara los id de memoria
# print(furgon3 == furgon4) # False pq son distintos
# print(furgon3 is furgon4) # False pq no apuntan al mismo id de memoria
# print(furgon1 == furgon4) # False porque aunque tienen la misma info, 
                          # no estan en el mismo id y si no hay eq se analiza la igualdad por id

# b. Modificá el código dado para que la comparación de dos objetos de la clase Camion devuelva
# True cuando todos sus atributos sean iguales.

# c. ¿Qué atributo hace único a nuestros objetos? Identificá el atributo que hace único al objeto 
# Camion y modificá el código para que la comparación de dos objetos de la clase Camion devuelva True 
# cuando ese atributo sea igual.
    # El atributo que hace unico al objeto es la patente. 

# d. Si dos personas tienen el mismo DNI, entonces... ¡Son la misma persona! ¿Cómo evitarías asignar 
# el mismo DNI a dos personas distintas? Siguiendo esta analogía, adaptá el código anterior para el 
# caso de los camiones.

# f. Creá un pequeño menú que te permita:

# 1. Registrar un nuevo camión.
# 2. Modificar la carga de un camión.
# 3. Mostrar por terminal la lista de camiones registrados, del más antiguo al más moderno.
# 4. Mostrar por terminal la marca que más veces fue registrada.

def registrar_camion(camiones):
    patente = input('Ingrese la patente: ')
    marca = input('Ingrese la marca: ')
    carga = input('Ingrese la carga: ')
    anio = int(input('Ingrese el año: '))
    modelo = input('Ingrese el modelo: ')
    
    try:
        c = Camion(patente, marca, carga, anio, modelo)
        camiones.append(c)
    except TypeError as e:
        print(f'Error: {e}')
    except ValueError as e:
        print(f'Error: {e}')
    return camiones

def modificar_carga(camiones):
    patente_cambio = input('Ingrese la patente del camión que desea modificar: ')
    carga_nueva = input('Ingrese la nueva carga: ')
    encontrado = False
    for camion in camiones:
        if camion.patente == patente_cambio:
            camion.carga = carga_nueva
            print('El cambio de carga se realizó exitosamente.')
            encontrado = True
    if encontrado == False:
        print('El camión ingresado no está registrado')
    return camiones

def lista_camiones(camiones):
    lista_ordenada = sorted(camiones, key=lambda c:c.anio)
    for camion in lista_ordenada:
        print(camion)

def top_marca(camiones):
    marcas=[]
    for camion in camiones:
        marcas.append(camion.marca)
    max_marca = max(marcas, key=lambda x: marcas.count(x))
    return print(f'La marca más popular es {max_marca}')
    
def menu():
    opciones = {
        1: registrar_camion,
        2: modificar_carga,
        3: lista_camiones,
        4: top_marca,
    }
    while True:
        opcion = int(input('1. Registrar un nuevo camión.\n2. Modificar la carga de un camión.\n3. Mostrar por terminal la lista de camiones registrados, del más antiguo al más moderno.\n4. Mostrar por terminal la marca que más veces fue registrada.\n5) Salir\nIngrese una opción: '))
        accion = opciones.get(opcion)
        if opcion == 5:
            break
        if accion:
            accion(camiones)
        else:
            print('Opción no válida.')
        
        
if __name__ == '__main__':
    camiones = []
    menu()
    
