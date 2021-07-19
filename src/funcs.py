from pygame import font, draw, display
from Cards import colours

class btn():
    def __init__(self, colour, x, y, width, height) -> None:
        self.colour = colour
        self.position = x,y
        self.dimensions = width,height
        
    def build(self, surface):
        draw.rect(surface, self.colour, (self.position, self.dimensions))


def createMenu(screenWidth, screenHeight, screen):
    btnWidth = 200
    btnHeight = 75
    btnCentred = (screenWidth/2) - (btnWidth/2)
    btnOnY = (screenHeight/4) - (btnHeight/2)

    classicGMBtn = btn(colours['white'], btnCentred, btnOnY, btnWidth, btnHeight)
    classicGMBtn.build(screen)