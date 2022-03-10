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
 """

from matplotlib import artist
from DISClib.ADT import list as lt
import config as cf
import model
import csv
import sys

csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def newController(tipo_catalogo):

    control = {'model':None
    }

    control['model'] = model.newCatalog(tipo_catalogo)
    model.ordenamientoShell(control['model']["tracks"], model.cmpTracksIDs)
    model.ordenamientoShell(control['model']["albums"], model.cmpAlbumsIDs)
    model.ordenamientoShell(control['model']["artists"], model.cmpArtistsIDs)
    return control

# Funciones para la carga de datos

def loadData(tamanio_archivo ,control):

    album_size = loadAlbums(tamanio_archivo, control)
    artist_size = loadArtists(tamanio_archivo, control)
    track_size = loadTracks(tamanio_archivo, control)
    
    return album_size, artist_size, track_size


def loadAlbums(tamanio_archivo, control):

    albumsfile = cf.data_dir + f'spotify-albums-utf8-{tamanio_archivo}.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for album in reader:
      model.addAlbum(control, album)
    return model.listSize(control["model"]['albums'])
    

def loadArtists(tamanio_archivo, control):

    albumsfile = cf.data_dir + f'spotify-artists-utf8-{tamanio_archivo}.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for artist in reader:
      model.addArtists(control, artist)
    return model.listSize(control["model"]['artists'])


def loadTracks(tamanio_archivo, control):

    albumsfile = cf.data_dir + f'spotify-tracks-utf8-{tamanio_archivo}.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for track in reader:
      model.addTrack(control, track)
    return model.listSize(control["model"]['tracks'])


# Funciones para la creacion de datos

def getAlbumID(lst) -> list:
  return model.getAlbumID(lst)

def linearSearch_Requerimiento6(lst, AlbumIDList):
  return model.linearSearch_Requerimiento6(lst, AlbumIDList)

# Funciones de ordenamiento
def ordenamientoSelection(control, funcion):
  return model.ordenamientoSelection(control, funcion)

def ordenamientoInsetion(control, funcion):
  return model.ordenamientoInsetion(control, funcion)

def ordenamientoShell(lst, funcion):
  return model.ordenamientoShell(lst, funcion)

def ordenamientoMerge(control, funcion):
  return model.ordenamientoMerge(control, funcion)

def ordenamientoQuick(control, funcion):
  return model.ordenamientoQuick(control, funcion)

# Funciones de consulta sobre el catálogo

def FirstThreeLastThree(list, list_size):
  firstThree, lastThree = model.firstThreeLastThree(list, list_size)
  return firstThree, lastThree

def listSize(list):
  return model.listSize(list)

def interpolationSearch_Requerimiento1(lst, pos1, lst_size, elementToFind, primeroUltimo):
  return model.interpolationSearch_Requerimiento1(lst, pos1, lst_size, elementToFind, primeroUltimo)

def BuscarTracksTOP(control, top):
  criterio = "tracks"
  ordenado = ordenamientoMerge(control, criterio, cmpTracksPopularity)
  TopTracks = model.buscarTracksTOP(ordenado, top)
  return TopTracks

def listaArtistasID(lst, datos):
  
  lista = model.ordenamientoMerge(lst,"artists", (model.cmpArtistsID_tracksID,))
  string = ""
  for i in datos:
    string += lt.getElement(lista, model.binarySearch(lista, i, "id"))["name"] + ", "
  return string

  
def binarySearch(lst, elemento, elementoDiccionario):
  return model.binarySearch(lst, elemento, elementoDiccionario)

# generalizarlo
def binarySearchLimites_tracks(control, elemento, primeroUltimo):
  return model.binarySearchLimites(control["model"]["tracks"], elemento, "artists_id", primeroUltimo)

def linearSearch_Requerimiento4(lst, element, mercado):
  return model.linearSearch_Requerimiento4(lst, element, mercado)

def contador_elementos(lst, element):
  return model.contador_elementos(lst, element)

def agregarNombreArtista_TrackName(lst, lstArtists, lstTracks):
  for _ in lt.iterator(lst):
    ArtistID = _["artist_id"]
    _["artist_name"] = lt.getElement(lstArtists, binarySearch(lstArtists, ArtistID, "id"))["name"]

# Funciones de comparacion
def cmpArtistsByFollowers(artist1, artist2):
  return model.cmpArtistsByFollowers(artist1, artist2)

def cmpTracksPopularity(track1, track2):
  return model.cmpTracksPopularity(track1, track2)



def buscarCancionPorID(control, elementoBuscado):
  lista_ordenada = model.ordenamientoShell(control["model"]["albums"], "tracks", model.cmpIDTracks)
  index = model.binarySearch(lista_ordenada, elementoBuscado, "id")
  if index == -1:
    return "Not found"
  else:
    return lt.getElement(lista_ordenada, index)["name"]

def albumName_Requerimiento4(control, elemento):
  lista = model.ordenamientoShell(control["model"]["albums"], model.cmpAlbumsIDs)
  return lt.getElement(lista ,binarySearch(lista, elemento, "id"))["name"]

def listaArtistas_IDaNombre(control, lista_artistas):
  lista = model.ordenamientoShell(control["model"]["artists"] , model.cmpArtistsID_tracksID)
  string = ""
  for i in lista_artistas:
    string += lt.getElement(lista, binarySearch(lista, i, "id"))["name"] + ", "
  return string[:-2]

def buscarIDArtista(control, elementoBuscado):
  lista_ordenada = model.ordenamientoShell(control["model"]["artists"] , model.cmpArtistsByName)
  index = model.binarySearch(lista_ordenada, elementoBuscado, "name")
  if index == -1:
    return "Not found"
  else:
    return lt.getElement(lista_ordenada, index)["id"]
