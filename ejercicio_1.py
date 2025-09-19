# Siguiendo el ejercicio del Camión realizado en la actividad anterior, el objetivo es crear nuevas 
# clases reutilizando la mayor cantidad de código posible mediante herencia. A continuación, se detallan
# los requisitos para cada clase. Recuerda implementar la restricción de unicidad de patentes de manera
# que aplique a todos los vehículos terrestres (autos y camiones) simultáneamente, pero no a las 
# embarcaciones.

# #### Clase Auto
# - Similar al Camión, pero sin atributo de carga.
# - Tiene exactamente 4 ruedas (los camiones tienen 8).
# - Atributo `posicion_inicial` que inicia en 0 al crear el objeto.
# - Implementa el método `trasladarse(desplazamiento: int)`, que actualiza la posición sumando el
# desplazamiento y retorna un mensaje indicando el movimiento por tierra.

# ```python

class Vehículo:  
    def __init__(self, marca:str, año:int, desplazamiento: int, posicion_inicial = 0):
        self.marca = self.validar_cadena(marca)
        self.año = self.validar_entero(año)
        self.posicion_inicial = posicion_inicial
        self.desplazamiento = self.validar_entero(desplazamiento)
    
    def validar_cadena(self, cadena: str):
        if not isinstance(cadena, str):
            raise TypeError('El texto ingresado debe ser una cadena.')
        if len(cadena) == 0:
            raise ValueError('El texto ingresado no puede ser vacío.')
        return cadena
        
    def validar_entero(self, entero:int):
        if not isinstance(entero, int):
            raise TypeError('El texto ingresado debe ser un número entero.')
        if len(str(entero)) == 0:
            raise ValueError('El texto ingresado no puede ser vacío')
        return entero
    
        
class Camion(Vehículo):
    patentes_usadas = set() 
     
    def __init__(self, marca:str, año:int, modelo:str, patente:str, carga:str, desplazamiento: int, posicion_inicial = 0):
        super().__init__(marca,año, desplazamiento, posicion_inicial)
        self.patente = self.validar_patente(patente)
        self.modelo = self.validar_cadena(modelo)
        self.carga = self.validar_cadena(carga)
        
    def __str__(self):
        return f"Camión: #{self.patente} \nMarca: {self.marca} \nCarga: {self.carga} \nAño: {self.año}  \nModelo: {self.modelo}"

    def __eq__(self, otro):
        if not isinstance(otro, Camion):
            raise TypeError('El objeto debe ser una instancia de la clase Camion.')
        return (self.patente == otro.patente)
     
    def validar_patente (self, patente):
        if patente in Camion.patentes_usadas:
            raise ValueError(f'La patente {patente} ya está asignada a otro camion.')
        else:
            Camion.patentes_usadas.add(patente)
        return patente
    
    def trasladarse(self, desplazamiento):
        self.posicion_inicial += desplazamiento
        return f'El vehículo se ha desplazado {desplazamiento} por tierra, y ahora se encuentra en la posición {self.posicion_inicial}.'

class Auto(Vehículo):
    def __init__(self, marca:str, año:int, patente:str, modelo:str,  desplazamiento: int, posicion_inicial= 0):
        super().__init__(marca,año, desplazamiento,posicion_inicial)
        self.patente = Camion.validar_patente(self,patente)
        self.modelo = self.validar_cadena(modelo)
        
    def __str__(self):
        return f'Auto: #{self.patente} \nMarca: {self.marca} \nAño: {self.año}  \nModelo: {self.modelo}\n{Camion.trasladarse(self, self.desplazamiento)}'

#### Clase Lancha
# - Puede desplazarse, con `posicion_inicial` iniciando en 0.
# - Atributos: marca, año y marca de motor (no tiene ruedas ni carga).
# - Las patentes de lanchas son independientes (no comparten restricción con vehículos terrestres).
# - Método `trasladarse(desplazamiento: int)` que actualiza la posición y retorna un mensaje indicando
# movimiento por agua a motor.

