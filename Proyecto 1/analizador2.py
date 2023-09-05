from aritmeticas import Aritmetica
from Lexema import Lexema
from trigonometricas import Trigonometricas
from errores import Errores
#archivo = open('prueba2.txt', 'r')
#leer = ''
#for i in archivo.readlines():
#    leer += i
class analizador2:
    def __init__(self):
        self.col = 1
        self.fil = 1
        self.lista_lexemas = []
        self.lista_errores = []
        #self.instruc
        #self.lexemas
        
        self.reservadas = {
            'OPERACION':'Operacion',
            'VALOR1': 'Valor1',
            'AVALOR2': 'Valor2',
            'ASUMA': 'Suma',
            'ARESTA': 'Restaa',
            'AMULTIPLICACION': 'Multiplicacion',
            'ADIVISION': 'Division',
            'APOTENCIA': 'Potencia',
            'ARAIZ': 'Raiz',
            'AINVERSO': 'Inverso',
            'ASENO': 'Seno',
            'ACOSENO': 'Coseno',
            'ATANGENTE': 'Tangente',
            'AMODULO': 'Modulo',
            'ATEXTO': 'Texto',
            'ACOLORFONDONODO': 'Color-Fondo-Nodo',
            'ACOLORFUENTENODO': 'Color-Fuente-Nodo',
            'AFORMANODO': 'Forma-Nodo',
            'COMA': ',',
            'PUNTO': '.',
            'DOSPUNTOS': ':',
            'IZQUIERDO': '[',
            'DERECHO': ']',
            'LLAVEIZ': '{',
            'LLAVEDER': '}'       
        }
        self.lexemas = list(self.reservadas.values())

    def instruccion(self, cadena:str):
        lexema = ""
        count = 0
        while cadena:
            i = cadena[count]
            count += 1  
            if i == '\"':
                lexema, cadena = self.armar_lexema(cadena[count:])
                #Si cadena no retorna nulo
                if lexema and cadena:
                    self.col +=1
                    l = Lexema(lexema, self.fil, self.col)
                    
                    #Aqui almacena todas las palabras lexemas
                    self.lista_lexemas.append(l)
                    #se le suma el tamaño del lexema a la columna y se le suma 1 como inicia el 0
                    self.col += len(lexema) + 1
                    #y se reinicia el count
                    count = 0
            #elif i.isdigit():
            elif ord(i) >= 48 and ord(i) <= 57:
                #int(i)
                token, cadena = self.num(cadena)
                if token and cadena:
                    self.col +=1
                    #arma el lexema
                    n = Lexema(token, self.fil, self.col)
                    self.lista_lexemas.append(n)

                    self.col += len(str(token))+1
                    count = 0

            elif i == "[" or i == "]":
                c = Lexema(i, self.fil, self.col)
                self.lista_lexemas.append(c)
                cadena = cadena[1:]
                count = 0
                self.col += 1 
            #Si encinetra una taulación    
            elif i == "\t":
                #Se le suman 4 espacios a la columna
                self.col += 4
                # y se eliminan esos 4 espacios
                cadena = cadena[4:]
                count = 0
            elif i =="\n":
                cadena = cadena[1:]
                count = 0
                self.fil += 1
                #Se reinicia la columna a 1
                self.col = 1
            elif i == ' ' or i == '\r' or i == "{" or i == '}' or i == ','or i == '.' or i == ':':
                self.fil += 1
                cadena = cadena[1:]
                count = 0

            else:
                self.lista_errores.append(Errores(i, self.fil, self.col))
                cadena = cadena[1:]
                count = 0
                self.col += 1 

        return self.lista_lexemas, self.lista_errores
    
    def armar_lexema(self, cadena):
        lexema = ""
        count = ""
        for i in cadena:
            count += i
            if i == '\"':
                #lexema va recorriendo las palabras y arma la palabara para aceptarlo como un caracter valido
                #se regresa la cadena con la posición del count  hasta el final por eso los :
                return lexema, cadena[len(count):]
            else:
                lexema += i
        return None, None 

    def num(self, cadena:str):
        num = ""#token
        count = ""
        decimal = False
        for i in cadena:
            count += i
            if i ==".":
                decimal = True
            if i == '\"' or i == ' ' or i == '\n' or i == '\t':
                if decimal:
                    return float(num), cadena[len(count)-1:]
                else:
                    return int(num), cadena[len(count)-1:]
            else:
                num += i

        return None, None

    def operar(self):
        operacion = ""
        n1 = ""
        n2 = ""
        #lexema1 = list
        while self.lista_lexemas:
            lexema1 = self.lista_lexemas.pop(0)
            if lexema1.operar(None) == "Operacion":
                operacion = self.lista_lexemas.pop(0)
            elif lexema1.operar(None)== "Valor1":
                n1 = self.lista_lexemas.pop(0)
                if n1.operar(None) == "[":
                    n1 = self.operar()
            elif lexema1.operar(None)== "Valor2":
                n2 = self.lista_lexemas.pop(0)
                if n2.operar(None) == "[":
                    n2 = self.operar()

            if operacion and n1 and n2:
                return Aritmetica(n1,n2,operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna}')
            elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):
                return Trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
        return None
         

    #def getErrores(self):
    #    return self.lista_errores
    def getErrores(self):
        #self.lista_errores: list = self.getErrores()
        contador = 1
        print("{")
        for error in self.lista_errores:
            error = self.lista_errores.pop(0)
            print(error.operar(contador),",")
            contador+= 1
        print("}")

    def operar_(self):
        instruc= []
        contador = 1
        while True:
            operacio = self.operar()
            if operacio:
                instruc.append(operacio)
            else:
                break
        for i in instruc:
            print(f"Resultado operación {contador}: ",i.operar(None))
            #print(i.operar.tipo(None))
            print("**************************************************")
            contador+=1




"""
a = analizador2()
a.instruccion(leer)

a.operar_()
"""

#print(a)