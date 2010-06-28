'''
Created on June 28, 2009

@author: William Madison
'''

#Import the Abstract Base Class (abc) module.

import abc

class BaseCollision(object):
  '''
    This class is an abstract representation
    of our Entity construct. It will house
    several abstract methods, which will be thrust
    upon the subclasses for implementation details.
  '''
  __metaclass__ = abc.ABCMeta
  
  @abc.abstractmethod
  def handleCollision(self):
    '''
      This is an abstract representation of the
      function responsible for providing the 
      concrete implementation with a means
      of handling a collision of a given type.
    '''
    return
