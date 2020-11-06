from BetrayalBoard import Board
from RandomAgent import RandomAgent

class BetrayalGame():
    players = []
    activePlayer = 0
    turnCount = 0
    tilesRevealed = 0
    omenCount = 0
    hauntRevealed = False

    def __init__(self, agents):
        self.players = agents
        self.board = Board()

    def playGame(self):
        """
        So long as the haunt hasn't begun, give each player a turn
            Allowing them to progress through the mansion
            and flip tiles and draw cards
        """
        # Primary game loop
        while self.hauntRevealed == False:
            # Each player gets a turn each round
            for player in range(len(self.players)):
                # Each player can take multiple actions on a turn
                moves = self.players[player].speed
                while moves > 0:
                    # Get the action they are going to take
                    action = self.players[player].getNextAction(self.board)
                    # This means move in one of the four cardinal directions
                    if action < 4:
                        nextTile = self.board.movePlayer(player, action)
                        if nextTile == "undefined":
                            moves -= 1
                        elif nextTile == "omen":
                            omenCount += 1
                            self.rollHaunt()
                            moves = 0
                        else:
                            moves = 0
                    else:
                        print("Misunderstood action")



    def rollHaunt(self):
        """
        Make a random roll, if less than current Omen Count, start haunt
        """
        hauntRoll = 0
        for i in range(6):
            hauntRoll += random.choice([0,1,2])
        if hauntRoll < self.omenCount:
            self.hauntRevealed = True
        return self.hauntRevealed


