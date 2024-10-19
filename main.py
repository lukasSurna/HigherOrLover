import random

#Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

#return random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

#return shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

#main
print('Welcome to Higher or Lower')
print('You have to choose whether the next card to be shown will be higher or lower then the current card')
print('Getting it right adds 20 points; get it wrong and you lose 15 points')
print('You have 50 points to start')