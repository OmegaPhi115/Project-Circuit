"""
Base pour toutes les images avec coordonées specifiques

Contien:
x: position X haut gauche
y: position Y haut gauche

image: image a montrer
image_taille_x: taille x de l'image
image_taille_y: taille y de l'image
"""

import pygame

class Widget:
    def __init__(self, x, y, fen):
        self.x = x
        self.y = y
        self.fen = fen

    def Get_image_size(self):
        self.image = image
        if image != "No Image":
            foo = pygame.image.load(a).get_rect().size
            self.image_taille_x = foo[0]
            self.image_taille_y = foo[1]

    def Convert_center_to_topright(self):
        if self.image != "No Image":
            self.Get_image_size(self.image)
            self.x = self.x - (image_taille_x / 2) + 1
            self.y = self.y - (image_taille_y / 2) + 1
