"""
Constantes du jeu
"""

def init():
    # graphismes
    global Window_taille, img_logo_taille_x, img_logo_taille_y, img_logo50_taille_x, img_logo50_taille_y, \
        img_circuit_OR, img_circuit_NOR, img_circuit_AND, img_circuit_NAND, img_circuit_XOR, img_circuit_XNOR, \
        img_circuit_taille_x, img_circuit_taille_y, img_button_ON, img_button_OFF, img_button_taille_x,\
        img_button_taille_y

    Window_taille = (500, 500)

    img_logo_taille_x = 709
    img_logo_taille_y = 329

    img_logo50_taille_x = 355
    img_logo50_taille_y = 164

    #       Circuit
    img_circuit_OR = "Ressources\\Graphique\\OR.png"
    img_circuit_NOR = "Ressources\\Graphique\\NOR.png"
    img_circuit_AND = "Ressources\\Graphique\\AND.png"
    img_circuit_NAND = "Ressources\\Graphique\\NAND.png"
    img_circuit_XOR = "Ressources\\Graphique\\XOR.png"
    img_circuit_XNOR = "Ressources\\Graphique\\XNOR.png"

    img_circuit_taille_x = 100
    img_circuit_taille_y = 40

    #       Boutton
    img_button_ON = "Ressources\\Graphique\\button_onvb.png"
    img_button_OFF = "Ressources\\Graphique\\button_offvb.png"

    img_button_taille_x = 40
    img_button_taille_y = 40

    #       screen
    global img_screen_off, img_screen_on_1, img_screen_on_2, img_screen_on_3, img_screen_on_4, img_screen_on_5, \
        img_screen_taille_x, img_screen_taille_y
    img_screen_off = "Ressources\\Graphique\\fin.png"
    img_screen_on_1 = "Ressources\\Graphique\\fin1.png"
    img_screen_on_2 = "Ressources\\Graphique\\fin2.png"
    img_screen_on_3 = "Ressources\\Graphique\\fin3.png"
    img_screen_on_4 = "Ressources\\Graphique\\fin4.png"
    img_screen_on_5 = "Ressources\\Graphique\\fin5.png"

    img_screen_taille_x = 100
    img_screen_taille_y = 40

    #       couleurs
    global COLOR_RED, COLOR_GREEN, COLOR_GRAY_NIGHTMODE
    COLOR_RED = (255, 0, 0)
    COLOR_GREEN = (0, 255, 0)
    COLOR_GRAY_NIGHTMODE = (40, 40, 40)

    #       theme
    global couleur_off, couleur_on
    couleur_off = COLOR_RED
    couleur_on = COLOR_GREEN
