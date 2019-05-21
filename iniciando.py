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
        var = IntVar()
        
        self.configure(relief = GROOVE)
        self.configure(borderwidth="2")
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth= 1.0)
        
        Label(self,text='Registration Planner',font=('bold','20')).place(relx=0.33,rely=0.1)
      
        Label(self,text='Nome',font=('bold','15')).place(relx=0.24,rely=0.25) 
        self.nome=Entry(self,font=('bold','15'))
        self.nome.place(relx=0.4,rely=0.25)
        
        Label(self,text='Email',font=('bold','15')).place(relx=0.24,rely=0.4)
        self.email = Entry(self,font=('bold','15'))
        self.email.place(relx=0.4,rely=0.4)
        
        Label(self,text='Ocupação',font=('bold','15')).place(relx=0.22,rely=0.55)
        self.ocup = Entry(self,font=('bold','15'))
        self.ocup.place(relx=0.40,rely=0.55)
        
        Label(self, text="Gender", font=("bold", 15)).place(relx= 0.25, rely= 0.69)
        Radiobutton(self, text = "Male", font = ("bold", 15), variable = var, value = 1).place(relx = 0.43, rely = 0.69)
        Radiobutton(self, text = "Female", font = ("bold", 15), variable = var, value = 2).place(relx = 0.6, rely = 0.69)
      
        self.botaocadastra = tk.Button(self,text='Cadastrar',font=('bold','15'),bg ='brown',
                                    fg='white', command = self.app.cadastrausuario).place(relx = 0.33,rely = 0.83, relwidth = 0.35)
        
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
        
        self.titulo1 = tk.Label(self, text="Lista de Afazeres") 
        self.titulo1["font"] = ("Arial", "10", "bold")
        self.titulo1.grid(row=0, column=0, sticky="")
        
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
        
        self.apagar = tk.Button(self)
        self.apagar["text"] = "Apagar"
        self.apagar["font"] = ("Arial", "10", "bold") 
        self.apagar["command"] = self.app.apagar
        self.apagar.grid(row=4, column=1, sticky="")
        
        self.perfil = tk.Button(self)
        self.perfil["text"] = "Perfil \n Nome: Kathleen da Silva \n Ocupação: Estudante"
        self.perfil["font"] = ("Arial", "10", "bold") 
        self.perfil["command"] = self.app.ir_perfil
        self.perfil.grid(row=0, column=2, sticky="")
                
        self.tarefas_realizadas = tk.Button(self) 
        self.tarefas_realizadas["text"] = "Tarefas Realizadas"
        self.tarefas_realizadas["font"] = ("Arial","12")
        self.tarefas_realizadas["command"] = self.app.tarefas_feitas
        self.tarefas_realizadas.grid(row=1, column=2, sticky="")

        self.graficos = tk.Button(self) 
        self.graficos["text"] = "Verificar Rendimento \n Semanal"
        self.graficos["font"] = ("Arial","12")
        self.graficos["command"] = self.app.ir_graficos
        self.graficos.grid(row=2, column=2, sticky="")

class TarefasRealizadas(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, minsize=200, weight=1)
        self.rowconfigure(2, minsize=200, weight=1)
        self.rowconfigure(3, weight=1)
        
        self.titulo = tk.Label(self, text="Tarefas Realizadas")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.grid(row=0, column=0, sticky="nw")
        
        self.voltar = tk.Button(self) #botão 1
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Arial", "12")
        self.voltar["command"] = self.app.mudar_tela_principal
        self.voltar.grid(row=1, column=0, sticky="sw")

class Gráficos(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, minsize=200, weight=1)
        self.rowconfigure(2, minsize=200, weight=1)
        self.rowconfigure(3, weight=1)
        
        self.titulo = tk.Label(self, text="Gráfico de rendimento semanal")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.grid(row=0, column=0, sticky="nsew")
        
        self.voltar = tk.Button(self) #botão 1
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Arial", "12")
        self.voltar["command"] = self.app.mudar_tela_principal
        self.voltar.grid(row=1, column=0, sticky="sw")

class Perfil(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, minsize=200, weight=1)
        self.rowconfigure(2, minsize=200, weight=1)
        self.rowconfigure(3, weight=1)
        
        self.titulo = tk.Label(self, text="Configurações do Perfil")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.grid(row=0, column=0, sticky="nsew")
        
        self.voltar = tk.Button(self) #botão 1
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Arial", "12")
        self.voltar["command"] = self.app.mudar_tela_principal
        self.voltar.grid(row=1, column=0, sticky="sw")

class Aplicação:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")

        self.tela_principal = CadastroFeito(self)  # Tela principal.
        self.tela_principal.grid() 
        
        self.tela_atual = self.tela_principal
        self.tela_atual.grid()
        
        self.botaocadastra = CadastroFeito(self)
        self.tela_atual.grid() 
        
        self.tarefas_realizadas = TarefasRealizadas(self)
        self.tela_atual.grid() 
        
        self.graficos = Gráficos(self) 
        self.tela_atual.grid()
        
        self.perfil = Perfil(self)
        self.tela_atual.grid()
        
    def mudar_tela_principal(self):
        self.tela_atual.grid_forget()
        self.tela_principal.grid()
        self.tela_atual = self.tela_principal 

    def salvar(self):
        self.tela_atual.tarefas.insert(tk.END, chr(9745) + " " + self.tela_atual.conteudo_caixa_texto.get())
<<<<<<< HEAD

    
    def apertou_enter(self, event):
        self.salvar()
        self.tela_atual.conteudo_caixa_texto.set('')
=======
        self.tela_atual.conteudo_caixa_texto.set("")
>>>>>>> 0baf5dff8360c6d888fafd84528eeca39acba352
        

    def apagar(self):
        items = self.tela_atual.tarefas.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.tela_atual.tarefas.delete( idx,idx )
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
        self.tela_atual.grid_forget()
        self.graficos.grid()
        self.tela_atual = self.graficos

    def ir_perfil(self):
        self.tela_atual.grid_forget()
        self.perfil.grid()
        self.tela_atual = self.perfil


    def roda(self):
        self.root.mainloop()

app = Aplicação()
app.roda()