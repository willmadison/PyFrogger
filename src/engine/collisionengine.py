from src.collisions.collisionfactory          import CollisionFactory
from src.entities.AnimatedEntities.logentity  import LogEntity
from src.entities.AnimatedEntities.carentity  import CarEntity
import sys, pygame

class CollisionEngine(object):

  def __init__(self):
    self.collisionEntities  = pygame.sprite.Group()
    self.hazardZones        = []
    self.collisionList      = []

  def setControlledEntity(self, entity):
    self.controlledEntity = entity

  def addCollisionEntity(self, entity):
    self.collisionEntities.add(entity)

  def setPlayerLifeCounter(self, playerLifeCounter):
    self.playerLifeCounter  = playerLifeCounter
   
  def checkForAndHandleCollisions(self):
    listOfCollisionEntities = self.checkForCollisions()

    if len(listOfCollisionEntities) > 0:
      for entity in listOfCollisionEntities:
        if isinstance(entity, CarEntity):
          collisionFactory    = CollisionFactory()
          carCollisionHandler = collisionFactory.createCarCollision(self.controlledEntity)
          carCollisionHandler.handleCollision()
          self.playerLifeCounter.remove()
          break

        elif isinstance(entity, LogEntity):
          break

  def checkForCollisions(self):
    listCollision = pygame.sprite.spritecollide(self.controlledEntity, self.collisionEntities, False)
    
    if listCollision == []:
      self.collisionList.append(listCollision)

    return True
