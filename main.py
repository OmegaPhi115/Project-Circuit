row_count = 7 + (1 + 1) # number of rows / nombre rangées circuit

from Ressources.Code.Fonctions.Music_loader import musique
from Ressources.Code.Game import Game

musique()

game_on = True
a = Game()
while game_on:
    game_on = a.Run(row_count)

#bouton minimum despace = 1 --> 0