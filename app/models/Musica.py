class Musica:
    def __init__(self):
        self.__id = ''
        self.__nome = ''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def artista(self):
        return self.__artista

    @artista.setter
    def artista(self, artista):
        self.__artista = artista

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @property
    def album(self):
        return self.__album

    @album.setter
    def album(self, album):
        self.__album = album
