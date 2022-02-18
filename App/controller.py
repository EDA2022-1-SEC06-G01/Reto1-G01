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

def newController():

    control = {'model':None
    }

    control['model'] = model.newCatalog()
    return control

# Funciones para la carga de datos

def loadData(control):

    catalog = control['model']
    album = loadAlbums(catalog)
    artist = loadArtists(catalog)
    track = loadTracks(catalog)
        
    return album, artist, track, catalog

def loadAlbums(catalog):

    albumsfile = cf.data_dir + 'spotify-albums-utf8-small.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for album in reader:
      model.addAlbum(catalog, album)
    return model.albumsSize(catalog)
    
def loadArtists(catalog):

    albumsfile = cf.data_dir + 'spotify-artists-utf8-small.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for artist in reader:
      model.addArtists(catalog, artist)
    return model.artistSize(catalog)

def loadTracks(catalog):

    albumsfile = cf.data_dir + 'spotify-tracks-utf8-small.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for track in reader:
      model.addTrack(catalog, track)
    return model.trackSize(catalog)


# Funciones para la creacion de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def artistFirst3Last3(catalog):
  data = model.artistFirst3Last3(catalog)
  return data

def albumFirst3Last3(catalog):
  data = model.albumFirst3Last3(catalog)
  return data

def trackFirst3Last3(catalog):
  data = model.trackFirst3Last3(catalog)
  return data

