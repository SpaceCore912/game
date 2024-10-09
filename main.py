# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [] 
for rank in ranks:
            for suit in suits:
                deck.append((rank,suit))
#print(deck)


# Shuffle the deck 
for x in range(len(deck)):
    deck[x]=deck[random.randint(1,len(deck))-1]

lendeck=len(deck)
print(lendeck)

#Split the deck into two hands
deck1=deck[:26]
deck1extra=[]
deck2=deck[26:]
deck2extra=[]
print(deck1)

def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    
    if ranks.index(p1_card[0])>ranks.index(p2_card[0]):
        return 1

    elif ranks.index(p1_card[0])<ranks.index(p2_card[0]):
        return 2
    else:
        return 0
def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    p1card=deck.pop[0]
    p2card=deck.pop[0]
    output=card_comparison(p1card,p2card)
    if output=0:
        war()
    elif output=1:
        deck1.extend([p1card,p2card])
    elif output=2:
        dock2.extend([p1card,p2card])
def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    deck
    while 

def play_game():
    """Main function to run the game."""
    # Your code here
 
# Call the main function to start the game
play_game()
    
