import tkinter as tk
from tkinter import messagebox

class ListaAlumnos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.texLista = ""
        self.title("Lista de alumnos")
        self.geometry("450x400")
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)

        self.Entrada = tk.Entry(self,font=("Arial",12))
        self.Entrada.grid(row=1,column=0,padx=5,pady=5,sticky="we")

        self.TextInformativo = tk.Label(self,text="Ingrese los nombres de los alumnos",font=("Arial", 10, "italic"))
        self.TextInformativo.grid(row=0,column=0,columnspan=2,pady=5)

        self.RegistrarEntrada = tk.Button(self,text="Añadir un alumno",command=self.AñadirTexto)
        self.RegistrarEntrada.grid(row=2,column=0,pady=10,sticky="we")
        
        self.LimpiarEntradas = tk.Button(self,text="Limpiar lista",command=self.LimpiarLista)
        self.LimpiarEntradas.grid(row=3,column=0,pady=10,sticky="we")
        
        self.Lista = tk.Label(self,justify="left",anchor="nw",text="No hay alumnos registrados")
        self.Lista.grid(row=1,column=1,columnspan=2, rowspan=3,sticky="nsew",padx=10,pady=5)

    def AñadirTexto(self):
        TextoEntrada = self.Entrada.get()
        if not TextoEntrada.strip():
            self.TextInformativo.config(text="NO PUEDE DEJAR ESTE CAMPO EN BLANCO",fg="Red")
        else:
            self.texLista +=  TextoEntrada + "\n"
            self.TextInformativo.config(text="SE AÑADIO CORRECTAMENTE",fg="Green")
            self.Lista.config(text= self.texLista)
    def LimpiarLista(self):
        self.Lista.config(text="No hay alumnos registrados")
        self.texLista = ""
        self.TextInformativo.config(text="Lista vaciada",fg="Black")

if __name__ == "__main__":
    lisAlum = ListaAlumnos()
    lisAlum.mainloop()