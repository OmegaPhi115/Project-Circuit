"""
circuit refaire les sprites car pas dans theme

map generation:
bouton = [[x, y], ...]
circuit = #bas gauche premier, hautdroite dernier [(x, y), ...]
"""

# imports
import pygame
from pygame.locals import *
from Constantes import *
import random
import time

# map loading
row_count = 5 + (1 + 1) # nombre rangé circuit + (screen + bouton)
taille = (1300, 700)

# todo protection entrées

if True:
    # nombre circuits et boutons
    row_circuit = row_count - 2
    #retirer le premier
    row_circuit -= 1

    i = 0
    care = 1
    liste_circuit_row = []
    while i <= row_circuit:
        circuit_count = care
        liste_circuit_row.append(care)
        care *= 2
        i += 1
    bouton_count = care
    # bouton x
    t = list(taille)
    taille_x = t[0]
    taille_y = t[1]


    # y

    # bou = (taille_y-fenetre - (taille_screen) - (nombrederangéedecircuit * leurtaille) - (tailledesboutons) /
    # ((nombredecircuit + 1 + 1) + 1)
    repartition_y = int((taille_y - img_screen_taille_y - (row_circuit * img_circuit_taille_y) -
                         img_button_taille_y) / ((row_count+ 1)))

    # x
    #screen
    screen_pos = [int(taille_x / 2), int(repartition_y + int((img_screen_taille_y) / 2))]

    repartition_y_taken = 0
    repartition_y_taken += int(repartition_y + img_screen_taille_y)

    # circuit x

    map_circuit = []
    for nbr_cir in liste_circuit_row:
        circuit_repartition_x = int((taille_x - (nbr_cir * img_circuit_taille_x)) / (nbr_cir + 1))
        pos = 0
        i = 1
        map_tempo = []
        while i <= nbr_cir:
            pos = pos + circuit_repartition_x + (img_circuit_taille_x / 2)

            map_tempo.append([pos, repartition_y_taken + repartition_y + int(img_circuit_taille_y / 2)])
            pos += img_circuit_taille_x / 2
            i += 1
        map_tempo.reverse()
        for i in map_tempo:
            map_circuit.append(i)
        repartition_y_taken += repartition_y + img_circuit_taille_y

    map_circuit.reverse()


    #bouton

    # bou = (500 - (nombredebouton * lataille)) / lenombred'espace + 1

    bouton_repartition_x = int((taille_x - (bouton_count * img_button_taille_x)) / (bouton_count + 1))

    # tempo car metre y dinamiquement
    map_bouton = []
    pos = 0
    for i in range(0, bouton_count):
        pos = pos + bouton_repartition_x + (img_button_taille_x / 2)
        map_bouton.append([pos, int(repartition_y_taken + repartition_y + int((img_button_taille_y / 2)))])
        pos += img_button_taille_x / 2

    if bouton_repartition_x < img_circuit_taille_x:
        print("agrandir fenetre en x")
    if repartition_y < 40:
        print("agrandir fenetre en y")



# class
class Boutton:
    """boutton D'entrée"""

    def __init__(self, x, y, mode="center"):
        # position
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
        # TODO modifier graphisme
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
        window_game.blit(self.current_image, (self.xPos, self.yPos))

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
        LineMaker(self.graphical_output[0], self.graphical_output[1], destination_location[0], destination_location[
            1], colo, 2)


class Circuit:
    """
    Class finale de circuit
    """

    def __init__(self, x, y, mode="center"):
        self.x = x
        self.y = y
        self.operation = "or"
        self.image = "not init"
        self.output = 0

        self.graphical_input_a = [self.x - 20, self.y]
        self.graphical_input_b = [self.x + 20, self.y]

        self.graphical_output = [self.x, self.y]

        if mode == "center":
            self.x = self.x - (img_circuit_taille_x / 2) + 1
            self.y = self.y - (img_circuit_taille_y / 2) + 1

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

    def logic(self, a, b):
        """s'ocupe d'effectuer le calcule"""
        # on regarde si les entrées sont bonnes
        opera = self.operation

        mod_entry_check = self.Circuit_Entry_Checker()  # je suis main()
        mod_entry_check.operation(opera)
        mod_entry_check.entry(a)
        mod_entry_check.entry(b)

        module_logic = self.Circuit_Logic_operateur()

        # quelle est l'operation ? la faire et la metre dans outpu
        outpu = 0
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

        if outpu:
            outpu = 1
        else:
            outpu = 0

        # on rend outpu
        self.output = outpu

    def deplacer(self, x, y):
        """change les coordonées"""
        self.x = int(x)
        self.y = int(y)
        self.placer()

    def changer_operation(self, ope):
        """change l'operation par entré"""
        self.operation = ope
        self.changer_image()

    def changer_image(self):
        """Change l'image en raport avec l'operation"""
        # todo change image operation
        if self.operation == "or":
            self.image = pygame.image.load(img_circuit_OR).convert_alpha()
        if self.operation == "nor":
            self.image = pygame.image.load(img_circuit_NOR).convert_alpha()
        if self.operation == "and":
            self.image = pygame.image.load(img_circuit_AND).convert_alpha()
        if self.operation == "nand":
            self.image = pygame.image.load(img_circuit_NAND).convert_alpha()
        if self.operation == "xor":
            self.image = pygame.image.load(img_circuit_XOR).convert_alpha()
        if self.operation == "xnor":
            self.image = pygame.image.load(img_circuit_XNOR).convert_alpha()

    def placer(self):
        """Placer sur la surface"""
        xy_coord = (self.x, self.y)
        window_game.blit(self.image, xy_coord)

    def update(self):
        """actualisation"""
        self.placer()

    def line_tracer(self, destination_location):
        if self.output == 0:
            colo = couleur_off
        else:
            colo = couleur_on
        LineMaker(self.graphical_output[0], self.graphical_output[1], destination_location[0], destination_location[
            1], colo, 2)


