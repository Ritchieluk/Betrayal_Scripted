import random
class RandomAgent():
    # Dict of attributes to the index on their array of values
    attributes = {"Might": 5, "Speed": 5, "Sanity": 5, "Intelligence": 5}
    # Arrays of possible attributes
    might = [0,1,2,3,4,5,6,7,8]
    speed = [0,1,2,3,4,5,6,7,8]
    sanity = [0,1,2,3,4,5,6,7,8]
    intelligence = [0,1,2,3,4,5,6,7,8]
    playerNum = -1
    hasVisited = {"Larder": False, "Library": False, "Gymnasium": False, "Chapel": False, "Vault": False}
    itemCount = 0
    omensDiscovered = 0

    def __init__(self, playerNumber):
        self.playerNum = playerNumber

    def changeScores(self, mightScores, initialMight, speedScores, initialSpeed, 
        sanityScores, initialSanity, intelligenceScores, initialIntelligence):
        self.might = mightScores
        self.attributes["Might"] = initialMight
        self.speed = speedScores
        self.attributes["Speed"] = initialSpeed
        self.sanity = sanityScores
        self.attributes["Sanity"] = initialSanity
        self.intelligence = intelligenceScores
        self.attributes["Intelligence"] = initialIntelligence

    def takeAction(self, boardState):
        return random.choice(boardState.getActions(self.playerNum)) 


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

    def getMight(self):
        return self.might[self.attributes["Might"]]
    
    def getSpeed(self):
        return self.speed[self.attributes["Speed"]]

    def getSanity(self):
        return self.sanity[self.attributes["Sanity"]]
        
    def getIntelligence(self):
        return self.intelligence[self.attributes["Intelligence"]]