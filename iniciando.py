from tkinter import *

class Aplicação:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Bem vinda, Kathleen")
        self.msg["font"] = ("Arial", "12", "italic")
        self.msg["width"] = 20
        self.msg["height"] = 1
        self.msg.pack (side=LEFT)
        
        self.button1 = Button(self.widget1)
        self.button1["text"] = "Próximas Entregas"
        self.button1["font"] = ("Arial", "12")
        self.button1["width"] = 20 #largura 
        self.button1["height"] = 5 #altura
        self.button1["command"] = self.mudarTela1
        self.button1.pack ()
        
        self.button2 = Button(self.widget1)
        self.button2["text"] = "Entregas Feitas"
        self.button2["font"] = ("Arial","12")
        self.button2["width"] = 20
        self.button2["height"] = 5
        self.button2["command"] = self.mudarTela2
        self.button2.pack ()
        
        self.button3 = Button(self.widget1)
        self.button3["text"] = "Rendimento"
        self.button3["font"] = ("Arial","12")
        self.button3["width"] = 20
        self.button3["height"] = 5
        self.button3["command"] = self.mudarTela3
        self.button3.pack ()
        
    def mudarTela1(self):
        if self.button1["text"] == "Próximas Entregas":
            self.button1["text"] = "Entregas:"
        else:
            self.button1["text"] = "Entregas"
            
    def mudarTela2(self):
        if self.button2["text"] == "Entregas Feitas":
            self.button2["text"] = "Entregas Feitas:"
        else:
            self.button2["text"] = "Entregas"
            
    def mudarTela3(self):
       if self.button3["text"] == "Rendimento":
           self.button3["text"] = "Gráficos:"
       else:
           self.button3["text"] = "ok"
            
        
  
  
root = Tk()
Aplicação(root)
root.mainloop()
