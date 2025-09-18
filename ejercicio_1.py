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

from Camiones import Camion

class Auto(Camion):
     def __init__(self, patente:str, marca:str, anio:int, modelo:str)  # Completa con los atributos necesarios
         pass

#     def trasladarse(self, desplazamiento):
#         # Actualiza posición y retorna mensaje
#         pass
# ```

# #### Clase Lancha
# - Puede desplazarse, con `posicion_inicial` iniciando en 0.
# - Atributos: marca, año y marca de motor (no tiene ruedas ni carga).
# - Las patentes de lanchas son independientes (no comparten restricción con vehículos terrestres).
# - Método `trasladarse(desplazamiento: int)` que actualiza la posición y retorna un mensaje indicando movimiento por agua a motor.

# ```python
# class Lancha:
#     def __init__(self, patente, marca, año, marca_motor):
#         pass

#     def trasladarse(self, desplazamiento):
#         # Actualiza posición y retorna mensaje específico
#         pass
# ```

# #### Clase Velero
# - Similar a la Lancha, se desplaza por agua, pero con cantidad de velas en lugar de motor.
# - Método `trasladarse(desplazamiento: int)` que retorna un mensaje indicando movimiento por agua a vela.

# ```python
# class Velero:
#     def __init__(self, patente, marca, año, cantidad_velas):
#         pass

#     def trasladarse(self, desplazamiento):
#         # Actualiza posición y retorna mensaje específico
#         pass
# ```

# #### Clase Anfibio
# - Vehículo que puede trasladarse por tierra o por agua (a motor).
# - Por defecto, `trasladarse(desplazamiento: int)` lo hace por tierra.
# - Implementa un método adicional para trasladarse por agua.

# ```python
# class Anfibio:
#     def __init__(self, patente, ...):  # Completa con atributos heredados y propios
#         pass

#     def trasladarse(self, desplazamiento):
#         # Por defecto, por tierra
#         pass

#     def trasladarse_por_agua(self, desplazamiento):
#         # Método adicional para agua
#         pass
# ```

# Recuerda utilizar herencia para evitar duplicación de código. Los mensajes de retorno deben ser específicos según el tipo de vehículo y medio de transporte.


if __name__ == '__main__':
    pass