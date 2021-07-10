import pygame
from pygame.constants import FULLSCREEN, RESIZABLE
from Cards import Cards, colours

"""
#reg1 = RegularCards((0,255,0), '1')
prototypeCard = Cards((255,0,0), 'regular')

def createCards():
     #should not be hard coded. should be computer decided. but not sure how.
     prototypeCard.build(screen)
     #reg1.build(screen)
"""
     
def main():
     
    pygame.init()
    
    programIcon = pygame.image.load('../assets/kopicaticon.PNG')
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption("Kopi Cat")
    
    screen = pygame.display.set_mode((720,480), pygame.RESIZABLE)
    
    isRunning = True
    while isRunning:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False 
                pygame.display.quit()

        for event in pygame.event.get():
            if event.type == pygame.WINDOWMAXIMIZED:
                pygame.display.quit()
                screen
                pygame.display.init()

        screen.fill((40,0,180))
    
        prototypeCard = Cards(colours["red"], 'normal')
        prototypeCard.build(screen, (280,180,150,230))

        pygame.display.update()


if __name__ == "__main__":
    main()    
