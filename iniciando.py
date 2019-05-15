import tkinter as tk

class TelaPrincipal(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        #Configurações do design
        self.rowconfigure(0, minsize=200, weight=1) #linhas
        self.rowconfigure(1, minsize=200, weight=1)
        self.rowconfigure(2, minsize=200, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, minsize=200, weight=1) #colunas
        self.columnconfigure(1, minsize=200, weight=1)
        self.columnconfigure(2, minsize=200, weight=1)
        self.columnconfigure(3, weight=1)
        
        self.titulo1 = tk.Label(self, text="Lista de Afazeres") 
        self.titulo1["font"] = ("Arial", "10", "bold")
        self.titulo1.grid(row=0, column=0, sticky="nw")
        
        self.tarefas = tk.Listbox(self)
        self.tarefas.grid(row=1, column=0, sticky="nsew")
        
        self.conteudo_caixa_texto = tk.StringVar()
        
        self.caixa_texto = tk.Entry(self)
        self.caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
        self.caixa_texto.grid(row=2, column=0, sticky="ew") 

        self.salvar = tk.Button(self)
        self.salvar["text"] = "Salvar"
        self.salvar["command"] = self.app.salvar
        self.salvar.grid(row=1, column=1, sticky="sw")
        
        self.apagar = tk.Button(self)
        self.apagar["text"] = "Apagar"
        self.apagar["command"] = self.app.apagar
        self.apagar.grid(row=1, column=2, sticky="sw")
        
        self.perfil = tk.Button(self)
        self.perfil["text"] = "Perfil \n Nome: Kathleen da Silva \n Ocupação: Estudante"
        self.perfil["font"] = ("Arial", "10", "bold") 
        self.perfil["command"] = self.app.ir_perfil
        self.perfil.grid(row=0, column=3, sticky="ne")
                
        self.tarefas_realizadas = tk.Button(self) 
        self.tarefas_realizadas["text"] = "Tarefas Realizadas"
        self.tarefas_realizadas["font"] = ("Arial","12")
        self.tarefas_realizadas["command"] =self.app.tarefas_feitas
        self.tarefas_realizadas.grid(row=1, column=3, sticky="se")

        self.graficos = tk.Button(self) 
        self.graficos["text"] = "Verificar Rendimento \n Semanal"
        self.graficos["font"] = ("Arial","12")
        self.graficos["command"] = self.app.ir_graficos
        self.graficos.grid(row=2, column=3, sticky="se")

class TarefasRealizadas(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, weight=1)
        
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
        self.rowconfigure(1, weight=1)
        
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
        self.rowconfigure(1, weight=1)
        
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
        self.root.geometry("800x800+100+100")
        
        self.tela_principal = TelaPrincipal(self)  # Tela principal.
        self.tela_principal.grid() 
        
        self.tela_atual = self.tela_principal
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
        
    def apagar(self):
        items = self.tela_atual.tarefas.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.tela_atual.tarefas.delete( idx,idx )
            pos = pos + 1
            
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