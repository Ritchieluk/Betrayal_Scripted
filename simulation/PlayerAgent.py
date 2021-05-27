from RandomAgent import RandomAgent
from BetrayalGame import BetrayalGame
from Node import Node
import random
import copy

class PlayerAgent(RandomAgent):
    """
    Inherits the RandomAgent class, modifies its takeAction function
        and includes logic to more intelligently select actions.
    """


    def __init__(self, playerNumber, type):
        super().__init__(playerNumber)
        self.time = 0
        self.name = type
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
        else:
            self.evaluationFunction = self.defaultEvaluation

    def takeAction(self, boardState):
        board = copy.deepcopy(boardState)
        root = Node(board)
        pMoves = board.getActions(self.playerNum)
        print(pMoves)
        count = 0

        while(count < 50):
            if count < len(pMoves):
                nextState = copy.deepcopy(board)
                nextAction = pMoves[count]
                nextState.movePlayer(self.playerNum, nextAction, True)
                nextNode = Node(nextState, nextAction, root)
                root.appendChild(nextNode)
                result = self.simulate(nextNode.getGameState())
                nextNode.backProp(result)
            else:
                nextLeaf = self.select(root)
                nextState = copy.deepcopy(nextLeaf.getGameState())
                if len(nextState.getActions(self.playerNum)) > 0:
                    nextAction = random.choice(nextState.getActions(self.playerNum))
                    nextState.movePlayer(self.playerNum, nextAction, True)
                    nextNode = Node(nextState, nextAction, nextLeaf)
                    nextLeaf.appendChild(nextNode)
                    result = self.simulate(nextNode.getGameState())
                    nextNode.backProp(result)

            count += 1
            self.time += 1

        if len(pMoves) > 0:
            bestMove = random.choice(pMoves)
        maxValue = -1

        for child in root.getChildren():
            if child.getQ() > maxValue and child.getMove() in pMoves:
                maxValue = child.getQ()
                bestMove = child.getMove()
        return bestMove

    def select(self, root):
        """
        navigates from root to leaf
        uses UCB to choose best node
        returns node
        """
        if len(root.getChildren()) is 0:
            return root
        currNode = root
        nodes = []
        nodes.append(root)
        uct = -1
        bestNode = root
        while(len(nodes) > 0):
            currNode = nodes.pop()
            if currNode.getUCT(self.time)>uct and len(currNode.getGameState().getActions(self.playerNum)) > 0:
                uct = currNode.getUCT(self.time)
                bestNode = currNode
            if len(currNode.getChildren())>0:
                for child in currNode.getChildren():
                    nodes.append(child)
                    
        return bestNode

    def simulate(self, state):
        """ 
        Given the current gameState of the passed in node,
        simulate till end
        Return which tuple (1,1) if we won, (0,1) if we lost
        """
        agents = [RandomAgent(0)]

        game = BetrayalGame(agents, True) 
        state = copy.deepcopy(state)
        game.board = state
        game.playGame()
        

        return self.evaluationFunction(game.board)

    """
    Function defaultEvaluation(self, boardState)
    Returns 0 for each action, meaning each action is
       equally as valuable
    """
    def defaultEvaluation(self, boardState):
        return 1


    """
    Function explorationEvaluation(self, boardState):
    Returns 1 for each action resulting in visiting an unexplored room
        and 0 for the rest.
    """
    def explorationEvaluation(self, boardState):
        """
        actions = []
        for action in boardState.getActions(self.playerNum):
            resultingRoomName, resultingRoomType = boardState.getRoom(self.playerNum, action)
            if resultingRoomName is "none":
                actions.append(1)
            else:
                actions.append(0)
        return actions
        """
        return boardState.revealerCounts[self.playerNum]

    """
    Function omenEvaluation(self, boardState):
    Returns 1 if the action results in the player ending in an unexplored room
        with an Omen card.
    """
    def omenEvaluation(self, boardState):
        """
        actions = []
        for action in boardState.getActions(self.playerNum):
            resultingRoomName, resultingRoomType = boardState.getRoom(self.playerNum, action)
            if resultingRoomName is "none":
                actions.append(1 + self.omensDiscovered)
            else:
                actions.append(self.omensDiscovered)
        return actions
        """
        return boardState.players[self.playerNum].omensDiscovered

    """
    Function hauntEvaluation(self, boardState):
    Returns -1 if the action results in the player ending in an unexplored room
        with an Omen card, varied by how many existing omens there are.
    """
    def hauntEvaluation(self, boardState):
        """
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
        return -10 if boardState.players[self.playerNum].isTraitor else 10

    """
    def statsEvaluation(self, boardState):
    Returns 1 for each state that results in an increase of statistics
        tracks which stat spaces its already visited
    """
    def statsEvaluation(self, boardState):
        """
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
        player = boardState.players[self.playerNum]
        diff = 0
        for attribute in player.attributes.keys():
            diff += player.attributes[attribute] - player.startingAttributes[attribute]
        return diff

            
    """
    def itemsEvaluation(self, boardState):
    Returns X for each state that results in an increase of items, where X
        is the number of items increased.
    """
    def itemsEvaluation(self, boardState):
        """
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
        return boardState.players[self.playerNum].itemCount


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
