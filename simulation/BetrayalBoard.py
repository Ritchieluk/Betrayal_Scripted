import json, random, os.path

class Board():
    boardState = {"upper": [], "ground": [], "basement": []}
    playerLocations = [] # Array of tuples (floor, (x,y)) indexed by player number representing their location.
    revealedRooms = {} # Room names mapped to types
    roomStack = {} # Room names mapped to types
    roomLocations = {} # Map of names to coordinate tuples
    haunt = False

    def __init__(self, numPlayers):
        for floor in self.boardState.keys():
            for i in range(20):
                temp = []
                for j in range(20):
                    temp.append("")
                self.boardState[floor].append(temp)
        self.boardState["upper"][10][10] = "Upper"
        self.roomLocations["Upper"] = ("upper", (10,10))
        self.boardState["ground"][10][10] = "Entrance"
        self.roomLocations["Entrance"] = ("ground", (10,10))
        self.boardState["ground"][10][11] = "Foyer"
        self.roomLocations["Foyer"] = ("ground", (10,11))
        self.boardState["basement"][10][10] = "Basement"
        self.roomLocations["Basement"] = ("basement", (10,10))

        for i in range(numPlayers):
            self.playerLocations.append(("ground", (10,10)))
        self.initializeTileStack()
        
    

    def initializeTileStack(self):
        """
        load in all the rooms from a json file, then shuffle them
        """
        with open('assets/tiles.json', 'r') as outfile:
            ids = json.load(outfile)
            for room in ids:
                self.roomStack[room["name"]] = room["type"]


    def getActions(self, playerNum):
        """ 
        Given a player's location, return current available
        actions for them to take, always including no-op
        """
        moves = []
        location = self.playerLocations[playerNum]
        floor = location[0]
        coordinates = location[1]
        if(coordinates[0]<20):
            moves.append(0)
        if(coordinates[0]>0):
            moves.append(2)
        if(coordinates[1]<20):
            moves.append(1)
        if(coordinates[1]>0):
            moves.append(3)
        return moves

        
    def addTile(self, location):
        """
        Given a tile, add the newTile into the tree of tiles and the
        array of existing tiles based on where the player decided to put it
        """
        # TODO: Change to return a tile and a card, or false if no card
        # Take a random tile from the stack
        tileName = random.choice(list(self.roomStack.keys())) 
        print("{} tile revealed!".format(tileName))
        # Move it into the revealed rooms dict
        self.revealedRooms[tileName] = self.roomStack[tileName]
        del self.roomStack[tileName]
        # set its new location
        self.roomLocations[tileName] = (location[1][0], location[1][1])
        self.boardState[location[0]][location[1][0]][location[1][1]] = tileName
        return (tileName, self.revealedRooms[tileName])



    def movePlayer(self, playerNum, direction):
        # Check if move can be made
        name = "unknown"
        type = "undefined"
        if (self.isLegalPlayerMovement(playerNum, direction)):
            # Move the player
            coordinates = self.playerLocations[playerNum][1]
            if direction == 0:
                coordinates = (coordinates[0], coordinates[1]+1)
                print("Player {} has moved Up".format(playerNum))
            elif direction == 1:
                coordinates = (coordinates[0] + 1, coordinates[1])
                print("Player {} has moved Right".format(playerNum))
            elif direction == 2:
                coordinates = (coordinates[0], coordinates[1]-1)
                print("Player {} has moved Down".format(playerNum))
            elif direction == 3:
                coordinates = (coordinates[0]-1, coordinates[1])
                print("Player {} has moved Left".format(playerNum))
            self.playerLocations[playerNum] = (self.playerLocations[playerNum][0], coordinates)
            location = self.playerLocations[playerNum]
            # Check if there is already a room tile there
            if(self.boardState[location[0]][location[1][0]][location[1][1]] == ""):
                # Add the tile
                location = self.playerLocations[playerNum]
                name, type = self.addTile(location)
                return name, type
        else:
            print("ERROR ---- Unexpected movement detected ---- ")
        return name, type
        
    def getRoom(self, player, direction):
        if self.isLegalPlayerMovement(player, direction):
            coords = self.resultingCoordinate(player, direction)
            if coords is not False:
                for room in self.revealedRooms.keys():
                    if self.revealedRooms[room] == coords:
                        return room, self.revealedRooms[room]
                return "none", "none"
            return False, False

    def isLegalPlayerMovement(self, player, direction):
        if direction == 0:
            if self.playerLocations[player][1][1] + 1 <= 20:
                return True
        elif direction == 1:
            if self.playerLocations[player][1][0] + 1 <= 20:
                return True
        elif direction == 2:
            if self.playerLocations[player][1][1] - 1 >= 0:
                return True
        elif direction == 3:
            if self.playerLocations[player][1][0] - 1 >= 0:
                return True
        return False

    def isLegalTileAssignment(self, player, direction):
        if self.isLegalPlayerMovement(player, direction):
            coords = self.resultingCoordinate(player, direction)
            if coords is not False:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                for room in self.revealedRooms.keys():
                    if self.revealedRooms[room] == coords:
                        return False
        else:
            return False
        return True

    def resultingCoordinate(self, player, direction):
        if self.isLegalPlayerMovement(self, player, direction):
            coords = self.playerLocations[player][1]
            if direction == 0:
                return (coords[0], coords[1]+1)
            elif direction == 1:
                return (coords[0] + 1, coords[1])
            elif direction == 2:
                return (coords[0], coords[1] -1 )
            elif direction == 3:
                return (coords[0] - 1, coords[1])
        return False
    
