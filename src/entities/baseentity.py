'''
Created on Dec 9, 2009

@author: William Madison
'''

#Import the Abstract Base Class (abc) module.

import abc

class BaseEntity(object):
  '''
    This class is an abstract representation
    of our Entity construct. It will house
    several abstract methods, which will be thrust
    upon the subclasses for implementation details.
  '''
  __metaclass__ = abc.ABCMeta
  
  @abc.abstractmethod
  def setGameScreen(self, gameScreen):
    '''
      This is an abstract representation of the
      function responsible for providing the 
      concrete implementation with a reference
      to its parent surface.
      
      @param gameScreen:
    '''
    return
  
  @abc.abstractmethod
  def setController(self, myController):
    '''
      This is an abstract representation of the
      function responsible for providing the 
      concrete implementation with a reference
      to its controller.
      
      @param myController:
    '''
    return
  
  @abc.abstractmethod
  def respond(self, eventFired):
    '''
      This is an abstract representation of the
      function responsible for encapsulating how
      a concrete entity responds to a given event.
      
      @param eventFired:
    '''
    return
    
    
        