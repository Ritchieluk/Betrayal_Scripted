from BetrayalBoard import Board
import random

class BetrayalGame():
    players = []
    activePlayer = 0
    turnCount = 0
    tilesRevealed = 0
    omenCount = 0
    hauntRevealed = False

    def __init__(self, agents):
        self.players = agents
        self.board = Board(len(agents))

    def playGame(self):
        """
        So long as the haunt hasn't begun, give each player a turn
            Allowing them to progress through the mansion
            and flip tiles and draw cards
        """
        # Primary game loop
        while not self.hauntRevealed:
            # Each player gets a turn each round
            for player in range(len(self.players)):
                # Each player can take multiple actions on a turn
                moves = self.players[player].getSpeed()
                attemptedVault = False
                while moves > 0 and not self.hauntRevealed:
                    # Get the action they are going to take
                    action = self.players[player].takeAction(self.board)
                    # This means move in one of the four cardinal directions

                    # Pass playerNum, gameState, and action decided to Drama Manager
                    # Return an appropriate action, if no action is taken proceed with
                    #   standard simulation

                    if action < 4:
                        rooms = self.board.revealedRooms
                        name, nextTile = self.board.movePlayer(player, action)
                        if name not in rooms:
                                self.players[player].tilesExplored += 1
                        if nextTile == "undefined":
                            moves -= 1
                        elif nextTile == "omen":
                            self.omenCount += 1
                            self.players[player].omensDiscovered += 1
                            self.rollHaunt()
                            moves = 0
                        elif nextTile == "item":
                            self.players[player].itemCount += 1
                            moves = 0
                        else:
                            moves = 0

                        # ================== Tile Specific Actions =========================
                        if name == "Gymnasium" and not self.players[player].hasVisited["Gymnasium"]:
                            self.players[player].adjustAttribute("Speed", 1)
                            self.players[player].hasVisited["Gymnasium"] = True
                        elif name == "Larder" and not self.players[player].hasVisited["Larder"]:
                            self.players[player].adjustAttribute("Might", 1)
                            self.players[player].hasVisited["Larder"] = True
                        elif name == "Chapel" and not self.players[player].hasVisited["Chapel"]:
                            self.players[player].adjustAttribute("Sanity", 1)
                            self.players[player].hasVisited["Chapel"] = True
                        elif name == "Library" and not self.players[player].hasVisited["Library"]:
                            self.players[player].adjustAttribute("Intelligence", 1)
                            self.players[player].hasVisited["Library"] = True
                        elif name == "Vault" and not self.players[player].hasVisited["Vault"] and not attemptedVault:
                            intCheck = 0
                            int = self.players[player].getIntelligence()
                            attemptedVault = True
                            for i in range(int):
                                intCheck += random.choice([0,1,2])
                            if intCheck >= 5:
                                self.players[player].hasVisted["Vault"] = True
                                self.players[player].itemCount += 2

                    else:
                        print("Misunderstood action")
                    if self.hauntRevealed:
                        self.players[player].isTraitor = True
                        break



    def rollHaunt(self):
        """
        Make a random roll, if less than current Omen Count, start haunt
        """
        hauntRoll = 0
        for i in range(6):
            hauntRoll += random.choice([0,1,2])
        print("===================================")
        print("|ROLL FOR THE HAUNT!!! SPOOooOOKYY|")
        print("===================================")
        print("| Roll Required: {}               |".format(self.omenCount))
        print("| Roll: {}                        |".format(hauntRoll))
        
        if hauntRoll < self.omenCount:
            self.hauntRevealed = True
            print("|       THE HAUNT HAS BEGUN      |")
        else:
            print("|      YOU'RE SAFE THIS TIME     |")
        print("===================================")
        return self.hauntRevealed


