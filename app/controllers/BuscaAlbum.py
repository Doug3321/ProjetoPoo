from app.controllers.service.BuscaAlbumService import BuscaAlbumService as ba

class BuscaAlbum:
  @staticmethod
  def buscaAlbuns(query, quant):
    try:
      lista = ba.buscaAlbuns(query, quant)
      return lista
    except:
      raise Exception("Erro ao buscar álbuns")
    