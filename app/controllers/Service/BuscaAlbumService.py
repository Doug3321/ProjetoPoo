from models import Album
import SpotifyService as ss
busca = ss.sp

import BuscaMusicasService as buscaMusica
import BuscaArtistasService as buscaArtista

class BuscaAlbumService:
  
  @staticmethod
  def buscaAlbum(id) -> Album:
    try:
      busca.getAlbum(id = id)
    except:
      raise Exception("Erro ao buscar álbum")
  
  
  @staticmethod
  def buscaAlbums(query) -> list:
    try:
      dataAlbuns = busca.Search(q=query, market=None, type='album')
      albuns = list()
      
      for i in dataAlbuns['albums']['items']:
        album = Album()
        album.id = i['id']
        album.data = i['release_date']
        album.nome = i['name']
        #album.artistas = buscaArtista.getArtista(i['artists']['id'])
        #album.fotos = i['images']
        album.url = i['url']
        #album.generos = i['']
        
        albuns.append(album)
      
      return albuns
    except:
      raise Exception("Erro ao tentar buscar álbuns")