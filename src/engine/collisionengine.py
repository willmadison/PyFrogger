from src.collisions.collisionfactory            import CollisionFactory
from src.entities.AnimatedEntities.logentity    import LogEntity
from src.entities.AnimatedEntities.carentity    import CarEntity
from src.entities.StaticEntities.hazardentity   import HazardEntity
from src.entities.StaticEntities.safezoneentity import SafeZoneEntity
import sys, pygame

class CollisionEngine(object):

  def __init__(self, gameEngine):
    self.collisionEntities = []
    self.gameEngine        = gameEngine

  def setControlledEntity(self, entity):
    self.controlledEntity = entity

  def addCollisionEntity(self, entity):
    self.collisionEntities.append(entity)

  def setPlayerLifeCounter(self, playerLifeCounter):
    self.playerLifeCounter  = playerLifeCounter
   
  def checkForAndHandleCollisions(self):
    
    entityCollidedWith  = self.checkForCollisions()

    collisionFactory    = CollisionFactory()

    if isinstance(entityCollidedWith, CarEntity):
      carCollisionHandler = collisionFactory.createCarCollision(self.controlledEntity, self.playerLifeCounter)
      carCollisionHandler.handleCollision()

    elif isinstance(entityCollidedWith, LogEntity):
      logCollidedWith     = entityCollidedWith
      logCollisionHandler = collisionFactory.createLogCollision(logCollidedWith, self.controlledEntity)
      logCollisionHandler.handleCollision()
    
    elif isinstance(entityCollidedWith, HazardEntity):
      hazardZoneCollisionHandler = collisionFactory.createHazardZoneCollision(self.controlledEntity, self.playerLifeCounter)
      hazardZoneCollisionHandler.handleCollision()          

    elif isinstance(entityCollidedWith, SafeZoneEntity):
      safeZoneCollisionHandler = collisionFactory.createSafeZoneCollision(self.controlledEntity, self.gameEngine)
      safeZoneCollisionHandler.handleCollision()          

  def checkForCollisions(self):
    for collisionEntity in self.collisionEntities:
      if pygame.sprite.collide_rect(self.controlledEntity, collisionEntity) == True:
        return collisionEntity 
    return None 
    
