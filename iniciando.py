import tkinter as tk

class TelaPrincipal(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, minsize=200, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, minsize=410, weight=1)
        self.columnconfigure(1, weight=1)

        self.titulo = tk.Label(self, text="Perfil \n Nome: Kathleen da Silva \n Ocupação: Estudante")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo["width"] = 20
        self.titulo["height"] = 5
        self.titulo.grid(row=0, column=1, rowspan=3, columnspan=1, sticky="ne")
        
        self.titulo1 = tk.Label(self, text="Lista de Afazeres")
        self.titulo1["font"] = ("Arial", "10", "bold")
        self.titulo1["width"] = 20
        self.titulo1["height"] = 5
        self.titulo1.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nw")
        
        self.button1 = tk.Button(self) #botão 2
        self.button1["text"] = "Adicionar Tarefa"
        self.button1["font"] = ("Arial","12")
        self.button1["width"] = 30
        self.button1["height"] = 5
        self.button1["command"] =self.app.mudar_tela_1
        self.button1.grid(row=1, column=1, sticky="sw")

        self.button2 = tk.Button(self) #botão 2
        self.button2["text"] = "Tarefas Realizadas"
        self.button2["font"] = ("Arial","12")
        self.button2["width"] = 30
        self.button2["height"] = 5
        self.button2["command"] =self.app.mudar_tela_2
        self.button2.grid(row=1, column=1, sticky="se")

        self.button3 = tk.Button(self) #botão 3
        self.button3["text"] = "Verificar Rendimento \n Semanal"
        self.button3["font"] = ("Arial","12")
        self.button3["width"] = 30
        self.button3["height"] = 5
        self.button3["command"] = self.app.mudar_tela_3
        self.button3.grid(row=2, column=1, sticky="se")

class Tela1(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app.root)
        
        self.app = app
        
        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, weight=1)
        
        self.titulo = tk.Label(self, text="Tela 1")
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
        self.button.grid(row=1, column=0, sticky="ne")

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
        
        self.tela_principal = TelaPrincipal(self)  # Tela principal.
        self.tela_1 = Tela1(self)
        
        self.tela_atual = self.tela_principal
        self.tela_atual.grid()
        

        self.tela_2 = Tela2(self)
        self.tela_atual.grid()
        
        self.tela_3 = Tela3(self)
        self.tela_atual.grid()
        

    def mudar_tela_principal(self):
        self.tela_atual.grid_forget()
        self.tela_principal.grid()
        self.tela_atual = self.tela_principal

    def mudar_tela_1(self):
        self.tela_atual.grid_forget()
        self.tela_1.grid()
        self.tela_atual = self.tela_1
    
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



#TENTANDO DAR COMMIT, ALGUEM ME AJUDAAAAAAAAAAAAAA


