"""J'aurait du commenter"""
from Ressources.Code.Importations_Globales import *
def location_calculs(input_row,taille):
    #output screen_pos, map_circuit, map_bouton
    if input_row <= 1:
        print("error: row_count must be higher than 1")
        raise TypeError
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
    t = list(taille)
    taille_x = t[0]
    taille_y = t[1]
    # y
    # bou = (taille_y-fenetre - (taille_screen) - (nombrederangéedecircuit * leurtaille) - (tailledesboutons) /
    # ((nombredecircuit + 1 + 1) + 1)
    repartition_y = int((taille_y - img_screen_taille_y - (row_circuit * img_circuit_taille_y) -
                         img_button_taille_y) / ((input_row + 1)))
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

    return screen_pos, map_circuit, map_bouton