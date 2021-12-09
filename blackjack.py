#seed the needed functions
import random
import time

#seed randomness in the function
random.seed(time.time())

#define user defined functions
def shuffle():
    for a in range(52):
        b = random.randrange(0,51)
        temp = refarray[a]
        refarray[a] = refarray[b]
        refarray[b] = temp

def validator(bottom, top, number):
    if number > bottom and number < top:
        pass
    else:
        print("Invalid Input, please try again")
        number = input()
        validator(bottom, top, number)

def takebet():
    try:
        bet = int(input())
        validator(0, money, bet)
    except:
        print("Enter a number please")
        takebet()

def display():
    row1 = "Dealer Hand =>"
    row2 = "Player Hand =>"
    print("Dealer Hand => ", end='')
    for a in range(len(dealerhand)):
        print(deck[dealerhand[a]].name, "of", deck[dealerhand[a]].suit, " ", end='')
    print("Value:", dealervalue)
    print("Player Hand => ", end='')
    for a in range(len(playerhand)):
        print(deck[playerhand[a]].name, "of", deck[playerhand[a]].suit, " ", end='')
    print("Value:", playervalue)
  
    
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
    for b in range(8):
        deck.append( Card(numbers[b], suits[a], b+2))
    #Face Cards
    for b in range(3):
        deck.append( Card(faces[b], suits[a], 10))
    #The Ace
    deck.append( Card("Ace", suits[a], 1))


#create a reference array of numbers 0 to 52 to determine the draw order of cards
refarray = []
for a in range(52):
    refarray.append(a)

#game initialization
money = 1000 #How much the player has
cardsdrawn = 0
shuffle()

#main game loop
while True:

    #ask for bet
    print("How much do you want to bet on this round? You have $", money)
    takebet()
        
    #draw 2 for dealer
    dealerhand = []
    dealervalue = 0
    for a in range(2):
            dealerhand.append(refarray[cardsdrawn])
            cardsdrawn += 1
            dealervalue = dealervalue + deck[dealerhand[a]].value
              
    #draw 2 for player
    playerhand = []
    playervalue = 0
    for a in range(2):
            playerhand.append(refarray[cardsdrawn])
            cardsdrawn += 1
            playervalue = playervalue + deck[playerhand[a]].value

    #display the current standings
    display()

    #player turn
    
    #dealer turn

    #end of round

    break
  

