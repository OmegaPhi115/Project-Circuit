row_count = 4 + (1 + 1) # number of rows / nombre rangées circuit

from Ressources.Code.Importations_Globales import *
from Ressources.Code.Fonctions.Music_loader import musique
from Ressources.Code.Fonctions.Game import Game
import os

musique()

#Boucle infinie
game_on = True

a = Game()
while game_on:
    game_on = a.main(row_count)
