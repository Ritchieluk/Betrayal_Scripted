from BetrayalGame import BetrayalGame
from RandomAgent import RandomAgent

agents = []

for i in range(4):
    agents.append(RandomAgent(i))


game = BetrayalGame(agents)
game.playGame()