# Pseudo for solitaire logic



if dest in self.acegroups:
    ## Checks that the card can go to the ace group
    if card.suit == acegroup[-1].suit:
        if card.value == (acegroup[-1].value + 1) or 2:
            move the card
else:
    ## Checks that the card can legally move to that column
    if not card.suit == column[-1].suit and column[-1].hidden == 0:
        if card.value == (column[-1].value - 1):
            move the card(s)
        elif:
            card.value == 13 and column == []: # If it's a king and the space is empty
                move the card
        elif:
            hidden == True:
                move the card
    else:
        print('illegal move')

