'''
Created on June 28, 2009

@author: William Madison
'''

from src.collisions.carcollision        import CarCollision
from src.collisions.logcollision        import LogCollision
from src.collisions.hazardzonecollision import HazardZoneCollision
from src.collisions.safezonecollision   import SafeZoneCollision

class CollisionFactory(object):

  def __init__(self):
    pass

  def createCarCollision(self, entFrog, playerLifeCounter):
    carCollision = CarCollision(entFrog, playerLifeCounter)
    return carCollision

  def createLogCollision(self, entLog, entFrog):
    logCollision = LogCollision(entLog, entFrog)
    return logCollision
  
  def createHazardZoneCollision(self, entFrog, playerLifeCounter):
    hazardZoneCollision = HazardZoneCollision(entFrog, playerLifeCounter)
    return hazardZoneCollision

  def createSafeZoneCollision(self, entSafeZone, entFrog, playerLifeCounter, gameEngine):
    safeZoneCollision = SafeZoneCollision(entSafeZone, entFrog, playerLifeCounter, gameEngine)
    return safeZoneCollision
