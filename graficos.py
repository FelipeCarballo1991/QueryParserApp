from doctest import master
import tkinter as tk
from tkinter import messagebox
#import pyperclip as clipboard
#import os
from query_formatter import query_formatter

class SubWindow:

    def __init__(self):
        
        #self.frame = tk.Frame(self.master)
        self.subwindow = tk.Toplevel()
        self.frame = tk.Frame(self.subwindow)
        self.frame.pack(expand = True, fill = tk.BOTH)
        #self.subwindow.pack()
        self.subwindow.grab_set() # Mantiene el foco de la ventana hasta que se cierre y devuelve la interacción con la ventana principal el root en este caso.
        #self.subwindow.grab_set_global()
        self.subwindow.focus_set() # Mantiene el foco cuando se abre la ventana.
        #self.subwindow.pack()

        self.etiqueta = tk.Label(self.frame,text = "Ingrese Nombre del archivo")
        self.etiqueta.pack()

        self.caja_texto = tk.Entry(self.frame)
        self.caja_texto.pack()

        self.button = tk.Button(self.frame,text = "Convertir",command = self.csv_export)
        self.button.pack(side = tk.LEFT)

    def csv_export(self):
        mensaje = messagebox.showinfo("Success","Exportado en el escritorio")
        self.destroy() 

    def destroy(self):
        self.frame.destroy()
        self.subwindow.destroy()

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

        self.text_input = ""

        #Creo los botones                    
        self.button = tk.Button(self.frame,text = "Parsear",command = self.getInput)
        self.button.pack(side = tk.LEFT)

        self.button = tk.Button(self.frame,text = "Original",command = self.originalInput)
        self.button.pack(side = tk.LEFT)

        #self.button = tk.Button(self.frame,text = "Copiar",command = self.copy)
        #self.button.pack(side = tk.LEFT)

        self.button = tk.Button(self.frame,text = "Excel",command = self.excel_export) #TODO exportar excel
        self.button.pack(side = tk.LEFT)   
        self.button = tk.Button(self.frame,text = "CSV",command = self.csv_export) #TODO exportar CSV
        self.button.pack(side = tk.LEFT)   

        self.button = tk.Button(self.frame,text = "Borrar",command = self.clear)
        self.button.pack(side = tk.RIGHT)   
    
    def csv_export(self):
        self.subwindow = SubWindow()
        self.subwindow.subwindow.mainloop()
        #mensaje = messagebox.showinfo("CSV","Exportado en el escritorio")

    def excel_export(self):
        self.subwindow = SubWindow()
        self.subwindow.subwindow.mainloop()
        #mensaje = messagebox.showinfo("EXCEL","Exportado en el escritorio")      

    def getInput(self): 
        self.text_input = self.text.get("1.0","end")
        query_parser = query_formatter(self.text.get("1.0","end"),debug= True)        
        self.clear()
        self.insert(query_parser)
    
    #def copy(self): 
    #    #clipboard.copy(self.text_input)        
    #    command = 'echo ' + self.text.get("1.0","end") + '| clip'
    #    os.system(command)
    
    def originalInput(self): 
        #query_parser = query_formatter(self.text.get("1.0","end"),debug= True)
        self.clear()
        self.insert(self.text_input)
                
    
    def clear(self): 
        self.text.delete("1.0","end")

    def insert(self,result): 
        self.text.insert(tk.INSERT,result)   



root = tk.Tk()
root.title("QueryParser v2")
window = Window(root)
root.mainloop()


