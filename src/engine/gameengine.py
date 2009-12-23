from src.core.iniparser import IniParser
from src.engine.displayengine import DisplayEngine

from src.entities.entityfactory import EntityFactory
from src.controllers.animated.carcontroller import CarController

from src.entities.AnimatedEntities.carentity import CarEntity

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

    entFrog = defaultEntityFactory.buildFrog()
    entFrog.draw()

    # Create the Animated Cars
    entCar = CarEntity([20, 300], 4.2)
    entCar.setGameScreen(self.DisplayEngine) 
    contCarAnimation = CarController(entCar)
    entCar.setController(contCarAnimation)

    entCar2 = CarEntity([20, 250], 5)
    entCar2.setGameScreen(self.DisplayEngine) 
    contCarAnimation = CarController(entCar2)
    entCar2.setController(contCarAnimation)

    entCar3 = CarEntity([20, 210], 2)
    entCar3.setGameScreen(self.DisplayEngine) 
    contCarAnimation = CarController(entCar3)
    entCar3.setController(contCarAnimation)

    # Add a Car Entities to the Game Layer
    self.DisplayEngine.addLayer(listStaticBackgroundEntities)
    self.DisplayEngine.addLayer(entCar) 
    self.DisplayEngine.addLayer(entCar2) 
    self.DisplayEngine.addLayer(entCar3) 
    self.DisplayEngine.addUserControlledLayer(entFrog) 

    # This variable keeps the run active
    self.running = True

  def run(self):
    """
      Constantly render updates to the surface
    """
    self.engDisplay.updateDisplay()
    
  def quit(self):
    return True

  @property
  def DisplayEngine(self):
    return self.engDisplay





