"""
Probleme: pas de boutons interactifs
solution: touches 1 2 3
"""
#TODO classe circuit

#imports
import pygame
from pygame.locals import *

#creation surface
pygame.init()
window_resolution = (550, 600)  #resolution de la surface en pixls (tupple)
window_game = pygame.display.set_mode(window_resolution)


#class Boutton:
#    #TODO boutton
#    pass


class Circuit:
    """
    Class finale de circuit
    """
    def __init__(self, x, y, ope):
        self.x = x
        self.y = y
        self.operation = ope
        self.changer_image()

    class Circuit_Entry_Checker:
        """Regarde si les entrées sont valides sinon erreur: OperationError"""

        class OperationError(Exception):
            """Erreur D'entrée d'operation logique"""

            def __init__(self, wrong_operation):
                print("Erreur D'entrée d'operation logique")
                print("")
                if wrong_operation != "Operation Variable not set":
                    print(str(wrong_operation) + " n'est pas une entrée correcte")
                else:
                    print("La variable d'operation n'est pas initialisée")

        def operation(self, op):
            # print("uhliuhouihmo!" + op)
            if op != "or" and op != "and" and op != "xor" and op != "nor" and op != "nand" and op != "xnor":
                if op == "init":
                    op = "Operation Variable Not Set"
                raise self.OperationError(op)

        class EntryError(Exception):
            """Erreur D'entrée d'operation logique"""

            def __init__(self, wrong_operation):
                print("Erreur D'entrée d'operation logique")
                print("")
                print(str(wrong_operation) + " n'est pas une entrée correcte, doit etre 1 ou 0")

        def entry(self, a):
            # entrées
            # print("test")
            # print(a)

            a = int(a)
            if a != 1 and a != 0:
                raise self.EntryError(a)

    class Circuit_Logic_operateur:
        """class de logic de circuit"""

        def AND(self, a, b):  # android
            if a + b == 2:
                return True
            else:
                return False

        def OR(self, a, b):  # ordroid
            if a + b >= 1:
                return True
            else:
                return False

        def XOR(self, a, b):  # xordroid
            if a + b == 1:
                return True
            else:
                return False

        def NOR(self, a, b):  # nordroid
            return not (self.OR(a, b))

        def NAND(self, a, b):  # nandroid
            return not (self.AND(a, b))

        def XNOR(self, a, b):  # xnordroid
            return not (self.XOR(a, b))

    def logic(self, a, b, opera="null"):
        """s'ocupe d'effectuer le calcule"""
        # on regarde si les entrées sont bonnes
        if opera == "null" or "":
            opera = self.operation
        else:
            self.operation = opera

        mod_entry_check = Circuit_Entry_Checker()  ## je suis main()
        mod_entry_check.operation(opera)
        mod_entry_check.entry(a)
        mod_entry_check.entry(b)

        module_logic = Circuit_Logic_operateur()
        # quelle est l'operation ? la faire et la metre dans outpu
        if opera == "and":
            outpu = module_logic.AND(a, b)
        elif opera == "or":
            outpu = module_logic.OR(a, b)
        elif opera == "xor":
            outpu = module_logic.XOR(a, b)
        elif opera == "nand":
            outpu = module_logic.NAND(a, b)
        elif opera == "nor":
            outpu = module_logic.NOR(a, b)
        elif opera == "xnor":
            outpu = module_logic.XNOR(a, b)
        else:
            outpu = "impossible"

        # on rend outpu
        self.output = outpu

    def deplacer(self, x, y):
        """change les coordonées"""
        self.x = int(x)
        self.y = int(y)
        self.placer()

    def changer_operation(self, ope):
        self.operation = ope
        self.changer_image()

    def changer_image(self):
        self.image = pygame.image.load("OR.png").convert_alpha()

    def placer(self):
        xy_coord = (self.x, self.y)
        window_game.blit(self.image, xy_coord)

    def actualiser(self):
        #TODO lire nput de bouton
        #self.logic()
        self.placer


fond = pygame.image.load("patacorn_by_justpatacorn-dbvwznm.jpg").convert()
window_game.blit(fond, (0,0))

circuita = Circuit(100, 300, "OR")
circuita.placer()

circuitb = Circuit(100 + 200, 300, "OR")
circuitb.placer()

circuitc = Circuit(100+100, 300-100, "OR")
circuitc.placer()

pygame.display.flip()
#mainloop
Launched = True
while Launched:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Launched = False
