#inports||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
import tkinter as tk
import math
import random

#On crée la fennetre principale
fenetre_principale = tk.Tk()
fenetre_principale.geometry("400x500")
fenetre_principale.title("Projet Circuits")
fenetre_principale.rowconfigure(0, weight=1)
fenetre_principale.columnconfigure(0, weight=1)

#On crée l'arierre plan sur la fenetre pricipale
C = tk.Canvas(fenetre_principale, height = 500, width = 500, bg="green", borderwidth = 0)
C.place(x = 0,y = 0, anchor = "nw")

#Mainloop
def Refresh():
    """Refresh du programe"""
    fenetre_principale.update_idletasks()
    fenetre_principale.update()
while 1:
    Refresh()