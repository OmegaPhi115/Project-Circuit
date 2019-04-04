row_count = 0 + (1 + 1) # number of rows / nombre rangées circuit

from Ressources.Code.Importations_Globales import *
from Ressources.Code.Fonctions.Music_loader import musique
from Ressources.Code.Fonctions.Game import Game
import os

musique()

game_on = True
a = Game()
while game_on:
    game_on = a.Run(row_count)



#bouton cacher alors que screen trop de place

#bouton minimum despace = 1 --> 0

#tout les bouton qui sont sur le clic change d'etats
#--> seulement 1 bouton