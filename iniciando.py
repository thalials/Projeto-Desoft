# -*- coding: utf-8 -*-
import sqlite3
from tkinter import *
import tkinter as tk

#Criar conexão e cursor
con = sqlite3.connect('banco.db')
cur = con.cursor()

#Criar tabela clientes
cur.execute("""CREATE TABLE IF NOT EXISTS clientes (
            nome VARCHAR,
            telefone VARCHAR PRIMARY KEY,
            endereco VARCHAR,
            comp VARCHAR)""")

# Fonte para pesquisa: https://gist.github.com/volneyrock/db7e28e118f0e0ba2a73

class TelaPrincipal(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
#--------------------------------------TKINTER INTERFACE/ TELA DE CADASTRO ------------------------------------------------#

        self.titulo = tk.Label(self, text="Registration Planner") 
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.grid(row=1, column=4, sticky="N")
                
        self.caixa_texto1 = tk.StringVar()
        self.caixa_texto2 = tk.StringVar()
        self.caixa_texto3 = tk.StringVar()
        
        self.entrada1= tk.Entry(self)
        self.entrada1.configure(textvariable = self.caixa_texto1)
        self.entrada1.grid(row=3, column=3, sticky="N")  
  
        self.nome = tk.Label(self, text="Nome") 
        self.nome["font"] = ("Arial", "12", "bold")
        self.nome.grid(row=3, column=2, sticky="n")
       
        self.entrada2= tk.Entry(self)
        self.entrada2.configure(textvariable = self.caixa_texto2)
        self.entrada2.grid(row=5, column=3, sticky="nsew")  
  
        self.email = tk.Label(self, text="Email") 
        self.email["font"] = ("Arial", "12", "bold")
        self.email.grid(row=5, column=2, sticky="nsew")
         
        self.entrada3 = tk.Entry(self)
        self.entrada3.configure(textvariable = self.caixa_texto3)
        self.entrada3.grid(row=7, column=3, sticky="nsew")  
  
        self.ocup = tk.Label(self, text="Ocupação") 
        self.ocup["font"] = ("Arial", "12", "bold")
        self.ocup.grid(row=7, column=2, sticky="nsew")
      
        var = tk.IntVar()
        
        tk.Label(self, text="Gender", font=("bold", 15)).grid(row=20, column=3, sticky="nsew")
        tk.Radiobutton(self, text = "Male", font = ("bold", 15), variable = var, value = 1).grid(row=20, column=4, sticky="nsew")
        tk.Radiobutton(self, text = "Female", font = ("bold", 15), variable = var, value = 2).grid(row=20, column=5, sticky="nsew")
      
        self.botaocadastra = tk.Button(self,text='Cadastrar',font=('bold','10'),bg ='brown',
                                    fg='white', command = self.app.cadastrausuario).grid(row=40, column= 4 , sticky="nsew")
        
        def cadastrausuario(self):
            nome = self.nome.get()
            ocup = self.ocup.get()
            email = self.email.get() 
        
#-----------------------------------------FUNÇÕES-----------------------------------------------------------#                
class CadastroFeito(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        #Configurações do design
        self.rowconfigure(0, minsize=100, weight=1) #linhas
        self.rowconfigure(1, minsize=100, weight=1)
        self.rowconfigure(2, minsize=200, weight=1)
        self.rowconfigure(3, minsize=100, weight=1)
        self.rowconfigure(4, minsize=100, weight=1)
        self.columnconfigure(0, minsize=300, weight=1) #colunas
        self.columnconfigure(1, minsize=300, weight=1)
        self.columnconfigure(2, minsize=200, weight=1)
        
        self.configure(background="black") #definindo cor do fundo
        
        self.titulo1 = tk.Label(self, text="Lista de Afazeres") 
        self.titulo1["font"] = ("Arial", "20", "bold")
        self.titulo1.grid(row=0, column=0, sticky="")
        self.titulo1["foreground"]='white'
        self.titulo1["bg"]='black'
        
        self.tarefas = tk.Listbox(self)
        self.tarefas.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="nsew", padx=5)
        
        self.conteudo_caixa_texto = tk.StringVar()
        
        self.caixa_texto = tk.Entry(self)
        self.caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
        self.caixa_texto.grid(row=3, column=0, columnspan=2, sticky="new", padx=5, pady=5)  

        self.salvar = tk.Button(self)
        self.salvar["text"] = "Salvar"
        self.salvar["font"] = ("Arial", "10", "bold") 
        self.salvar["command"] = self.app.salvar
        self.salvar.grid(row=4, column=0, sticky="")
        self.salvar["bg"] = "red"
        
        self.apagar = tk.Button(self)
        self.apagar["text"] = "Apagar"
        self.apagar["font"] = ("Arial", "10", "bold") 
        self.apagar["command"] = self.app.apagar
        self.apagar.grid(row=4, column=1, sticky="")
        self.apagar["bg"] = "red"
        
        self.perfil = tk.Button(self)
        self.perfil["text"] = "Perfil \n Nome: Kathleen da Silva \n Ocupação: Estudante"
        self.perfil["font"] = ("Arial", "10", "bold") 
        self.perfil["command"] = self.app.ir_perfil
        self.perfil.grid(row=0, column=2, sticky="")
        self.perfil["bg"] = "red"
                
        self.tarefas_realizadas = tk.Button(self) 
        self.tarefas_realizadas["text"] = "Tarefas Realizadas"
        self.tarefas_realizadas["font"] = ("Arial","12")
        self.tarefas_realizadas["command"] = self.app.tarefas_feitas
        self.tarefas_realizadas.grid(row=1, column=2, sticky="")
        self.tarefas_realizadas["bg"] = "red"

        self.graficos = tk.Button(self) 
        self.graficos["text"] = "Verificar Rendimento \n Semanal"
        self.graficos["font"] = ("Arial","12")
        self.graficos["command"] = self.app.ir_graficos
        self.graficos.grid(row=2, column=2, sticky="")
        self.graficos["bg"] = "red"
        
        self.arquivar = tk.Button(self) 
        self.arquivar["text"] = "Arquivar"
        self.arquivar["font"] = ("Arial", "12", "bold")
        self.arquivar["command"] = self.app.tarefas_ar
        self.arquivar.grid(row=4, column=2, sticky="")
        self.arquivar["bg"] = "red"

class TarefasRealizadas(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=100, weight=1) # linhas
        self.rowconfigure(1, minsize=400, weight=1)
        self.rowconfigure(2, minsize=100, weight=1)
        
        self.columnconfigure(0, minsize=200, weight=1) #colunas
        self.columnconfigure(1, minsize=400, weight=1)
        self.columnconfigure(2, minsize=200, weight=1)
        
        self.configure(background="black")
        
        self.titulo = tk.Label(self, text="Tarefas Realizadas")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.grid(row=0, column=0, columnspan=3, sticky="", padx=5, pady=5)
        self.titulo["foreground"]='white'
        self.titulo["bg"]='black'
                
        self.voltar = tk.Button(self) #botão 1
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Arial", "12")
        self.voltar["command"] = self.app.mudar_tela_principal
        self.voltar.grid(row=1, column=0, sticky="sw")
        self.voltar["bg"] = "red"
        
        self.lista_ar = tk.Listbox(self)
        self.lista_ar.grid(row=1, column=1, sticky="")

class Gráficos(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, minsize=200, weight=1)
        self.rowconfigure(2, minsize=200, weight=1)
        
        self.columnconfigure(0, minsize=200, weight=1) #colunas
        self.columnconfigure(1, minsize=400, weight=1)
        self.columnconfigure(2, minsize=200, weight=1)
        
        self.configure(background="black")
        
        self.titulo = tk.Label(self, text="Gráfico de rendimento semanal")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.grid(row=0, column=1, sticky="")
        self.titulo["foreground"]='white'
        self.titulo["bg"]='black'
        
        self.voltar = tk.Button(self) #botão 1
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Arial", "12")
        self.voltar["command"] = self.app.mudar_tela_principal
        self.voltar.grid(row=2, column=0, sticky="sw", padx=5, pady=5)
        self.voltar["bg"]='red'

class Perfil(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, minsize=200, weight=1)
        self.rowconfigure(2, minsize=200, weight=1)
        
        self.columnconfigure(0, minsize=200, weight=1) #colunas
        self.columnconfigure(1, minsize=400, weight=1)
        self.columnconfigure(2, minsize=200, weight=1)
               
        self.configure(background="black")
        
        self.titulo = tk.Label(self, text="Configurações do Perfil")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.grid(row=0, column=1, sticky="nsew")
        self.titulo["foreground"]='white'
        self.titulo["bg"]='black'
        
        self.voltar = tk.Button(self) #botão 1
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Arial", "12")
        self.voltar["command"] = self.app.mudar_tela_principal
        self.voltar.grid(row=1, column=0, sticky="sw")
        self.voltar["bg"]='red'                

class Aplicação:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")

        self.tela_principal = TelaPrincipal(self)  # Tela principal.
        self.tela_atual = self.tela_principal
        
        self.perfil = Perfil(self)
        self.tela_atual.grid()
        self.botaocadastra = CadastroFeito(self)
        self.tarefas_realizadas = TarefasRealizadas(self)
        self.graficos = Gráficos(self) 
        self.perfil = Perfil(self)
        
        self.tela_atual.grid()
        
    def mudar_tela_principal(self):
        self.tela_atual.grid_forget()
        self.botaocadastra.grid()
        self.tela_atual = self.botaocadastra 

    def salvar(self):
        self.tela_atual.tarefas.insert(tk.END, chr(9745) + " " + self.tela_atual.conteudo_caixa_texto.get())
        self.tela_atual.conteudo_caixa_texto.set("")
    
    def apertou_enter(self, event):
#        self.tela_atual.tarefas.insert(tk.END, chr(9745) + " " + self.tela_atual.conteudo_caixa_texto.get())
#        self.tela_atual.conteudo_caixa_texto.set("")
        self.root.bind('<Return>', self.salvar)

    def apagar(self):
        items = self.botaocadastra.tarefas.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.botaocadastra.tarefas.delete( idx,idx )
            pos = pos + 1
    
    def cadastrausuario(self):
        self.tela_atual.grid_forget()
        self.botaocadastra.grid()
        self.tela_atual = self.botaocadastra  
        
    def tarefas_feitas(self):
        self.tela_atual.grid_forget()
        self.tarefas_realizadas.grid()
        self.tela_atual = self.tarefas_realizadas
        
    def ir_graficos(self):
        self.botaocadastra.grid_forget()
        self.graficos.grid()
        self.tela_atual = self.graficos

    def ir_perfil(self):
        self.botaocadastra.grid_forget()
        self.perfil.grid()
        self.tela_atual = self.perfil
        
    def tarefas_ar(self):
        for i in self.botaocadastra.tarefas.curselection():
            self.tarefas_realizadas.lista_ar.insert(tk.END, self.tela_atual.tarefas.get(i))
        items = self.botaocadastra.tarefas.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.botaocadastra.tarefas.delete( idx,idx )
            pos = pos + 1

    def roda(self):
        self.root.mainloop()

app = Aplicação()
app.roda()

#pra commitar