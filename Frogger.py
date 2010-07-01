# This is needed for global package support across all modules
import sys
sys.path.insert(0, "../")

import pygame
from src.engine.gameengine import GameEngine
from pygame.locals import *

if __name__ == "__main__":
  Frogger = GameEngine()
  Frogger.init()
  
  while Frogger.running == True:
    Frogger.run()

