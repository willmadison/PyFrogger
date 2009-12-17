from src.entities.baseentity import BaseEntity
import pygame

class TruckEntity(BaseEntity):

  def __init__(self, coordinates=[0,0]):

    # Convert to a recognizable system of notation
    self.dimensions = {
      'width'   : 80,
      'height'  : 25
    }

    # Convert to a recognizable system of notation
    self.coordinates = {
      'x' : coordinates[0],
      'y' : coordinates[1]
    }

    # Define this entities surface
    self.surfEntity = pygame.Surface((self.Dimensions['width'], self.Dimensions['height'])).convert()
    self.setColorKey((255, 0, 0))
    self.draw()


  def setGameScreen(self, gameScreen):
    self.surfGameDisplay = gameScreen

  def setController(self, myController):
    self.myController = myController

  def respond(self, eventFired):
    self.myController.respond(eventFired)

  def setColorKey(self, color=(255,255,255)):
    """ Create a color key to make transparent """
    self.Surface.fill(color)
    self.Surface.set_colorkey(color)

  def draw(self):
    """ Create the graphic for the truck entity (r, g, b) (x, y, width, height) """

    # Tuple representing the base color of the truck
    tupTruckColor = (255, 255, 255)

    # Main Truck Body
    pygame.draw.rect(self.Surface, tupTruckColor, (0,  7, 80, 11))
    pygame.draw.rect(self.Surface, tupTruckColor, (28, 5, 52, 15))
    pygame.draw.rect(self.Surface, tupTruckColor, (8,  5, 10, 15))
    
    # Set images for each direction the truck can face, that way we don't have to rotate the image
    # manually every time
    self.arrFacingDirectionImages = {
      'UP'   : pygame.transform.rotate(self.Surface,  -90),
      'DOWN' : pygame.transform.rotate(self.Surface,   90),
      'RIGHT': pygame.transform.rotate(self.Surface, -180),
      'LEFT' : pygame.transform.rotate(self.Surface,    0)
    }

  def update(self):
    """ Update the coordinates for this entity """
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
  
  from src.controllers.frogcontroller import FrogController
  from src.core.validationframework   import ValidationFramework
  
  Validation = ValidationFramework()

  # Draw entities ... do stuff that needs to be rendered to the Main Display
  entTruck = TruckEntity([0, 0])
  truckControl = FrogController(entTruck)
  entTruck.setController(truckControl)
  entTruck.setGameScreen(Validation.Surface) 

  Validation.addToRunQueue(entTruck.update)
  
  while Validation.running == True:
    for event in Validation.getEvents():
      Validation.run()
      entTruck.respond(event)    

  Validation.quit()
