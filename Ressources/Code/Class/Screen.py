from Ressources.Code.Data.Importations_Globales import *

class Screen:
    def __init__(self, fen, x, y, mode="center"):
        self.fen = fen
        self.x = x
        self.y = y

        self.graphical_input = [self.x, self.y]

        self.image_count = 0
        self.state = 0

        if mode == "center":
            self.x = self.x - (img_screen_taille_x / 2) + 1
            self.y = self.y - (img_screen_taille_y / 2) + 1

        self.placer()

    def change_state(self):
        if self.state == 0:
            self.state = 1
            self.image_count = 1
        else:
            self.image_count += 1

    def placer(self):
        img = "state invalid"
        if self.image_count == 0:
            img = img_screen_off
        if self.image_count == 1:
            img = img_screen_on_1
        if self.image_count == 2:
            img = img_screen_on_2
        elif self.image_count == 3:
            img = img_screen_on_3
        elif self.image_count == 4:
            img = img_screen_on_4
        elif self.image_count == 5:
            img = img_screen_on_5
        img = pygame.image.load(img).convert_alpha()
        self.fen.blit(img, (self.x, self.y))

    def update(self):
        self.placer()