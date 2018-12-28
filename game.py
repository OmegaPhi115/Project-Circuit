from tkinter import *
from math import *
import random

#initialisation fenetre
fen = Tk()
fen.geometry("400x500")
fen.title("Projet Circuits")
fen.rowconfigure(0, weight=1)
fen.columnconfigure(0, weight=1)

photobuttona = 0
photobuttonb = 0
photobuttonc = 0

C = Canvas(fen, height = 500, width = 500, bg="green", borderwidth = 0)
C.place(x = 0,y = 0, anchor = "nw")
C.create_line(100,380,100,320, fill="orange")

class button():
    """boutton qui s'allume et qui séteint"""
    def __init__(self, fen_tk, x, y):
        #graphismes
        self.imgon = PhotoImage(file='images\\button_off.gif')
        self.imgoff = PhotoImage(file='images\\button_off.gif')

        #position
        self.xPos = x
        self.yPos = y

        #logique
        self.state = 0 #off

        #créer button
        self.button = Button(fen_tk, command=clic())

    def graphisme_update(self):
        """mise a jour des graphismes"""
        if self.state == 0:
            self.button.configure(image = self.imgoff)
        else:
            self.button.configure(image = self.imgoff)
        fen_graphic_update()

    def clic (self):
        """action quand button cliquer"""
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0
        self.graphisme_update()

    def place(self):
        """place sur la fenetre"""
        self.button.place(x=self.xPos, y=self.yPos, anchor = "center")



def maploader(nommap):
    """Fonction qui lit du fichier de la map et retranscrit les donées dans des variable"""
    if nommap == "classique":
        #allez chercher fichier
        #nom button = [xmin, ymin, xmax, ymax]
        buta = [80, 380, 120, 420]
        butb = [180, 380, 220, 420]
        butc = [280, 380, 320, 420]
        #liste de liste : [3, [buta,[80, 380, 120, 420],0]
        #                 [nombre de button, [nom buton, [coordonée], etat],...]

buttonindex = [3, ["buta",[80, 380, 120, 420],0], ["butb",[180, 380, 220, 420],0], ["butc",[280, 380, 320, 420],0]]



def test(a = ""):
    print("je suis la")
    print (a)

def clic(nombutton):

    i = 1
    while i <= buttonindex[0]:
        if buttonindex[i][0] == nombutton:
            #changement d'etat dans la liste buttonindex
            if buttonindex[i][2] == 0:
                buttonindex[i][2] = 1
            else:
                buttonindex[i][2] = 0
            graphic()
            break
        i += 1

imgoff = PhotoImage(file='images\\button_off.gif')
imgon = PhotoImage(file='images\\button_on.gif')
#fonction responssable de changer les images
def graphic ():
    i = 1
    #imgtampon = PhotoImage(file='images\\Patacorn.gif')  test
    #changement des images des bouttons
    while i <= buttonindex[0]:
        if buttonindex[i][0] == "buta":
            if buttonindex[i][2] == 0:
                buttona.configure(image=imgoff)
                C.create_line(100,380,100,320, fill="orange")
            if buttonindex[i][2] == 1:
                buttona.configure(image=imgon)
                C.create_line(100,380,100,320, fill="blue")

        if buttonindex[i][0] == "butb":
            if buttonindex[i][2] == 0:
                buttonb.configure(image=imgoff)
                C.create_line(200,380,200,300,140,300, fill="orange")
            if buttonindex[i][2] == 1:
                buttonb.configure(image=imgon)

        if buttonindex[i][0] == "butc":
            if buttonindex[i][2] == 0:
                buttonc.configure(image=imgoff)
                C.create_line(300,380,300,320, fill="orange")
            if buttonindex[i][2] == 1:
                buttonc.configure(image=imgon)
                C.create_line(300,380,300,320, fill="blue")
        i = i + 1

buttona = Button(fen, command= lambda: clic("buta"))
buttona.place(x=100, y=400, anchor = "center")
buttonb = Button(fen, command= lambda: clic("butb"))
buttonb.place(x=200, y=400, anchor = "center")
buttonc = Button(fen, command= lambda: clic("butc"))
buttonc.place(x=300, y=400, anchor = "center")
graphic()

x = 100
y = 300

def circuitalea():
    """choisi operation au hazard"""
    a = ["or", "nor", "and", "nand", "xor", "xnor"]
    i = random.choice(a)
    if i == "or":
        return "images\\OR.gif"
    elif i == "nor":
        return "images\\NOR.gif"
    elif i == "and":
        return "images\\AND.gif"
    elif i == "nand":
        return "images\\NAND.gif"
    elif i == "xor":
        return "images\\XOR.gif"
    elif i == "xnor":
        return "images\\XNOR.gif"

def fermer():
    a = 0 / 0

def fen_graphic_update():
    try:
        self.tk.update_idletasks()
        self.tk.update()
    except TclError:
        pass

photoa = PhotoImage(file=circuitalea())
G1 = Button(fen, image=photoa)
G1.place(x = x,y = y, anchor = "center")

x = x + 100
photob = PhotoImage(file=circuitalea())
G2 = Button(fen, image=photob)
G2.place(x = x,y = y - 100, anchor = "center")

x = x + 100
photoc = PhotoImage(file=circuitalea())
G3 = Button(fen, image=photoc)
G3.place(x = x,y = y, anchor = "center")

#end
graphic()
fen.mainloop()

