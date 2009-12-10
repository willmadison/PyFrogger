'''
Created on Dec 9, 2009

@author: William Madison
'''

from entitycontroller import EntityController

class FrogController(EntityController):
  '''
    This is the concrete implementation of 
    a Frog Controller, which extends the 
    abstract Entity Controller.
  '''

  def __init__(self, controlledEntity):
    '''
      Initializes the Frog Controller.
    '''
        
    self.controlledEntity = controlledEntity
    
  def setEntity(self, controlledEntity):
    '''
      This function assigns the given entity
      to this instance's controlledEntity property.
      
      @param controlledEntity:
    '''
    
    self.controlledEntity = controlledEntity
    
  def respond(self, eventFired):
    '''
      This function implements the controller's 
      response interface, which determines how the
      controller causes the entity under its control
      to respond (or not)
      
      @param eventFired:
    '''
    pass
  
  def move(self, direction):
    '''
      This function causes the Entity under its control
      to move in the given direction.
      
      @param direction:
    '''
    pass
  
  
      
    
    