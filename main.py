# Import necessary modules
import random
import time
start_time=time.time()
# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [] 
for rank in ranks:
            for suit in suits:
                deck.append((rank,suit))



random.shuffle(deck)
print(deck)

time.sleep(3)

#Split the deck into two hands
deck1=deck[:26]
deck2=deck[26:]
deck1extra=[]
deck2extra=[]



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
def play_round():
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    
    i=0
    while deck1 != [] and deck2  != []:
        p1card=deck1[0]
        p2card=deck2[0]
        
        output=card_comparison(p1card,p2card)
        
        if output==0:
            
            
            
            list=[]
            war(list,deck1,deck2)
        

        if output==1:
            deck1extra.extend([p1card,p2card])
            deck1.pop(0)    
            deck2.pop(0)
        if output==2:
            deck2extra.extend([p1card,p2card])
            deck1.pop(0)    
            deck2.pop(0)
        print(len(deck1))
        print(len(deck2))
        
        
        i+=1
        print(str(i)+"times")
    print("hello")
    time.sleep(0.3)
    return deck1extra, deck2extra

def war(list,deck1,deck2):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    global deck1extra, deck2extra
    list1=list
    i=0
    print("\nPEACE")
    
    while i<5:
        list1.append(deck1[0])
        list1.append(deck2[0])
        deck1.pop(0)
        deck2.pop(0)

        if deck1==[]:
            if deck1extra==[]:
                 print('the end')
                 return False
            deck1=deck1extra
            random.shuffle(deck1)
        
        if deck2==[]:
            if deck2extra==[]:
                 print('the end')
                 return False
            deck2=deck2extra
            random.shuffle(deck2)
        i+=1
    output=card_comparison(list1[-6],list1[-1]) 
    if output==0:
        war(list1,deck1,deck2)
    if output==1:
        deck1extra.extend(list1)
        
    if output==2:
        deck2extra.extend(list1)
        
    
    
    return False

    
#main game
i=0

while (deck1 != [] and deck2 != []):
        
        play_round()
        print("\nround "+ str(i+1))
        print("\n\n")
        print("deck1: "+ str(deck1))
        print("\ncards taken from player 2: " + str(deck1extra))
        print("\n\n")
        print("deck2: "+ str(deck2))
        print("\ncards taken from player 1: " + str(deck2extra))
        print("\n\n")
        if  len(deck1)==0:
            deck1=deck1extra
            random.shuffle(deck1)
            deck1extra=[]
        if   len(deck2)==0:
            deck2=deck2extra
            random.shuffle(deck2) 
            deck2extra=[]   
        print("deck1 shuffled: "+ str(deck1))
        print("\ndeck2 shuffled: "+ str(deck2))
        time.sleep(0.3)
        i+=1
if deck1==[]:
     print("\n\nplayer1 lost")
if deck2==[]:
     print("\n\nplayer2 lost")


end_time=time.time()
print(str(i+1) +" rounds were played")
print(end_time-start_time)