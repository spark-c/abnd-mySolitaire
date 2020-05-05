# Solitaire board

import Deck, allCards

class Board(object):

    def __init__(self):
        self.a = []
        self.b = []
        self.c = []
        self.d = []
        self.e = []
        self.f = []
        self.g = []
##        self.heart = []
##        self.diamond = []
##        self.spade = []
##        self.club = []
        self.empty = ''

        self.columns = [self.a,
                        self.b,
                        self.c,
                        self.d,
                        self.e,
                        self.f,
                        self.g]
        self.acegroups = {
            'heartgroup':{
                'contents':[],
                'suit':'hearts'},
            'diamondgroup':{
                'contents':[],
                'suit':'diamonds'},
            'clubgroup':{
                'contents':[],
                'suit':'clubs'},
            'spadegroup':{
                'contents':[],
                'suit':'spades'}}

        
        i = 0
        for column in self.columns: # Deals the base/hidden cards
            Deck.move(i, Deck.deck, column, True)
            i += 1

        for column in self.columns: # Deals the face-up cards
            Deck.move(1, Deck.deck, column)
        
        self.stack = Deck.deck # The remainder of the deck = the stack


    def draw(self):
        # use string.center(len, optional-fill-char) to structure columns       
        columnsLen = [len(self.a), #finds how many cards are in each row
                      len(self.b),
                      len(self.c),
                      len(self.d),
                      len(self.e),
                      len(self.f),
                      len(self.g)]
        rowsNeeded = max(columnsLen) #determines how many rows need to print
        
        #PRINT BOARD
        print('|' + self.stack[2].center(15) + '|') #bottom card of stack

        print('|' +
              self.stack[1].center(15) +
              '|' +
              self.empty.center(15) + #space btwn stack and aces
              '|', end = '')
        for group in self.acegroups:
            try: # In case the ace group is empty
                print(self.acegroups[group]['contents'][-1].center(15) + '|', end = '')
            except:
                print(self.empty.center(15) + '|', end = '')
        print(self.empty.center(15))

        print('|' + self.stack[0].center(15) + '|\n') #top card of stack

        print('\n', end = '') #empty row before main area

        for row in range(0, rowsNeeded + 1): #do this however many rows we need
            print('|', end = '') #first pipe of row
            for column in self.columns: #for each column in this row
                try: # We need a try/except in case the column does not have a card at that index
                    if allCards.Cards[column[row]]['hidden'] == True: # If the card is 'hidden', print xxx in its place
                        print('xxx'.center(15) + '|', end = '')
                    else:
                        print(column[row].center(15) + '|', end = '') # Otherwise, print the card
                except:
                    print(self.empty.center(15) + '|', end = '') # fills with empty space
                    continue
            print('\n', end = '')
                  
        




        
        
