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

    catalog = control['model']
    album_size = loadAlbums(tamanio_archivo, catalog)
    artist_size = loadArtists(tamanio_archivo, catalog)
    track_size = loadTracks(tamanio_archivo, catalog)
    
    return album_size, artist_size, track_size, catalog


def loadAlbums(tamanio_archivo, catalog):

    albumsfile = cf.data_dir + f'spotify-albums-utf8-{tamanio_archivo}.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for album in reader:
      model.addAlbum(catalog, album)
    return model.albumsSize(catalog)
    
def loadArtists(tamanio_archivo, catalog):

    albumsfile = cf.data_dir + f'spotify-artists-utf8-{tamanio_archivo}.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for artist in reader:
      model.addArtists(catalog, artist)
    return model.artistSize(catalog)

def loadTracks(tamanio_archivo, catalog):

    albumsfile = cf.data_dir + f'spotify-tracks-utf8-{tamanio_archivo}.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for track in reader:
      model.addTrack(catalog, track)
    return model.trackSize(catalog)


# Funciones para la creacion de datos

# Funciones de ordenamiento
def ordenamientoSelection(catalog):
  return model.ordenamientoSelection(catalog)

def ordenamientoInsetion(catalog):
  return model.ordenamientoInsetion(catalog)

def ordenamientoShell(catalog):
  return model.ordenamientoShell(catalog)

# Funciones de consulta sobre el catálogo

def artistFirstThreeLastThree(catalog, list_size):
  firstThree, lastThree = model.firstThreeLastThree(catalog, "artists", list_size)
  return firstThree, lastThree

def albumFirstThreeLastThree(catalog, list_size):
  firstThree, lastThree = model.firstThreeLastThree(catalog, "albums", list_size)
  return firstThree, lastThree

def trackFirstThreeLastThree(catalog, list_size):
  firstThree, lastThree = model.firstThreeLastThree(catalog, "tracks", list_size)
  return firstThree, lastThree

