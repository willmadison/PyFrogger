from src.engine.displayengine import DisplayEngine
import pygame

class ValidationFramework(object):
  """
    This class is a utility for creating a screen object and updating it.
    Basically this acts as an encapsulation
  """

  def __init__(self, displayWidth=500, displayHeight=400):

    # Create the display
    self.engDisplay = DisplayEngine((displayWidth, displayHeight))

    # Create a queue to manage the actions that will loop in the run method
    self.arrRunQueue = []

    # Keep running with this set to True
    self.running = True

  def addToRunQueue(self, method):
    """ Add a action to loop in the run method """
    self.RunQueue.append(method)

  def run(self):
    """ Run the methods that need to loop """
    for runMethod in self.RunQueue:
      runMethod()

    self.engDisplay.updateDisplay()
    
  def getEvents(self):
    '''
      This function captures all of the pygame events, for later use.
    '''      
    return pygame.event.get()

  def quit(self):
    pygame.quit()

  @property
  def RunQueue(self):
    """ Return the current run queue """
    return self.arrRunQueue


  @property
  def Surface(self):
    """ Return the Main Display Surface """
    return self.engDisplay.Surface 
