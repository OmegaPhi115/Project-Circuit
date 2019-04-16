"""
crée des lines
"""
from Ressources.Code.Data.Importations_Globales import *

def LineMaker(fen, pointxa, pointya, pointxb, pointyb, color, width=1, fromage="up", to="up"):
    if fromage == "up":
        if to == "up":
            middley = int((pointyb + pointya) / 2)
            pygame.draw.line(fen, color, (pointxa, pointya), (pointxa, middley), width)
            pygame.draw.line(fen, color, (pointxa, middley), (pointxb, middley), width)
            pygame.draw.line(fen, color, (pointxb, middley), (pointxb, pointyb), width)