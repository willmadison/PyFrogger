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
    self.myController = myController

  def respond(self, eventFired):
    self.myController.respond(eventFired)

  def draw(self):
    pygame.draw.rect(self.Surface, (100, 146, 40), (0, 0, 5, 5))
    pygame.draw.rect(self.Surface, (100, 146, 40), (3, 6, 5, 5))
    pygame.draw.rect(self.Surface, (100, 146, 40), (6, 0, 5, 5))

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
  
  from src.controllers.frogcontroller import FrogController

  from src.core.validationframework import ValidationFramework
  
  from entities.StaticEntities.staticentity import StaticEntity
  
  Validation = ValidationFramework()
  
  #Todo: Encapsulate and clean up the creation of ALL of the static entities
  #and perhaps all entities in general, (i.e. Factory Pattern)

  # Draw entities ... do stuff that needs to be rendered to the Main Display
  
  # Create Static Entities (i.e. visual aspects of the Game Screen)
  
  # Colors:
  
  COLOR_FROG_GREEN       = (100, 146, 40)
  COLOR_BACKGROUND_GREEN = (79, 116, 32)
  COLOR_NAVY_BLUE        = (29, 41, 90)
  COLOR_PALE_YELLOW      = (255, 244, 86)
  COLOR_BLACK            = (0, 0, 0)
  
  POINT_ORIGIN     = [0, 0]
  WATER_LOCATION   = [18, 35]
  WATER_DIMENSIONS = [464, 160]
  
  entWater = StaticEntity(WATER_LOCATION, WATER_DIMENSIONS, COLOR_NAVY_BLUE)
  entWater.setGameScreen(Validation.Surface)
  
  
  POINT_UPPERSWLOCATION = [18, 170]
  SIDEWALK_DIMENSIONS   = [464, 25]
  
  entUpperSideWalk = StaticEntity(POINT_UPPERSWLOCATION, SIDEWALK_DIMENSIONS, COLOR_PALE_YELLOW)
  entUpperSideWalk.setGameScreen(Validation.Surface)
  
  POINT_LOWERSWLOCATION = [18, 350]
  
  entLowerSideWalk = StaticEntity(POINT_LOWERSWLOCATION, SIDEWALK_DIMENSIONS, COLOR_PALE_YELLOW)
  entLowerSideWalk.setGameScreen(Validation.Surface)  
  
  STREET_LOCATION   = [18, 150]
  STREET_DIMENSIONS = [464, 225]
  
  entStreet = StaticEntity(STREET_LOCATION, STREET_DIMENSIONS, COLOR_BLACK)
  entStreet.setGameScreen(Validation.Surface)  
  
  BACKGROUND_LOCATION   = [0, 30]
  BACKGROUND_DIMENSIONS = [500, 400]
  
  entBackGround = StaticEntity(BACKGROUND_LOCATION, BACKGROUND_DIMENSIONS, COLOR_BACKGROUND_GREEN)
  entBackGround.setGameScreen(Validation.Surface)
  
  DIVIDERA_LOCATION  = [80,30]
  DIVIDER_DIMENSIONS = [70, 30]
  
  entSafeZoneDividerA = StaticEntity(DIVIDERA_LOCATION, DIVIDER_DIMENSIONS, COLOR_BACKGROUND_GREEN)
  entSafeZoneDividerA.setGameScreen(Validation.Surface)
  
  DIVIDERB_LOCATION  = [220,30]
  
  entSafeZoneDividerB = StaticEntity(DIVIDERB_LOCATION, DIVIDER_DIMENSIONS, COLOR_BACKGROUND_GREEN)
  entSafeZoneDividerB.setGameScreen(Validation.Surface)
  
  DIVIDERC_LOCATION  = [360,30]
  
  entSafeZoneDividerC = StaticEntity(DIVIDERC_LOCATION, DIVIDER_DIMENSIONS, COLOR_BACKGROUND_GREEN)
  entSafeZoneDividerC.setGameScreen(Validation.Surface)
    
  # Create Controlled Entities (i.e. those Entities that will be controllable via User Input)
    
  entFrog = FrogEntity([240, 370])
  frogControl = FrogController(entFrog)
  entFrog.setController(frogControl)
  entFrog.setGameScreen(Validation.Surface) 
  entFrog.draw()

  Validation.addToRunQueue(entBackGround.update)
  Validation.addToRunQueue(entStreet.update)
  Validation.addToRunQueue(entWater.update)
  Validation.addToRunQueue(entSafeZoneDividerA.update)
  Validation.addToRunQueue(entSafeZoneDividerB.update)
  Validation.addToRunQueue(entSafeZoneDividerC.update)
  Validation.addToRunQueue(entUpperSideWalk.update)
  Validation.addToRunQueue(entLowerSideWalk.update)
  Validation.addToRunQueue(entFrog.update)
  
  while Validation.running == True:
    for event in Validation.getEvents():
      Validation.run()
      entFrog.respond(event)    
    
  Validation.quit()