# ```python
class Lancha(Vehículo):
    def __init__(self, marca: str, año: int, patente: str, marca_motor: str,  desplazamiento: int, posicion_inicial= 0):
        super().__init__(marca, año, desplazamiento, posicion_inicial)
        self.patente = self.validar_cadena(patente)
        self.marca_motor = self.validar_cadena(marca_motor)
        
    def __str__(self):
        return f'Lancha: #{self.patente} \nMarca: {self.marca} \nMarca del motor: {self.marca_motor} \nAño: {self.año} \n{self.trasladarse(self.desplazamiento)}'
        
    def trasladarse(self, desplazamiento):
        self.posicion_inicial += desplazamiento
        return f'El vehículo se ha desplazado {desplazamiento} por agua, y ahora se encuentra en la posición {self.posicion_inicial}.'

# #### Clase Velero
# - Similar a la Lancha, se desplaza por agua, pero con cantidad de velas en lugar de motor.
# - Método `trasladarse(desplazamiento: int)` que retorna un mensaje indicando movimiento por agua a vela.

# ```python
class Velero(Vehículo):
    def __init__(self, marca: str, año: int, desplazamiento: int, patente: str, cantidad_velas: int, posicion_inicial=0):
        super().__init__(marca, año, desplazamiento, posicion_inicial)
        self.patente = self.validar_cadena(patente)
        self.cantidad_velas = self.validar_entero(cantidad_velas)

    def __str__(self):
        return f'Velero: #{self.patente} \nMarca: {self.marca} \nCantidad de velas: {self.cantidad_velas} \nAño: {self.año} \n{Lancha.trasladarse(self,self.desplazamiento)}'

# #### Clase Anfibio
# - Vehículo que puede trasladarse por tierra o por agua (a motor).
# - Por defecto, `trasladarse(desplazamiento: int)` lo hace por tierra.
# - Implementa un método adicional para trasladarse por agua.

# ```python
class Anfibio(Vehículo):
    medios_posibles = {'tierra', 'agua'}
    
    def __init__(self, marca: str, año: int, desplazamiento: int,patente: str,posicion_inicial=0, medio_transporte='tierra'):  # Completa con atributos heredados y propios
        super().__init__(marca, año, desplazamiento, posicion_inicial)
        self.patente = self.validar_cadena(patente)
        self.medio_transporte = medio_transporte

    def setter_medio(self, medio_transporte):
        medio_transporte.lower()
        if self.medio_transporte not in Anfibio.medios_posibles:
            raise ValueError(f'El medio de transporte debe ser uno de los siguientes: {self.medios_posibles}')
        self.medio_transporte = medio_transporte
        return medio_transporte
                    
    def __str__(self):
        if self.medio_transporte.lower() == 'agua':
            return f'Anfibio: #{self.patente} \nMarca: {self.marca} \nAño: {self.año} \n{Lancha.trasladarse(self, self.desplazamiento)}'
        else:
            return f'Anfibio: #{self.patente} \nMarca: {self.marca} \nAño: {self.año} \n{Camion.trasladarse(self, self.desplazamiento)}'
            

# ```

# Recuerda utilizar herencia para evitar duplicación de código. Los mensajes de retorno
# deben ser específicos según el tipo de vehículo y medio de transporte.


if __name__ == '__main__':
    camiones = []
    
    Auto1 = Auto ('Ford',2021,'AA220SD','Fiesta',4)
    Lancha1 = Lancha('Lock', 2020,'AA220SD', 'Mercedes', 3)
    Velero1 = Velero('Moneda', 2014, 7,'BB332SS', 2)
    Anfibio1 = Anfibio('Kia',2020,2, 'BB333DD')
    
    print(Auto1)
    print(Lancha1)
    print(Velero1)
    print(Anfibio1)