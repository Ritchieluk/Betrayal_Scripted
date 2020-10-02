class Board():
    boardState = {"upper": [], "ground": [], "basement": []}
    playerLocations = {}

    def __init__(self, numPlayers):
        for floor in boardState.keys():
            for i in range(20):
                temp = []
                for j in range(20):
                    temp.append("")
                boardState[floor].append(temp)
        boardState["upper"][10][10] = "Upper"
        boardState["ground"][10][10] = "Entrance"
        boardState["ground"][10][11] = "Foyer"
        boardState["basement"][10][10] = "Basement"

        for i in range(numPlayers):
            playerLocations[0] = ("ground", (10,10))
        
    

    def initializeTileStack(self):
        """
        load in all the rooms from a json file, then shuffle them
        """

    def getActions(self, playerNum):
        """ 
        Given a player's location, return current available
        actions for them to take, always including no-op
        """
        
    def addTile(self, startingTile, newTile, direction):
        """
        Given a tile, add the newTile into the tree of tiles and the
        array of existing tiles based on where the player decided to put it
        """

    def flipTile(self):
        return rooms.pop()

    def movePlayer(self, playerNum, newTile):
        

    def isLegalPlayerMovement(self, player, direction):
        return True

    def isLegalTileAssignment(self, player, direction):
        return True

    
