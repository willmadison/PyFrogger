from src.entities.baseentity import BaseEntity
import pygame

class FrogEntity(BaseEntity):

  def __init__(self, coordinates=[0,0]):
    pygame.sprite.DirtySprite.__init__(self)

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

    self.startingCoordinates = {
      'x' : coordinates[0],
      'y' : coordinates[1]
    }

    # Define this entities surface
    self.surfEntity = pygame.Surface((self.Dimensions['width'], self.Dimensions['height']))
    self.rect = self.surfEntity.get_rect(left=self.coordinates['x'], top=self.coordinates['y'])

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
    self.rect.move_ip(self.Coordinates['x'], self.Coordinates['y'])
    self.rect.top   = self.Coordinates['y']
    self.rect.left  = self.Coordinates['x']
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
  def CollideSurface(self):
    return self.surfCollide

  @property
  def GameSurface(self):
    return self.surfGameDisplay


if __name__ == "__main__":
  
  from src.core.validationframework         import ValidationFramework  
  from src.entities.entityfactory               import EntityFactory
  
  Validation = ValidationFramework()
  
  # Create a new EntityFactory
  
  defaultEntityFactory = EntityFactory(Validation.engDisplay)

  # Draw entities ... do stuff that needs to be rendered to the Main Display
  
  # Create Static Entities (i.e. visual aspects of the Game Screen)

  listStaticBackgroundEntities = defaultEntityFactory.buildBackground()
    
  # Create Controlled Entities (i.e. those Entities that will be controllable via User Input)
    
  entFrog = defaultEntityFactory.buildFrog()
  entFrog.draw()
  
  # Add each of the update methods of the static entites to the run queue
  
  for staticEntity in listStaticBackgroundEntities:
    Validation.addToRunQueue(staticEntity.update)

  Validation.addToRunQueue(entFrog.update)
  
  while Validation.running == True:
    for event in Validation.getEvents():
      Validation.run()
      entFrog.respond(event)    
    
  Validation.quit()
