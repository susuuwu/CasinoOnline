#seed the needed functions
import random
import time

#define a class "card" that will hold a name, suit and value
class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

#create a list "deck" to store our cards in
deck = []

#use lists to make defining the cards much easier
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
faces = ["Jack", "Queen", "King"]
numbers = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

#define all 52 cards in the deck
for a in range(4):
    #Numbered Cards
    for b in range(9):
        deck.append( Card(numbers[b], suits[a], b+2))
    #Face Cards
    for b in range(3):
        deck.append( Card(faces[b], suits[a], 10))
    #The Ace
    deck.append( Card("Ace", suits[a], 1))

#show that our list "deck" holds a valid deck
#for i in range(52):
    #print(deck[i].name, "of", deck[i].suit, "value", deck[i].value)

#create a reference list to represent our deck proper
refdeck = []
ref = 0 #cardsdrawn
for i in range(52):
    refdeck.append(i)

#prove that it holds a valid list
#for i in range(52):
    #print(refdeck[i])

#define user defined functions to shuffle and draw from the deck
def shuffle(): #randomizes the refdeck
    #clear all user hands first!
    for a in range(52):
        b = random.randrange(0,51)
        temp = refdeck[a]
        refdeck[a] = refdeck[b]
        refdeck[b] = temp

#prove the function works
#shuffle()
#for i in range(52):
    #print(refdeck[i])

def draw():
    global ref
    ref += 1
    return refdeck[ref-1]

#use an example hand to show how the draw function works
#hand =  []
#shuffle()

#for i in range(3):
    #temp = draw()
    #hand.append(temp)

#for i in range(len(hand)):
    #print(deck[hand[i]].name, "of", deck[hand[i]].suit, "value", deck[hand[i]].value)

#define the variables and lists needed for the game
phand = []  #playerhand
dhand = [] #dealerhand
money = 1000 #give the player $1000
pvalue = 0 #player hand value
dvalue = 0 #dealer hand value
pmove = 'h'


#define the functions needed for the blackjack game
def betvalidator(top,bet):
    if bet > 0 and bet <= top:
        return bet
    else:
        print("Invalid Value, please enter again")
        bet = int(input())
        validator(top,bet)

def tfvalidator(tf):
    if tf == 'y':
        return
    elif tf == 'n':
        pass
    else:
        print("Invalid Input, try again")
        tf = input()
        tf = tfvalidator(tf)
      
#main game loop
while True:
    #reset for the next game
    pvalue = 0
    dvalue = 0
    phand.clear()
    dhand.clear()
    #clear player and dealer hands
    shuffle()
    
    #ask for the bet
    print("How much do you want to bet? You have $", money)
    bet = int(input())
    bet = betvalidator(money,bet)
    
    #deal 2 to the dealer
    for i in range(2):
        temp = draw()
        dhand.append(temp)
        dvalue = dvalue + deck[dhand[i]].value 
        
    #deal 2 to the player
    for i in range(2):
        temp = draw()
        phand.append(temp)
        pvalue = pvalue + deck[phand[i]].value 

    #display the current standings
    #print("Dealer Hand:", deck[dhand[0]].name, "of", deck[dhand[0]].suit, "and an Unknown Card. Value ???")
    print("Dealer Hand:", deck[dhand[0]].name, "of", deck[dhand[0]].suit, deck[dhand[1]].name, "of", deck[dhand[1]].suit, "Value", dvalue)
    print("Player Hand:", deck[phand[0]].name, "of", deck[phand[0]].suit, deck[phand[1]].name, "of", deck[phand[1]].suit, "Value", pvalue)
    
    #player can hit and stand to their liking until a bust
    while pvalue < 21 and pmove == 'h':
        print("Hit or Stand? h/s (case sensitive)")
        pmove = input()
        if pmove == 'h':
            #draw a new card for the player
            temp = draw()
            phand.append(temp)
            pvalue = pvalue + deck[phand[i]].value
            #display the new player hand
            print("Player Hand:", end=' ')
            for i in range(len(phand)):
                print(deck[phand[i]].name, "of", deck[phand[i]].suit, end=' ')
            print("Value", pvalue)
            if pvalue > 21:
                print("Bust!")
                money = money - bet #deal with the money, the program does not recognize bet as in integer however
                break
            else:
                pass 
        elif pmove == 's':
            pass
        else:
            print("Invalid Input, try again")
            pmove = 'h'
        
    #dealer does their move
    if pvalue <= 21:
        while dvalue < 17:
            temp = draw()
            dhand.append(temp)
            dvalue = dvalue + deck[dhand[len(dhand)-1]].value
            print("Dealer Hand:", end=' ')
            for i in range(len(dhand)):
                print(deck[dhand[i]].name, "of", deck[dhand[i]].suit, end=' ')
            print("Value", dvalue)
            if dvalue > 21:
                print("Dealer Busts!")
                money = money + bet #does not think bet is an integer    
    elif pvalue > 21:
        pass
    
    #compare the winner and do the schmoney transfer
    if dvalue > 21 or pvalue > 21:
        pass
    else:
        if dvalue >= pvalue: 
            print("Dealer Wins")
            money = money - bet
        elif pvalue > dvalue:
            print("Player Wins")
            money = money + bet

    #ask for continuance or boot a broke player
    if money == 0:
        print("Come back when you have money")
        break
    elif money > 0:
        print("Would you like to continue (y/n) (case sensitive)")
        tf = input()
        if tf == 'n':
            quit()
        elif tf == 'y':
            pass
        
