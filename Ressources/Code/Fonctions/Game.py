from Ressources.Code.Class.Boutton import Boutton
from Ressources.Code.Class.Circuit import Circuit
from Ressources.Code.Class.Screen import Screen
from Ressources.Code.Fonctions.Location_Calculs import location_calculs
from Ressources.Code.Importations_Globales import *
from Ressources.Code.Class.Loading_Animation import *


# todo trouver nom pour jeu


# class
class Game:
    def __init__(self):
        self.taille = Window_taille

    def start(self, row_count):
        # creation surface
        pygame.display.set_caption('Project Circuit')
        self.window_game = pygame.display.set_mode(self.taille, pygame.RESIZABLE)
        #self.window_game.blit(pygame.image.load("Ressources\\Graphique\\Logo N&B 50%.png").convert_alpha(), (250, 250))
        pygame.display.flip()
        self.Widget_creation(row_count)

    def Widget_creation(self, row_count):
        self.Widgets_location(row_count)

        # creer bouton
        self.bouton_list = []
        for coo_bouton_a_generer in self.map_bouton:
            self.bouton_list.append(Boutton(self.window_game, coo_bouton_a_generer[0], coo_bouton_a_generer[1]))

        # creer circuit
        self.circuit_list = []
        for coo_circuit_a_generer in self.map_circuit:
            self.circuit_list.append(Circuit(self.window_game, coo_circuit_a_generer[0], coo_circuit_a_generer[1]))

        #attribuer les operations:
        #creer list opera
        self.liste_operations = []
        for circuit in self.circuit_list:
            self.liste_operations.append(random.choice(["or", "nor", "and", "nand", "xor", "xnor"]))
        print(self.liste_operations)

        #apliquer
        for i in range(len(self.liste_operations)):
            print(self.liste_operations[i])
            self.circuit_list[i].changer_operation(self.liste_operations[i])
            #self.circuit_list[i]

        # creer screen
        self.seen = Screen(self.window_game, self.screen_pos[0], self.screen_pos[1])

    def Widgets_location(self, row_count):
        self.screen_pos, self.map_circuit, self.map_bouton = location_calculs(row_count, self.taille)

    def Run(self, row_count):
        self.start(row_count)

        # mainloop
        Launched = True
        self.win_count_down = 0
        self.clic_count = 0

        while Launched:
            # surface = pygame.display.get_surface()
            # taille = surface.get_width(), surface.get_height()
            # print(taille)
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Launched = False
                    game_on = False

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.seen.state == 0:
                        for bouton in self.bouton_list:
                            bouton.tester_clic(event.pos[0], event.pos[1])
                            if bouton.last_clic:
                                self.clic_count += 1

                if event.type == VIDEORESIZE:
                    self.taille = event.dict['size']
                    return True

            # fin des events

            # actualisation logique
            output = []
            for bouton in self.bouton_list:
                output.append(bouton.state)
            for circui in self.circuit_list:
                circui.logic(output[0], output[1])
                output.append(circui.output)
                # retirer les deux utiliser
                trash = output.pop(0)
                trash = output.pop(0)
            self.seen.state = output.pop(0)

            if self.seen.state == 1:
                if self.clic_count == 0:
                    return True
            self.Acualisation_graphique()

            # win ?
            if self.seen.state == 1:
                self.seen.change_state()
                self.seen.update()
                pygame.display.flip()
                time.sleep(0.01)
                self.win_count_down += 1
                if self.win_count_down == 4:
                    self.seen.change_state()
                    self.seen.update()
                    pygame.display.flip()
                    print("win !")
                    print("clic count: " + str(self.clic_count))
                    print()
                    time.sleep(1)
                    s = pygame.Surface((1000, 750), pygame.SRCALPHA)  # per-pixel alpha
                    s.fill((40, 40, 40, 150))  # notice the alpha value in the color
                    self.window_game.blit(s, (0, 0))
                    pygame.display.flip()
                    return True

    def Acualisation_graphique(self):
        # actualisation graphique
        actu_graph = True
        if actu_graph:
            # 1) fond
            self.window_game.fill([40, 40, 40])

            #quelle fond utilier ?
            if list(self.taille)[0] >= 800:
                if list(self.taille)[1] >= 400:
                    fond = pygame.image.load("Ressources\\Graphique\\Logo N&B.png").convert_alpha()
                    self.window_game.blit(fond,((((list(self.taille)[0]) / 2) - img_logo_taille_x / 2), ((list(self.taille)[
                                         1]) / 2) - img_logo_taille_y / 2))
                else:
                    fond = pygame.image.load("Ressources\\Graphique\\Logo N&B 50%.png").convert_alpha()
                    self.window_game.blit(fond,
                                     ((((list(self.taille)[0]) / 2) - img_logo50_taille_x / 2), ((list(self.taille)[
                                         1]) / 2) - img_logo50_taille_y / 2))
            else:
                fond = pygame.image.load("Ressources\\Graphique\\Logo N&B 50%.png").convert_alpha()
                self.window_game.blit(fond,
                                 ((((list(self.taille)[0]) / 2) - img_logo50_taille_x / 2), ((list(self.taille)[
                                     1]) / 2) - img_logo50_taille_y / 2))

            # 2) lignes
            graphical_input = []

            for circui in self.circuit_list:
                graphical_input.append(circui.graphical_input_a)
                graphical_input.append(circui.graphical_input_b)
            graphical_input.append(self.seen.graphical_input)

            #        coo fin
            graphical_input.append([250, 0])

            for bouton in self.bouton_list:
                current_input = graphical_input.pop(0)
                bouton.line_tracer(current_input)

            for circui in self.circuit_list:
                current_input = graphical_input.pop(0)
                circui.line_tracer(current_input)

            # 3) objets
            for bouton in self.bouton_list:
                bouton.update()

            for circui in self.circuit_list:
                circui.update()

            self.seen.update()

        # actualisation fen
        pygame.display.flip()