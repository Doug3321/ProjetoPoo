from app.controllers.service.SpotifyService import SpotifyService as ss

from app.models.Artista import Artista
from app.models.Foto import Foto
class BuscaArtistaService:
  
  @staticmethod
  def buscaArtista(id) -> Artista:
    dataArtista = ss.sp.artist(artist_id=id)
    artista = Artista()
    
    artista.id = id
    artista.generos = dataArtista['genres']
    artista.nome = dataArtista['name']
    artista.popularidade = dataArtista['popularity']
    artista.url = dataArtista['external_urls']['spotify']
    artista.seguidores = dataArtista['followers']['total']
    artista.foto = Foto(dataArtista['images'][0]['url'], dataArtista['images'][0]['height'], dataArtista['images'][0]['width'])
    return artista
  
  @staticmethod
  def buscaArtistas(query, quant) -> list:
    listaArtistas = ss.sp.search(q=query, limit=quant, type='artist')
    artistas = []

    print(listaArtistas)
    for e in listaArtistas['artists']['items']:
      artista = Artista()
      artista.id = e['id']
      artista.nome = e['name']
      artista.popularidade = e['popularity']
      artista.url = e['external_urls']['spotify']
      artista.seguidores = e['followers']['total']
      artista.generos = e['genres']
      artista.foto = Foto(e['images'][0]['url'], e['images'][0]['height'], e['images'][0]['width'])
    
      artistas.append(artista)
  
    return artistas