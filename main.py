from Ressources.Code.Class.Boutton import *
from Ressources.Code.Class.Circuit import *
from Ressources.Code.Class.Screen import *


"""
map generation:
bouton = [[x, y], ...]
circuit = #bas gauche premier, hautdroite dernier [(x, y), ...]
"""

# Entrées
row_count = 3 + (1 + 1) # number of rows / nombre rangées circuit

try:
    if row_count <= 1:
        print("error: row_count must be higher than 1")
        raise TypeError
except TypeError:
    start_up = "Wrong Entries: row_count"

taille = (500, 500)
def location_calculs(input_row, screen_size):
    global screen_pos, map_circuit, map_bouton
    # nombre circuits et boutons
    row_circuit = input_row - 2
    # retirer le premier
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
    t = list(screen_size)
    taille_x = t[0]
    taille_y = t[1]
    # y
    # bou = (taille_y-fenetre - (taille_screen) - (nombrederangéedecircuit * leurtaille) - (tailledesboutons) /
    # ((nombredecircuit + 1 + 1) + 1)
    repartition_y = int((taille_y - img_screen_taille_y - (row_circuit * img_circuit_taille_y) -
                         img_button_taille_y) / ((row_count + 1)))
    # x
    # screen
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
    # bouton
    # bou = (500 - (nombredebouton * lataille)) / lenombred'espace + 1
    bouton_repartition_x = int((taille_x - (bouton_count * img_button_taille_x)) / (bouton_count + 1))
    # tempo car metre y dinamiquement
    map_bouton = []
    pos = 0
    for i in range(0, bouton_count):
        pos = pos + bouton_repartition_x + (img_button_taille_x / 2)
        map_bouton.append([pos, int(repartition_y_taken + repartition_y + int((img_button_taille_y / 2)))])
        pos += img_button_taille_x / 2
    if bouton_repartition_x < 0:
        print("agrandir fenetre en x")
    if repartition_y < 40:
        print("agrandir fenetre en y")

# jeu

def Game(map_bouton, map_circuit, screen_coo):
    global window_game, taille, game_on
    # creation surface
    pygame.init()
    #todo trouver nom pour jeu
    pygame.display.set_caption('Project Circuit')
    window_game = pygame.display.set_mode(taille, pygame.RESIZABLE)

    fond = pygame.image.load("Ressources\\Graphique\\Sans titre.png").convert()
    window_game.blit(fond, (0, 0))

    # creer bouton
    bouton_list = []
    for coo_bouton_a_generer in map_bouton:
        bouton_list.append(Boutton(window_game, coo_bouton_a_generer[0], coo_bouton_a_generer[1]))
    for bouton in bouton_list:
        bouton.placer()

    # creer circuit
    circuit_list = []
    for coo_circuit_a_generer in map_circuit:
        circuit_list.append(Circuit(window_game, coo_circuit_a_generer[0], coo_circuit_a_generer[1]))
    for circuit in circuit_list:
        circuit.changer_operation(random.choice(["or", "nor", "and", "nand", "xor", "xnor"]))
        circuit.placer()
    # creer screen
    seen = screen(window_game, screen_coo[0], screen_coo[1])

    # mainloop
    Launched = True
    win_count_down = 0
    clic_count = 0

    while Launched:

        #surface = pygame.display.get_surface()
        #taille = surface.get_width(), surface.get_height()
        #print(taille)
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

            if event.type==VIDEORESIZE:
                taille = event.dict['size']
                return

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
                    return

        # actualisation fen
        pygame.display.flip()

game_on = True

while game_on:
    location_calculs(row_count, taille)
    Game(map_bouton, map_circuit, screen_pos)
