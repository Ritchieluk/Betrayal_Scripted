"""
Drama Manager Agent

"""
from BetrayalBoard import Board

class DramaManager():
    board = Board()
    playerDist = []

    def __init__(self, numPlayers):
        for i in range(numPlayers):
            dict = {"items": 0, "rooms": 0, "omens": 0, "traitor": True}
            playerDist.append(dict)

    def getNextAction(self, board, playerNum, playerAction):
    
    
    def buildDistribution(self, playerNum):
    """
    Using that player's history, calculate a distribution across
        available actions using evaluation functions.
    """


"""
- Item Count
- Rooms explored
- Omens Encountered
- Stats modified
- Wants traitor/does not want traitor   
"""