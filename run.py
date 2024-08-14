from app.controllers.BuscaMusicas import BuscaMusicas

def main():
  print("Informe o titulo, nome, ano, artista ou album da musica")
  query = input("Pesquisa: ")
  
  lista = BuscaMusicas.buscaMusicas(query)
  
  print(lista)
  
if __name__ == "__main__":
  main()