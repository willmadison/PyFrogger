import sys, pygame

class CollisionEngine(object):

  def __init__(self):
    self.collisionEntities  = pygame.sprite.Group()
    self.hazardZones        = []

  def setControlledEntity(self, entity):
    self.controlledEntity = entity

  def addCollisionEntity(self, entity):
    self.collisionEntities.add(entity)
   
  def checkForCollision(self):
    listCollision = pygame.sprite.spritecollide(self.controlledEntity, self.collisionEntities, False)
    
    if listCollision == []:
      return False
    return listCollision

