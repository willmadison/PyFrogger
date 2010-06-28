from src.entities.baseentity  import BaseEntity
from src.core.colors          import *
import pygame

class FrogEntity(BaseEntity):

  def __init__(self, coordinates=[0,0]):
    pygame.sprite.DirtySprite.__init__(self)

    # Convert to a recognizable system of notation
    self.dimensions = {
      'width'   : 25,
      'height'  : 25
    }

    # Define move offsets
    self.moveVerticalOffset   = 5;
    self.moveHorizontalOffset = 0;

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
    self.surfEntity.fill(COLOR_KEY)
    self.surfEntity.set_colorkey(COLOR_KEY) # Make froggie transparent
    self.rect = self.surfEntity.get_rect(left=self.coordinates['x'], top=self.coordinates['y'])

  def setGameScreen(self, gameScreen):
    self.surfGameDisplay = gameScreen

  def setController(self, myController):
    self.myController = myController

  def respond(self, eventFired):
    self.myController.respond(eventFired)

  def draw(self):
    FROG_SCALE_DIMENSIONS = (3, 3)
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((0, 5), FROG_SCALE_DIMENSIONS)) # Left Webbing of Hand

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((2, 2), FROG_SCALE_DIMENSIONS)) # Left Arm
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((2, 4), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((2, 6), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((2, 8), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((2, 10), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((4, 10), FROG_SCALE_DIMENSIONS))

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((0, 20), FROG_SCALE_DIMENSIONS)) # Left Webbing of Foot

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((2, 23), FROG_SCALE_DIMENSIONS)) # Left Foot
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((2, 21), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((2, 19), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((2, 17), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((4, 17), FROG_SCALE_DIMENSIONS))

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((22, 5), FROG_SCALE_DIMENSIONS)) # Right Webbing of Hand

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((20, 2), FROG_SCALE_DIMENSIONS)) # Right Arm
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((20, 4), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((20, 6), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((20, 8), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((20, 10), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((18, 10), FROG_SCALE_DIMENSIONS))

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((22, 20), FROG_SCALE_DIMENSIONS)) # Right Webbing of Foot

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((20, 23), FROG_SCALE_DIMENSIONS)) # Right Foot
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((20, 21), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((20, 19), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((20, 17), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((18, 17), FROG_SCALE_DIMENSIONS))

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((9, 21), FROG_SCALE_DIMENSIONS)) # Base of Body
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((12, 21), FROG_SCALE_DIMENSIONS))
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((13, 21), FROG_SCALE_DIMENSIONS))

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((8, 19), FROG_SCALE_DIMENSIONS)) # Second Layer of Body
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((11, 19), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((14, 19), FROG_SCALE_DIMENSIONS)) 

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((6, 17), FROG_SCALE_DIMENSIONS)) # Third Layer of Body
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((9, 17), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((12, 17), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((14, 17), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((16, 17), FROG_SCALE_DIMENSIONS)) 

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((6, 14), FROG_SCALE_DIMENSIONS)) # Fourth Layer of Body
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((9, 14), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((12, 14), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((14, 14), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((16, 14), FROG_SCALE_DIMENSIONS)) 

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((6, 11), FROG_SCALE_DIMENSIONS)) # Fifth Layer of Body
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((9, 11), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((12, 11), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((14, 11), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((16, 11), FROG_SCALE_DIMENSIONS)) 

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((6, 8), FROG_SCALE_DIMENSIONS)) # Sixth Layer of Body
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((9, 8), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((12, 8), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((14, 8), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((16, 8), FROG_SCALE_DIMENSIONS)) 

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((6, 5), FROG_SCALE_DIMENSIONS)) # Seventh Layer of Body
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((9, 5), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((12, 5), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((14, 5), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((16, 5), FROG_SCALE_DIMENSIONS)) 

    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((9, 3), FROG_SCALE_DIMENSIONS)) # Head
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((12, 3), FROG_SCALE_DIMENSIONS)) 
    pygame.draw.rect(self.Surface, COLOR_FROG_GREEN, ((13, 3), FROG_SCALE_DIMENSIONS)) 

    pygame.draw.rect(self.Surface, COLOR_FROG_RED, ((6, 5), FROG_SCALE_DIMENSIONS)) # Eyes
    pygame.draw.rect(self.Surface, COLOR_FROG_RED, ((16, 5), FROG_SCALE_DIMENSIONS))

  def update(self):
    self.rect.move_ip(self.Coordinates['x'], self.Coordinates['y'])
    self.rect.top   = self.Coordinates['y']
    self.rect.left  = self.Coordinates['x']
    self.GameSurface.blit(self.Surface, (self.Coordinates['x'], self.Coordinates['y']))

  def resetToStartingPosition(self):
    self.coordinates['x'] = self.startingCoordinates['x']
    self.coordinates['y'] = self.startingCoordinates['y']

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
