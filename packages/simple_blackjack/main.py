from utils import game

print("Welcome to simple black jack")


end_game = False
while not end_game:
    is_player_turn = True
    is_computer_turn = True
    player_loose = False
    game.init_game()
    game.player_start()
    print(f"your hand {game.player_hand["cards"]}")
    print(f"computer hand {game.computer_hand["cards"]}")
    #TODO: refactor some methods and import game's status in game.py
    while is_player_turn and not player_loose:
        choice = input("please write pick to pick a card or stay to end your turn: ").lower()
        if choice == "pick":
            card = game.draft_a_card()
            game.add_card_to_hand(card, game.player_hand)
            print(f"you got {card["name"]}")
            print(f"now you have {game.player_hand}")
        elif choice == "stay":
            is_player_turn = False
        if game.exceeded(game.player_hand["score"]):
            player_loose = True
    while is_computer_turn and not player_loose:
        is_computer_turn = game.game_ai()
    print(f"computer hand: {game.computer_hand}")
    game.select_winner()
    #TODO: add choice for end the game
            