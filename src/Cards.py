from pygame import draw

colours = {
    "red" : (255, 0, 0),
    "blue" : (0, 0, 255),
    "green" : (0, 255, 0),
    "yellow" : (255, 255, 0),
    "white" : (255, 255, 255),
    "black" : (0, 0, 0)
}

class Cards():

    def __init__(self, colour, cardType):
        self.colour = colour
        self.type = cardType
        
    def build(self, surface):
        draw.rect(surface,self.colour,(100,300,100,300))
        

class RegularCards(Cards):

    def __init__(self, colour, cardType, cardNumber):
        super().__init__(colour, cardType)
        self.cardType = 'regular'
        self.cardNumber = cardNumber


class PowerCards(Cards):

    def __init__(self, colour, cardType, cardPower):
        super().__init__(colour, cardType)
        self.cardType = 'power'
        self.cardPower = cardPower


class WildCards(Cards):

    def __init__(self, cardType, colour, cardPower):
        super().__init__(cardType, colour)
        self.cardsType = 'wild'
        self.colour = None 
        self.cardPower = cardPower

 
#special cards made by us.
class SpecialCards(Cards):
    
    def __init__(self, cardType, colour, cardPower, cardNumber):
        super().__init__(colour, cardType)
        self.cardType = 'special'
        self.cardPower = cardPower
        self.cardNumber = cardNumber
        
        
