from src.core.iniparser                      import IniParser
from src.engine.displayengine                import DisplayEngine
from src.engine.collisionengine              import CollisionEngine
from src.entities.AnimatedEntities.logentity import LogEntity

from src.entities.entityfactory              import EntityFactory
from src.controllers.animated.carcontroller  import CarController

from src.entities.AnimatedEntities.carentity import CarEntity
from src.controllers.animated.logcontroller  import LogController

import sys

class GameEngine(object):

  def __init__(self):
    return None

  def init(self):
    # Get some constants which we will need later
    self.GameConfig   = IniParser("engine.ini")
    intDisplayWidth   = int(self.GameConfig.get("EngineCore", "displayWidth"))
    intDisplayHeight  = int(self.GameConfig.get("EngineCore", "displayHeight"))
    
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
    #listCollisionEntities = [entCar, entCar2, entCar3, entCar4]
    listCollisionEntities = []

    # Add a Car Entities to the Game Layer
    self.DisplayEngine.addLayer(listStaticBackgroundEntities)

    # Add the logs to the Game Layer
    self.DisplayEngine.addLayer(entFirstLog)
    self.DisplayEngine.addLayer(entSecondLog)
    self.DisplayEngine.addLayer(entLastLog)

    self.DisplayEngine.addUserControlledLayer(entFrog)

    self.DisplayEngine.addLayer(entCar)
    self.DisplayEngine.addLayer(entCar2)
    self.DisplayEngine.addLayer(entCar3)
    self.DisplayEngine.addLayer(entCar4)
    self.DisplayEngine.addLayer(entCar5)

    # Adding these entities into the collision engine will let the engine monitor
    # their position and on the action of a rectangle collision, the controlled
    # entity will be handled based on it's collision based methods
    self.CollisionEngine.setControlledEntity(entFrog)
    for collisionEntity in listCollisionEntities:
      self.CollisionEngine.addCollisionEntity(collisionEntity)

    # This variable keeps the run active
    self.running = True

  def run(self):
    """
      Constantly render updates to the surface
    """
    # if we find a collision then update the coordinates of the controlled entity
    # before it gets drawn to the display
    collisionFound = self.CollisionEngine.checkForCollision()
    if collisionFound != False:
      # Reset the position of the frog
      self.DisplayEngine.Frog.coordinates['x'] = self.DisplayEngine.Frog.startingCoordinates['x']
      self.DisplayEngine.Frog.coordinates['y'] = self.DisplayEngine.Frog.startingCoordinates['y']
      self.entLifeCounter.remove()
      print "Current Life Count: " + str(self.entLifeCounter.Lives)
      if self.entLifeCounter.Lives == 0:
        print "GAME OVER!"
        sys.exit()

    self.engDisplay.updateDisplay()
    
  def quit(self):
    return True

  @property
  def DisplayEngine(self):
    return self.engDisplay
  
  @property
  def CollisionEngine(self):
    return self.engCollision





