from Ressources.Code.Importations_Globales import *

pygame.mixer.init(44100, -16, 2, 4096)
#todo finish path finder
def musique():
    no = 0
    for root, directories, filenames in os.walk(
            "C:\\Users\\François\\Documents\\GitHub\\Project-Circuit\\Ressources\\Son\\Music"):#todo changer ca pls
        for filename in filenames:
            filename = str(filename)
            if filename.endswith(".wav"):
                pygame.mixer.music.load("C:\\Users\\François\\Documents\\GitHub\\Project-Circuit\\Ressources\\Son\\Music\\perso\\08 - You Will Be Evaluated Later.wav")
                no = 1

    if no == 1:
        pygame.mixer.music.play()