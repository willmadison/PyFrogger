from src.entities.baseentity import BaseEntity
import pygame

class LifeEntity(BaseEntity):

  def __init__(self):
    # Define how many lifes to start with
    self.intLifeCounter = 3

  def remove(self, intLife=-1):
    return self._modify(intLife)

  def add(self, intLife=1):
    return self._modify(intLife)

  def _modify(self, intLife):
    self.intLifeCounter += intLife
    return True

  def setGameScreen(self):
    pass

  def setController(self):
    pass

  def respond(self):
    pass

  def draw(self):
    pass

  @property
  def Lives(self):
    return self.intLifeCounter
  
