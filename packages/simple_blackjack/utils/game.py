import random
from packages.simple_blackjack.utils import card

player_hand = {
    "score": 0,
    "cards": []
}

computer_hand = {
    "score": 0,
    "cards": []
}

deck = []

lower_value = 1

def init_game():
    global deck
    global lower_value
    if len(deck) < 30:
        deck = card.generate_deck(lower_value)
    
    

def player_start():
    global computer_hand
    global player_hand
    
    for val in range(0, 2):
        add_card_to_hand(draft_a_card(), player_hand)
        
    add_card_to_hand(draft_a_card(), computer_hand)
    


def exceeded(score: int): 
    return score > 21


def game_ai():
    global computer_hand
    computer_score = computer_hand["score"]
    if computer_score < player_hand["score"]:
        if not exceeded(computer_score + lower_value):
            #draft a card
            card = handle_ace_ai(draft_a_card())

    

def draft_a_card():
    return random.choice(deck)

def handle_ace_ai(card: dict):
    #TODO: use a design pattern like builder or factory instead of if
    if card["value"] == 0:
        if not exceeded(computer_hand["score"] + 11):
            card["value"] = 11
        else:
            card["value"] = 1
    add_card_to_hand(card, computer_hand)
            
def add_card_to_hand(card: dict, hand:dict):
    hand["cards"].append(card)
    hand["score"] += card["value"]



    
        