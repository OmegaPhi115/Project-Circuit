import os
from Ressources.Code.Importations_Globales import *

class Loading_Animation:

    def __init__(self, fen, x, y):
        self.fen = fen
        self.x = x
        self.y = y
        self.images = []
        for root, directories, filenames in os.walk("Ressources\\Graphique\\Logo out\\"):
            for filename in filenames:
                self.images.append("Ressources\\Graphique\\Logo out\\" + str(filename))
        self.image_index = 0

    def anim(self):
        self.fen.blit(pygame.image.load(self.images[self.image_index]).convert_alpha(), (self.x, self.y))
        if self.image_index == 44:
            self.image_index = 0
        else:
            self.image_index = self.image_index + 1
        pygame.display.flip()
