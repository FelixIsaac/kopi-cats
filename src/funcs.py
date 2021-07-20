import pygame
from pygame.event import post
from Cards import colours

class btn():
    def __init__(self, colour, x, y, width, height) -> None:
        self.colour = colour
        self.position = x,y
        self.dimensions = width,height
        
    def build(self, surface):
        pygame.draw.rect(surface, self.colour, (self.position, self.dimensions))


def getMousePos():
    cursorPos = (-1000, -1000)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursorPos = pygame.mouse.get_pos()
    
    return cursorPos
    

def isClicked(objX, objY, objWidth, objHeight, cursorPos):
    if cursorPos[0] > objX and cursorPos[0] < objX + objWidth and cursorPos[1] > objY and cursorPos[1] < objY + objHeight:
        return True
    


def createMenu(screenWidth, screenHeight, screen):
    btnWidth = 200
    btnHeight = 75
    btnCentred = (screenWidth/2) - (btnWidth/2)
    btnOnY = (screenHeight/4) - (btnHeight/2)

    classicGMBtn = btn(colours['white'], btnCentred, btnOnY, btnWidth, btnHeight)
    classicGMBtn.build(screen)