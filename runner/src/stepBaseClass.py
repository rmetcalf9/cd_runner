


class stepBaseClass():
  name=None
  type=None
  def __init__(self, name, type):
    self.name = name
    self.type = type

  def isImplemented(self):
    return False

  def getName(self):
    return self.name

  def getType(self):
    return self.type