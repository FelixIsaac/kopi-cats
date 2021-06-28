#draw cards at beginning
def startGameDraw():
    #get game settings for selected number of cards to be drawn at the start
    #randomly select card types for each card drawn

    pass


#draw 2 cards
def draw2cards():
    #next player in rotation will add 2 cards and will have their turn skipped. 

    #if the "stacking rule" is enabled and if the next player has a +2 card, they can stack.
    #when the a player does not have a +2 card or does not place it in time, then they will add
    #the total number of cards that have stacked. Additonally their turn will be skipped.

    pass


#reverse card
def noYou():
    #the rotation of turns is reversed.
    
    pass


#skip card
def skipTurn():
    #skip the next player.

    pass


#wild card
def colourPicker():
    #picks the colour of the next card to be played.

    pass


#wild draw 4 card
def wildDraw4():
    #picks the colour of the next card to be played and
    #the next player in the rotation has to add 4 cards and their turn is skipped.

    #if the "stacking rule" is enabled and if the next player has a +2 card of the same selected colour
    #or a wild draw 4 card, they can stack.
    #when the a player does not have a +2 card or a wild draw 4 card or does not place it in time, 
    # then they will add the total number of cards that have stacked. Additonally their turn will be skipped.

    pass


#kopicat card
def kopicat():
    #when a player plays this card, player now referred to as the copycat, will discard cards of identical type
    #or number as the next few players discarded cards in their turn. the effect of copycat will wear off when it
    #returns back to their turn. 
    #i.e. player 1 places kopicat card and becomes 'copycat'. player 2 places a 7, and at the same time copycat 
    #places a 7 from their deck in player 2's turn. this reoccurs for each other player's turn. 

    #penalty 1: when copycat does not have a card of the same number as the other player, no card will be placed by 
    #copycat in any of the other player's turns. Additionally, their turn is skipped.
    #i.e. copycat 'copies' from player 2 and places the same number card. player 3 places a 1, but copycat does not 
    #have a 1. copycat does not place any card in player 3's turn or any player after that. copycat's turn is then 
    #skipped.
    
    #penalty 2: if the kopicat card is played as the last card, the player will receive one selected card respectively
    #choesn by the players. 
    #i.e. player 2 gives a selected card to copycat. this occurs for every player after copycat.
    
    pass
    
    
#when 1 card left
def shoutUno():
    #player must shout uno when they have 1 card.
    #can be called just before the player places their second-last card.
    
    pass


#when a player does not call uno in time.
def unoCatch():
    #call out a player who did not call uno when they have 1 card left.
    #if caught the player has to add 2 cards. 

    #button to uno catch would be appear on screen the moment a player places their 2nd last card and
    #has not called uno.
    
    pass

