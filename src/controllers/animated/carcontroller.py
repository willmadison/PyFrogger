'''
Created on Dec 9, 2009

@author: William Madison
'''
from src.controllers.entitycontroller import EntityController
import pygame
from pygame.locals import * #@UnusedWildImport
import random

class CarController(EntityController):
  '''
    This is the concrete implementation of 
    a Frog Controller, which extends the 
    abstract Entity Controller.
  '''

  def __init__(self, controlledEntity):
    '''
      Initializes the Car Controller.
    '''
    self.controlledEntity = controlledEntity
    
    self.dictKeyActionMap = {}
    
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
    # The entity has migrated off the x axis
    if self.Entity.Coordinates['x'] >= 450:
      self.Entity.Coordinates['x'] = 0 # todo: Set this to the screen width
      self.Entity.speed = random.uniform(2.0, 7.0)

    self.Entity.Coordinates['x'] += self.Entity.speed
      
  
  def move(self, direction):
    '''
      This function causes the Entity under its control
      to move in the given direction.
      
      @param direction:
    '''
    # Assume that the move will be successful.
    
    moveSuccessful = True
      
    dictDirectionMap = {
                       'UP'   : -self.Entity.Dimensions['height'], # Move the entity up by its Height in Pixels
                       'DOWN' :  self.Entity.Dimensions['height'], # Move the entity down by its Height in Pixels
                       'LEFT' : -self.Entity.Dimensions['width'],  # Move the entity left by its Width in Pixels
                       'RIGHT':  self.Entity.Dimensions['width']   # Move the entity right by its Width in Pixels
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
    
    
    
  
  
      
    
    
