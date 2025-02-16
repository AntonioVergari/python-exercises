from os import system
import auction

end_auction = False
while not end_auction:
    print("Welcome to this auction")
    name = input("write you name: ")
    #TODO: check for input validations
    bid = float(input("write you bid: "))
    auction.insert_auctioner(name, bid)
    is_valid_input = False
    while not is_valid_input:
        other_participant = input("there are other participant? write yes or no").lower()
        if other_participant == "yes" or other_participant == "y":
            is_valid_input = True
            system('clear')
            #win
            system('cls')
            
        elif other_participant == "no" or other_participant == "n":
            is_valid_input = True
            end_auction = True
        else:
            print('I don\'t understand, please answer the following question')
            
print(f"the winner is: {auction.get_auction_winner()}")