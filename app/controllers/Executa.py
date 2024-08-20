from app.controllers.BuscaMusicas import BuscaMusicas
from app.controllers.BuscaArtistas import BuscaArtistas
from app.controllers.BuscaAlbum import BuscaAlbum

from app.models.exceptions.LimitException import LimitException
from app.models.exceptions.QueryException import QueryException


class Executa:
  
  def testaQuery(self, query):
    if query == None:
      raise QueryException('Não passou nenhuma parâmetro.')
  
  def testaQuant(self, quant):
    if quant > 20 or quant < 1:
      raise LimitException('Quantidade invalidas! Escolha entre 1 ~ 20.')
  
  def busca(self, search_type, query, quant):
    try:
      self.testaQuery(query)
      self.testaQuant(quant)
      
      if search_type == "Song":
        listaMusicas = BuscaMusicas.buscaMusicas(query, quant)
        return (listaMusicas, 'song')
      
      elif search_type == "Artist":
        listaArtistas = BuscaArtistas.buscaArtistas(query, quant)
        return (listaArtistas, 'artist')
      
      elif search_type == "Album":
        listaAlbuns = BuscaAlbum.buscaAlbuns(query, quant)
        return (listaAlbuns, 'album')
      
    except QueryException as qe:
      return f'{qe}'
    except LimitException as le:
      return f'{le}'
    except Exception as e:
      return f'{e}'
      