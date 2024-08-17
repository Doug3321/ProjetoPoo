from app.controllers.service.SpotifyService import SpotifyService as ss

from app.controllers.service.BuscaArtistaService import BuscaArtistaService as bas
from app.models.Musica import Musica

class BuscaMusicaService:

  @staticmethod
  def buscaMusica(id) -> Musica:
    dataMusica = ss.sp.track(track_id=id)
    musica = Musica()
    
    musica.id = id
    musica.nome = dataMusica['name']
    musica.popularidade =  dataMusica['popularity']
    musica.url = dataMusica['external_urls']['spotify']
    for art in dataMusica['artists']:
      valor = bas.buscaArtista(art['id'])
      musica.artista.append(valor)
    
    return musica
  
  @staticmethod
  def buscaMusicas(query, quant) -> list:
    listaMusicas = ss.sp.search(q=query, limit=quant, type='track')
    musicas = []
  
    for e in listaMusicas['tracks']['items']:
      musica = Musica()
      musica.id = e['id']
      musica.nome = e['name']
      musica.popularidade = e['popularity']
      musica.url = e['external_urls']['spotify']
      
      for art in e['artists']:
        valor = bas.buscaArtista(art['id'])
        musica.artista.append(valor)
    
      musicas.append(musica)
  
    return musicas
    