'''
Created on Dec 9, 2009

@author: William Madison
'''

#Import the Abstract Base Class (abc) module.

import abc

class EntityController(object):
  '''
    This class is an abstract representation
    of our controller construct. It will house
    several abstract methods, which will be thrust
    upon the subclasses for implementation details.
  '''
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def setEntity(self, controlledEntity):
    '''
     Set the classes controlled Entity instance
     variable, (i.e. the entity which this controller
     controls)
    '''      
    return
   
  @abc.abstractmethod
  def respond(self, eventFired):
    '''
     Abstract implementation of a controller's 
     response interface, which determines how the
     controller causes the entity under its control
     to respond (or not)
    '''
    return
    
  def quit(self):
    '''
      This function will quit the application if a
      "Quit" event is fired.
    '''      
    pass
    
  def pause(self):
    '''
      This function will cause the game to pause
      if the "Pause" event is fired.
    '''
    pass
    
    
      
    
      
    