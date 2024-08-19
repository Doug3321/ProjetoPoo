from app.controllers.BuscaMusicas import BuscaMusicas
from app.controllers.BuscaArtistas import BuscaArtistas
from app.views.interface import create_interface

def main():
  #print("Informe o titulo, nome, ano, artista da musica")
  #query = input("Pesquisa: ")
  
  #print("Informe o titulo, nome, ano, artista ou generos do artista")
  #query = input("Pesquisa:")
  
  #listaMusicas = BuscaMusicas.buscaMusicas(query, 2)
  #listaArtistas = BuscaArtistas.buscaArtistas(query, 2)
  #print(listaMusicas)
  #print('Codigo principal')
  create_interface()

if __name__ == "__main__":
  main()