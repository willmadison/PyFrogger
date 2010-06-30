'''
Created on June 28, 2009

@author: William Madison
'''

from src.collisions.basecollision import BaseCollision

class LogCollision(BaseCollision):

  def __init__(self, entLog, entFrog):
    self.frogCollidedWith = entFrog
    self.logCollidedWith  = entLog

  def handleCollision(self):
    '''
      This is the function responsible for providing the 
      means of handling a collision of between a Log and a Frog.
    '''
    #Move the Frog in Tandem with the Log.

    frogsNewXCoordinate = self.FrogCollidedWith.Coordinates['x'] + self.LogCollidedWith.speed

    # Check with the Frog's Controller to be sure we're moving the frog into a valid position
    if self.FrogCollidedWith.Controller.isValidXCoordinate(frogsNewXCoordinate) :
      self.FrogCollidedWith.Coordinates['x'] = frogsNewXCoordinate

  @property
  def FrogCollidedWith(self):
    return self.frogCollidedWith

  @property
  def LogCollidedWith(self):
    return self.logCollidedWith
