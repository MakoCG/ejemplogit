from tkinter import *

class Inicio:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calculadora básica")
        self.ventana.geometry("500x700")
        self.ventana.resizable(0,0)
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.resultado = StringVar()

    def construir(self):
        marco = Frame(self.ventana, width=250, height=50)
        marco.pack_propagate(False)
        marco.pack(fill=X)
        titulo = Label(marco, text="Calculadora en práctica", 
        padx=20, pady=20, fg="#206a5d", bg="#bfdcae", font=('LCDD',30))
        titulo.pack(fill=X, expand=True, side=TOP, anchor=N)
        marco_form = Frame(self.ventana, width=250, height=400, padx=20)
        marco_form.pack_propagate(False)
        marco_form.pack(fill=X, side=TOP)
        label_resultado = Label(marco_form,textvariable=self.resultado, font=('LCDD',20))
        label_resultado.pack(side=TOP, anchor=N)
        label_n1 = Label(marco_form, text="Numero 1", font=('LCDD',20), fg="#81b214", bg="#f1f1e8")
        label_n1.pack(side=TOP, anchor=NW)
        n1_txt = Entry(marco_form, textvariable=self.n1, font=('LCDD',20))
        n1_txt.pack(side=TOP, fill=X, expand=True)
        label_n2 = Label(marco_form, text="Numero 2", font=('LCDD',20), fg="#81b214", bg="#f1f1e8")
        label_n2.pack(side=TOP, anchor=NW)
        n2_txt = Entry(marco_form, textvariable=self.n2, font=('LCDD',20))
        n2_txt.pack(side=TOP, fill=X, expand=True)
        marco_botones = Frame(self.ventana, width=250, height=100)
        marco_botones.pack_propagate(False)
        marco_botones.pack(side=TOP, fill=X, expand=True)
        boton_suma = Button(marco_botones, text="SUMAR", font=('Modern No. 20',15), 
        height=20, width=5, fg="#81b214", bg="#f1f1e8")
        boton_suma.pack(side=LEFT, expand=True, fill=X)
        boton_resta = Button(marco_botones, text="RESTAR", font=('Modern No. 20',15), 
        height=20, width=5, fg="#81b214", bg="#f1f1e8")
        boton_resta.pack(side=LEFT, expand=True, fill=X)
        marco_botonesbajo = Frame(self.ventana, width=250, height=100)
        marco_botonesbajo.pack_propagate(False)
        marco_botonesbajo.pack(side=TOP, fill=X, expand=True)
        boton_multi = Button(marco_botonesbajo, text="MULTIPLICACION", 
        font=('Modern No. 20',15), height=20, width=5, fg="#81b214", bg="#f1f1e8")
        boton_multi.pack(side=LEFT, expand=True, fill=X)
        boton_divi = Button(marco_botonesbajo, text="DIVISION", 
        font=('Modern No. 20',15), height=20, width=5, fg="#81b214", bg="#f1f1e8")
        boton_divi.pack(side=LEFT, expand=True, fill=X)

    def mostrar(self):
        self.ventana.mainloop()

inicio = Inicio()
inicio.construir()
inicio.mostrar()