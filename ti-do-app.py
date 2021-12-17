import tkinter
from tkinter import *
import tkinter as tk
from math import *



fenetre1 = tk.Tk()
fenetre1.state("zoomed")
fenetre1.configure(bg='#696969')
fenetre1.title("To Do App".center(460))



def fenetre2_verif():
    fenetre2 = Toplevel()
    fenetre2.geometry("150x150")
    fenetre2.configure(bg='#696969')
    oui = tk.Button(fenetre2, text="OUI !", activebackground='red',activeforeground='white', fg= 'white' , bg='#696969',  command= fenetre2.destroy and fenetre1.destroy).grid(row=1, column=6)
    
    non = tk.Button(fenetre2, text="NON !",activebackground='red',activeforeground='white', fg= 'white' , bg='#696969',  command= fenetre1.destroy).grid(row=2, column=4)
   



txt1=Label(fenetre1, fg='white' , bg='#696969', text="User Name :").grid(row=1, column=1) 
txt2=Label(fenetre1, fg='white' , bg='#696969', text='Password :').grid(row=2, column=1) 
A=Entry(fenetre1) 
B=Entry(fenetre1)
A.grid(row=1, column=2) 
B.grid(row=2, column=2)    
    






quitter = tk.Button(fenetre1, text="Quitter", activebackground='red',activeforeground='white', fg= 'white' , bg='#696969',  command= fenetre2_verif)
quitter.grid()


fenetre1.mainloop()