'''
Created on June 28, 2009

@author: William Madison
'''

from src.collisions.carcollision import CarCollision
#from src.collisions.logcollision import LogCollision


class CollisionFactory(object):

  def __init__(self):
    pass

  def createCarCollision(self, entFrog):
    carCollision = CarCollision(entFrog)
    return carCollision

  #def createLogCollision(self, entLog, entFrog):
    #logCollision = CarCollision(entLog, entFrog)
    #return logCollision
