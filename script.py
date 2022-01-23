import os
from tkinter import *
from tkinter import messagebox

class Func():
    def add(self):
        dados = str(self.entrada_1.get())
        self.lista.append(dados)
        self.entrada_1.delete(0, END)
    def rodar_script(self):
        try:
            for i in self.lista:
                os.startfile(i)
        except:
            messagebox.showerror(title="Erro", message="Informe somente sites.")
    def listar(self):
        cont = 0
        for i in self.lista:
            cont +=1
        self.lb_2["text"] = "Total de: {} - {}".format(cont, self.lista)
  
class Aplicativo(Func):
    def __init__(self):
        root = Tk()
        root.geometry("260x170+547+200")
        root.title("Gerar script")
        self.lista = []
        self.root = root
        self.widgets()
        mainloop()
    def widgets(self):
        self.lb_1 = Label(self.root, text="Informe o programa ou site para add ao script").pack()
        self.entrada_1 = Entry(self.root)
        self.entrada_1.pack()
        self.btn_add_script = Button(self.root, text="Add ao script", command=self.add).pack()
        self.lb_2 = Label(self.root, text="")
        self.lb_2.pack()
        self.bnt_listar = Button(self.root, text="Listar adicionados", command=self.listar).pack()
        self.btn_rodar_script = Button(self.root, text="Rodar script", command=self.rodar_script).pack()
        
Aplicativo()