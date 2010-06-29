'''
Created on Dec 21, 2009

@author: William Madison
'''

from src.entities.ControlledEntities.frogentity  import FrogEntity
from src.entities.GameControlEntities.lifeentity import LifeEntity
from src.entities.StaticEntities.staticentity    import StaticEntity
from src.controllers.frogcontroller              import FrogController
from src.core.colors                             import * #@UnusedWildImport


class EntityFactory(object):
  
  def __init__(self, myDisplayEngine):
    '''
      Set the factory's internal Display Engine Reference.
    '''
    
    self.displayEngine   = myDisplayEngine
    self.surfGameDisplay = myDisplayEngine.Surface

  def buildLifeCounter(self):

    entLife = LifeEntity()

    return entLife
 
  def buildFrog(self):
    '''
      Construct the Controllable Frog Entity.
    '''
    
    # Create a new frog, initially located at the bottom middle
    # of the playing screen.
    
    entFrog = FrogEntity([240, 370])
    
    # Set its controller.
    
    frogControl = FrogController(entFrog)
    entFrog.setController(frogControl)
    
    # Set its reference to the game screen
    
    entFrog.setGameScreen(self.Surface)
    
    # Return the newly created frog.
    
    return entFrog
  
  def buildBackground(self):
    '''
      Construct the Game Screen Background.
    '''
    
    # Create an empty list to contain the static entities
    # that comprise the background of the screen.
    
    entBackgroundEntities = []
    
    # Create the basic green background.
    
    entBackGround = self.__createBackground()
    
    # Create the Street.
    
    entStreet = self.__createStreet()
    
    # Create the Water.
    
    entWater = self.__createWater()
    
    # Create the Safezone Dividers
    
    DIVIDERA_LOCATION  = [80,30]
    entSafeZoneDividerA = self.__createDivider(DIVIDERA_LOCATION)
    
    DIVIDERB_LOCATION  = [210,30]
    DIVIDERB_DIMENSIONS = [90, 30]
    entSafeZoneDividerB = self.__createDivider(DIVIDERB_LOCATION, DIVIDERB_DIMENSIONS)
    
    DIVIDERC_LOCATION  = [360,30]
    entSafeZoneDividerC = self.__createDivider(DIVIDERC_LOCATION) 
    
    # Create the upper and lower sidewalks.
    
    POINT_UPPERSWLOCATION = [18, 160]
    entUpperSideWalk = self.__createSidewalk(POINT_UPPERSWLOCATION)
    
    POINT_LOWERSWLOCATION = [18, 340]
    entLowerSideWalk = self.__createSidewalk(POINT_LOWERSWLOCATION)

    # Add the scoreboard

    SCOREBOARD_LOCATION = [0, 0]
    entScoreBoard  = self.__createScoreboard(SCOREBOARD_LOCATION)
    
    # Add each of the static background entities to the list of background entities
    # in the order in which they need to be realized on screen.
    
    entBackgroundEntities.append(entBackGround) 
    entBackgroundEntities.append(entStreet)
    entBackgroundEntities.append(entWater)
    entBackgroundEntities.append(entSafeZoneDividerA)
    entBackgroundEntities.append(entSafeZoneDividerB)
    entBackgroundEntities.append(entSafeZoneDividerC)
    entBackgroundEntities.append(entUpperSideWalk)
    entBackgroundEntities.append(entLowerSideWalk)
    entBackgroundEntities.append(entScoreBoard)
    
    # Return the list of background entities to the caller.   
    
    return entBackgroundEntities
  
  def __createBackground(self):
    BACKGROUND_LOCATION   = [0, 30]
    BACKGROUND_DIMENSIONS = [500, 400]
    entBackGround         = StaticEntity(BACKGROUND_LOCATION, BACKGROUND_DIMENSIONS, COLOR_BACKGROUND_GREEN)
    entBackGround.setGameScreen(self.Surface)
    return entBackGround

  def __createStreet(self):
    STREET_LOCATION   = [18, 150]
    STREET_DIMENSIONS = [464, 210]
    entStreet = StaticEntity(STREET_LOCATION, STREET_DIMENSIONS, COLOR_BLACK)
    entStreet.setGameScreen(self.Surface)
    return entStreet

  def __createWater(self):
    WATER_LOCATION   = [18, 35]
    WATER_DIMENSIONS = [464, 150]
    entWater = StaticEntity(WATER_LOCATION, WATER_DIMENSIONS, COLOR_NAVY_BLUE)
    entWater.setGameScreen(self.Surface)
    return entWater

  def __createDivider(self, location, dimensions=[70, 30]):
    entSafeZoneDivider = StaticEntity(location, dimensions, COLOR_BACKGROUND_GREEN)
    entSafeZoneDivider.setGameScreen(self.Surface)
    return entSafeZoneDivider

  def __createSidewalk(self, location):
    SIDEWALK_DIMENSIONS = [464, 25]
    entSidewalk = StaticEntity(location, SIDEWALK_DIMENSIONS, COLOR_PALE_YELLOW)
    entSidewalk.setGameScreen(self.Surface)
    return entSidewalk    

  def __createScoreboard(self, location):
    SCOREBOARD_DIMENSIONS = [500, 30]
    entSidewalk = StaticEntity(location, SCOREBOARD_DIMENSIONS, COLOR_WHITE)
    entSidewalk.setGameScreen(self.Surface)
    return entSidewalk    
  
  @property
  def Surface(self):
    return self.surfGameDisplay
  
  
    
