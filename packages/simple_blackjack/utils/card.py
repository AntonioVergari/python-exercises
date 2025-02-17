
seeds = ["Heart", "Diamonds", "Club", "Spade"]


def generate_deck(lower_card: int):
    deck = []
    for seed in seeds:
        for level in range(lower_card, 11):
            deck.append({
                "name": f"{level} of {seed}",
                "value": level
            })
        #specials
        deck.append({
            "name": f"Jack of {seed}",
            "value": 10
        })
        
        deck.append({
            "name": f"Queen of {seed}",
            "value": 10
        })
                
        deck.append({
            "name": f"King of {seed}",
            "value": 10
        })
        
        deck.append({
            "name": f"Ace of {seed}",
            "value": 0
        })
    return deck
        
        
def is_lower_card_valid(lower_card: int):
    return lower_card >= 1 and lower_card <= 10


