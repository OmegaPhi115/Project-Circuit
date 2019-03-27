row_count = 3 + (1 + 1) # number of rows / nombre rangées circuit

from Ressources.Code.Importations_Globales import *
from Ressources.Code.Fonctions.Music_loader import musique
from Ressources.Code.Fonctions.Game import Game
import os

musique()

#Boucle infinie
game_on = True

while game_on:
    game_on = Game(row_count)
