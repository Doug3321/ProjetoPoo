from app.controllers.service.SpotifyService import SpotifyService as ss
from app.models.Musica import Musica

def buscaMusicas(query):
  listaMusicas = ss.sp.search(q=query, limit=3, type='track')
  musicas = []
  
  for e in listaMusicas['tracks']['items']:
    musica = Musica()
    musica.id = e['id']
    musica.nome = e['name']
    musica.popularidade = e['popularity']
    musica.url = e['external_urls']['spotify']
    musica.artista_nome = e['artists'][0]['name']
    
    musicas.append(musica)
  
  return musicas
    