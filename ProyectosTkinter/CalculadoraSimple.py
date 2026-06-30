import tkinter as tk
from tkinter import messagebox

class CalculadoraSimple(tk.Tk):
    def __init__(self):
        super().__init__()
        for i in range(4):
            self.grid_columnconfigure(i,weight=1)
        self.title("Calculadora Simple")
        self.geometry("350x470")
        self.resizable(0,0)
        self.MostrarResultado = tk.Entry(self,justify="right")
        self.MostrarResultado.config(width=20, font=("Arial",20))
        self.MostrarResultado.grid(row=0,column=0,columnspan=4,padx=10,pady=10,sticky="we")

        Botones = [(5,0,"0"),(4,0,"1"),(3,0,"4"),(2,0,"7"),(1,0,"AC"),
                   (5,1,"."),(4,1,"2"),(3,1,"5"),(2,1,"8"),(1,1,"("),
                   (5,2,"⌫"),(4,2,"3"),(3,2,"6"),(2,2,"9"),(1,2,")"),
                   (5,3,"="),(4,3,"+"),(3,3,"-"),(2,3,"*"),(1,3,"/")]
        for fila,columna,texto in Botones:
            Boton = tk.Button(self, text=texto,width=5,height=4,font=("Arial",10),command=lambda tex=texto: self.click_num(tex) )
            Boton.grid(row=fila, column=columna, padx=3, pady=3,sticky="we")

    def click_num(self,t):
        TextoActual = self.MostrarResultado.get()
        if t == "AC":
            self.MostrarResultado.delete(0,tk.END)

        elif t == "⌫" and len(TextoActual)>0:
            self.MostrarResultado.delete(len(TextoActual)-1, "end")
        
        elif t == "=":
            try:
                Resultado = str(eval(TextoActual))
                self.MostrarResultado.delete(0,tk.END)
                self.MostrarResultado.insert(0,Resultado)
            except ZeroDivisionError:
                self.MostrarResultado.delete(0,tk.END)
                self.MostrarResultado.insert(0,"(Error)eres animal,no?")
            except Exception:
                self.MostrarResultado.delete(0,tk.END)
                self.MostrarResultado.insert(0,"Error de sintaxis")
        else:
            if "Error" in TextoActual:
                self.MostrarResultado.delete(0, "end")
                TextoActual = ""
            
            self.MostrarResultado.delete(0,"end")
            self.MostrarResultado.insert(0,TextoActual + t)

if __name__ == "__main__":
    MiCalculadora = CalculadoraSimple()
    MiCalculadora.mainloop()
