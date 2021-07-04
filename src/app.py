import pygame
from Cards import Cards, colours

def main():
     
    pygame.init()
    
    programIcon = pygame.image.load('./assets/kopicaticon.PNG')
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption("Kopi Cat")

    screen = pygame.display.set_mode((720,480))
    
    prototypeCard = Cards(colours["red"], 'normal')
    prototypeCard.build(screen)

    isRunning = True
    while isRunning:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False 
                pygame.display.quit()

        pygame.display.update()


if __name__ == "__main__":
    main()    
