class Foto:
  def __init__(self, url, altura, largura) -> None:
    self.__url = url
    self.__altura = altura
    self.__largura = largura
    
  def __repr__(self) -> str:
    return f'foto: {self.__url}, altura: {self.__altura}, largura: {self.__largura}\n'