"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import config as cf
import sys
import csv
import controller
import csv
from DISClib.ADT import list as lt
from prettytable import PrettyTable
assert cf
import model

csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController(tipo_catalogo):

    control = controller.newController(tipo_catalogo)
    return control


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar los albumes en un periodo de tiempo")
    print("3- Encontrar los artistas mas pouplares")
    print("4- Encontrar las canciones mas populares")
    print("5- Encontrar la canción mas popular de un artista")
    print("6- Organizar con un tipo de ordenamiento iterativo")
    print("7- Encontrar la discografía de un artista")
    print("8- Clasificar las canciones con mayor distribución")
    print("0- Salir")


def loadData(tamanio_archivo):

    album, artist, track = controller.loadData(tamanio_archivo, control)
    return album, artist, track

# Prints
def print_artistFirstThreeLastThree(lista_primerosArtistas, lista_ultimosArtistas):
    x = PrettyTable()
    x.field_names = ['name', 'artist_popularity', 'Popularidad', 'Número de seguidores']
    
    if lista_primerosArtistas:
        for _ in range(1,4):
            datos_artista = lt.getElement(lista_primerosArtistas, _)
            x.add_row([
                datos_artista['name'],
                datos_artista['genres'],
                datos_artista['artist_popularity'],
                datos_artista['followers']
            ])

    if lista_ultimosArtistas:
        x.add_row(["...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "..."])
        for _ in range(1,4):
            datos_artista = lt.getElement(lista_ultimosArtistas, _)
            x.add_row([
                datos_artista['name'],
                datos_artista['genres'],
                datos_artista['artist_popularity'],
                datos_artista['followers']
            ])
            
    print(x.get_string())
    
def print_requerimiento2(lista, n):
    x = PrettyTable()
    x.field_names = ['artist_popularity', 'followers', 'name', 'relevant_track_name', 'genres']
    for _ in range(1, n):
        datos = lt.getElement(lista, _)
        x.add_row([
            datos['artist_popularity'],
            datos['followers'],
            datos['name'],
            controller.buscarCancionPorID(control, datos['track_id']),
            datos['genres']        
        ])
    print(x.get_string())


def print_albumFirstThreeLastThree(lista_primerosAlbums, lista_ultimosAlbums):
    x = PrettyTable()
    x.field_names = ['name', 'album_type', 'release_date']

    if lista_primerosAlbums:
        for _ in range(1,4):
            datos_albums = lt.getElement(lista_primerosAlbums, _)
            x.add_row([
                datos_albums['name'],
                datos_albums['album_type'],
                datos_albums['release_date']
            ])

    if lista_ultimosAlbums:
        x.add_row(["...", "...", "..."])
        x.add_row(["...", "...", "..."])
        x.add_row(["...", "...", "..."])
        for _ in range(1,4):
            datos_albums = lt.getElement(lista_ultimosAlbums, _)
            x.add_row([
                datos_albums['name'],
                datos_albums['album_type'],
                datos_albums['release_date']
            ])

    print(x.get_string())


def print_trackFirstThreeLastThree(lista_primerosAlbums, lista_ultimosAlbums):
    x = PrettyTable()
    x.field_names = ['name', 'popularity', 'disc_number', 'track_number', 'duration_ms', 'href']

    if lista_primerosAlbums:
        for _ in range(1,4):
            datos_albums = lt.getElement(lista_primerosAlbums, _)
            x.add_row([
                datos_albums['name'],
                datos_albums['popularity'],
                datos_albums['disc_number'],
                datos_albums['track_number'],
                datos_albums['duration_ms'],
                datos_albums['href'],
            ])

    if lista_ultimosAlbums:
        x.add_row(["...", "...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "...", "..."])
        for _ in range(1,4):
            datos_albums = lt.getElement(lista_ultimosAlbums, _)
            x.add_row([
                datos_albums['name'],
                datos_albums['popularity'],
                datos_albums['disc_number'],
                datos_albums['track_number'],
                datos_albums['duration_ms'],
                datos_albums['href'],
            ])

    print(x.get_string())


control = newController("SINGLE_LINKED")
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo_catalogo = input("Con que tipo de representacion de lista quieres cargar el catalogo (ARRAY_LIST / SINGLE_LINKED): ")
        control = newController(tipo_catalogo)

        tamanio_archivo_input = input("Con que tipo tamaño quieres cargar el archivo (5, 10, 20, 30, 50, 80, small, large): ")
        if tamanio_archivo_input.isnumeric() == True:
            tamanio_archivo_input = tamanio_archivo_input+"pct"
        else:
            tamanio_archivo_input = tamanio_archivo_input
        album_size, artist_size, track_size = loadData(tamanio_archivo_input)
        
        artistFirstThree, artistLastThree = controller.FirstThreeLastThree(control["model"]["artists"], artist_size)
        albumFirstThree, albumLastThree = controller.FirstThreeLastThree(control["model"]["albums"], album_size)
        trackFirstThree, trackLastThree = controller.FirstThreeLastThree(control["model"]["tracks"], track_size)

        print("\nCargando información de los archivos ....\n")
        
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print('artist id count: ' + str(artist_size))
        print('albums id count: ' + str(album_size))
        print('tracks id count: ' + str(track_size))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        print("\n\nThe first 3 and last 3 artists in the range are...")
        print_artistFirstThreeLastThree(artistFirstThree, artistLastThree)
        print("\n\nThe first 3 and last 3 albums in the range are...")
        print_albumFirstThreeLastThree(albumFirstThree, albumLastThree)
        print("\n\nThe first 3 and last 3 tracks in the range are...")
        print_trackFirstThreeLastThree(trackFirstThree, trackLastThree)


    elif int(inputs[0]) == 2:
        inicial, final = input("fechas con espacio: ").split()
        organized = controller.ordenamientoMerge_Requerimiento1(control)
        index_anio_inicial = controller.interpolationSearch_Requerimiento1(organized, 1, lt.size(organized), inicial, True)
        index_anio_final = controller.interpolationSearch_Requerimiento1(organized, 1, lt.size(organized), final, False)
        sublista = lt.subList(organized, index_anio_inicial, (index_anio_final - index_anio_inicial))
        albumFirstThree, albumLastThree = controller.FirstThreeLastThree(sublista, controller.listSize(sublista))
        print_albumFirstThreeLastThree(albumFirstThree, albumLastThree)


    elif int(inputs[0]) == 3:
        n = int(input("Ingrese la cantidad de artistas que quiere en su top: "))
        organized = controller.ordenamientoShell_Requerimiento2(control)
        top_n = lt.subList(organized, 1, n)
        print_requerimiento2(top_n, controller.listSize(top_n))
        albumFirstThree, albumLastThree = controller.FirstThreeLastThree(top_n, controller.listSize(top_n))
        print_artistFirstThreeLastThree(albumFirstThree, albumLastThree)

    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        tipo = input("Escoje un tipo de ordenamiento (selection, insertion, shell, merge o quick): ")
        criterio = "artists"
        funcion = controller.cmpArtistsByFollowers
        if tipo.lower() == "selection":
            tiempo, organizado = controller.ordenamientoSelection(control, criterio, funcion)
            print(f"El tiempo que tomo el ordenamiento Selection en organizar los datos fue {tiempo}")

        elif tipo.lower() == "insertion":
            tiempo, organizado = controller.ordenamientoInsetion(control, criterio, funcion)
            print(f"El tiempo que tomo el ordenamiento Insertion en organizar los datos fue {tiempo}")

        elif tipo.lower() == "shell":
            tiempo, organizado = controller.ordenamientoShell(control, criterio, funcion)
            print(f"El tiempo que tomo el ordenamiento Shell en organizar los datos fue {tiempo}")

        elif tipo.lower() == "merge":
             tiempo, organizado = controller.ordenamientoMerge(control, criterio, funcion)
             print(f"El tiempo que tomo el ordenamiento Merge en organizar los datos fue {tiempo}")

        elif tipo.lower() == "quick":
             tiempo, organizado = controller.ordenamientoQuick(control, criterio, funcion)
             print(f"El tiempo que tomo el ordenamiento Quick en organizar los datos fue {tiempo}")

        else: 
            print("Intente un nombre válido")

    elif int(inputs[0]) == 7:
        pass
    elif int(inputs[0]) == 8:
        pass
    else:
        sys.exit(0)
sys.exit(0)
