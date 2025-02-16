import sys
sys.path.append('packages')
from packages.secret_auction import auction

def test_winner():
    name1 = 'antonio'
    val1 = 50
    
    name2 = 'marina'
    val2 = 100
    
    auction.insert_auctioner(name1, val1)
    auction.insert_auctioner(name2, val2)
    
    
    result = auction.get_auction_winner()
    assert result[name2] == 100
    
    
def test_insert():
    name1 = 'antonio'
    val1 = 50
    
    name2 = 'marina'
    val2 = 100
    
    auction.insert_auctioner(name1, val1)
    auction.insert_auctioner(name2, val2)
    
    

    assert len(auction.auctioneers) == 2