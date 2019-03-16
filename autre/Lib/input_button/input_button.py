import tkinter
class input_button():
    """boutton D'entrée"""
    def __init__(self, fen_tk, x, y):
        #graphismes
        try:
            self.imgon = "Ressources\\Graphique\\button_on.gif"
            self.imgoff = "Ressources\\Graphique\\button_off.gif"
        except:
            print("Error: image is not init !")

        #position
        self.xPos = x
        self.yPos = y

        #logique
        self.state = "on" #off

        #créer button
        try:
            self.button_widget = Button(fen)
        except:
            print("Error: button is not init !")
        self.place()
        self.graphisme_update()

    def graphisme_update(self):
        """mise a jour des graphismes"""
        print("jifdjiodj" + str(self.state))
        if self.state == "off":
            print("here 1")
            self.button_widget.configure(self, image = self.imgoff)
            print("off")
        elif self.state == "on":
            print("here 2")
            self.button_widget.configure(self, image = self.imgon)
            print("on")
        fen_graphic_update()

    def clic(self):
        """action quand button cliquer"""
        if self.state == "off":
            self.state = "on"
        elif self.state == "on":
            self.state = "off"
        self.graphisme_update()

    def place(self):
        """place sur la fenetre"""
        self.button_widget.place(x=self.xPos, y=self.yPos, anchor = "center")

fen = Tk()
a = input_button()
