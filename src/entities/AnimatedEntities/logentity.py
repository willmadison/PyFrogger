'''
Created on Feb 9, 2010

@author: William Madison
'''
from src.entities.baseentity import BaseEntity
import pygame

class LogEntity(BaseEntity):
  '''
  This class is the object that represents
  the various logs that are on screen for the player
  to use to reach the safe zone and score points in the game.
  '''
  
  # Define a couple of constants to represent the orientation for how the
  # log will move across the screen.
  
  LEFT_TO_RIGHT = 1
  RIGHT_TO_LEFT = -1

  def __init__(self, coordinates=[0,0], speed=1, orientation=LEFT_TO_RIGHT):
    '''
    Constructor
    '''
    # Wrap this object in a Pygame Dirty Sprite Object
    pygame.sprite.DirtySprite.__init__(self)
    
    # Set the entities speed in pps
    self.speed = speed
    
    # Set the orientation of the Log (i.e. which direction it will go across the screen
    
    self.orientation = orientation
     
    # Convert to a recognizable system of notation
    self.dimensions = {
      'width'   : 100,
      'height'  : 25
    }

    # Convert to a recognizable system of notation
    self.coordinates = {
      'x' : coordinates[0],
      'y' : coordinates[1]
    }

    # Define this entities surface
    self.surfEntity = pygame.Surface((self.Dimensions['width'], self.Dimensions['height'])).convert()
    self.rect = self.surfEntity.get_rect(left=self.coordinates['x'], top=self.coordinates['y'])
    self.setColorKey()
    self.draw()

  def setGameScreen(self, engDisplay):
    self.engDisplay = engDisplay

  def setController(self, myController):
    self.myController = myController

  def respond(self, eventFired):
    """ Event Handler """
    return None

  def animate(self):
    """ Animation Handler """
    return self.myController.animate()

  def setColorKey(self, color=(255,255,255)):
    """ Create a color key to make transparent """
    self.Surface.fill(color)
    self.Surface.set_colorkey(color)

  def draw(self):
    """ Create the graphic for the car entity (r, g, b) (x, y, width, height) """

    logLocationAndSize = (0, 0, self.Dimensions['width'], self.Dimensions['height'])
    
    # Tuple representing the base color of the car
    tupLogColor   = (131, 48, 8)
    tupBlueColor  = (29, 41, 90) #@UnusedVariable

    # Log Background
    pygame.draw.rect(self.Surface, tupLogColor, logLocationAndSize)
    
  def update(self):
    """ Update the coordinates for this entity """
    self.rect.move_ip(self.Coordinates['x'], self.Coordinates['y'])
    self.rect.top = self.Coordinates['y']
    self.rect.left = self.Coordinates['x']
    self.GameSurface.blit(self.Surface, (self.Coordinates['x'], self.Coordinates['y']))

  def setDimensions(self, width, height):
    self.Dimensions['width'] = width
    self.Dimensions['height'] = height
  
  @property
  def Dimensions(self):
    return self.dimensions

  @property
  def Coordinates(self):
    return self.coordinates

  @property
  def Surface(self):
    return self.surfEntity

  @property
  def DisplayEngine(self):
    return self.engDisplay

  @property
  def GameSurface(self):
    return self.engDisplay.Surface

  @property
  def image(self):
    """
      These are used by pygame and are necessary in order for the parent object (DirtySprite)
    """
    return self.Surface
  
  if __name__ == "__main__":
  

    from src.entities.AnimatedEntities.logentity import LogEntity 
    from src.controllers.animated.logcontroller  import LogController
    from src.core.validationframework            import ValidationFramework
    
    Validation = ValidationFramework()
  
    # Draw entities ... do stuff that needs to be rendered to the Main Display
    entLog = LogEntity([0, 0])
    logController = LogController(entLog)
    entLog.setController(logController)
    entLog.setGameScreen(Validation.Surface) 
  
    Validation.addToRunQueue(entLog.update)
    
    while Validation.running == True:
      for event in Validation.getEvents():
        Validation.run()
        entLog.respond(event)    
  
    Validation.quit()     
        
