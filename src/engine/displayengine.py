import sys, pygame

class DisplayEngine(object):

  def __init__(self, resolution, depth=0, **flags):
    """ 
      Create the main display surface
    """

    try:
      pygame.init()

      # Create the display layers that we will need
      self.DisplayLayers = pygame.sprite.LayeredDirty()

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

  def addLayer(self, listLayer):
    """ Add a layer to the rendering engine """
    groupLayer = pygame.sprite.Group(listLayer)
    self.DisplayLayers.add(groupLayer)

  def updateDisplay(self):   
    """
      This method is responsible for constantly updating the main display surface.
      It also draws anything in the DisplayLayers layer to the screen in the order in which they were added
      Then we update only the updated layers, not the entire screen
    """
    self.DisplayLayers.update()
    listDisplayRectangles = self.DisplayLayers.draw(self.Surface)
    pygame.display.update(listDisplayRectangles)
    
  @property
  def Surface(self):
    return self.displaySurface
