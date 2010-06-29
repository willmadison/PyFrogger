'''
Created on Feb 9, 2010

@author: William Madison
'''
from src.controllers.entitycontroller import EntityController
import random


class LogController(EntityController):
  '''
  This controller is a very basic controller that controls the movement of logs
  across the game screen.
  '''


  def __init__(self, controlledEntity):
    '''
      Initializes the Log Controller.
    '''
    self.controlledEntity = controlledEntity
  
  def setEntity(self, controlledEntity):
    '''
      This function assigns the given entity
      to this instance's controlledEntity property.
      
      @param controlledEntity:
    '''
    
    self.Entity = controlledEntity
    
  def respond(self, eventFired):
    '''
      This function implements the controller's 
      response interface, which determines how the
      controller causes the entity under its control
      to respond (or not)
      
      @param eventFired:
    '''     
    return None 
      
  def animate(self):    
    # The entity has migrated off the x axis, with respect to its orientation.
    
    if self.Entity.orientation == self.Entity.LEFT_TO_RIGHT:
      if self.Entity.Coordinates['x'] >= 485 - self.Entity.Dimensions['width']:
        self.Entity.Coordinates['x'] = 50
        self.Entity.speed = int(random.uniform(1.0, 5.0)) * self.Entity.orientation
    
    else:
      if self.Entity.Coordinates['x'] <= 15: 
        self.Entity.Coordinates['x'] = 485 - self.Entity.Dimensions['width']        
        self.Entity.speed = int(random.uniform(1.0, 5.0)) * self.Entity.orientation
    
    self.Entity.Coordinates['x'] += self.Entity.speed 
      
  @property
  def Entity(self):
    return self.controlledEntity
