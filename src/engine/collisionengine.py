from src.collisions.collisionfactory          import CollisionFactory
from src.entities.AnimatedEntities.logentity  import LogEntity
from src.entities.AnimatedEntities.carentity  import CarEntity
from src.entities.StaticEntities.hazardentity import HazardEntity
import sys, pygame

class CollisionEngine(object):

  def __init__(self):
    #self.collisionEntities  = pygame.sprite.Group()
    self.collisionEntities = []

  def setControlledEntity(self, entity):
    self.controlledEntity = entity

  def addCollisionEntity(self, entity):
    self.collisionEntities.append(entity)

  def setPlayerLifeCounter(self, playerLifeCounter):
    self.playerLifeCounter  = playerLifeCounter
   
  def checkForAndHandleCollisions(self):
    
    listOfCollisionEntities = self.checkForCollisions()

    if len(listOfCollisionEntities) > 0:

      collisionFactory    = CollisionFactory()

      for entity in listOfCollisionEntities:
        if isinstance(entity, CarEntity):
          carCollisionHandler = collisionFactory.createCarCollision(self.controlledEntity)
          carCollisionHandler.handleCollision()
          #self.playerLifeCounter.remove()
          #self.playerLifeCounter.Text.setText(self.playerLifeCounter.Lives)
          break

        elif isinstance(entity, LogEntity):
          logCollidedWith     = entity
          logCollisionHandler = collisionFactory.createLogCollision(logCollidedWith, self.controlledEntity)
          logCollisionHandler.handleCollision()
          break
        
        elif isinstance(entity, HazardEntity):
          hazardZoneCollisionHandler = collisionFactory.createHazardZoneCollision(self.controlledEntity)
          hazardZoneCollisionHandler.handleCollision()          
          break

  def checkForCollisions(self):
    #listCollision = pygame.sprite.spritecollide(self.controlledEntity, self.collisionEntities, False)
    for collisionEntity in self.collisionEntities:
      if pygame.sprite.collide_rect(self.controlledEntity, collisionEntity) == True:
        return [collisionEntity] 
    return [] 
    
