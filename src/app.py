import pygame

def main():
     
    pygame.init()
    
    pygame.display.set_logo()
    pygame.display.set_caption("Kopi-Cat Uno")

    screen = pygame.display.set_mode((720,480))

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False 
                pygame.dispay.quit()


if __name__ == "__main__":
    main()    
