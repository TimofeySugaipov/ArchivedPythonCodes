import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return(f"{self.rank} of {self.suit}")

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                (self.deck).append(Card(suit,rank))
        
    def __str__(self):
        for card in self.deck:
            print(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return (self.deck).pop()
    
class Hand:

    def __init__(self):
        self.cards = []
        self.values = 0
        self.aces = 0
    def __str__(self):
        for card in self.cards:
            print(card)
    def add_card(self,card):
        (self.cards).append(card)
        self.values += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
            self.adjust_for_ace()
    def adjust_for_ace(self):
        if self.values > 21:
            self.values -=10

class Chips:

    def __init__(self,total):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
        print(f"Current Balance: {self.total}")
    def lose_bet(self):
        self.total -= self.bet
        print(f"Current Balance: {self.total}")

def take_bet():
    while True:
        try:
            n = int(input("Place your bet:"))
        except:
            print("Please enter an integer amount")
            continue
        else:
            if n > Chips.total:
                print(f"Insufficient funds\nCurrent Balance: {Chips.total}")
            else:
                 Chips.bet = n
                 print("Bet taken")
                 break

def hit(deck,hand):
    hand.add_card(deck.deal())

def hit_or_stand(deck,hand):
    global playing
    while playing:
        if hand.values > 21:
            break
        m = input("Hit(H) or Stand(S):").capitalize()
        if m == "Hit" or m == "H":
            hit(deck,hand)
            show_some(player,dealer)
        elif m == "Stand" or m == "S":
            playing = False

def show_some(player,dealer):
    print(f"\nDealer's Hand\n{dealer.cards[0]}\n?\nCurrent Value:?\n")
    print("Player's Hand\n")
    for i in player.cards:
        print(i)
    print(f"\nCurrent Value: {player.values}\n")

def show_all(player,dealer):
    print(f"\nDealer's Hand\n")
    for i in dealer.cards:
        print(i)
    print(f"\nCurrent Value: {dealer.values}\n")
    print("Player's Hand\n")
    for i in player.cards:
        print(i)
    print(f"\nCurrent Value: {player.values}\n")


def player_busts(player):
    return player.values > 21
    

def player_wins(player, dealer):
    return player.values > dealer.values

def dealer_busts(dealer):
    return dealer.values > 21
    
def dealer_wins(player, dealer):
    return dealer.values > player.values

    
def push(player, dealer):
    return player.values == dealer.values
    

Deck = Deck()
player = Hand()
dealer = Hand()
while True:
    try:
        balance = int(input("What's your balance: "))
    except:
        print("Please enter an integer balance")
    else:
        break
Chips = Chips(balance)
while True:
    print("A Game of BlackJack")
    Deck.shuffle()
    for i in range(0,4):
        card = Deck.deal()
        if i < 2:
            player.add_card(card)
        else:
            dealer.add_card(card)

    take_bet()
    
    show_some(player,dealer)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        hit_or_stand(Deck,player)

        if player_busts(player):
            Chips.lose_bet()
            print("Player bust\n")
            break

        while dealer.values < 17 or dealer.values < player.values:
            hit(Deck,dealer)
    
        show_all(player,dealer)
        if player_wins(player,dealer):
           Chips.win_bet()
           print("Player wins\n")
        elif dealer_busts(dealer):
            Chips.win_bet()
            print("Dealer bust\n")
        elif push(player,dealer):
            print("Push, bet returned\n")
        else:
            Chips.lose_bet()
            print("Dealer Wins\n")

    
    play_again = input("Would you like to play again? Yes(Y) or No(N)?").capitalize()
    if play_again == "Yes" or play_again == "Y":
        playing = True
    else:
        break
    pl,dl= len(player.cards),len(dealer.cards)
    for i in range(0,pl):
        p = (player.cards).pop()
        (Deck.deck).append(p)
    for i in range(0,dl):
        d = (dealer.cards).pop()
        (Deck.deck).append(d)
    player.values = 0
    dealer.values = 0
            
    
    






        
    
        
