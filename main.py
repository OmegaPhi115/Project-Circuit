#imports
import pygame

#creation surface
pygame.init()
window_resolution = (640,480)#resolution de la surface en pixls (tupple)
window_game = pygame.display.set_mode(window_resolution)




#mainloop
Launched = True
while Launched == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Launched = False