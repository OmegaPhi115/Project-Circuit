import tkinter as tk

class input_button():
    """boutton D'entrée"""
    #1) graphismes
    self.imgon = tk.PhotoImage(file="images\\button_off.gif")
    self.imgoff = tk.PhotoImage(file="images\\button_on.gif")

    #position
    self.xPos = x
    self.yPos = y

    #logique
    self.state = "on" #off