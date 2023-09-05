import os
from tkinter import *
from tkinter import filedialog
from contextlib import redirect_stdout
from tkinter import messagebox
from analizador2 import analizador2

class Ventana:
    def __init__ (self):
        self.a = analizador2()
        self.raiz = Tk()
        #Ventana principal
        self.raiz.title("Proyecto 1")
        self.raiz.geometry("550x500")
        self.raiz.resizable(False,False)
        #self.raiz.iconbitmap("Icono.ico")
    
        self.frame = Frame(self.raiz)
        self.frame.place(x=0, y=0, width=550, height=500)
        self.frame.config(bg="#e7aebc")
        #Textos
         
        self.archivo = Label(self.frame, text="Archivo", bg="#c63b97", font=("petfinder", 14))
        self.archivo.place(x=10, y= 0, width=150, height=30,)
        
        self.ayuda = Label(self.frame, text="Ayuda", bg="#c989d6", font=("petfinder", 14))
        self.ayuda.place(x=10, y= 270, width=150, height=30,)
        
        # Botones del laado de archivo
        self.b1 = Button(self.frame, text="Abrir",bg="#c866b9", command=self.abrirTXT, font=("petfinder", 12)).place(x=10, y= 30, width=150, height=30)
        self.b2 = Button(self.frame, text="Guardar", bg="#c866b9", command=self.guardar, font=("petfinder", 12)).place(x=10, y= 60, width=150, height=30)
        self.b3 = Button(self.frame, text="Guardar Como",bg="#c866b9", command= self.guardarComo,font=("petfinder", 12)).place(x=10, y= 90, width=150, height=30)
        self.b4 = Button(self.frame, text="Analizar", bg="#c866b9",command=self.analizar ,font=("petfinder", 12)).place(x=10, y= 120, width=150, height=30)
        self.b5 = Button(self.frame, text="Errores",bg="#c866b9",command= self.errores,font=("petfinder", 12)).place(x=10, y= 150, width=150, height=30)
        self.b6 = Button(self.frame, text="Salir", bg="#c866b9",command=self.raiz.destroy,font=("petfinder", 12)).place(x=10, y= 180, width=150, height=30)
        
        # Botones del laado de ayuda
        self.b7 = Button(self.frame, text="Manual de usuario",bg="#dfc9f5", command=self.manual_usuario,font=("petfinder", 12)).place(x=10, y= 300, width=150, height=30)
        self.b8 = Button(self.frame, text="Manual de Técnico",bg="#dfc9f5",command=self.manual_tecnico ,font=("petfinder", 12)).place(x=10, y= 330, width=150, height=30)
        self.b9 = Button(self.frame, text="Temas de ayuda",bg="#dfc9f5", command=self.Datosayuda ,font=("petfinder", 12)).place(x=10, y= 360, width=150, height=30)
        
        #Text area
        self.texto = Text (self.frame)
        self.texto.place (x=170, y=5,width=360, height=470 )
        self.scroll = Scrollbar(self.texto)
        self.scroll.pack(side=RIGHT, fill=Y)      
        self.texto.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.texto.yview)
        
        self.raiz.mainloop()
    
    def abrirTXT(self):
        self.texto.delete('1.0',END)
        self.text_file = filedialog.askopenfilename(initialdir = "/Descargas", title = "Holi busca tu archivo",filetypes = ( ("TXT", "*.txt*"),("All Files", "*.*") ))
            
        try:
            text = open(self.text_file,'r+', encoding="utf-8")
            contenido = text.read()
            self.texto.insert(1.0, contenido)
            self.leer = contenido
            text.close()
            messagebox.showinfo(title="¡Felicidades!", message="Archivo cargado con éxito")
        except UnicodeDecodeError:
         messagebox.showerror(title="Advertencia" ,message="Aún no hay archivo cargado")
    

    def guardar(self):
        texto1=self.texto.get(1.0,END)
        print(texto1)
        if self.text_file==None:
            self.guardarComo()
        else:
            self.text3=open(self.text_file,"w+",encoding="utf-8")
            self.text3.write(texto1)
            
            self.text3.close()

            messagebox.showinfo("Guardar", "Los datos se han guardado correctamente")

    def guardarComo(self):

        archivo_guardar=filedialog.asksaveasfilename(initialdir = "/",title = "Guardar archivo",defaultextension=".txt", filetypes = (("txt files","*.txt"),("all files","*.*")))
        try:
            if archivo_guardar is not None:
                contenido=self.texto.get(1.0,END)
                archivo2=open(archivo_guardar,"w+",encoding="utf-8")
                archivo2.write(contenido)
                archivo2.close()
                self.text_file=archivo_guardar
                messagebox.showinfo("Guardar Como", "el archivo se guardo correctamente")
            else:
                print('no archivo ')
        except FileNotFoundError:
            messagebox.showerror("Error", "no se pudo guardar el archivo")
  
    def Datosayuda(self):
        
        messagebox.showinfo(title="Temas de Ayuda", message="Lenguajes Formales de Programacion B- \nProyecto 1 \nNombre: Andrea Jazmin Rodriguez Citalán\nCarnet: 202110553")

    def analizar(self):
        archi = open(self.text_file, "r")
        leer = ""
        for i in archi.readlines():
            leer += i

        self.a.instruccion(leer)
        self.a.operar_()
        with open('Resultados.txt', 'w',encoding="utf-8") as archivo:
            with redirect_stdout(archivo):
                self.a.instruccion(leer)
                self.a.operar_()
                #archivo.close()
        os.system('Resultados.txt')
        #os.system("resultado.pdf")

        #self.texto.insert(1.0, self.a)
    
                #self.a.getErrores()
        
        
        
        #self.texto.insert(1.0,self.a.operar())

    def errores(self):
        self.a.getErrores()
        #archivo = self.a.getErrores()
        with open('ERRORES_202110553.txt', 'w', encoding="utf-8") as archivo:
            with redirect_stdout(archivo):
                self.a.getErrores()
                #archivo.close()
        os.system('ERRORES_202110553.txt')
        #file = open("ERRORES_202110553","w")
        
        #self.a.getErrores()
        #file.close()

    def manual_tecnico(self):
        path = "Tecnico.pdf"
        os.system(path)

    def manual_usuario(self):
        path = "usuario.pdf"
        os.system(path)

    #Cargar archivos 
Ventana()