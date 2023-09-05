from abstraccion import Expresion
class Errores(Expresion):
    def __init__(self,lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)

    def operar(self, error):
        no_= f'\t\t"No.": {error}\n'
        desc = '\t\t"Descripción-Token": {\n'
        lex = f'\t\t\t"Lexema": {self.lexema}\n'
        tipo = '\t\t\t"Tipo": Error\n'
        fila = f'\t\t\t"Columna": {self.fila}\n'
        col = f'\t\t\t"Fila": {self.columna}\n'
        fin = '\t\t}\n'
        return '\t{\n' + no_+ desc + lex + tipo + fila + col + fin + '\t}'
    
    def getColumna(self):
        return super().getColumna()
    def getFila(self):
        return super().getFila()