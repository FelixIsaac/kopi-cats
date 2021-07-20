from pygame import draw

colours = {
    "red" : (255, 0, 0),
    "blue" : (0, 0, 255),
    "green" : (0, 255, 0),
    "yellow" : (255, 255, 0),
    "white" : (255, 255, 255),
    "black" : (0, 0, 0)
}


class Card():

    def __init__(self, colour):
        self.colour = colour
        
    def build(self, surface, x, y, width, height):
        draw.rect(surface, self.colour, (x, y, width, height))
        

class RegularCard(Card):

    def __init__(self, colour, cardNumber):
        super().__init__(colour)
        self.type = 'regular'
        self.cardNumber = cardNumber


class PowerCard(Card):

    def __init__(self, colour, cardPower):
        super().__init__(colour)
        self.type = 'power'
        self.cardPower = cardPower


class WildCard(Card):

    def __init__(self, cardPower):
        self.type = 'wild'
        self.colour = None 
        self.cardPower = cardPower

 
#special cards made by us.
class SpecialCard(Card):
    
    def __init__(self, colour, cardPower, cardNumber):
        super().__init__(colour)
        self.type = 'special'
        self.cardPower = cardPower
        self.cardNumber = cardNumber
        
        
