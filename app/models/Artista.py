class Artista:
    def __init__(self) -> None:
        self.__id = ''
        self.__nome = ''
        self.__url = ''
        self.__generos = ''
        self.__popularidade = 0
        self.__seguidores = 0
        self.__foto = ''

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
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def generos(self):
        return self.__generos

    @generos.setter
    def generos(self, generos):
        self.__generos = generos
    @property
    def popularidade(self):
        return self.__popularidade

    @popularidade.setter
    def popularidade(self, popularidade):
        self.__popularidade = popularidade

    @property
    def seguidores(self):
        return self.__seguidores

    @seguidores.setter
    def seguidores(self, seguidores):
        self.__seguidores = seguidores
        
    @property
    def foto(self):
        return self.__foto

    @foto.setter
    def foto(self, foto):
        self.__foto = foto

    def __repr__(self) -> str:
        return f'Nome: {self.nome} - Seguidores: {self.seguidores} - Generos: {self.generos} - Pagina Spotify: {self.url}\n'