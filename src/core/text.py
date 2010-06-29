import pygame
import os
from src.entities.baseentity  import BaseEntity
from src.core.iniparser       import IniParser

# Define Font Types
FONT_COURIER = "Courier New"
FONT_BLOX    = "Blox.ttf"

class Text(BaseEntity):

  def __init__(self, fontFace, text, color, size):
    pygame.sprite.DirtySprite.__init__(self)
    gameConfig      = IniParser("engine.ini")
    fontDirName     = gameConfig.get("Text", "fontDir")
    fontFile        = os.path.join("src", "core", "fonts", fontFace)

    try:
      self.font     = pygame.font.Font(fontFile, size)
    except:
      print "Could not load regular font: " + fontFile

    self.color  = color
    self.size   = size
    self.text   = text

    self.render()

  def draw(self, (x, y)):
    self.x, self.y = x, y
    self.GameSurface.blit(self.Surface, (x, y))

  def setGameScreen(self, gameScreen):
    self.surfGameDisplay = gameScreen

  def setText(self, text):
    self.text = str(text)

  def render(self):
    self.surface = self.font.render(self.text, True, self.color) # True flag is for anti-aliasing
    self.image   = self.surface

  def update(self):
    self.render()
    self.GameSurface.blit(self.Surface, (self.x, self.y))

  def respond(self):
    pass

  def setController(self):
    pass

  @property
  def Surface(self):
    return self.surface

  @property
  def GameSurface(self):
    return self.surfGameDisplay


class SysText(Text):

  def __init__(self, fontFace, text, color, size):
    pygame.sprite.DirtySprite.__init__(self)
    try:
      self.font = pygame.font.SysFont(fontFace, size)
    except:
      print "Could not load system font."

    self.color  = color
    self.size   = size
    self.text   = text

    self.surface = self.font.render(self.text, True, self.color) # True flag is for anti-aliasing
    self.image   = self.surface
