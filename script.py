import os
from tkinter import *
from tkinter import messagebox
import schedule
import time

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
            messagebox.showerror(title="Erro", message="Informe somente programas e sites.")
    def listar(self):
        cont = 0
        for i in self.lista:
            cont +=1
            self.lb_3["text"] = "Total de: {}".format(cont)
        self.lb_2["text"] = "{}".format (self.lista)
    def programar(self):
        dados = int(self.entrada_2.get())
        schedule.every(dados).minutes.do(self.rodar_script)
        while True:
            schedule.run_pending()
            time.sleep(1)

class Aplicativo(Func):
    def __init__(self):
        root = Tk()
        root.geometry("270x260+547+250")
        root.title("Gerar script")
        self.lista = []
        self.root = root
        self.widgets()
        mainloop()
    def widgets(self):
        Label(self.root, text="Informe o programa ou site para add ao script").pack()
        self.entrada_1 = Entry(self.root)
        self.entrada_1.pack()
        self.btn_add_script = Button(self.root, text="Add ao script", command=self.add).pack()
        self.bnt_listar = Button(self.root, text="Listar adicionados", command=self.listar).pack()
        self.lb_2 = Label(self.root, text="")
        self.lb_2.pack()
        self.lb_3 = Label(self.root, text="")
        self.lb_3.pack()
        self.btn_rodar_script = Button(self.root, text="Rodar script agora", command=self.rodar_script).pack()
        Label(self.root, text="Se preferir você pode informar abaixo\no intervalo em minutos para rodar o script").pack()
        self.entrada_2 = Entry(self.root)
        self.entrada_2.pack()
        self.btn_programar = Button(self.root, text="Programar", command=self.programar).pack()
Aplicativo()