import tkinter as tk
import random
from tkinter import messagebox

class GeneradorContraseñas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generador de contraseñas")
        self.geometry("370x300")
        self.caracteres = "abcdefghijklmnopqrstuvwxyz0123456789!@#$"

        self.Texto = tk.Label(self,text="Ingrese el numero de caracteres que tendra su contraseña")
        self.Texto.pack(pady=5)
        
        self.NumeroCaracteres = tk.Entry(self,font=("Arial",12))
        self.NumeroCaracteres.pack(pady=5)

        self.BotonGenerar = tk.Button(self,text="Generar contraseña",command=self.GenerarContra)
        self.BotonGenerar.pack()

        self.TextoResultado = tk.Label(self,font=("Arial",10))
        self.TextoResultado.pack(pady=18)

    def GenerarContra(self):
        vueltas = self.NumeroCaracteres.get()
        try:
            contraseña = ""
            for i in range(int(vueltas)):
                contraseña += random.choice(self.caracteres)
            self.TextoResultado.config(text=contraseña,fg="Black")
        except ValueError:
            self.TextoResultado.config(text="DEBE INGRESAR UN NUMERO ENTERO EN LA ENTRADA",fg="Red")

if __name__ == "__main__":
        GeneradorContra = GeneradorContraseñas()
        GeneradorContra.mainloop()
