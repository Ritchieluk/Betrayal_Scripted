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
            self.playerDist.append(dict)

    def getNextAction(self, newBoard, playerNum, playerAction):
    """
    Given the board state and active player's next action, determine
        the intervention taken, if any
    """
        self.board = newBoard
        dist = self.buildDistribution(playerNum)
    
    def buildDistribution(self, playerNum):
    """
    Using that player's history, calculate a distribution across
        available actions using evaluation functions.
    """

    def giveItem(self):
    """
    Give the player an item room or return false if no such room exists
    """
        for room in self.board.roomStack:
            if room["type"] == "item":
                if room not in self.board.revealedRooms:
                    return room
        return False

    def giveEmptyRoom(self):
    """
    Give the player an empty room or return false if no such room exists
    """
        for room in self.board.roomStack:
            if room["type"] == "undefined":
                if room not in self.board.revealedRooms:
                    return room
        return False

    def giveOmenRoom(self):
    """
    Give the player an omen room or return false if no such room exists
    """
        for room in self.board.roomStack:
            if room["type"] == "omen":
                if room not in self.board.revealedRooms:
                    return room
        return False


    def giveStatModifier(self):
    """
    Give the player a stat modifier room, or event if none exist, or return false
    """
        statRooms = ["Larder", "Gynmasium", "Library", "Chapel"]
        for room in self.board.roomStack:
            if room in statRooms:
                if room not in self.board.revealedRooms:
                    return room
        return False

    def giveTraitor(self):
    """
    Calculate a omen/tile combination to return
    """
        hauntCombinations = {"Girl": ["Abandoned Room", "Catacombs", "Gymnasium", "Junk Room"], 
            "Spirit Board": ["Balcony", "Furnace Room", "Kitchen", "Master Bedroom", "Charred Room", "Gallery", "Servant's Quarters"],
            "Dog": ["Balcony", "Dining Room", "Master Bedroom", "Servant's Quarters"],
            "Madman": ["Catacombs", "Furnace Room", "Gallery", "Master Bedroom"],
            "Mask": ["Pentagram Chamber"],
            "Medallion": ["Pentagram Chamber"],
            "Skull": ["Pentagram Chamber", "Balcony", "Charred Room", "Gymnasium", "Master Bedroom"],
            "Ring": ["Catacombs", "Gallery", "Gymnasium", "Kitchen"],
            "Book": ["Charred Room", "Furnace Room", "Junk Room"]}
        for omen in hauntCombinations.keys():
            for room in hauntCombinations[omen]:
                if omen not in self.board and room not in self.board.revealedRooms:
                    return (omen, room)
        return False


"""
- Item Count
- Rooms explored
- Omens Encountered
- Stats modified
- Wants traitor/does not want traitor   
"""