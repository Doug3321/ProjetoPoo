class Foto:
    def __init__(self, url, altura, largura) -> None:
        self.__url = url
        self.__altura = altura
        self.__largura = largura

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, value):
        self.__altura = value

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, value):
        self.__largura = value
        
    def __repr__(self) -> str:
        return f'foto: {self.__url}, altura: {self.__altura}, largura: {self.__largura}\n'
