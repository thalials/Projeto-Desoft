from tkinter import *

class Aplicação:
    def __init__(self, master=None):
        self.widgetp = Frame(master) #tela principal
        self.widgetp.pack()
        self.titulo = Label(self.widgetp, text="Bem vinda, Kathleen")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo["width"] = 20
        self.titulo["height"] = 5
        self.titulo.pack(side=LEFT)
        self.widgetp.pack ()
        
        self.button1 = Button(self.widgetp) #botão 1
        self.button1["text"] = "Próximas Entregas"
        self.button1["font"] = ("Arial", "12")
        self.button1["width"] = 20 #largura 
        self.button1["height"] = 5 #altura
        self.button1["command"] = self.mudarTela1
        self.button1.pack ()

        self.button2 = Button(self.widgetp) #botão 2
        self.button2["text"] = "Entregas Feitas"
        self.button2["font"] = ("Arial","12")
        self.button2["width"] = 20
        self.button2["height"] = 5
        self.button2["command"] = self.mudarTela2
        self.button2.pack ()

        self.button3 = Button(self.widgetp) #botão 3
        self.button3["text"] = "Rendimento"
        self.button3["font"] = ("Arial","12")
        self.button3["width"] = 20
        self.button3["height"] = 5
        self.button3["command"] = self.mudarTela3
        self.button3.pack ()
        
        
    def mudarTela1(self):
        if self.button1["text"] == "Próximas Entregas":
            self.button1["text"] = "x"
        else:
            self.button1["text"] = "Próximas Entregas"
            
    def mudarTela2(self):
        if self.button2["text"] == "Entregas Feitas":
            self.button2["text"] = "y"
        else:
            self.button2["text"] = "Entregas Feitas"
            
    def mudarTela3(self):
       if self.button3["text"] == "Rendimento":
           self.button3["text"] = "z"
       else:
           self.button3["text"] = "Rendimento"
           
           
class telas:
        def __init__(self, master=None):
            self.tela3 = Frame(master) #tela 3
            self.tela3.pack()
            self.titulo = Label(self.tela3, text="Entregas:")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo["width"] = 20
            self.titulo["height"] = 5
            self.titulo.pack(side=LEFT)
            self.tela3.pack ()
            
            self.tela2 = Frame(master) #tela 2
            self.tela2.pack()
            self.titulo = Label(self.tela2, text="Bem vinda, Kathleen")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo["width"] = 20
            self.titulo["height"] = 5
            self.titulo.pack(side=LEFT)
            self.tela2.pack ()
        
            self.telat1 = Frame(master) #tela 1
            self.tela1.pack()
            self.titulo = Label(self.tela1, text="Próximas Entregas")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo["width"] = 20
            self.titulo["height"] = 5
            self.titulo.pack(side=LEFT)
            self.tela1.pack ()
        
        
        

root = Tk()
Aplicação(root)
root.mainloop()
