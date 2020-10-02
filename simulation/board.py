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
        
    def addTile(self):
        
    def flipTile(self):

    def movePlayer(self):

    def isLegalPlayerMovement(self, player, direction):

    def isLegalTileAssignment(self, player, direction):

    
