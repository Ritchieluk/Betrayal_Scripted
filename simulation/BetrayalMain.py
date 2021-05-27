from BetrayalGame import BetrayalGame
from RandomAgent import RandomAgent
from PlayerAgent import PlayerAgent

agents = []
types = ["Explorer"]

count = 0
for type in types:
    agents.append(PlayerAgent(count, typeagent))
    count += 1


game = BetrayalGame(agents)
game.playGame()
print("game finished")