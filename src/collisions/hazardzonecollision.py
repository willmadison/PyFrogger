''' 
Created on June 29, 2009

@author: William Madison 
'''

from src.collisions.basecollision import BaseCollision

class HazardZoneCollision(BaseCollision):

  def __init__(self, entFrog, playerLifeCounter): 
    self.frogCollidedWith  =  entFrog 
    self.playerLifeCounter = playerLifeCounter

  def handleCollision(self): 
    '''
      This is the function responsible for providing the 
      means of handling a collision of between a Car and a Frog.
    '''
    self.PlayerLifeCounter.remove()
    self.playerLifeCounter.Text.setText(self.playerLifeCounter.Lives)
    self.FrogCollidedWith.Controller.resetFrogToStartingPosition()

  @property
  def FrogCollidedWith(self):
    return self.frogCollidedWith

  @property
  def PlayerLifeCounter(self):
    return self.playerLifeCounter
