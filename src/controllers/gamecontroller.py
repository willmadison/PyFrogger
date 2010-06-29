'''
Created on Dec 9, 2009

@author: William Madison
'''
import pygame
from src.controllers.entitycontroller import BaseController
from pygame.locals import * #@UnusedWildImport

class GameController(BaseController):
  '''
    This is the concrete implementation of 
    a Frog Controller, which extends the 
    abstract Entity Controller.
  '''

  def __init__(self, gameEngine):
    '''
      Initializes the Game Controller.
    '''
    self.gameEngine = gameEngine

    self.dictKeyActionMap = {
                             K_ESCAPE : self.quit,
                             K_n      : self.GameEngine.reset
                            }
    
  def respond(self, eventFired):
    '''
      This function implements the controller's 
      response interface, which determines how the
      controller causes the entity under its control
      to respond (or not)
      
      @param eventFired:
    '''     
    
    # If this is a valid key event:
    
    if (eventFired.type == KEYDOWN and
        eventFired.key in self.KeyActionMap):
      
      # Respond Accordingly
      
      self.KeyActionMap[eventFired.key]() 
      
    # Otherwise if and only if this is a quit event, quit the application.
    
    elif eventFired.type == QUIT:
      self.quit()
  
  @property
  def GameEngine(self):
    return self.gameEngine

  @property
  def KeyActionMap(self):
    return self.dictKeyActionMap
    
    
    
  
  
      
    
    
