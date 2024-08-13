import Foto

class Artista:
    def __init__(self):
        self.__nome = str()
        self.__generos = list()
        self.__id = str()
        self.__foto = Foto()
        self.__popularidade = int()
        self.__perfil_spotify = str()
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def generos(self):
        return self.__generos

    @generos.setter
    def generos(self, generos):
        self.__generos = generos

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def foto(self):
        return self.__foto

    @foto.setter
    def foto(self, foto):
        self.__foto = foto

    @property
    def popularidade(self):
        return self.__popularidade

    @popularidade.setter
    def popularidade(self, popularidade):
        self.__popularidade = popularidade

    @property
    def perfil_spotify(self):
        return self.__perfil_spotify

    @perfil_spotify.setter
    def perfil_spotify(self, perfil_spotify):
        self.__perfil_spotify = perfil_spotify