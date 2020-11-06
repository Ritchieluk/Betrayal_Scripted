import json, random, os.path

class Board():
    boardState = {"upper": [], "ground": [], "basement": []}
    playerLocations = [] # Array of tuples (floor, (x,y)) indexed by player number representing their location.
    revealedRooms = {} # Room names mapped to types
    roomStack = {} # Room names mapped to types
    roomLocations = {} # Map of names to coordinate tuples


    def __init__(self, numPlayers):
        for floor in boardState.keys():
            for i in range(20):
                temp = []
                for j in range(20):
                    temp.append("")
                boardState[floor].append(temp)
        self.boardState["upper"][10][10] = "Upper"
        self.roomLocations["Upper"] = ("upper", (10,10))
        self.boardState["ground"][10][10] = "Entrance"
        self.roomLocations["Entrance"] = ("ground", (10,10))
        self.boardState["ground"][10][11] = "Foyer"
        self.roomLocations["Foyer"] = ("ground", (10,11))
        self.boardState["basement"][10][10] = "Basement"
        self.roomLocations["Basement"] = ("basement", (10,10))

        for i in range(numPlayers):
            self.playerLocations[0] = ("ground", (10,10))
        self.initializeTileStack()
        
    

    def initializeTileStack(self):
        """
        load in all the rooms from a json file, then shuffle them
        """
        with open('assets/tiles.json', 'r') as outfile:
            ids = json.load(outfile)
            print(ids)
            for room in ids:
                self.roomStack.push(room["name"], room["type"])
        print(self.roomStack)


    def getActions(self, playerNum):
        """ 
        Given a player's location, return current available
        actions for them to take, always including no-op
        """
        moves = []
        location = playerLocations[playerNum]
        floor = location.first()
        coordinates = location.second()
        if(coordinates.first()<20):
            moves.append(0)
        if(coordinates.first()>0):
            moves.append(2)
        if(coordinates.second()<20):
            moves.append(1)
        if(coordinates.second()>0):
            moves.append(3)
        return moves

        
    def addTile(self, location):
        """
        Given a tile, add the newTile into the tree of tiles and the
        array of existing tiles based on where the player decided to put it
        """
        # Take a random tile from the stack
        tileName = random.choice(self.roomStack.keys()) 
        # Move it into the revealed rooms dict
        self.revealedRooms[tileName] = self.roomStack[tileName]
        del roomStack[tileName]
        # set its new location
        self.roomLocations[tileName] = (location.second().first(), location.second().second())
        self.boardState[location.first()][location.second().first()][location.second.second()] = tileName
        return self.revealedRooms[tileName]



    def movePlayer(self, playerNum, direction):
        # Check if move can be made
        type = "undefined"
        if (self.isLegalPlayerMovement(playerNum, direction)):
            # Move the player
            if direction == 0:
                self.playerLocations[playerNum].second().second() += 1
            elif direction == 1:
                self.playerLocations[playerNum].second().first() += 1
            elif direction == 2:
                self.playerLocations[playerNum].second().second() -= 1
            elif direction == 3:
                self.playerLocations[playerNum].second().first() -= 1
            # Check if there is already a room tile there
            if(self.boardState[location.first()][location.second().first()][location.second().second()] == ""):
                # Add the tile
                location = self.playerLocations[playerNum]
                type = self.addTile(location)
                return type
        else:
            print("ERROR ---- Unexpected movement detected ---- ")
        return type
        

    def isLegalPlayerMovement(self, player, direction):
        if direction == 0:
            if playerLocations[playerNum].second().second() + 1 <= 20:
                return True
        elif direction == 1:
            if playerLocations[playerNum].second().first() + 1 <= 20:
                return True
        elif direction == 2:
            if playerLocations[playerNum].second().second() - 1 >= 0:
                return True
        elif direction == 3:
            if playerLocations[playerNum].second().first() - 1 >= 0:
                return True
        return False

    def isLegalTileAssignment(self, player, direction):
        return True

    
