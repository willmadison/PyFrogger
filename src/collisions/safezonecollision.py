''' Created on June 29, 2009

@author: William Madison '''

from src.collisions.basecollision import BaseCollision
from src.entities.entityfactory   import EntityFactory

class SafeZoneCollision(BaseCollision):

  def __init__(self, entSafeZone, entFrog, playerLifeCounter, gameEngine): 
    self.safeZoneCollidedWith = entSafeZone 
    self.frogCollidedWith     = entFrog 
    self.gameEngine           = gameEngine
    self.playerLifeCounter    = playerLifeCounter 

  def handleCollision(self): 
    '''
      This is the function responsible for providing the 
      means of handling a collision of between a SafeZone and a Frog.
    '''

    defaultEntityFactory = EntityFactory(self.gameEngine.DisplayEngine)

    if self.safeZoneCollidedWith.IsOccupied :
      self.PlayerLifeCounter.remove()
      self.PlayerLifeCounter.Text.setText(self.playerLifeCounter.Lives)
      self.FrogCollidedWith.Controller.resetFrogToStartingPosition()

    else :
      self.safeZoneCollidedWith.markOccupied()
      defaultEntityFactory = EntityFactory(self.gameEngine.engDisplay)

    self.gameEngine.safeFrogs.append(self.frogCollidedWith)

    # Unhook the controller from the Frog that landed safely.
    self.frogCollidedWith.setController(None)
    entNewFrog = defaultEntityFactory.buildFrog() 
    entNewFrog.draw()
    self.gameEngine.DisplayEngine.addUserControlledLayer(entNewFrog)
    self.gameEngine.CollisionEngine.setControlledEntity(entNewFrog)

  @property
  def FrogCollidedWith(self):
    return self.frogCollidedWith

  @property
  def PlayerLifeCounter(self):
    return self.playerLifeCounter
