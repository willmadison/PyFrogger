'''
Created on Dec 9, 2009

@author: William Madison
'''

from src.controllers.entitycontroller import EntityController
import pygame
from pygame.locals import * #@UnusedWildImport

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
    
    self.dictKeyActionMap = {
                             pygame.K_UP     : self.moveUp,
                             pygame.K_DOWN   : self.moveDown,
                             pygame.K_LEFT   : self.moveLeft,
                             pygame.K_RIGHT  : self.moveRight                    
                            }
    
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
    
    # If this is a valid key event:
    
    if (eventFired.type == KEYDOWN and
        eventFired.key in self.KeyActionMap):
      
      # Respond Accordingly
      
      self.KeyActionMap[eventFired.key]() 
      
    # Otherwise if and only if this is a quit event, quit the application.
    
    elif eventFired.type == QUIT:
      self.quit()
  
  def moveUp(self):
    self.move('UP')
  
  def moveDown(self):
    self.move('DOWN')
    
  def moveLeft(self):
    self.move('LEFT')
    
  def moveRight(self):
    self.move('RIGHT')  
  
  def move(self, direction):
    '''
      This function causes the Entity under its control
      to move in the given direction.
      
      @param direction:
    '''
    # Assume that the move will be successful.
    
    moveSuccessful = True
      
    dictDirectionMap = {
                       'UP'   : -self.Entity.Dimensions['height'] - self.Entity.moveVerticalOffset,   # Move the entity up by its Height in Pixels
                       'DOWN' :  self.Entity.Dimensions['height'] + self.Entity.moveVerticalOffset,   # Move the entity down by its Height in Pixels
                       'LEFT' : -self.Entity.Dimensions['width']  - self.Entity.moveHorizontalOffset, # Move the entity left by its Width in Pixels
                       'RIGHT':  self.Entity.Dimensions['width']  + self.Entity.moveHorizontalOffset  # Move the entity right by its Width in Pixels
                       }
    
    # If the user intends to move vertically update the y coordinate accordingly.
    
   # self.Entity.surfEntity = self.Entity.arrFacingDirectionImages[direction]
  
    if direction in ['UP', 'DOWN']:
      self.Entity.Coordinates['y'] += dictDirectionMap[direction]
      
    # Otherwise the user intends to move horizontally, so update the x coordinate accordingly.
      
    else:
      self.Entity.Coordinates['x'] += dictDirectionMap[direction]

    return moveSuccessful
      
  @property
  def Entity(self):
    return self.controlledEntity
  
  @property
  def KeyActionMap(self):
    return self.dictKeyActionMap
    
    
    
  
  
      
    
    
