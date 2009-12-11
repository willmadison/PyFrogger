from src.entities.baseentity import BaseEntity
import pygame

class FrogEntity(BaseEntity):

  def __init__(self, coordinates=[0,0]):

    # Convert to a recognizable system of notation
    self.dimensions = {
      'width'   : 25,
      'height'  : 25
    }

    # Convert to a recognizable system of notation
    self.coordinates = {
      'x' : coordinates[0],
      'y' : coordinates[1]
    }

    # Define this entities surface
    self.surfEntity = pygame.Surface((self.Dimensions['width'], self.Dimensions['height']))

  def setGameScreen(self, gameScreen):
    self.surfGameDisplay = gameScreen

  def setController(self, myController):
    return

  def respond(self, eventFired):
    return

  def draw(self):
    pygame.draw.rect(self.Surface, (0, 255, 0), (0, 0, 5, 5))
    pygame.draw.rect(self.Surface, (0, 255, 0), (3, 6, 5, 5))
    pygame.draw.rect(self.Surface, (0, 255, 0), (6, 0, 5, 5))

  def update(self):
    self.GameSurface.blit(self.Surface, (self.Coordinates['x'], self.Coordinates['y']))

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
  def GameSurface(self):
    return self.surfGameDisplay


if __name__ == "__main__":

  try:
    from src.core.validationframework import ValidationFramework

    Validation = ValidationFramework()

    # Draw entities ... do stuff that needs to be rendered to the Main Display
    entFrog = FrogEntity([25, 25])
    entFrog.setGameScreen(Validation.Surface) 
    entFrog.draw()

    Validation.addToRunQueue(entFrog.update)
    
    while Validation.running == True:
      Validation.run()

    Validation.quit()
    
  except StandardError as Error:
    print Error
