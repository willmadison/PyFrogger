from src.core.iniparser                      import IniParser
from src.engine.displayengine                import DisplayEngine
from src.engine.collisionengine              import CollisionEngine
from src.entities.AnimatedEntities.logentity import LogEntity

from src.entities.entityfactory              import EntityFactory
from src.controllers.animated.carcontroller  import CarController

from src.entities.AnimatedEntities.carentity import CarEntity
from src.controllers.animated.logcontroller  import LogController

from src.controllers.gamecontroller          import GameController

from src.core.text                           import *
from src.core.colors                         import *

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
    
    # Init the main display engine
    self.engDisplay = DisplayEngine(
      (intDisplayWidth, intDisplayHeight)
    )

    defaultEntityFactory = EntityFactory(self.engDisplay)

    listStaticBackgroundEntities = defaultEntityFactory.buildBackground()

    self.engCollision = CollisionEngine()
    self.entLifeCounter = defaultEntityFactory.buildLifeCounter()

    entFrog = defaultEntityFactory.buildFrog()
    entFrog.draw()

    # Create the Animated Cars
    entCar = CarEntity([20, 189], 4.2)
    entCar.setGameScreen(self.DisplayEngine)
    contCarAnimation = CarController(entCar)
    entCar.setController(contCarAnimation)

    entCar2 = CarEntity([20, 219], 5)
    entCar2.setGameScreen(self.DisplayEngine)
    contCarAnimation = CarController(entCar2)
    entCar2.setController(contCarAnimation)

    entCar3 = CarEntity([20, 249], 2)
    entCar3.setGameScreen(self.DisplayEngine)
    contCarAnimation = CarController(entCar3)
    entCar3.setController(contCarAnimation)

    entCar4 = CarEntity([20, 279], 1)
    entCar4.setGameScreen(self.DisplayEngine)
    contCarAnimation = CarController(entCar4)
    entCar4.setController(contCarAnimation)

    entCar5 = CarEntity([20, 309], 3)
    entCar5.setGameScreen(self.DisplayEngine)
    contCarAnimation = CarController(entCar5)
    entCar5.setController(contCarAnimation)
    
    # Create an animated Log
    listLastLogCoordinates = [1,70]
    intLastLogSpeed        = 2
    
    entLastLog = LogEntity(listLastLogCoordinates, intLastLogSpeed, LogEntity.LEFT_TO_RIGHT)
    entLastLog.setGameScreen(self.DisplayEngine)
    contLastLogAnimation = LogController(entLastLog)
    entLastLog.setController(contLastLogAnimation)
    
    listSecondLogCoordinates = [1,100]
    intSecondLogSpeed        = 2
    
    entSecondLog = LogEntity(listSecondLogCoordinates, intSecondLogSpeed, LogEntity.RIGHT_TO_LEFT)
    entSecondLog.setGameScreen(self.DisplayEngine)
    contSecondLogAnimation = LogController(entSecondLog)
    entSecondLog.setController(contSecondLogAnimation)
    
    listFirstLogCoordinates = [1,130]
    intFirstLogSpeed        = 2
    
    entFirstLog = LogEntity(listFirstLogCoordinates, intFirstLogSpeed, LogEntity.LEFT_TO_RIGHT)
    entFirstLog.setGameScreen(self.DisplayEngine)
    contFirstLogAnimation = LogController(entFirstLog)
    entFirstLog.setController(contFirstLogAnimation)
    
    # Anything that can collide with the frog should be appended here
    listCollisionEntities = [entCar, entCar2, entCar3, entCar4, entCar5]
    listCollisionEntities.append(entFirstLog)
    listCollisionEntities.append(entSecondLog)

    # Add a Car Entities to the Game Layer
    self.DisplayEngine.addLayer(listStaticBackgroundEntities)

    # Add the logs to the Game Layer
    self.DisplayEngine.addLayer(entFirstLog)
    self.DisplayEngine.addLayer(entSecondLog)
    self.DisplayEngine.addLayer(entLastLog)

    # Add the universal game controller
    UniversalGameController = GameController(self)
    self.DisplayEngine.addUserControlledLayer(entFrog)
    self.DisplayEngine.addGameController(UniversalGameController)

    self.DisplayEngine.addLayer(entCar)
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
    # if we find a collision then update the coordinates of the controlled entity
    # before it gets drawn to the display
    self.CollisionEngine.checkForAndHandleCollisions()
    if self.entLifeCounter.Lives == 0:
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

    self.engDisplay.updateDisplay()

    # Freezes the Display
    self.DisplayEngine.setFreezeState(self.freezeState)
    
  def quit(self):
    return True

  def reset(self):
    if self.freezeState == True:
      self.entLifeCounter.add(3)
      self.entLifeCounter.Text.setText(self.entLifeCounter.Lives)
      self.freezeState = False

  @property
  def DisplayEngine(self):
    return self.engDisplay
  
  @property
  def CollisionEngine(self):
    return self.engCollision





