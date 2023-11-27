# packages 
import random, cards

# Player cards array
player_cards = []

# Computer cards array
dealer_cards = []

# first draw
available_cards = cards.FULL_DECK

# STEP-1: Deal two cards to player and to dealer. Deal them 1-by-1
def deal_first_hand():

    card1 = random.choice(available_cards)
    card2 = random.choice(available_cards)
    card3 = random.choice(available_cards)
    card4 = random.choice(available_cards)

    player_cards.append(card1)
    player_cards.append(card3)
    dealer_cards.append(card2)
    dealer_cards.append(card4)

    available_cards.remove(card1)
    available_cards.remove(card2)
    available_cards.remove(card3)
    available_cards.remove(card4)

# STEP-2: show player cards and first crad of the dealer
def show_first_hand():

    print(f'Your cards: {player_cards}')
    print(f"Computer's first card: {dealer_cards[0]}")

# STEP-3: draw cards and show cards after first hand
def player_draw_card():
    
    draw_status = True
    
    while draw_status: 
        
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if draw == "y":
            card = random.choice(available_cards)
            available_cards.remove(card)
            player_cards.append(card)
            show_cards(player_cards)
            if check_if_bust(player_cards):
                break
        
        elif draw == "n":
            draw_status = False
            show_cards(dealer_cards)
            if check_if_bust(dealer_cards):
                break

        else:
            print("Error: Invalid Option!")
            player_draw_card()

def show_cards(card_set):
    if card_set == player_cards:
        print(f'Your cards: {card_set}')
    elif card_set == dealer_cards:
        print(f"Computer's hand: {dealer_cards}")

def check_if_bust(card_set):
    
    sum = 0

    for value in card_set:
        sum += cards.card_values[value]
    
    if sum > 21:
        print("BUST! You Lost!")
        show_cards(dealer_cards)
        return True
    
    return False

continue_playing = True
# Game
while continue_playing:

    deal_first_hand()
    show_first_hand()
    player_draw_card()

    continue_playing = False