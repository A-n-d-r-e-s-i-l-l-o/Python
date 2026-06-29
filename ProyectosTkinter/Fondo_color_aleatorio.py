import tkinter as tk
import random
from tkinter import messagebox

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi ventana")
        self.geometry("400x400")
        self.config(bg="white")
        self.resizable(False,False)
        self.BotonCambiarFondo = tk.Button(text="Cambiar fondo",command=self.CambiarColorFondo)
        self.BotonCambiarFondo.pack(pady=160)
    
    def CambiarColorFondo(self):
        Colores = ["Red","Black","Orange","Green","Purple","Brown","Gray","Pink","White","Yellow"]
        ColorFondo = random.choice(Colores)
        self.config(bg=ColorFondo)
    

if __name__ == "__main__":
    MiVentana = Ventana()
    MiVentana.mainloop()
    