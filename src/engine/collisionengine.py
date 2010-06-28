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
   
  def checkForCollision(self):
    listCollision = pygame.sprite.spritecollide(self.controlledEntity, self.collisionEntities, False)
    
    if listCollision == []:
      self.collisionList.append(listCollision)
      return False

    return True

