from Ressources.Code.Class.Boutton import Boutton
from Ressources.Code.Class.Circuit import Circuit
from Ressources.Code.Class.Screen import Screen
from Ressources.Code.Fonctions.Location_Calculs import location_calculs
from Ressources.Code.Importations_Globales import *
from Ressources.Code.Class.Loading_Animation import *

# class
class Game:
    def __init__(self):
        self.taille = Window_taille

    def loca(self, row_count):
        self.screen_pos, self.map_circuit, self.map_bouton = location_calculs(row_count, self.taille)

    def main(self, row_count):
        self.loca(row_count)
        # creation surface
        # todo trouver nom pour jeu
        pygame.display.set_caption('Project Circuit')
        window_game = pygame.display.set_mode(self.taille, pygame.RESIZABLE)

        fond = pygame.image.load("Ressources\\Graphique\\Sans titre.png").convert()
        window_game.blit(fond, (0, 0))

        ffffl = Loading_Animation(window_game, 0, 0)

        # creer bouton
        bouton_list = []
        for coo_bouton_a_generer in self.map_bouton:
            bouton_list.append(Boutton(window_game, coo_bouton_a_generer[0], coo_bouton_a_generer[1]))
        for bouton in bouton_list:
            bouton.placer()

        # creer circuit
        circuit_list = []
        for coo_circuit_a_generer in self.map_circuit:
            circuit_list.append(Circuit(window_game, coo_circuit_a_generer[0], coo_circuit_a_generer[1]))
        for circuit in circuit_list:
            circuit.changer_operation(random.choice(["or", "nor", "and", "nand", "xor", "xnor"]))
            circuit.placer()
        # creer screen
        seen = Screen(window_game, self.screen_pos[0], self.screen_pos[1])

        # mainloop
        Launched = True
        win_count_down = 0
        clic_count = 0

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
                    if seen.state == 0:
                        for bouton in bouton_list:
                            bouton.tester_clic(event.pos[0], event.pos[1])
                            if bouton.last_clic:
                                clic_count += 1

                if event.type == VIDEORESIZE:
                    self.taille = event.dict['size']
                    return True

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
                    return True

            # actualisation graphique
            actu_graph = True
            if actu_graph:
                # 1) fond
                window_game.fill([40, 40, 40])

                #quelle fond utilier ?
                if list(self.taille)[0] >= 800:
                    if list(self.taille)[1] >= 400:
                        fond = pygame.image.load("Ressources\\Graphique\\Logo N&B.png").convert_alpha()
                        window_game.blit(fond,((((list(self.taille)[0]) / 2) - img_logo_taille_x / 2), ((list(self.taille)[
                                             1]) / 2) - img_logo_taille_y / 2))
                    else:
                        fond = pygame.image.load("Ressources\\Graphique\\Logo N&B 50%.png").convert_alpha()
                        window_game.blit(fond,
                                         ((((list(self.taille)[0]) / 2) - img_logo50_taille_x / 2), ((list(self.taille)[
                                             1]) / 2) - img_logo50_taille_y / 2))
                else:
                    fond = pygame.image.load("Ressources\\Graphique\\Logo N&B 50%.png").convert_alpha()
                    window_game.blit(fond,
                                     ((((list(self.taille)[0]) / 2) - img_logo50_taille_x / 2), ((list(self.taille)[
                                         1]) / 2) - img_logo50_taille_y / 2))

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
                    seen.change_state()
                    seen.update()
                    pygame.display.flip()
                    time.sleep(0.01)
                    win_count_down += 1
                    if win_count_down == 4:
                        seen.change_state()
                        seen.update()
                        pygame.display.flip()
                        print("win !")
                        print("clic count: " + str(clic_count))
                        time.sleep(1)
                        s = pygame.Surface((1000, 750), pygame.SRCALPHA)  # per-pixel alpha
                        s.fill((40, 40, 40, 150))  # notice the alpha value in the color
                        window_game.blit(s, (0, 0))
                        #ffffl.anim()
                        pygame.display.flip()
                        return True

            # actualisation fen
            pygame.display.flip()