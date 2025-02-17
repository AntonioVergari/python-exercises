from packages.simple_blackjack.utils import card



def test_card_gen():
    
    deck = card.generate_deck(1)
    
    assert len(deck) == 56
    

def test_card_gen_wrong():
    
    false = card.is_lower_card_valid(20)
    
    assert false == False
    
def test_card_gen_correct():
    
    true = card.is_lower_card_valid(2)
    
    assert true == True