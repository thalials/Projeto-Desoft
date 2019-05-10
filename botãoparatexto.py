# -*- coding: utf-8 -*-
"""
tentado criar um jeito de fazer listas
"""

import tkinter as tk
  
class Application:
    def __init__(self, master=None):
        self.window = tk.Tk()
        self.window.title("Gerenciador de tarefas")
        self.window.geometry("300x200+100+100")
        self.window.rowconfigure(0, minsize=150, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, minsize=120, weight=1)
        self.window.columnconfigure(1, weight=1)

        self.tarefas = tk.Listbox(self.window)
        self.tarefas.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        self.conteudo_caixa_texto = tk.StringVar()
        
        caixa_texto = tk.Entry(self.window)
        caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
        caixa_texto.grid(row=1, column=0, padx=20, sticky="ew")
        
        caixa_texto.bind("<Return>", self.apertou_enter)
        
        botão = tk.Button(self.window)
        botão.configure(text="Salvar")
        botão.configure(command=self.salvar)
        botão.grid(row=1, column=1)
        
        botão = tk.Button(self.window)
        botão.configure(text="Apagar")
        botão.configure(command=self.apagar)
        botão.grid(row=1, column=2)
        
    def iniciar(self):
        self.window.mainloop()
    
    def apertou_enter(self):
        self.salvar(caixa_texto)
    
    def salvar(self):
        self.tarefas.insert(tk.END, self.conteudo_caixa_texto.get())
        
    def apagar(self):
        items = self.tarefas.curselection()
        pos = 0
        for i in items :
            idx = int(i) - pos
            self.tarefas.delete( idx,idx )
            pos = pos + 1


        

caixa_texto = 10
app = Application()
app.iniciar()