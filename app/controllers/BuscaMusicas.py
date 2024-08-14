from app.controllers.service.BuscaMusicaService import buscaMusicas

class BuscaMusicas:
  
  @staticmethod
  def buscaMusicas(query):
    try:
      lista = buscaMusicas(query)
      return lista
    except:
      raise Exception("Erro ao buscar musica")