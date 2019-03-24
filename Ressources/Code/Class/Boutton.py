from Ressources.Code.Fonctions.LineMaker import *


class Boutton:
    """boutton D'entrée"""

    def __init__(self, fen, x, y, mode="center"):
        # position
        self.fen = fen
        self.xPos = x
        self.yPos = y

        self.graphical_output = [self.xPos, self.yPos]

        if mode == "center":
            self.xPos = self.xPos - (img_button_taille_x / 2) + 1
            self.yPos = self.yPos - (img_button_taille_y / 2) + 1

        # hitbox:
        self.hitbox_xa = self.xPos  # |                                 a-----|
        self.hitbox_ya = self.yPos  # |                                 |     |
        # |                                                             |     |
        self.hitbox_xb = img_button_taille_x + self.xPos  # |           |     |
        self.hitbox_yb = img_button_taille_y + self.yPos  # |           |-----b

        # grafique:
        self.current_image = "none"

        # logique
        self.state = 0
        self.last_clic = False

        self.graphisme_update()

    def graphisme_update(self):
        """mise a jour des graphismes"""
        if self.state == 0:
            self.current_image = pygame.image.load(img_button_OFF).convert_alpha()
        elif self.state == 1:
            self.current_image = pygame.image.load(img_button_ON).convert_alpha()

    def tester_clic(self, x_clic, y_clic):
        if x_clic > self.hitbox_xa:
            if y_clic > self.hitbox_ya:
                # coin [a] verifié
                if x_clic < self.hitbox_xb:
                    if y_clic < self.hitbox_yb:
                        self.last_clic = True
                        self.clicker()
                    else:
                        self.last_clic = False
                else:
                    self.last_clic = False
            else:
                self.last_clic = False
        else:
            self.last_clic = False

    def clicker(self):
        """action quand button cliquer"""
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 0
        self.graphisme_update()

    def placer(self):
        """place sur la fenetre"""
        self.fen.blit(self.current_image, (self.xPos, self.yPos))

    def update(self):
        """
        update le bouton
        on le place
        """
        self.placer()

    def line_tracer(self, destination_location):
        if self.state == 0:
            colo = couleur_off
        else:
            colo = couleur_on
        LineMaker(self.fen, self.graphical_output[0], self.graphical_output[1], destination_location[0],
                  destination_location[
            1], colo, 2)