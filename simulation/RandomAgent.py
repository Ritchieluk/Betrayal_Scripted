import random
class RandomAgent():
    # Dict of attributes to the index on their array of values
    attributes = {"Might": 0, "Speed": 0, "Sanity": 0, "Intelligence": 0}
    # Arrays of possible attributes
    might = [0,1,2,3,4,5,6,7,8]
    speed = [0,1,2,3,4,5,6,7,8]
    sanity = [0,1,2,3,4,5,6,7,8]
    intelligence = [0,1,2,3,4,5,6,7,8]
    playerNum = -1

    def __init__(self, playerNumber, mightScores, initialMight, speedScores, initialSpeed, 
        sanityScores, initialSanity, intelligenceScores, initialIntelligence):
        self.playerNum = playerNumber
        self.might = mightScores
        self.attributes["Might"] = initialMight
        self.speed = speedScores
        self.attributes["Speed"] = initialSpeed
        self.sanity = sanityScores
        self.attributes["Sanity"] = initialSanity
        self.intelligence = intelligenceScores
        self.attributes["Intelligence"] = initialIntelligence

    def takeAction(self, boardState):
        # TODO: Enable smarter options
        return random.choice(boardState.getActions()) 


    def takePhysicalDamage(self, amount):
        for i in range(amount):
            if self.attributes["Speed"] > self.attributes["Might"]:
                self.attributes["Speed"] -= 1
            else:
                self.attributes["Might"] -= 1
        return self.isAlive()


    def takeMentalDamage(self, amount):
        for i in range(amount):
            if self.attributes["Sanity"] > self.attributes["Intelligence"]:
                self.attributes["Sanity"] -= 1
            else:
                self.attributes["Intelligence"] -= 1
        return self.isAlive()


    def adjustAttribute(self, attribute, amount):
        self.attributes[attribute] += amount
        return self.isAlive()


    def isAlive(self):
        for attribute in self.attributes.values():
            if attribute == 0:
                return False
        return True