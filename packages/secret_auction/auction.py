auctioneers = {}

highest_bidder = None

def insert_auctioner(name: str, bid: float):
    '''
    Adds a bidder to the auction with their bid amount.
    
    Args:
    name (str): The name of the bidder.
    bid (float): The bid amount.
    '''
    global highest_bidder
    auctioneers[name] = bid
    
    if highest_bidder is not None:
        highest_auctioner_bid = auctioneers[highest_bidder]
        if bid > highest_auctioner_bid:
            highest_bidder = name
    else:
        highest_bidder = name
        

def get_auction_winner():
    '''
    Adds a bidder to the auction with their bid amount.
    
    Returns:
    dict: A dictionary with the highest bidder's name as the key and their bid amount as the value
    '''
    return {highest_bidder: auctioneers[highest_bidder]}