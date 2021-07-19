import pygame, os, Cards
from funcs import createMenu

#additional vars
#------------------------------#
colours = Cards.colours
clock = pygame.time.Clock()
def refresh():
    pygame.display.update()
#------------------------------#


def drawOver(bgColour):
    #use only when there is movement of shapres involved. not sure about blits.
    refresh()
    if not gameOver:
        screen.fill(colours[bgColour])
    refresh()


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

    #gameState vars
    #------------------------------#
    global gameMode, gameOver
    FPS = 120
    gameMode = 0
    gameOver = False

    isRunning = True
    #------------------------------#


    while isRunning:
        #game init stuff
        #------------------------------#
        gameEvs = pygame.event.get()

        clock.tick(FPS) 

        for event in gameEvs:
            if event.type == pygame.QUIT:
                pygame.display.quit()

        #------------------------------#

        if gameMode == 0:
            #gameMode = 0 also is menu. 

            createMenu(screenWidth, screenHeight, screen)
            refresh()

        elif gameMode == 1:
            #for now, test site. 
            cardWidth, cardHeight = 138, 200    

            screen.fill(colours['blue'])

            testCard = Cards.RegularCard(colours['red'], 9)
            testCard.build(screen, (screenWidth/2 - cardWidth/2), (screenHeight/2 - cardHeight/2), cardWidth, cardHeight)
            #^ screenWidth/2 - cardWidth/2 is centre of screen on x-axis 

            refresh()       

        
        

if __name__ == "__main__":
    main()    
