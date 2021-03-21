from RandomAgent import RandomAgent
import random

class PlayerAgent(RandomAgent):
    """
    Inherits the RandomAgent class, modifies its takeAction function
        and includes logic to more intelligently select actions.
    """

    evaluationFunction = defaultEvaluation

    def __init__(self, playerNumber, type):
        super().__init__(self, playerNumber)
        if type == "Explorer":
            self.evaluationFunction = self.explorationEvaluation
        elif type == "Omen":
            self.evaluationFunction = self.omenEvaluation
        elif type == "Haunt":
            self.evaluationFunction = self.hauntEvaluation
        elif type == "Stats":
            self.evaluationFunction = self.statsEvaluation
        elif type == "Collector":
            self.evaluationFunction = self.itemsEvaluation

    """
    Function defaultEvaluation(self, boardState)
    Returns 0 for each action, meaning each action is
       equally as valuable
    """
    def defaultEvaluation(self, boardState):
        actions = []
        for action in boardState.getActions(self.playerNum):
            actions.append(0)
        return actions


    """
    Function explorationEvaluation(self, boardState):
    Returns 1 for each action resulting in visiting an unexplored room
        and 0 for the rest.
    """
    def explorationEvaluation(self, boardState):
        actions = []
        for action in boardState.getActions(self.playerNum):
            resultingRoomName, resultingRoomType = boardState.getRoom(self.playerNum, action)
            if resultingRoomName is "none":
                actions.append(1)
            else:
                actions.append(0)
        return actions

    """
    Function omenEvaluation(self, boardState):
    Returns 1 if the action results in the player ending in an unexplored room
        with an Omen card.
    """
    def omenEvaluation(self, boardState):
        actions = []
        for action in boardState.getActions(self.playerNum):
            resultingRoomName, resultingRoomType = boardState.getRoom(self.playerNum, action)
            if resultingRoomName is "none":
                actions.append(1 + self.omensDiscovered)
            else:
                actions.append(self.omensDiscovered)
        return actions

    """
    Function hauntEvaluation(self, boardState):
    Returns -1 if the action results in the player ending in an unexplored room
        with an Omen card, varied by how many existing omens there are.
    """
    def hauntEvaluation(self, boardState):
        # Count the number of current Omens
        count = 0
        for roomType in boardState.revealedRooms.values():
            if roomType == "omen":
                count += 1
        actions = []
        for action in boardState.getActions(self.playerNum):
            resultingRoomName, resultingRoomType = boardState.getRoom(self.playerNum, action)

            if resultingRoomName == "none":
                actions.append(-1 * self.simulateHauntRoll(count) + .5)
            else:
                actions.append(0)
        return actions

    """
    def statsEvaluation(self, boardState):
    Returns 1 for each state that results in an increase of statistics
        tracks which stat spaces its already visited
    """
    def statsEvaluation(self, boardState):
        actions = []
        for action in boardState.getActions(self.playerNum):
            # Check that that action moves the player into a stats
            #   room that hasn't already been visited
            resultingRoomName, resultingRoomType = boardState.getRoom(self.playerNum, action)
            if resultingRoomName is not False and resultingRoomName is not "none":
                if resultingRoomName in self.hasVisited.keys():
                    if not self.hasVisited[resultingRoomName]:
                        actions.append(2)
                    else:
                        actions.append(-1)
                else:
                    actions.append(0)
            if resultingRoomName is "none":
                actions.append(1)
        return actions
            
    """
    def itemsEvaluation(self, boardState):
    Returns X for each state that results in an increase of items, where X
        is the number of items increased.
    """
    def itemsEvaluation(self, boardState):
        actions = []
        for action in boardState.getActions(self.playerNum):
            resultingRoomName, resultingRoomType = boardState.getRoom(self.playerNum, action)

            if resultingRoomName is not False and resultingRoomName is not "none":
                if resultingRoomName is "Vault" and not self.hasVisited["Vault"]:
                    actions.append(5)
                else:
                    actions.append(-1)
            elif resultingRoomName is "none":
                actions.append(1)
            else:
                actions.append(0)
        return actions


    """
    Function simulateHauntRoll(self, numOmens):
    Given the number of omens, this function a percentage out of 100 attempts 
        that the haunt was rolled
    """
    def simulateHauntRoll(self, numOmens):
        
        for j in range(100):
            hauntCount = 0
            hauntRoll = 0
            for i in range(6):
                hauntRoll += random.choice([0,1,2])
            if hauntRoll > numOmens:
                hauntCount += 1
        return hauntCount / 100
