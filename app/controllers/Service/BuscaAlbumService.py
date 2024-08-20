from app.controllers.service.SpotifyService import SpotifyService as ss

from app.controllers.service.BuscaArtistaService import BuscaArtistaService as bas
from app.models.Album import Album
from app.models.Foto import Foto

class BuscaAlbumService:
  @staticmethod
  def buscaAlbuns(query, quant) -> list:
    listaAlbuns = ss.sp.search(q=query, limit=quant, type='album')
    albuns = []
  
    for e in listaAlbuns['albums']['items']:
      album = Album()
      album.id = e['id']
      album.num_musicas = e['total_tracks']
      album.url = e['external_urls']['spotify']
      album.nome = e['name']
      album.data_lancamento = e['release_date']
      album.foto = Foto(e['images'][0]['url'], e['images'][0]['height'], e['images'][0]['width'])
      
      for art in e['artists']:
        valor = bas.buscaArtista(art['id'])
        album.artistas.append(valor)
    
      albuns.append(album)
  
    return albuns
  