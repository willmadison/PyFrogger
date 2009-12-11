import sys, pygame

class DisplayEngine(object):

  def __init__(self, resolution, depth=0, **flags):
    """ 
      Create the main display surface
    """

    try:
      pygame.init()

      # We are not using flags right now so just default flags to 0
      if len(flags) == 0:
        displayFlags = 0
      
      # Set the depth, should automatically default to current desktop
      intDepth = depth

      # Create the main display surface
      self.displaySurface = pygame.display.set_mode(
        (resolution[0], resolution[1]),
        displayFlags,
        intDepth
      )
    
    except StandardError as Error:
      print Error

  def updateDisplay(self):
    
    try:
      pygame.display.update()
    
    except StandardError as Error:
      print Error
      sys.exit()

  @property
  def Surface(self):
    return self.displaySurface
