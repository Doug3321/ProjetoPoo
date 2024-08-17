class Musica:
    def __init__(self) -> None:
        self.__id = ''
        self.__nome = ''
        self.__url = ''
        self.__popularidade = 0
        self.__artista = []

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
    def popularidade(self):
        return self.__popularidade

    @popularidade.setter
    def popularidade(self, popularidade):
        self.__popularidade = popularidade
    
    @property
    def artista(self):
        return self.__artista

    @artista.setter
    def artista(self, artista):
        self.__artista = artista
        
    def __repr__(self) -> str:
        return f'Nome: {self.nome} --Artistas: {self.artista} --Popularidade: {self.popularidade} --Pagina Spotify: {self.url}\n'
