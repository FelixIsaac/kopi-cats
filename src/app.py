import pygame, os
from Cards import Cards, colours
from funcs import createMenu


def main():
    # game init stuff
    #------------------------------# 
    pygame.init()
    
    programIcon = pygame.image.load(os.path.join('.', 'assets\kopicaticon.png'))
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption("Kopi Cat")

    global screenWidth, screenHeight, screen
    screenWidth = 720
    screenHeight = 480
    
    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
    #------------------------------#

    isRunning = True
    while isRunning:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

        screen.fill((40, 0, 180))
    
        prototypeCard = Cards(colours["red"], 'normal')
        prototypeCard.build(screen, (280,180,150,230))

        pygame.display.update()
        createMenu()


if __name__ == "__main__":
    main()    
