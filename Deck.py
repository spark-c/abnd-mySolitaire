# Solitaire Deck

import allCards, random, Board


def shuffle(deck):
    population = allCards.Cards.keys()
    deck = random.sample(population, 52)
    return deck

def move(amt, src, dest, hidden=False):
    if amt > 0: # Pulls cards from the top
        moving = src[0:amt]
        hiddenSwap(moving, hidden)
        del src[0:amt]
        dest.extend(moving)
    if amt < 0: # Pulls cards from the bottom
        moving = src[amt:]
        hiddenSwap(moving, hidden)
        del src[amt:]
        dest.extend(moving)


def move_to_ace(amt, src, dest):
    working = allCards.Cards[src[-1]]
    if working['suit'] == dest['suit']:
        if working['value'] == (allCards.Cards[dest['contents'][-1]]['value']) + 1:
            move(amt, src, dest)

## use info from the link
## https://stackoverflow.com/questions/15210148/get-parents-keys-from-nested-dictionary
## to figure out how to identify the dict or whatever













def hiddenSwap(moving, hidden):
    if hidden == False:
        for card in moving:
            if allCards.Cards[card]['hidden'] == 1:
                allCards.Cards[card]['hidden'] = 0
    if hidden == True:
        for card in moving:
            if allCards.Cards[card]['hidden'] == 0:
                allCards.Cards[card]['hidden'] = 1



deck = []
deck = shuffle(deck)