class screen:
    def __init__(self, x, y, mode="center"):
        self.x = x
        self.y = y

        self.graphical_input = [self.x, self.y]

        self.state = 0

        if mode == "center":
            self.x = self.x - (img_screen_taille_x / 2) + 1
            self.y = self.y - (img_screen_taille_y / 2) + 1

        self.placer()

    def change_state(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0

    def placer(self):
        if self.state == 0:
            img = img_screen_off
        else:
            img = img_screen_on_4
        img = pygame.image.load(img).convert_alpha()
        window_game.blit(img, (self.x, self.y))

    def update(self):
        self.placer()


# methodes
def LineMaker(pointxa, pointya, pointxb, pointyb, color, width=1, fromage="up", to="up"):
    if fromage == "up":
        if to == "up":
            middley = int((pointyb + pointya) / 2)
            pygame.draw.line(window_game, color, (pointxa, pointya), (pointxa, middley), width)
            pygame.draw.line(window_game, color, (pointxa, middley), (pointxb, middley), width)
            pygame.draw.line(window_game, color, (pointxb, middley), (pointxb, pointyb), width)


# jeu



def Game(map_bouton, map_circuit, screen_coo):
    global window_game
    # creation surface
    pygame.init()
    window_game = pygame.display.set_mode(taille)

    fond = pygame.image.load("Ressources\\Graphique\\Sans titre.png").convert()
    window_game.blit(fond, (0, 0))

    # creer bouton
    bouton_list = []
    for coo_bouton_a_generer in map_bouton:
        bouton_list.append(Boutton(coo_bouton_a_generer[0], coo_bouton_a_generer[1]))
    for bouton in bouton_list:
        bouton.placer()

    # creer circuit
    circuit_list = []
    for coo_circuit_a_generer in map_circuit:
        circuit_list.append(Circuit(coo_circuit_a_generer[0], coo_circuit_a_generer[1]))
    for circuit in circuit_list:
        circuit.changer_operation(random.choice(["or", "nor", "and", "nand", "xor", "xnor"]))
        circuit.placer()
    # creer screen
    seen = screen(screen_coo[0], screen_coo[1])

    # mainloop
    Launched = True
    win_count_down = 0
    clic_count = 0

    while Launched:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Launched = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                for bouton in bouton_list:
                    bouton.tester_clic(event.pos[0], event.pos[1])
                    if bouton.last_clic:
                        clic_count += 1

        # fin des events

        # actualisation logique
        output = []
        for bouton in bouton_list:
            output.append(bouton.state)
        for circui in circuit_list:
            circui.logic(output[0], output[1])
            output.append(circui.output)
            # retirer les deux utiliser
            trash = output.pop(0)
            trash = output.pop(0)
        seen.state = output.pop(0)

        if seen.state == 1:
            if clic_count == 0:
                return

        # actualisation graphique
        actu_graph = True
        if actu_graph:
            # 1) fond
            fond = pygame.image.load("Ressources\\Graphique\\Sans titre.png").convert()
            window_game.blit(fond, (0, 0))

            # 2) lignes
            graphical_input = []

            for circui in circuit_list:
                graphical_input.append(circui.graphical_input_a)
                graphical_input.append(circui.graphical_input_b)
            graphical_input.append(seen.graphical_input)

            #        coo fin
            graphical_input.append([250, 0])

            for bouton in bouton_list:
                current_input = graphical_input.pop(0)
                bouton.line_tracer(current_input)

            for circui in circuit_list:
                current_input = graphical_input.pop(0)
                circui.line_tracer(current_input)

            # 3) objets
            for bouton in bouton_list:
                bouton.update()

            for circui in circuit_list:
                circui.update()

            seen.update()

            # win ?
            if seen.state == 1:
                win_count_down += 1
                if win_count_down == 3:
                    print("win !")
                    print("clic count: " + str(clic_count))
                    time.sleep(1)
                    return

        # actualisation fen
        pygame.display.flip()

game_on = True

while game_on:
    Game(map_bouton, map_circuit, screen_pos)
