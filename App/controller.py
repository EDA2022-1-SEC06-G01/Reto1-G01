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
import config as cf
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def newController(tipo_catalogo):

    control = {'model':None
    }

    control['model'] = model.newCatalog(tipo_catalogo)
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

# Funciones de ordenamiento
def ordenamientoSelection(control, criterio, funcion):
  return model.ordenamientoSelection(control, criterio, funcion)


def ordenamientoInsetion(control, criterio, funcion):
  return model.ordenamientoInsetion(control, criterio, funcion)


def ordenamientoShell(control, criterio, funcion):
  return model.ordenamientoShell(control, criterio, funcion)


def ordenamientoMerge(control, criterio, funcion):
  return model.ordenamientoMerge(control, criterio, funcion)


def ordenamientoQuick(control, criterio, funcion):
  return model.ordenamientoQuick(control, criterio, funcion)

# Funciones de consulta sobre el catálogo

def FirstThreeLastThree(list, list_size):
  firstThree, lastThree = model.firstThreeLastThree(list, list_size)
  return firstThree, lastThree

def listSize(list):
  return model.listSize(list)

# Funciones de comparacion
def cmpArtistsByFollowers(artist1, artist2):
  return model.cmpArtistsByFollowers(artist1, artist2)

def cmpYears(date1, date2):
  return model.cmpYears(date1, date2)
