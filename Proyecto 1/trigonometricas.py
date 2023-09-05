from abstraccion import Expresion
from math import *

class Trigonometricas(Expresion):
    def __init__(self, L, tipo, fila, columna):
        self.L = L
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        left = ''
        if self.L != None:
            left = self.L.operar(arbol)
        
        if self.tipo.operar(arbol) == "Seno":
            print(f"La operación es Seno de {left}" )
            return sin(left)
        if self.tipo.operar(arbol) == "Coseno":
            print(f"La operación es Coseno de {left}" )
            return cos(left)
        if self.tipo.operar(arbol) == "Tangente":
            print(f"La operación es Tangente de {left}" )
            return tan(left)
        else:
            return 0
        
    def getFila(self):
        return super().getFila
    def getColumna(self):
        return super().getColumna