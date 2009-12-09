import ConfigParser, os

class IniParser(object):
  """
    This class handles the extrapolation of a ini file and provides a access layer
    to the contents of the ini file.  Basically a wrapper if you will

    Example Use:

    from IniParser import *

    MyConfig = IniParser("IniFile.ini")
    print MyConfig.get("MySection", "MyKey")

    ... or you can get back a formatted list of all items under a section by using:
    print MyConfig.get("MySection")
  """

  def __init__(self, strIniFileName):

    strRootPath = os.path.abspath(os.path.dirname(__file__))
    strConfigPath = os.path.normpath(os.path.join(strRootPath, '../../config/'))
    strFullIniPath = os.path.join(strConfigPath, strIniFileName)

    if os.path.exists(strFullIniPath) == True:
      self.objConfig = ConfigParser.ConfigParser()
      self.objConfig.read(strFullIniPath)

    else:
      print "ConfigParser could not open the file" + strIniFileName

  def get(self, section, key=""):

    if key == "":
      return self.objConfig.items(section)
    else:
      return self.objConfig.get(section, key)
