from app.controllers.BuscaMusicas import BuscaMusicas
from app.controllers.BuscaArtistas import BuscaArtistas
from app.controllers.BuscaAlbum import BuscaAlbum
def main():
  print("Informe o titulo, nome, ano, artista da musica")
  query = input("Pesquisa: ")
  
  #print("Informe o titulo, ano, artista ou generos do artista")
  #query = input("Pesquisa: ")
  
  #print("Informe o titulo, ano, artista ou generos do álbum")
  #query = input("Pesquisa: ")
  
  lista = BuscaMusicas.buscaMusicas(query, 2)
  #lista = BuscaArtistas.buscaArtistas(query, 2)
  #lista = BuscaAlbum.buscaAlbuns(query, 2)
  print('')
  
  for i in lista:
    print(i)
    print('----------------------------------')
  
if __name__ == "__main__":
  main()