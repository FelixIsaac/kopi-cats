import pygame
from Cards import Cards

def main():
     
    pygame.init()
    
    programIcon = pygame.image.load('./assets/kopicat.PNG')
    
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption("Kopi Cat")

    screen = pygame.display.set_mode((720,480))
    card1 = Cards((255,0,0), 'normal')
    card1.build(screen)

    

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False 
                pygame.display.quit()

        pygame.display.update()


if __name__ == "__main__":
    main()    
