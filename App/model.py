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
    organizado = sa.sort(catalog["model"][criterio], funcion)
    end_time = getTime()
    return deltaTime(start_time, end_time), organizado

def ordenamientoQuick(catalog, criterio, funcion):
    start_time = getTime()
    organizado = sa.sort(catalog["model"][criterio], funcion)
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