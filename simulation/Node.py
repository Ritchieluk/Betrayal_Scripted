import numpy as np
import sys
import copy
import time
import random
import argparse
######################################################
EXPLORATION_PARAMETER = 2**.5
class Node:
    type = 1
    children = []
    # given a move that creates it and its parent we can find the rest of the data we need
    def __init__(self, currentGameState, moveOfOrigin=None, nodeParent=None):
        self.move = moveOfOrigin # This is a move object
        self.parent = nodeParent # This is a Node object
        self.type = nodeParent.getType() ^ 1 if nodeParent is not None else 1# 1 for Max Node, 0 for Min Node, we do this operation because every child will have the opposite
        self.q = [0,0] # [wins, visits]
        self.state = copy.deepcopy(currentGameState)
        self.children = []
        
    def backProp(self, newResult):
        if self.type is 1:
            self.q[0] += newResult
            self.q[1] += 1
        elif self.type is 0:
            self.q[1] += 1
            potentialAdjustment = (self.q[0]+newResult)/self.q[1]
            count = 0
            for child in self.children:
                if child.getQ() < potentialAdjustment:
                    break
                else:
                    count+=1
            if count is len(self.children):
                self.q[0]+=newResult
            
        
        if self.parent is not None:
            self.parent.backProp(newResult)


    def getUCT(self, timeStep):
        uct = self.q[0]/self.q[1] + EXPLORATION_PARAMETER * (np.log(timeStep)/self.q[1])**.5
        return uct  
    
    def appendChild(self, childNode):
        self.children.append(childNode)
    
    def getMove(self):
        return self.move

    def getChildren(self):
        return self.children
    
    def getGameState(self):
        return self.state

    def getType(self):
        return self.type

    def getQ(self):
        return self.q[0]/self.q[1]
    
    def getQArray(self):
        return self.q

    def print(self):
        print("move",self.move)
        print("state",self.state)
        print("Num Moves: ", self.state.getMoves())
        print("children: ", self.children)
        print("q: ",self.q)

    def printChildren(self):
        newArray = []
        for child in self.children:
            newArray.append(child.getQArray())
        print(newArray)