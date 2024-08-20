from app.controllers.service.BuscaMusicaService import BuscaMusicaService as bm

class BuscaMusicas:
  
  @staticmethod
  def buscaMusicas(query, quant):
    try:
      lista = bm.buscaMusicas(query, quant)
      return lista
    except:
      raise Exception('Erro ao buscar Musicas')