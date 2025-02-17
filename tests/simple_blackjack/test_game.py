from packages.simple_blackjack.utils import game

def test_exceeded_true():
    result = game.exceeded(22)
    
    assert result == True

def text_exceeded_false():
    result_21 = game.exceeded(21)
    result_2 = game.exceeded(2)
    
    assert result_21 == False
    assert result_2 == False
    
    
def test_draft_card():
    game.init_game()
    card = game.draft_a_card()
    assert card["value"] != None
    assert card != None
    
def test_add_card():
    game.init_game()
    
    player = game.player_hand
    card = game.draft_a_card()
    
    game.add_card_to_hand(card, player)
    assert player["score"] == card["value"]
    assert len(player["cards"]) == 1