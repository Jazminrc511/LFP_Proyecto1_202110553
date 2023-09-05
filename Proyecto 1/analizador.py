archivo = open('prueba.txt', 'r')
leer = ''
for i in archivo.readlines():
    leer += i
#print(leer)

class analizador:
    def __init__(self, archivo: str):
        self.leer = archivo
        self.count = 0
        self.fil=0

        self.col = 0
        self.ListaErrores = [] # LISTA PARA GUARDAR ERRORES

    def token(self, token:str, estado_actual:str,estado_siguiente:str):
        if self.leer[self.count] != " ":
            text = self.juntarCaracteres(self.count, len(token))
            #print(text)
            if self.analizar(token, text):
                self.count += len(token)-1
                self.col += len(token)-1
                return estado_siguiente
            else:
                return "Error"
            
        else:
            return estado_actual
        
    def juntarCaracteres(self,indice:int, count:int):
        try:
            temp = ""
            for i in range(indice, indice + count):
                temp += self.leer[i]
            return temp
        except:
            return None
        
    def analizar(self, token, texto):
        try:
            count = 0
            token_temp = ""
            for i in texto:
                # Aqui los tokens haran match
                #print('COMBINACION -> ',i , '==', token[count])
                if str(i) == str(token[count]):
                    token_temp += i
                    count += 1
                else:
                    #print("type error 1")
                    return False
                
            print(f"------Encontre------{token_temp}")
            return True
        except:
            #print("type error 2")
            return False
        
    def digito(self, sig):
        actual = "D0"
        num = ""
        while self.leer[self.count] != "":
            #print(f'CARACTER - {self.leer[self.count] } | ESTADO - {actual} | FILA - {self.fil}  | COLUMNA - {self.col}')
            if self.leer[self.count] == '\n':
                self.fil += 1
                self.col = 0

            #Para salirse
            elif str(self.leer[self.count]) == '"':
                self.count -= 1
                return [sig, num]
            
            elif str(self.leer[self.count]) == ']':
                self.count -= 1
                return [sig, num]
            
            elif str(self.leer[self.count]) == '}':
                self.count -= 1
                return [sig, num]
            #Para reconocer decimal
            elif self.leer[self.count] == '.':
                token = "."
                if actual == 'D2' or actual == 'D0':
                    actual = "Error"
                elif self.leer[self.count] != ' ':
                    text = self.juntarCaracteres(self.count, len(token))
                    if self.analizar(token, text):
                        num += text
                        actual = 'D2'
                        self.count += len(token)-1
                        self.col += len(token)-1
                    else:
                        actual = "Error"

            # ************************
            #         ESTADOS
            # ************************
            elif actual == 'D0' or actual =='D1':
                if self.leer[self.count] != ' ':
                    actual = "Error"
                    for i in ['0','1','2','3','4','5','6','7','8','9']:
                        token = i
                        textJuntar = self.juntarCaracteres(self.count, len(token))
                        if self.analizar(token, textJuntar):
                            num += textJuntar
                            actual = 'D1'
                            break
            # D2 -> [0-9] D2 
            elif actual == 'D2':
                if self.leer[self.count] != ' ':
                    actual = "Error"
                    for i in ['0','1','2','3','4','5','6','7','8','9']:
                        textJuntar = self.juntarCaracteres(self.count, len(i))
                        if self.analizar(i, textJuntar):
                            num += textJuntar
                            actual = 'D2'
                            break

            if actual =="Error":
                    return ["Error", -1]
            # Se incrementa la posición
            if self.count < len(self.leer)-1:
                self.count +=1
            else:
                break     


    def operaciOnes(self, siguiente):
        actual = 'S1'
        hijo_derecho = ""
        hijo_izquierdo = ""
        operador = ""
        while self.leer[self.count] != "":
            #print(f'CARACTER - {self.leer[self.count] } | ESTADO - {actual} | FILA - {self.fil}  | COLUMNA - {self.col}')
            
            #Identifica los saltos de linea
            if self.leer[self.count] == '\n':
                self.fil += 1
                self.col = 0


            # ************************
            #         ESTADOS
            # ************************
            
            # S1 -> "Operacion" S2
            elif actual == "S1":
                actual = self.token('"Operacion"', 'S1', 'S2')
                #print("Estado actual: ",actual)

            # S2 -> : S3
            elif actual == "S2":
                actual = self.token(':', 'S2', 'S3')
                #print("Estado actual: ",actual)

            # S3 -> OPERADOR S4
            elif actual == "S3":
                operadores = ['"Suma"','"Resta"','"Multiplicacion"']
                for i in operadores:
                    actual = self.token(i, 'S3', 'S4')
                    if actual != "Error":
                        operador = i
                        break
                #print("Estado actual: ",actual)

            elif actual == "S4":
                actual = self.token('"Valor1"', 'S4', 'S5')
                #print("Estado actual: ",actual)

            elif actual == "S5":
                actual = self.token(':', 'S5', 'S6')
                #print("Estado actual: ",actual)

            elif actual == "S6":
                actual = self.token("[", "S6", "S7")
                if actual =="Error":
                    actual = "S9"
                    a = self.digito("S9")
                    if "Error" ==a[0]:
                        actual = "Error"
                    elif a[0] == "S9":
                        hijo_izquierdo = a[1]

            elif actual == "S7":
                a = self.operaciOnes("S8")
                actual = a[0]
                hijo_izquierdo = a[1]

            elif actual == "S8":
                actual = self.token("]", "S8", "S9")

            elif actual == "S9":
                if operador == '"Inverso"' or operador == '"Seno"':
                    self.count -= 1
                    # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                    print("\t*****OPERACION ARITMETICA*****")
                    print('\t',operador ,'(',hijo_izquierdo ,')' )
                    print('\t*******************************\n')
                    op = operador +'('+hijo_izquierdo +')'
                    return ['S14', op]  
                else:
                    actual = self.token('"Valor2"', 'S9', 'S10')
                
            elif actual == "S10":
                actual = self.token(':', 'S10', 'S11')

            elif actual == "S11":
                actual = self.token("[", "S11", "S12")
                if actual =="Error":
                    actual = "S14"
                    a = self.digito("S14")
                    if "Error" == a[0]:
                        actual ="Error"
                    elif "S14" == a[0]:
                        hijo_derecho = a[1]
                        # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                        print("\t*****OPERACION ARITMETICA*****")
                        print('\t',hijo_izquierdo , operador, hijo_derecho)
                        print('\t*******************************\n')
                        op = hijo_izquierdo + operador + hijo_derecho
                        return [siguiente, op]  
                
                    #actual = self.digito("S14")

            elif actual == "S12":
                actual ="S13"
                a = self.operaciOnes("S13")
                hijo_derecho = a[1]
                if "Error" == a[0]:
                    actual = "Error"

            elif actual == "S13":
                actual = self.token("]", "S13", "S14")
                print("\t*****OPERACION ARITMETICA*****")
                print('\t',hijo_izquierdo , operador, hijo_derecho)
                print('\t*******************************\n')
                op = hijo_izquierdo + operador + hijo_derecho
                return [siguiente, op]  
            
             # ERRORES 
            if actual == 'ERROR':
                print("********************************")
                print("\tERROR")
                print("********************************")
                # ERROR
                self.guardarErrores(self.lineas[self.index], self.fila, self.columna)
                return ['ERROR', -1]
            

            """
            elif actual == "S14":
                actual = self.token('}', 'S14', 'S15')


            elif actual == "S15":
                if self.leer[self.count] != " ":
                    actual == self.token(",", "S16", "S0")

            elif actual == "16":
                break

            if actual =="Error":
                actual = "S0"
                """

            # Se incrementa la posición
            if self.count < len(self.leer)-1:
                self.count +=1
            else:
                break   
                

    

    def compile(self):
        actual = 'S0'
        while self.leer[self.count] != "":
            #print(f'CARACTER - {self.leer[self.count] } | ESTADO - {actual} | FILA - {self.fil}  | COLUMNA - {self.col}')
            #Identifica los saltos de linea
            if self.leer[self.count] == '\n':
                self.fil += 1
                self.col = 0
            #S0 -> { S1
            elif actual == 'S0':
                actual = self.token('{', 'S0', 'S1')
                #print("Estado actual: ",actual)
            elif actual == 'S1':
                if self.leer[self.count]!= " ":
                    c = self.operaciOnes("S14")
                    actual = c[0]
                    print("\t*****RESULTADO*****")
                    print('\t',c[1])
                    print('\t*******************************\n')

                    #print("Estado actual: ",actual)
            elif actual == "S14":
                actual = self.token("}", "S14", "S15")

            elif actual == "S15":
                if self.leer[self.count] != " ":
                    actual = self.token(",", "S16", "S0")

            elif actual =="S16":
                break
            #Errores
            if actual =="Error":
                #print("Aqui ocurrio un error")
                actual = 'S0'

            #INCREMENTAR POSICION
            if self.count < len(self.leer) - 1:
                self.count +=1
            else:
                break
    def guardarErrores(self, token, fila, columna):
        self.ListaErrores.append({"token":token, "fila": fila, "columna":columna})


b = analizador(leer)
b.compile()