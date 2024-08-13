class foto:
  def __init__(self) -> None:
    self.__url = str()
    self.__height = int()
    self.__width = int()
    
  @property
  def url(self):
    return self.__url

  @url.setter
  def url(self, url):
    self.__url = url

  @property
  def height(self):
    return self.__height

  @height.setter
  def height(self, height):
    self.__height = height

  @property
  def width(self):
    return self.__width

  @width.setter
  def width(self, width):
    self.__width = width