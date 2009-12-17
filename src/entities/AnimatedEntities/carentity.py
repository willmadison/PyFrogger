from src.entities.baseentity import BaseEntity
import pygame

class CarEntity(BaseEntity):

  def __init__(self, coordinates=[0,0]):

    # Convert to a recognizable system of notation
    self.dimensions = {
      'width'   : 40,
      'height'  : 25
    }

    # Convert to a recognizable system of notation
    self.coordinates = {
      'x' : coordinates[0],
      'y' : coordinates[1]
    }

    # Define this entities surface
    self.surfEntity = pygame.Surface((self.Dimensions['width'], self.Dimensions['height'])).convert()
    self.setColorKey()
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
    """ Create the graphic for the car entity (r, g, b) (x, y, width, height) """

    # Tuple representing the base color of the car
    tupCarBodyColor = (150, 20, 255)
    tupBlackColor   = (0, 0, 0)

    # Main Car Body
    pygame.draw.rect(self.Surface, tupCarBodyColor, (0,  8, 38, 8))
    pygame.draw.rect(self.Surface, tupBlackColor,   (5, 11, 22, 2))

    # Car Wheels
    pygame.draw.rect(self.Surface, tupCarBodyColor, (0, 4,  10, 3))
    pygame.draw.rect(self.Surface, tupCarBodyColor, (20, 4, 10, 3))

    pygame.draw.rect(self.Surface, tupCarBodyColor, (0,  17, 10, 3))
    pygame.draw.rect(self.Surface, tupCarBodyColor, (20, 17, 10, 3))
    
    # Set images for each direction the car can face, that way we don't have to rotate the image
    # manually every time
    self.arrFacingDirectionImages = {
      'DOWN'   : pygame.transform.rotate(self.Surface,  -90),
      'UP' : pygame.transform.rotate(self.Surface,   90),
      'LEFT': pygame.transform.rotate(self.Surface, -180),
      'RIGHT' : pygame.transform.rotate(self.Surface,    0)
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
  entCar = CarEntity([0, 0])
  carControl = FrogController(entCar)
  entCar.setController(carControl)
  entCar.setGameScreen(Validation.Surface) 

  Validation.addToRunQueue(entCar.update)
  
  while Validation.running == True:
    for event in Validation.getEvents():
      Validation.run()
      entCar.respond(event)    

  Validation.quit()
