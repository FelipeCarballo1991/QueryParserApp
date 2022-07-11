import tkinter as tk
from query_formatter import query_formatter



class Window:

    def __init__(self,master):
        self.master = master
        

        #Creo el marco no ocurre nada
        self.frame = tk.Frame(self.master)
        #Configuro el color
        #self.frame.config(bg="lightblue") 
        #Si se expande la ventana tambien el frame         
        self.frame.pack(expand = True, fill = tk.BOTH)

        #Posiciono una etiqueta
        #self.label = tk.Label(self.frame, text= "Ingrese la query en formato select * from",anchor = "nw")
        #self.label.pack()
        
        #Creo una caja de texto
        self.text = tk.Text(self.frame)
        #Si se expande la ventana tambien el text       
        self.text.pack(expand = True, fill = tk.BOTH)
        self.text.pack()

        #Creo los botones                    
        self.button = tk.Button(self.frame,text = "Parsear",command = self.getInput)
        self.button.pack(side = tk.LEFT)

        self.button = tk.Button(self.frame,text = "Borrar",command = self.clear)
        self.button.pack(side = tk.LEFT)

    def getInput(self): 
        query_parser = query_formatter(self.text.get("1.0","end"))
        self.clear()
        self.insert(query_parser)
                
    
    def clear(self): 
        self.text.delete("1.0","end")

    def insert(self,result): 
        self.text.insert(tk.INSERT,result)   



root = tk.Tk()
root.title("QueryParser v2")
window = Window(root)
root.mainloop()