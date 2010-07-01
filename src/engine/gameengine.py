from src.core.iniparser                      import IniParser
from src.engine.displayengine                import DisplayEngine
from src.engine.collisionengine              import CollisionEngine

from src.controllers.animated.carcontroller  import CarController
from src.controllers.gamecontroller          import GameController

from src.entities.entityfactory                 import EntityFactory
from src.entities.AnimatedEntities.logentity    import LogEntity
from src.entities.AnimatedEntities.carentity    import CarEntity
from src.entities.StaticEntities.staticentity   import StaticEntity
from src.entities.StaticEntities.hazardentity   import HazardEntity
from src.entities.StaticEntities.safezoneentity import SafeZoneEntity
from src.controllers.animated.logcontroller     import LogController

from src.core.text                           import *
from src.core.colors                         import *

from random import uniform

import sys

class GameEngine(object):

  def __init__(self):
    return None

  def init(self):
    # Get some constants which we will need later
    self.GameConfig   = IniParser("engine.ini")
    intDisplayWidth   = int(self.GameConfig.get("EngineCore", "displayWidth"))
    intDisplayHeight  = int(self.GameConfig.get("EngineCore", "displayHeight"))

    self.gameWidth  = intDisplayWidth;
    self.gameHeight = intDisplayHeight;

    # a List containing all the safe frogs
    self.safeFrogs = []

    # Cheat sequence 
    self.cheatCharInput = []
    
    # Init the main display engine
    self.engDisplay = DisplayEngine(
      (intDisplayWidth, intDisplayHeight)
    )

    defaultEntityFactory = EntityFactory(self.DisplayEngine)

    listStaticBackgroundEntities = defaultEntityFactory.buildBackground()

    self.engCollision   = CollisionEngine(self)
    self.entLifeCounter = defaultEntityFactory.buildLifeCounter()

    entFrog = defaultEntityFactory.buildFrog()
    entFrog.draw()

    # Create the Animated Cars
    entCar1 = defaultEntityFactory.buildCar([20, 189], uniform(2,7),   generateRandomColor())
    entCar2 = defaultEntityFactory.buildCar([20, 219], uniform(2,7),   generateRandomColor())
    entCar3 = defaultEntityFactory.buildCar([20, 249], uniform(2,7),   generateRandomColor())
    entCar4 = defaultEntityFactory.buildCar([20, 279], uniform(2,7),   generateRandomColor())
    entCar5 = defaultEntityFactory.buildCar([20, 309], uniform(2,7),   generateRandomColor())

    # Create an animated Log
    listLastLogCoordinates = [1,70]
    intLastLogSpeed        = 3
    
    entLastLog = LogEntity(listLastLogCoordinates, intLastLogSpeed, LogEntity.LEFT_TO_RIGHT)
    entLastLog.setGameScreen(self.DisplayEngine)
    contLastLogAnimation = LogController(entLastLog)
    entLastLog.setController(contLastLogAnimation)
    
    listSecondLogCoordinates = [485,100]
    intSecondLogSpeed        = 2
    
    entSecondLog = LogEntity(listSecondLogCoordinates, intSecondLogSpeed, LogEntity.RIGHT_TO_LEFT)
    entSecondLog.setGameScreen(self.DisplayEngine)
    contSecondLogAnimation = LogController(entSecondLog)
    entSecondLog.setController(contSecondLogAnimation)
    
    listFirstLogCoordinates = [1,130]
    intFirstLogSpeed        = 1
    
    entFirstLog = LogEntity(listFirstLogCoordinates, intFirstLogSpeed, LogEntity.LEFT_TO_RIGHT)
    entFirstLog.setGameScreen(self.DisplayEngine)
    contFirstLogAnimation = LogController(entFirstLog)
    entFirstLog.setController(contFirstLogAnimation)
    
    #Create the Large Hazard Zone
    listHazardZones         = []
    LARGE_HAZARD_LOCATION   = [18, 65]
    LARGE_HAZARD_DIMENSIONS = [464, 95]
    entLargeHazardZone      = HazardEntity(LARGE_HAZARD_LOCATION, LARGE_HAZARD_DIMENSIONS, COLOR_NAVY_BLUE)
    entLargeHazardZone.setGameScreen(self.DisplayEngine)
    listHazardZones.append(entLargeHazardZone)

    #Create the Smaller Intermediate Hazard Zones
    HAZARD_ZONEA_LOCATION   = [80,30]
    HAZARD_ZONEA_DIMENSIONS = [70, 30]
    entHazardZoneA          = HazardEntity(HAZARD_ZONEA_LOCATION, HAZARD_ZONEA_DIMENSIONS, COLOR_BACKGROUND_GREEN)
    entHazardZoneA.setGameScreen(self.DisplayEngine)
    listHazardZones.append(entHazardZoneA)

    HAZARD_ZONEB_LOCATION   = [210,30]
    HAZARD_ZONEB_DIMENSIONS = [90, 30]
    entHazardZoneB          = HazardEntity(HAZARD_ZONEB_LOCATION, HAZARD_ZONEB_DIMENSIONS, COLOR_BACKGROUND_GREEN)
    entHazardZoneB.setGameScreen(self.DisplayEngine)
    listHazardZones.append(entHazardZoneB)

    HAZARD_ZONEC_LOCATION   = [360,30]
    HAZARD_ZONEC_DIMENSIONS = [70, 30]
    entHazardZoneC          = HazardEntity(HAZARD_ZONEC_LOCATION, HAZARD_ZONEC_DIMENSIONS, COLOR_BACKGROUND_GREEN)
    entHazardZoneC.setGameScreen(self.DisplayEngine)
    listHazardZones.append(entHazardZoneC)
    
    #Create the SafeZones 
    listSafeZones         = []
    SAFE_ZONEA_LOCATION   = [20,30]
    SAFE_ZONEA_DIMENSIONS = [60, 30]
    entSafeZoneA          = SafeZoneEntity(SAFE_ZONEA_LOCATION, SAFE_ZONEA_DIMENSIONS, COLOR_WHITE)
    entSafeZoneA.setGameScreen(self.DisplayEngine)
    listSafeZones.append(entSafeZoneA)

    SAFE_ZONEB_LOCATION   = [150,30]
    SAFE_ZONEB_DIMENSIONS = [60, 30]
    entSafeZoneB          = SafeZoneEntity(SAFE_ZONEB_LOCATION, SAFE_ZONEB_DIMENSIONS, COLOR_WHITE)
    entSafeZoneB.setGameScreen(self.DisplayEngine)
    listSafeZones.append(entSafeZoneB)

    SAFE_ZONEC_LOCATION   = [300,30]
    SAFE_ZONEC_DIMENSIONS = [60, 30]
    entSafeZoneC          = SafeZoneEntity(SAFE_ZONEC_LOCATION, SAFE_ZONEC_DIMENSIONS, COLOR_WHITE)
    entSafeZoneC.setGameScreen(self.DisplayEngine)
    listSafeZones.append(entSafeZoneC)

    SAFE_ZONED_LOCATION   = [430,30]
    SAFE_ZONED_DIMENSIONS = [52, 30]
    entSafeZoneD          = SafeZoneEntity(SAFE_ZONED_LOCATION, SAFE_ZONED_DIMENSIONS, COLOR_WHITE)
    entSafeZoneD.setGameScreen(self.DisplayEngine)
    listSafeZones.append(entSafeZoneD)

    # The GameEngine should be aware of how many safe zones we have total
    self.listSafeZones = listSafeZones

    #Add the Hazard Boundary Borders
    listHazardBoundaryBorders       = []
    LEFT_HAZARD_BOUNDARY_LOCATION   = [0, 30]
    LEFT_HAZARD_BOUNDARY_DIMENSIONS = [19, 130]
    entLeftHazardBoundary           = StaticEntity(LEFT_HAZARD_BOUNDARY_LOCATION, LEFT_HAZARD_BOUNDARY_DIMENSIONS, COLOR_BACKGROUND_GREEN)
    entLeftHazardBoundary.setGameScreen(self.DisplayEngine.Surface)
    listHazardBoundaryBorders.append(entLeftHazardBoundary)

    RIGHT_HAZARD_BOUNDARY_LOCATION   = [482, 30]
    RIGHT_HAZARD_BOUNDARY_DIMENSIONS = [19, 130]
    entRightHazardBoundary           = StaticEntity(RIGHT_HAZARD_BOUNDARY_LOCATION, RIGHT_HAZARD_BOUNDARY_DIMENSIONS, COLOR_BACKGROUND_GREEN)
    entRightHazardBoundary.setGameScreen(self.DisplayEngine.Surface)
    listHazardBoundaryBorders.append(entRightHazardBoundary)

    # Anything that can collide with the frog should be appended here
    listCollisionEntities = [entCar1, entCar2, entCar3, entCar4, entCar5]
    listCollisionEntities.append(entFirstLog)
    listCollisionEntities.append(entSecondLog)
    listCollisionEntities.append(entLastLog) 
    
    for hazardZone in listHazardZones:
      listCollisionEntities.append(hazardZone)

    for safeZone in listSafeZones:
      listCollisionEntities.append(safeZone)

    # Add a Background Entities to the Game Layer
    self.DisplayEngine.addLayer(listStaticBackgroundEntities)
    
    #Add the HazardZones to the Game Layer
    self.DisplayEngine.addLayer(listHazardZones)    

    #Add the SafeZones to the Game Layer
    self.DisplayEngine.addLayer(listSafeZones)    

    # Add the logs to the Game Layer
    self.DisplayEngine.addLayer(entFirstLog)
    self.DisplayEngine.addLayer(entSecondLog)
    self.DisplayEngine.addLayer(entLastLog)

    #Add the Hazard Boundary Borders

    self.DisplayEngine.addLayer(listHazardBoundaryBorders)

    # Add the universal game controller
    UniversalGameController = GameController(self)
    self.DisplayEngine.addUserControlledLayer(entFrog)
    self.DisplayEngine.addGameController(UniversalGameController)

    self.DisplayEngine.addLayer(entCar1)
    self.DisplayEngine.addLayer(entCar2)
    self.DisplayEngine.addLayer(entCar3)
    self.DisplayEngine.addLayer(entCar4)
    self.DisplayEngine.addLayer(entCar5)

    TitleText = Text(FONT_BLOX, "PyFrogger", COLOR_FROG_GREEN, 20)
    TitleText.setGameScreen(self.DisplayEngine.Surface)
    TitleText.draw((400, 4))

    LivesText = Text(FONT_BLOX, "Lives ", COLOR_FROG_GREEN, 20)
    LivesText.setGameScreen(self.DisplayEngine.Surface)
    LivesText.draw((10, 4))

    LivesCounterText = Text(FONT_BLOX, "3", COLOR_FROG_RED, 20)
    LivesCounterText.setGameScreen(self.DisplayEngine.Surface)
    LivesCounterText.draw((70, 4))

    self.entLifeCounter.setLifeTextEntity(LivesCounterText)

    entText = [ TitleText, LivesText, LivesCounterText ]
    self.DisplayEngine.addLayer(entText)

    self.CollisionEngine.setPlayerLifeCounter(self.entLifeCounter)

    # Adding these entities into the collision engine will let the engine monitor
    # their position and on the action of a rectangle collision, the controlled
    # entity will be handled based on it's collision based methods
    self.CollisionEngine.setControlledEntity(entFrog)
    for collisionEntity in listCollisionEntities:
      self.CollisionEngine.addCollisionEntity(collisionEntity)

    # This variable keeps the run active
    self.running = True
    self.freezeState = False

  def run(self):
    """
      Constantly render updates to the surface
    """
    # If we find a collision then update the coordinates of the controlled entity
    # before it gets drawn to the display
    self.CollisionEngine.checkForAndHandleCollisions()

    if self.entLifeCounter.Lives == 0:
      self.gameOver()
    
    if len(self.safeFrogs) == len(self.listSafeZones):
      self.win()

    self.DisplayEngine.updateDisplay()

    # Freezes the Display
    self.DisplayEngine.setFreezeState(self.freezeState)
    
  def quit(self):
    self.running = False

  def gameOver(self):
    GameOverText = Text(FONT_BLOX, "GAME OVER", COLOR_FROG_RED, 60)
    GameOverText.setGameScreen(self.DisplayEngine.Surface)
    GameOverText.draw((self.gameWidth / 2 - 130, self.gameHeight / 2))

    GameOverText2 = Text(FONT_BLOX, "Press ESC to Quit", COLOR_WHITE, 30)
    GameOverText2.setGameScreen(self.DisplayEngine.Surface)
    GameOverText2.draw((self.gameWidth / 2 - 120, self.gameHeight / 2 + 80))

    GameOverText3 = Text(FONT_BLOX, "Press N for a New Game", COLOR_FROG_RED, 30)
    GameOverText3.setGameScreen(self.DisplayEngine.Surface)
    GameOverText3.draw((self.gameWidth / 2 - 150, self.gameHeight / 2 + 120))

    self.freezeState = True # Flag to freeze the display

  def win(self):
    VictoryText = Text(FONT_BLOX, "YOU WIN", COLOR_FROG_RED, 60)
    VictoryText.setGameScreen(self.DisplayEngine.Surface)
    VictoryText.draw((self.gameWidth / 2 - 120, self.gameHeight / 2))

    Victory2 = Text(FONT_BLOX, "Press ESC to Quit", COLOR_WHITE, 30)
    Victory2.setGameScreen(self.DisplayEngine.Surface)
    Victory2.draw((self.gameWidth / 2 - 120, self.gameHeight / 2 + 80))

    Victory3 = Text(FONT_BLOX, "Press N for a New Game", COLOR_FROG_RED, 30)
    Victory3.setGameScreen(self.DisplayEngine.Surface)
    Victory3.draw((self.gameWidth / 2 - 150, self.gameHeight / 2 + 120))

    self.freezeState = True # Flag to freeze the display

  # a Fun little cheat :)
  def lifeCheat(self, keyPress):
    self.cheatCharInput.append(keyPress)

    cheatCharInput        = "pyfrogger"
    lengthOfCheatSequence = len(cheatCharInput)
    lenOfCharInput        = len(self.cheatCharInput) 

    # Need to see if we can actually test the string first, we may not have enough characters
    if (lenOfCharInput / lengthOfCheatSequence) > 0:
      # If the lengths are the same this means we have exactly one attempt to make
      if lenOfCharInput == lengthOfCheatSequence:
        testAttempts = 1
      else:
        testAttempts = lenOfCharInput - lengthOfCheatSequence

      for startingPosition in xrange(0, testAttempts):
        testSequence = "".join(self.cheatCharInput[startingPosition:(startingPosition + lengthOfCheatSequence)])
        if testSequence == cheatCharInput:
          self.entLifeCounter.add(99)
          self.entLifeCounter.Text.setText(self.entLifeCounter.Lives)

  def reset(self):
    if self.freezeState == True:
      self.entLifeCounter.set(3)
      self.entLifeCounter.Text.setText(self.entLifeCounter.Lives)

      self.freezeState = False
      self.DisplayEngine.PlayerDisplayLayers.empty()

      for safeZone in self.listSafeZones:
        safeZone.markUnoccupied()
      
      defaultEntityFactory = EntityFactory(self.DisplayEngine)
      entNewFrog = defaultEntityFactory.buildFrog() 
      entNewFrog.draw()
      self.DisplayEngine.addUserControlledLayer(entNewFrog)
      self.CollisionEngine.setControlledEntity(entNewFrog)

      self.safeFrogs = []

  @property
  def DisplayEngine(self):
    return self.engDisplay
  
  @property
  def CollisionEngine(self):
    return self.engCollision
