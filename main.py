import random

#Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 1

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
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue +1}
        startingDeckList.append(cardDict)
        
score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print(f'Starting card is: {currentCardRank} of {currentCardSuit}')
    print()
    
    for cardNumber in range(0, NCARDS):
        answer = input(f'Will the next card be higher or lower then the {currentCardRank} of {currentCardSuit}? (enter h or l): ')
        answer = answer.casefold()
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print(f'Next card is: {nextCardRank} of {nextCardSuit}')
        
        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You get it right, it was higher')
                score += 20
            else:
                print('Sorry, it was not higher')
                score -= 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score += 20
                print('You got it right, it was lower')
            else:
                score -= 15
                print('Sorry, it was not lower')
        
        print(f'Your score is: {score}')
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
    
    goAgain = input('To play again, press ENTER, or "q" to quit: ').strip().lower()
    if goAgain == 'q':
        print('Ok bye')
        break