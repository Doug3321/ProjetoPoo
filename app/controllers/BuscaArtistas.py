from app.controllers.Service.BuscaArtistaService import BuscaArtistaService as ba

class BuscaArtistas:
  
  @staticmethod
  def buscaArtistas(query, quant):
    try:
      lista = ba.buscaArtistas(query, quant)
      return lista
    except:
      raise Exception("Erro ao buscar Artistas")