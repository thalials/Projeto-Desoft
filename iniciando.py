import tkinter as tk

class TelaPrincipal(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=150, weight=1)
        self.rowconfigure(1, minsize=150, weight=1)
        self.rowconfigure(2, minsize=100, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, minsize=200, weight=1)
        self.columnconfigure(1, minsize=200, weight=1)
        self.columnconfigure(2, weight=1)

        self.titulo = tk.Label(self, text="Perfil \n Nome: Kathleen da Silva \n Ocupação: Estudante")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo["width"] = 50
        self.titulo["height"] = 5
        self.titulo.grid(row=0, column=2, sticky="ne")
        
        self.titulo1 = tk.Label(self, text="Lista de Afazeres")
        self.titulo1["font"] = ("Arial", "10", "bold")
        self.titulo1["width"] = 20
        self.titulo1["height"] = 5
        self.titulo1.grid(row=0, column=0, sticky="nw")
        
        self.tarefas = tk.Listbox(self)
        self.tarefas.grid(row=1, column=0, sticky="nsew")
        
        self.conteudo_caixa_texto = tk.StringVar()
        
        self.caixa_texto = tk.Entry(self)
        self.caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
        self.titulo["width"] = 10
        self.titulo["height"] = 5
        self.caixa_texto.grid(row=2, column=0, sticky="ew")
        
        self.botão1 = tk.Button(self)
        self.botão1["text"] = "Salvar"
        self.titulo["width"] = 5
        self.titulo["height"] = 5
        self.botão1["command"] = self.app.salvar
        self.botão1.grid(row=3, column=0, sticky="ew")
        
        self.botão2 = tk.Button(self)
        self.botão2.configure(text="Apagar")
        self.titulo["width"] = 5
        self.titulo["height"] = 5
        self.botão2["command"] = self.app.apagar
        self.botão2.grid(row=3, column=1, sticky="ew")
        
        self.button2 = tk.Button(self) #botão 2
        self.button2["text"] = "Tarefas Realizadas"
        self.button2["font"] = ("Arial","12")
        self.button2["width"] = 30
        self.button2["height"] = 5
        self.button2["command"] =self.app.mudar_tela_2
        self.button2.grid(row=1, column=2, sticky="se")

        self.button3 = tk.Button(self) #botão 3
        self.button3["text"] = "Verificar Rendimento \n Semanal"
        self.button3["font"] = ("Arial","12")
        self.button3["width"] = 30
        self.button3["height"] = 5
        self.button3["command"] = self.app.mudar_tela_3
        self.button3.grid(row=2, column=2, sticky="se")
        
class Tela2(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, weight=1)
        
        self.titulo = tk.Label(self, text="Tela 2")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo["width"] = 20
        self.titulo["height"] = 5
        self.titulo.grid(row=0, column=0, sticky="nw")
        
        self.button = tk.Button(self) #botão 1
        self.button["text"] = "volta"
        self.button["font"] = ("Arial", "12")
        self.button["width"] = 20 #largura 
        self.button["height"] = 5 #altura
        self.button["command"] = self.app.mudar_tela_principal
        self.button.grid(row=1, column=0, sticky="nsew")

class Tela3(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, weight=1)
        
        self.titulo = tk.Label(self, text="Gráfico de rendimento semanal")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo["width"] = 20
        self.titulo["height"] = 5
        self.titulo.grid(row=0, column=0, sticky="nsew")
        
        self.button = tk.Button(self) #botão 1
        self.button["text"] = "volta"
        self.button["font"] = ("Arial", "12")
        self.button["width"] = 20 #largura 
        self.button["height"] = 5 #altura
        self.button["command"] = self.app.mudar_tela_principal
        self.button.grid(row=1, column=0, sticky="nsew")

class Aplicação:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x510+100+100")
        
        self.tela_atual = TelaPrincipal(self)
        self.tela_atual.grid()
        
        self.tela_2 = Tela2(self)
        self.tela_atual.grid()
        
        self.tela_3 = Tela3(self)
        self.tela_atual.grid()

    def mudar_tela_principal(self):
        self.tela_atual.grid_forget()
        self.tela_principal.grid()
        self.tela_atual = self.tela_principal
    
    def salvar(self):
        self.tela_atual.tarefas.insert(tk.END, self.tela_atual.conteudo_caixa_texto.get())
        
    def apagar(self):
        items = self.tela_atual.tarefas.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.tela_atual.tarefas.delete( idx,idx )
            pos = pos + 1
            
    def mudar_tela_2(self):
        self.tela_atual.grid_forget()
        self.tela_2.grid()
        self.tela_atual = self.tela_2
    
    def mudar_tela_3(self):
        self.tela_atual.grid_forget()
        self.tela_3.grid()
        self.tela_atual = self.tela_3

    def roda(self):
        self.root.mainloop()
                   

app = Aplicação()
app.roda()