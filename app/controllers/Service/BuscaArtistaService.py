from app.controllers.Service.SpotifyService import SpotifyService as ss

from app.models.Artista import Artista

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
    
      artistas.append(artista)
  
    return artistas