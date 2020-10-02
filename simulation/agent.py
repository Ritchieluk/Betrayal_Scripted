class Agent():
    # Dict of attributes to the index on their array of values
    attributes = {"Might": 0, "Speed": 0, "Sanity": 0, "Intelligence": 0}
    # Arrays of possible attributes
    might = [0,1,2,3,4,5,6,7,8]
    speed = [0,1,2,3,4,5,6,7,8]
    sanity = [0,1,2,3,4,5,6,7,8]
    intelligence = [0,1,2,3,4,5,6,7,8]

    def __init__(self, mightScores, initialMight, speedScores, initialSpeed, 
        sanityScores, initialSanity, intelligenceScores, initialIntelligence):
        might = mightScores
        attributes["Might"] = initialMight
        speed = speedScores
        attributes["Speed"] = initialSpeed
        sanity = sanityScores
        attributes["Sanity"] = initialSanity
        intelligence = intelligenceScores
        attributes["Intelligence"] = initialIntelligence

    def takeAction(self, boardState):



    def takePhysicalDamage(self, amount):



    def takeMentalDamage(self, amount):



    def adjustAttribute(self, attribute, amount):
        attributes[attribute] += amount
        return self.isAlive()


    def isAlive():
        for attribute in attributes.values():
            if attribute == 0:
                return False
        return True