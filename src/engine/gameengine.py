from src.core.iniparser import IniParser
from src.engine.displayengine import DisplayEngine

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

    # This variable keeps the run active
    self.running = True

  def run(self):
    """
      Constantly render updates to the surface
    """
    self.engDisplay.updateDisplay()
    
  def quit(self):
    return True







