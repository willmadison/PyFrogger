'''
Created on Dec 14, 2009

@author: William Madison
'''

from src.entities.baseentity import BaseEntity
import pygame

class StaticEntity(BaseEntity):
  '''
    classdocs
  '''


  def __init__(self, coordinates=[0,0], dimensions = [500, 125], color = (0, 0, 255)):

    # Convert to a recognizable system of notation
    self.dimensions = {
      'width'   : dimensions[0],
      'height'  : dimensions[1]
    }
    
    # Convert to a recognizable system of notation
    self.coordinates = {
      'x' : coordinates[0],
      'y' : coordinates[1]
    }
    
    self.color = color

    # Define this entities surface
    self.surfEntity = pygame.Surface((self.Dimensions['width'], self.Dimensions['height']))
      
    self.draw((0, 0, self.Dimensions['width'], self.Dimensions['height']))
    
  def setGameScreen(self, gameScreen):
    '''
      This function provides this entity with a reference
      to its parent surface.
      
      @param gameScreen:
    '''
    self.surfGameDisplay = gameScreen
  
  def setController(self, myController):
    '''
      This function is invalid for static entities
      as they will NOT be controllable.
      
      @param myController:
    '''    
    raise NotImplementedError('setController() is invalid for StaticEntities!')
  
  def respond(self, eventFired):
    '''
      This function is invalid for static entities
      as they will NOT be controllable.
      
      @param eventFired:
    '''
    raise NotImplementedError('respond() is invalid for StaticEntities!')
  
  def draw(self, entityLocationAndSize = (0, 0, 25, 25)):
    '''
      This function is responsible for encapsulating how 
      the entity is displayed on the display surface
    '''
    pygame.draw.rect(self.Surface, self.Color, entityLocationAndSize)
    
  def update(self):
    self.GameSurface.blit(self.Surface, (self.Coordinates['x'], self.Coordinates['y']))
    
  
  @property
  def Coordinates(self):
    return self.coordinates
  
  @property
  def Color(self):
    return self.color
  
  @property
  def GameSurface(self):
    return self.surfGameDisplay
    
  @property
  def Dimensions(self):
    return self.dimensions

  @property
  def Surface(self):
    return self.surfEntity      