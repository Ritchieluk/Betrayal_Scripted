class Tile():
    tileId = -1
    neighbors = [-1, -1, -1, -1]

    def __init__(self, id, adjacents):
        self.tileId = id
        self.neighbors = adjacents

    def getRoomAction(self):
        return False

    def endTurnAction(self):
        return False
    
    def getUnexploredNeighbors(self):
        for n in self.neighbors:
            if self.neighbors[n] == -1:
                return n
            