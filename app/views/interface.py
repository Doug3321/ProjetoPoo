# app/views/interface.py
import tkinter as tk
from tkinter import font as tkfont
from app.controllers.BuscaMusicas import BuscaMusicas
from app.controllers.BuscaArtistas import BuscaArtistas
from app.controllers.BuscaAlbum import BuscaAlbum
import webbrowser

def search():
    query = query_entry.get()
    search_type = search_var.get()

    if search_type == "Song":
        listaMusicas = BuscaMusicas.buscaMusicas(query, 6)
        display_results(listaMusicas, 'song')
    elif search_type == "Artist":
        listaArtistas = BuscaArtistas.buscaArtistas(query, 6)
        display_results(listaArtistas, 'artist')
    elif search_type == "Album":
        listaAlbuns = BuscaAlbum.buscaAlbuns(query, 6)
        display_results(listaAlbuns, 'album')

def display_results(lista, type):
    song_canvas.delete("all")

    y_position = 10
    for item in lista:
        if type == 'song':
            display_text = f"Name: {item.nome}\nArtists: {', '.join([artist.nome for artist in item.artista])}\nPopularity: {item.popularidade}\nSpotify: {item.url}"
        elif type == 'artist':
            display_text = f"Name: {item.nome}\nGenres: {', '.join(item.generos)}\nPopularity: {item.popularidade}\nFollowers: {item.seguidores}\nSpotify: {item.url}"
        elif type == 'album':
            display_text = f"Name: {item.nome}\nNumber of Songs: {item.num_musicas}\nRelease Date: {item.data_lancamento}\nSpotify: {item.url}"
        
        # Create a frame for the card
        card_frame = tk.Frame(song_canvas, bg='#ffffff', bd=2, relief=tk.RAISED, width=780)
        card_frame.place(x=10, y=y_position, width=780, height=100)

        # Add item details to the card
        tk.Label(card_frame, text=display_text, font=custom_font, bg='#ffffff').pack(anchor='w', padx=10, pady=5)
        if type in ['song', 'artist', 'album']:
            link_label = tk.Label(card_frame, text="Listen on Spotify", font=custom_font, fg='#1DB954', bg='#ffffff', cursor="hand2")
            link_label.pack(anchor='w', padx=10, pady=5)
            link_label.bind("<Button-1>", lambda e, url=item.url: webbrowser.open(url))
        
        y_position += 120

    song_canvas.config(scrollregion=song_canvas.bbox("all"))

def create_interface():
    root = tk.Tk()
    root.title("Spotify Search")

    root.geometry("800x600")
    root.configure(bg='#f0f0f0')

    global custom_font
    custom_font = tkfont.Font(family="Helvetica", size=12)

    query_label = tk.Label(root, text="Enter search query:", font=custom_font, bg='#f0f0f0')
    query_label.pack(pady=10)

    global query_entry
    query_entry = tk.Entry(root, font=custom_font, width=70)
    query_entry.pack(pady=10)

    global search_var
    search_var = tk.StringVar(value="Song")

    search_type_frame = tk.Frame(root, bg='#f0f0f0')
    search_type_frame.pack(pady=10)
    tk.Radiobutton(search_type_frame, text="Song", variable=search_var, value="Song", font=custom_font, bg='#f0f0f0').pack(side=tk.LEFT, padx=10)
    tk.Radiobutton(search_type_frame, text="Artist", variable=search_var, value="Artist", font=custom_font, bg='#f0f0f0').pack(side=tk.LEFT, padx=10)
    tk.Radiobutton(search_type_frame, text="Album", variable=search_var, value="Album", font=custom_font, bg='#f0f0f0').pack(side=tk.LEFT, padx=10)

    search_button = tk.Button(root, text="Search", font=custom_font, command=search, bg='#4CAF50', fg='white', relief=tk.RAISED)
    search_button.pack(pady=10)

    global song_canvas
    song_canvas = tk.Canvas(root, bg='#f0f0f0')
    song_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=song_canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    song_canvas.config(yscrollcommand=scrollbar.set)

    canvas_frame = tk.Frame(song_canvas, bg='#f0f0f0')
    song_canvas.create_window((0, 0), window=canvas_frame, anchor='nw')

    global song_frame
    song_frame = canvas_frame

    root.bind("<Configure>", lambda e: song_canvas.config(scrollregion=song_canvas.bbox("all")))

    root.mainloop()

if __name__ == "__main__":
    create_interface()
