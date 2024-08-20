class Album:
    def __init__(self) -> None:
        self.__id = ''
        self.__nome = ''
        self.__url = ''
        self.__num_musicas = 0
        self.__data_lancamento = ''
        self.__artistas = []
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
    def num_musicas(self):
        return self.__num_musicas

    @num_musicas.setter
    def num_musicas(self, num_musicas):
        self.__num_musicas = num_musicas

    @property
    def data_lancamento(self):
        return self.__data_lancamento

    @data_lancamento.setter
    def data_lancamento(self, data_lancamento):
        self.__data_lancamento = data_lancamento

    @property
    def artistas(self):
        return self.__artistas

    @artistas.setter
    def artistas(self, artistas):
        self.__artistas = artistas
        
    @property
    def foto(self):
        return self.__foto

    @foto.setter
    def foto(self, foto):
        self.__foto = foto

    def __repr__(self) -> str:
        return f'Nome: {self.nome} --Artistas: {self.artistas} --Data de lançamento: {self.data_lancamento} --Número de musicas: {self.num_musicas} --Pagina Spotify: {self.url}\n'