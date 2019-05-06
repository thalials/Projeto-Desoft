from tkinter import *

class Aplicação:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Bem vinda, Kathleen")
        self.msg["font"] = ("Arial", "12", "italic")
        self.msg.pack ()
        self.tela1 = Button(self.widget1)
        self.tela1["text"] = "Próximas Entregas"
        self.tela1["font"] = ("Arial", "12")
        self.tela1["width"] = 120 #largura 
        self.tela1["height"] = 50 #altura
        self.tela1["command"] = self.mudarTexto
        self.tela1.pack ()
  
    def mudarTexto(self):
        if self.msg["text"] == "Próximas Entregas":
            self.msg["text"] = "Entregas:"
        else:
            self.msg["text"] = "Próximas Entregas"
  
  
  
root = Tk()
Aplicação(root)
root.mainloop()
