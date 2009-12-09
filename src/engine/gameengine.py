from src.core.iniparser import IniParser

class GameEngine(object):

  def __init__(self):
    GameConfig = IniParser("engine.ini")
    print GameConfig.get("EngineCore", "displayWidth")

  def init(self):
    return True

  def loop(self):
    return True

  def quit(self):
    return True
