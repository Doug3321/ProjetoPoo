class Album:
    def __init__(self):
        self.__id = str()
        self.__data = str()
        self.__nome = str()
        self.__musicas = list()
        self.__artistas = list()
        self.__generos = list()
        self.__fotos = list()
        self.__url = str()

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def artistas(self):
        return self.__artistas

    @artistas.setter
    def artistas(self, artista):
        self.__artistas.append(artista)

    @property
    def musicas(self):
        return self.__musicas

    @musicas.setter
    def musicas(self, musica):
        self.__musicas.append(musica)

    @property
    def generos(self):
        return self.__generos

    @generos.setter
    def generos(self, generos):
        self.__generos = generos
    
    @property
    def fotos(self):
        return self.__fotos

    @fotos.setter
    def fotos(self, foto):
        self.__fotos.append(foto)
        
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.url = url
