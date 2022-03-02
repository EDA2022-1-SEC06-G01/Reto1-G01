"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import selectionsort as sl
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as me
from DISClib.Algorithms.Sorting import quicksort as qu
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipo_catalogo):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'tracks': None,
               'albums': None,
               'artists': None}

    tipo = None
    if tipo_catalogo.lower() == 'array_list':
        tipo = 'ARRAY_LIST'
    elif tipo_catalogo.lower() == 'single_linked':
        tipo = 'SINGLE_LINKED'

    catalog['tracks'] = lt.newList(tipo)
    catalog['albums'] = lt.newList(tipo)
    catalog['artists'] = lt.newList(tipo)

    return catalog

# Funciones para agregar informacion al catalogo

def addTrack(catalog, track):
    # Se adiciona el track a la lista de tracks
    t = newTrack(
        track['id'],
        track['href'],
        track['album_id'],
        track['key'],
        track['track_number'],
        track['artists_id'],
        track['energy'],
        track['loudness'],
        track['valence'],
        track['danceability'],
        track['playlist'],
        track['speechiness'],
        track['popularity'],
        track['liveness'],
        track['tempo'],
        track['duration_ms'],
        track['acousticness'],
        track['available_markets'],
        track['lyrics'],
        track['disc_number'],
        track['instrumentalness'],
        track['preview_url'],
        track['name']
        )
    lt.addLast(catalog['tracks'], t)
    return catalog


def addAlbum(catalog, albums):
    # Se adiciona el album a la lista de albums
    t = newAlbum(
        albums['id'],
        albums['track_id'],
        albums['total_tracks'],
        albums['external_urls'],
        albums['album_type'],
        albums['available_markets'],
        albums['artist_id'],
        albums['images'],
        albums['release_date'],
        albums['name'],
        albums['release_date_precision']
        )
    lt.addLast(catalog['albums'], t)
    return catalog


def addArtists(catalog, artist):
    # Se adiciona el album a la lista de albums
    t = newArtist(
        artist['id'],
        artist['track_id'],
        artist['artist_popularity'],
        artist['genres'],
        artist['name'],
        artist['followers']
        )
    lt.addLast(catalog['artists'], t)

# Funciones para creacion de datos

def newAlbum(
    id,
    track_id,
    total_tracks,
    external_urls,
    album_type,
    available_markets,
    artist_id,
    images,
    release_date,
    name,
    release_date_precision
    ):

    album = {
        'id': '',
        'track_id': '',
        'total_tracks': '',
        'external_urls': '',
        'album_type': '',
        'available_markets': '',
        'artist_id': '',
        'images': '',
        'release_date': '',
        'name': '',
        'release_date_precision': ''
            }

    album['id'] = id
    album['track_id'] = track_id
    album['total_tracks'] = total_tracks
    album['external_urls'] = external_urls
    album['album_type'] = album_type
    album['available_markets'] = available_markets
    album['artist_id'] = artist_id
    album['images'] = images
    album['release_date'] = release_date
    album['name'] = name
    album['release_date_precision'] = release_date_precision

    return album


def newTrack(
    id,
    href,
    album_id,
    key,
    track_number,
    artists_id,
    energy,
    loudness,
    valence,
    danceability,
    playlist,
    speechiness,
    popularity,
    liveness,
    tempo,
    duration_ms,
    acousticness,
    available_markets,
    lyrics,
    disc_number,
    instrumentalness,
    preview_url,
    name
    ):

    track = {
        'id': '',
        'href': '',
        'album_id': '',
        'key': '',
        'track_number': '',
        'artists_id': '',
        'energy': '',
        'loudness': '',
        'valence': '',
        'danceability': '',
        'playlist': '',
        'speechiness': '',
        'popularity': '',
        'liveness': '',
        'tempo': '',
        'duration_ms': '',
        'acousticness': '',
        'available_markets': '',
        'lyrics': '',
        'disc_number': '',
        'instrumentalness': '',
        'preview_url': '',
        'name': ''
            }

    track['id'] = id
    track['href'] = href
    track['album_id'] = album_id
    track['key'] = key
    track['track_number'] = track_number
    track['artists_id'] = artists_id
    track['energy'] = energy
    track['loudness'] = loudness
    track['valence'] = valence
    track['danceability'] = danceability
    track['playlist'] = playlist
    track['speechiness'] = speechiness
    track['popularity'] = popularity
    track['liveness'] = liveness
    track['tempo'] = tempo
    track['duration_ms'] = duration_ms
    track['acousticness'] = acousticness
    track['available_markets'] = available_markets
    track['lyrics'] = lyrics
    track['disc_number'] = disc_number
    track['instrumentalness'] = instrumentalness
    track['preview_url'] = preview_url
    track['name'] = name

    return track


def newArtist(
    id,
    track_id,
    artist_popularity,
    genres,
    name,
    followers
    ):

    artist = {
        'id': '',
        'track_id': '',
        'artist_popularity': '',
        'genres': '',
        'name': '',
        'followers': ''
            }

    artist['id'] = id
    artist['track_id'] = track_id
    artist['artist_popularity'] = artist_popularity
    artist['genres'] = genres
    artist['name'] = name
    artist['followers'] = followers

    return artist


# Funciones de consulta

def albumsSize(catalog):
    return lt.size(catalog['albums'])

def artistSize(catalog):
    return lt.size(catalog['artists'])

def trackSize(catalog):
    return lt.size(catalog['tracks'])

def firstThreeLastThree(catalog, type, list_size):
    firstThree = lt.subList(catalog[type], 1, 3)
    lastThree = lt.subList(catalog[type], list_size-2, 3)
    return firstThree, lastThree



# Funciones de ordenamiento
def ordenamientoSelection(catalog, criterio, funcion):
    start_time = getTime()
    organizado = sl.sort(catalog["model"][criterio], funcion)
    end_time = getTime()
    return deltaTime(start_time, end_time), organizado
    

def ordenamientoInsetion(catalog, criterio, funcion):
    start_time = getTime()
    organizado = ins.sort(catalog["model"][criterio], funcion)
    end_time = getTime()
    return deltaTime(start_time, end_time), organizado

def ordenamientoShell(catalog, criterio, funcion):
    start_time = getTime()
    organizado = sa.sort(catalog["model"][criterio], funcion)
    end_time = getTime()
    return deltaTime(start_time, end_time), organizado

def ordenamientoMerge(catalog, criterio, funcion):
    start_time = getTime()
    organizado = me.sort(catalog["model"][criterio], funcion)
    end_time = getTime()
    return deltaTime(start_time, end_time), organizado

def ordenamientoQuick(catalog, criterio, funcion):
    start_time = getTime()
    organizado = qu.sort(catalog["model"][criterio], funcion)
    end_time = getTime()
    return deltaTime(start_time, end_time), organizado




# Funciones para medir tiempos de ejecucion

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed