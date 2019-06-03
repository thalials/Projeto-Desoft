import sqlite3
from tkinter import *
import tkinter as tk
import json

# Fonte para pesquisa:
# https://gist.github.com/volneyrock/db7e28e118f0e0ba2a73

class TelaPrincipal(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
#--------------------------------------TKINTER INTERFACE/ TELA DE CADASTRO ------------------------------------------------#
        self.app.root.geometry("775x600")
         
         #Configurações do design
         #linhas
        self.rowconfigure(0, minsize=100, weight=1) 
        self.rowconfigure(1, minsize=25, weight=1)
        self.rowconfigure(2, minsize=25, weight=1)
        self.rowconfigure(3, minsize=25, weight=1)
        self.rowconfigure(4, minsize=25, weight=1)
        self.rowconfigure(5, minsize=25, weight=1)
        self.rowconfigure(6, minsize=25, weight=1)
        self.rowconfigure(7, minsize=25, weight=1)
        self.rowconfigure(8, minsize=25, weight=1)
        self.rowconfigure(9, minsize=25, weight=1)
        self.rowconfigure(10, minsize=25, weight=1)
        self.rowconfigure(11, minsize=25, weight=1)
        self.rowconfigure(12, minsize=25, weight=1)
        self.rowconfigure(13, minsize=50, weight=1)
        self.rowconfigure(14, minsize=150, weight=1)
      
         # colunas
        self.columnconfigure(0, minsize = 100, weight=1) 
        self.columnconfigure(1, minsize = 50, weight=1)
        self.columnconfigure(2, minsize = 50, weight=1)
        self.columnconfigure(3, minsize = 275, weight=1)
        self.columnconfigure(4, minsize = 100, weight=1)
        self.columnconfigure(5, minsize = 50, weight=1)
        self.columnconfigure(6, minsize = 100, weight=1)
        self.columnconfigure(7, minsize = 25, weight=1)
        
        #definindo cor do fundo
        self.configure(background="khaki") 
        
        # Titulo da tela de cadastro
        self.titulo = tk.Label(self, text="Registration Planner") 
        self.titulo["font"] = ("Times New Roman", "20", "bold")
        self.titulo.grid(row=0, column=3, sticky="nsew")
        self.titulo["bg"] = "khaki"
        
        # caixas de texto referente a cada entrada no cadastro (nome completo, idade e ocupacao)
        self.caixa_texto1 = tk.StringVar()       
        self.caixa_texto2 = tk.StringVar()       
        self.caixa_texto3 = tk.StringVar()
        
        # Nome completo do usuario:  
        self.entrada1 = tk.Entry(self)
        self.entrada1.configure(textvariable = self.caixa_texto1)
        self.entrada1.grid(row=2, column=3, sticky="nsew", padx=2, pady =1)    
        self.nome = tk.Label(self, text="Nome completo") 
        self.nome["font"] = ("Times New Roman", "15", "bold")
        self.nome.grid(row=2, column=2, sticky="nsew")
        self.nome["bg"] = "khaki"
       
         # Informacoes de idade do usuario:
        self.entrada2 = tk.Entry(self)
        self.entrada2.configure(textvariable = self.caixa_texto2)
        self.entrada2.grid(row=5, column=3, sticky="nsew")   
        self.idade = tk.Label(self, text="Idade") 
        self.idade["font"] = ("Times New Roman", "15", "bold")
        self.idade.grid(row=5, column=2, sticky="nsew")
        self.idade["bg"] = "khaki"
       
        # informacoes de ocupacao do usuario:
        self.entrada3 = tk.Entry(self)
        self.entrada3.configure(textvariable = self.caixa_texto3)
        self.entrada3.grid(row=8, column=3, sticky="nsew")   
        self.ocup = tk.Label(self, text="Ocupação") 
        self.ocup["font"] = ("Times New Roman", "15", "bold")
        self.ocup.grid(row=8, column=2, sticky="nsew")
        self.ocup["bg"] = "khaki"
        
        # definicao do botao de cadastro 
        self.botaocadastra = tk.Button(self, text = "Cadastrar")
        self.botaocadastra["font"] = ("Times New Roman", "15", "bold")
        self.botaocadastra['bg'] = ('tomato3')
        self.botaocadastra['fg'] = ('white')
        self.botaocadastra["command"] = self.cadastrausuario
        self.botaocadastra.grid(row = 13 , column = 3, sticky = "nsew")
    
    # As informacoes dos usuarios serao salvas a cada vez que ele colocar seu nome completo, 
    # Abaixo esta parte do codigo que salva essas informacoes apos o cadastro 
    def salva_informacoes(self):
        with open("cadastros realizados.json", "r") as arquivo:
           texto = arquivo.read()
           
           # dicionario refere-se ao 'lugar' onde ficaram gravadas as informacoes de cadastro 
           # e a lista de tarefas que o usuario tem para fazer;
           # Todas essas informacoes ficarao salvas em um arquivo nomeado 'cadastros realizados';
        dicionario = json.loads(texto)     
        if self.app.nome not in dicionario:     
            dicionario[self.app.nome] = {"idade": self.app.idade, "ocupacao": self.app.ocup, "tarefas a fazer": []}
            # abre 'cadastros realizados.txt' sem apagar o que já existia 
            with open("cadastros realizados.json", "a") as arquivo:
                arquivo.write(json.dumps(dicionario)) 
           
    def cadastrausuario(self):
        self.app.nome = self.entrada1.get()
        self.app.idade = self.entrada2.get()
        self.app.ocup = self.entrada3.get()

        self.app.cadastrausuario()
        self.salva_informacoes()
        
#---------------------------------------------FRAMES---------------------------------------------------#
class CadastroFeito(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app

        #Configurações do design
        self.rowconfigure(0, minsize=100, weight=1) #linhas
        self.rowconfigure(1, minsize=100, weight=1)
        self.rowconfigure(2, minsize=100, weight=1)
        self.rowconfigure(3, minsize=100, weight=1)
        self.rowconfigure(4, minsize=100, weight=1)
        self.rowconfigure(5, minsize=100, weight=1)
        
        self.columnconfigure(0, minsize=375, weight=1) #colunas
        self.columnconfigure(1, minsize=200, weight=1)
        self.columnconfigure(2, minsize=50, weight=1)
        self.columnconfigure(3, minsize=50, weight=1)

        
        self.configure(background="khaki") #definindo cor do fundo
        
        self.titulo1 = tk.Label(self, text="Minhas tarefas") 
        self.titulo1["font"] = ("Times New Roman", "30", "bold")
        self.titulo1.grid(row=1, column=0, sticky="n")
        self.titulo1["foreground"]='black'
        self.titulo1["bg"]='khaki'
        
        self.tarefas = tk.Listbox(self)
        self.tarefas.grid(row=2, column=0, rowspan=3, columnspan=2, 
                          sticky="nsew", padx=5)
        self.tarefas.bind("<Delete>", self.app.apertou_delete)
        
        self.conteudo_caixa_texto = tk.StringVar()
        
        self.caixa_texto = tk.Entry(self)
        self.caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
        self.caixa_texto.grid(row=5, column=0, columnspan=2, 
                              sticky="new", padx=5, pady=5)  
        self.caixa_texto.bind("<Return>", self.app.apertou_enter)

        self.salvar = tk.Button(self)
        self.salvar["text"] = "Salvar"
        self.salvar["font"] = ("Times New Roman", "15", "bold") 
        self.salvar["command"] = self.app.salvar
        self.salvar.grid(row=3, column=2, sticky="")
        self.salvar["bg"] = "salmon1"
        
        self.apagar = tk.Button(self)
        self.apagar["text"] = "Apagar"
        self.apagar["font"] = ("Times New Roman", "15", "bold") 
        self.apagar["command"] = self.app.apagar
        self.apagar.grid(row=5, column=2, sticky="")
        self.apagar["bg"] = "salmon1"
        
        self.perfil = tk.Label(self, text="Perfil \n Nome: {0} \n Idade: {1} \n Ocupação: {2}".format(self.app.nome, self.app.idade, self.app.ocup))
        self.perfil["font"] = ("Times New Roman", "15") 
        self.perfil.grid(row=0, column=2, sticky="")
        self.perfil["bg"] = "salmon1"
                
        self.tarefas_realizadas = tk.Button(self) 
        self.tarefas_realizadas["text"] = "Tarefas Realizadas"
        self.tarefas_realizadas["font"] = ("Times New Roman","15")
        self.tarefas_realizadas["command"] = self.app.tarefas_feitas
        self.tarefas_realizadas.grid(row=1, column=2, sticky="")
        self.tarefas_realizadas["bg"] = "salmon1"


        self.graficos = tk.Button(self) 
        self.graficos["text"] = "Verificar Rendimento \n Semanal"
        self.graficos["font"] = ("Arial","12")
        self.graficos["command"] = self.app.ir_graficos
        self.graficos.grid(row=2, column=2, sticky="")
        self.graficos["bg"] = "salmon1"
        
        self.arquivar = tk.Button(self) 
        self.arquivar["text"] = "Feita!"
        self.arquivar["font"] = ("Arial", "12", "bold")
        self.arquivar["command"] = self.app.tarefas_ar
        self.arquivar.grid(row=4, column=2, sticky="")
        self.arquivar["bg"] = "salmon1"
        


    def update(self):
        self.perfil["text"] = "Perfil \n Nome: {0} \n Idade: {1} \n Ocupação: {2}".format(self.app.nome, self.app.idade, self.app.ocup)

class TarefasRealizadas(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=100, weight=1) # linhas
        self.rowconfigure(1, minsize=300, weight=1)
        self.rowconfigure(2, minsize=100, weight=1)
        self.rowconfigure(3, minsize= 100, weight=1)
        
        self.columnconfigure(0, minsize=200, weight=1) #colunas
        self.columnconfigure(1, minsize=300, weight=1)
        self.columnconfigure(2, minsize=200, weight=1)
        self.columnconfigure(3, minsize = 75, weight=1)
        
        self.configure(background="khaki")
        
        self.titulo = tk.Label(self, text="Tarefas Realizadas")
        self.titulo["font"] = ("Times New Roman", "20", "bold")
        self.titulo.grid(row=0, column=0, columnspan=3, sticky="", padx=5, pady=5)
        self.titulo["foreground"]='black'
        self.titulo["bg"]='khaki'
                
        self.voltar = tk.Button(self) #botão 1
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Times New Roman", "15")
        self.voltar["command"] = self.app.mudar_tela_principal
        self.voltar.grid(row=3, column=0, sticky="", padx=1, pady=5)
        self.voltar["bg"] = "salmon1"
        
        self.apagar = tk.Button(self)
        self.apagar["text"] = "Apagar"
        self.apagar["font"] = ("Times New Roman", "15") 
        self.apagar["command"] = self.app.apagar1
        self.apagar.grid(row=3, column=3, sticky="", padx=1, pady=5)
        self.apagar["bg"] = "salmon1"
        
        self.lista_feito = tk.Listbox(self)
        self.lista_feito.grid(row=1, column=0, rowspan=2, columnspan=4, sticky="nsew", padx=5, pady=5)

class Aplicação:
    def __init__(self):
        self.nome = ""
        self.ocup = ""
        self.idade = ""
        
        self.root = tk.Tk()
        self.root.geometry("775x600")
        self.root.title(string='MyPlanner')
        
        self.tela_principal = TelaPrincipal(self)  # Tela principal.
        self.botaocadastra = CadastroFeito(self)
        self.tarefas_realizadas = TarefasRealizadas(self)
        self.rendimento = Rendimento(self) 
        
        self.tela_atual = self.tela_principal
        self.tela_atual.grid()
        
    def mudar_tela_principal(self):
        self.tela_atual.grid_forget()
        self.botaocadastra.grid()
        self.tela_atual = self.botaocadastra 

    def salvar(self):
        if len(self.tela_atual.conteudo_caixa_texto.get()) == 0:
            print("digite uma tarefa")
        else:
            salvando_tarefas = self.tela_atual.conteudo_caixa_texto.get()
            self.tela_atual.tarefas.insert(tk.END, chr(9745) + " " + 
                            self.tela_atual.conteudo_caixa_texto.get())
            
            self.tela_atual.conteudo_caixa_texto.set("")
            self.salva_tarefas(salvando_tarefas) 
        
    def apertou_delete(self, event):
        self.apagar()
        
    def apagar(self):
        items = self.botaocadastra.tarefas.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.botaocadastra.tarefas.delete(idx, idx)
            pos = pos + 1
            
    def apagar1(self):
        items = self.tarefas_realizadas.lista_feito.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.tarefas_realizadas.lista_feito.delete( idx,idx )
    
    def cadastrausuario(self):
        self.tela_atual.grid_forget()
        self.botaocadastra.update()
        self.botaocadastra.grid()
        self.tela_atual = self.botaocadastra  
                    
    def apertou_enter(self, event):
        self.salvar()
        
    def tarefas_feitas(self):
        self.tela_atual.grid_forget()
        self.tarefas_realizadas.grid()
        self.tela_atual = self.tarefas_realizadas
        
    def tarefas_feito(self):
        for i in self.botaocadastra.tarefas.curselection():
            self.tarefas_realizadas.lista_feito.insert(tk.END, self.tela_atual.tarefas.get(i))
        items = self.botaocadastra.tarefas.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.botaocadastra.tarefas.delete( idx,idx )
            pos = pos + 1
   
    def salva_tarefas(self, tarefa):
        with open("cadastros realizados.json", "r") as arquivo:
           texto = arquivo.read()
      
        dicionario = json.loads(texto)  
        dicionario[self.nome]["tarefas a fazer"].append(tarefa)
        
        with open("cadastros realizados.json", "w") as arquivo:
            arquivo.write(json.dumps(dicionario)) 
           
    def roda(self):
        self.root.mainloop()

app = Aplicação()
app.roda()