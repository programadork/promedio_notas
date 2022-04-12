
from tkinter import *

root = Tk()
root.title("Promedio de notas del estudiante")
root.geometry("700x400")
root.config(bg="teal")

frame1 = LabelFrame(root,text="Datos del estudiante", font=("calibri", 14))
frame2 = LabelFrame(root,text="Promedio", font=("calibri", 14))

frame1.pack(fill="both", expand="yes", padx=20, pady=15)
frame2.pack(fill="both", expand="yes", padx=20, pady=15)

matematicas = IntVar()
naturales = IntVar()
sociales = IntVar()
lenguaje = IntVar()
promedio = StringVar()



#==============================================================
def mostrar():
    valor=(matematicas.get()+naturales.get()+sociales.get()+lenguaje.get())/4
    promedio.set(str(valor))

def reiniciar():
    matematicas.set("")  
    naturales.set("") 
    sociales.set("") 
    lenguaje.set("") 
    promedio.set("")   
#==============================================================

lbl1 = Label(frame1, text="Matematicas", width=20)
lbl1.grid(row=0, column=0, padx=5, pady=3)
entMat = Entry(frame1,textvariable=matematicas)   
entMat.grid(row=0, column=1, padx=5, pady=3) 


lbl1 = Label(frame1, text="Naturales", width=20)
lbl1.grid(row=1, column=0, padx=5, pady=3)
entMat = Entry(frame1,textvariable=naturales)   
entMat.grid(row=1, column=1, padx=5, pady=3) 


lbl1 = Label(frame1, text="Sociales", width=20)
lbl1.grid(row=2, column=0, padx=5, pady=3)
entMat = Entry(frame1,textvariable=sociales)   
entMat.grid(row=2, column=1, padx=5, pady=3) 


lbl1 = Label(frame1, text="Lenguaje", width=20)
lbl1.grid(row=3, column=0, padx=5, pady=3)
entMat = Entry(frame1,textvariable=lenguaje)   
entMat.grid(row=3, column=1, padx=5, pady=3) 


lbl1 = Label(frame2, text="Promedio", width=20)
lbl1.grid(row=0, column=0, padx=5, pady=3)
entpromedio = Entry(frame2,textvariable=promedio)   
entpromedio.grid(row=0, column=1, padx=5, pady=3) 

btn1 = Button(frame2, text="Promedio", width=10, height=2,command=mostrar)
btn1.grid(row=3, column=1, padx=10, pady=10)

btn2 = Button(frame2, text="Reiniciar", width=10, height=2,command=reiniciar)
btn2.grid(row=3, column=3, padx=10, pady=10)







root.mainloop()