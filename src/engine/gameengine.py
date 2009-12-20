from src.core.iniparser import IniParser
from src.engine.displayengine import DisplayEngine

from src.entities.animatedentities.carentity import CarEntity

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

    # Create the Animated Cars
    entCar = CarEntity([0, 0])
    entCar.setDisplayEngine(self.DisplayEngine) 

    # Add a Car Entities to the Game Layer
    self.DisplayEngine.addLayer(entCar) 

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





