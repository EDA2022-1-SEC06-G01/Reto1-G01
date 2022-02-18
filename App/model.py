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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'tracks': None,
               'albums': None,
               'artists': None}

    catalog['tracks'] = lt.newList('ARRAY_LIST')
    catalog['albums'] = lt.newList('ARRAY_LIST')
    catalog['artists'] = lt.newList('ARRAY_LIST')

    return catalog

# Funciones para agregar informacion al catalogo

def addTrack(catalog, track):
    # Se adiciona el track a la lista de tracks
    t = newTrack(track['name'], track['available_markets'], track['duration_ms'], track['track_number'])
    lt.addLast(catalog['tracks'], t)
    return catalog

def addAlbum(catalog, albums):
    # Se adiciona el album a la lista de albums
    t = newAlbum(albums['name'], albums['available_markets'], albums['release_date'], albums['release_date'])
    lt.addLast(catalog['albums'], t)
    return catalog

def addArtists(catalog, artist):
    # Se adiciona el album a la lista de albums
    t = newArtist(artist['name'], artist['genres'], artist['artist_popularity'], artist['followers'])
    lt.addLast(catalog['artists'], t)

# Funciones para creacion de datos

def newAlbum(nombre, tipo, disponibilidad, lanzamiento):

    album = {'nombre': '',
             'tipo': '',
             'disp': '',
             'lanz': ''
            }

    album['nombre'] = nombre
    album['tipo'] = tipo
    album['disp'] = disponibilidad
    album['lanz'] = lanzamiento

    return album

def newTrack(nombre, disponibilidad, duracion, cancion):

    track = {'nombre': '',
             'disponibilidad': '',
             'duracion': '',
             'cancion': ''
            }
    track['nombre'] = nombre
    track['disponibilidad'] = disponibilidad
    track['duracion'] = duracion
    track['numero_cancion'] = cancion
    return track

def newArtist(nombre, generos, popularidad, seguidores):

    artist = {'nombre': '',
              'generos': '',
              'popularidad': '',
              'seguidores': ''
            }
    artist['nombre'] = nombre
    artist['generos'] = generos
    artist['popularidad'] = popularidad
    artist['seguidores'] = seguidores
    return artist

# Funciones de consulta

def albumsSize(catalog):
    return lt.size(catalog['albums'])

def artistSize(catalog):
    return lt.size(catalog['artists'])

def trackSize(catalog):
    return lt.size(catalog['tracks'])

def albumFirst3Last3(catalog):
    lst = catalog["albums"]["elements"]
    lista = []
    for i in range(0,3):
        lista.append(lst[i])
    for _ in range(2,-1,-1):
        lista.append(lst[-_-1])
    return lista

def artistFirst3Last3(catalog):
    lst = catalog["artists"]["elements"]
    lista = []
    for i in range(0,3):
        lista.append(lst[i])
    for _ in range(2,-1,-1):
        lista.append(lst[-_-1])
    return lista

def trackFirst3Last3(catalog):
    lst = catalog["tracks"]["elements"]
    lista = []
    for i in range(0,3):
        lista.append(lst[i])
    for _ in range(2,-1,-1):
        lista.append(lst[-_-1])
    return lista

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento