from abstraccion import Expresion

class Aritmetica(Expresion):
    
    def __init__(self,L ,R , tipo, fila, columna):
        self.L = L
        self.R = R
        self.tipo = tipo
        super().__init__(fila, columna)
        
        
    def operar(self, arbol):
        Lvalue = ''
        Rvalue = ''

        if self.L != None:
            Lvalue = self.L.operar(arbol)
            #print(self.L.operar(arbol))
        if self.R != None:
            Rvalue = self.R.operar(arbol)

        if self.tipo.operar(arbol) == 'Suma':
            print(f"La operación es Suma {Lvalue} + {Rvalue}" )
            #print(self.tipo.operar)
            return Lvalue + Rvalue
        elif self.tipo.operar(arbol) == 'Resta':
            print(f"La operación es Resta {Lvalue} - {Rvalue}" )
            #print(self.tipo.operar)
            return Lvalue - Rvalue
        elif self.tipo.operar(arbol) == 'Multiplicacion':
            print(f"La operación es Multiplicación {Lvalue} * {Rvalue}" )
            return Lvalue * Rvalue
        elif self.tipo.operar(arbol) == 'Division':
            print(f"La operación es División {Lvalue} / {Rvalue}" )
            return Lvalue / Rvalue
        elif self.tipo.operar(arbol) == 'Modulo':
            print(f"La operación es Modulo {Lvalue} % {Rvalue}" )
            return Lvalue % Rvalue
        elif self.tipo.operar(arbol) == 'Potencia':
            print(f"La operación es potencia {Lvalue}^{Rvalue}" )
            return Lvalue ** Rvalue
        elif self.tipo.operar(arbol) == 'Raiz':
            print(f"La operación es Raiz {Lvalue}^1/{Rvalue}" )
            return Lvalue ** (1/Rvalue)
        elif self.tipo.operar(arbol) == 'Inverso':
            print(f"La operación es Inverso 1/{Lvalue}")
            return 1/Lvalue
        
        else:
            
            return 0
        
    def getFila(self):
        return super().getFila
    
    def getColumna(self):
        return super().getColumna