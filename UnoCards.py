class Cards():

    def __init__(self, colour, cardType):
        self.colour = colour
        self.type = cardType




class RegularCards(Cards):

    def __init_(self, colour, cardType, cardNumber):
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

    