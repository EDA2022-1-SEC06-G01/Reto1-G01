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
import controller
from DISClib.ADT import list as lt
from prettytable import PrettyTable
assert cf


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

    album, artist, track, catalogo = controller.loadData(tamanio_archivo, control)
    return album, artist, track, catalogo


def printArtists(lista_primerosArtistas, lista_ultimosArtistas):
    x = PrettyTable()
    x.title = "Primeros 3 y ultimos 3 artistas"
    x.field_names = ['Nombre', 'Géneros', 'Popularidad', 'Número de seguidores']
    if lista_primerosArtistas:
        for _ in range(1,4):
            datos_artista = lt.getElement(lista_primerosArtistas, _)
            genero = datos_artista['generos'].replace("[", "").replace("]", "").replace("'", "")
            x.add_row([datos_artista['nombre'],
            genero if len(genero) != 0 else "Ninguno",
            datos_artista['popularidad'], datos_artista['seguidores']
            ])
    if lista_ultimosArtistas:
        x.add_row(["...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "..."])
        for _ in range(1,4):
            datos_artista = lt.getElement(lista_ultimosArtistas, _)
            genero = datos_artista['generos'].replace("[", "").replace("]", "").replace("'", "")
            x.add_row([datos_artista['nombre'],
            genero if len(genero) != 0 else "Ninguno",
            datos_artista['popularidad'], datos_artista['seguidores']
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
        tipo_catalogo = input("Con que tipo de representacion de lista quieres cargar el catalogo: ")
        control = newController(tipo_catalogo)

        tamanio_archivo_input = input("Con que tipo tamaño quieres cargar el archivo: ")
        if tamanio_archivo_input.isnumeric() == True:
            tamanio_archivo_input = tamanio_archivo_input+"pct"
        else:
            tamanio_archivo_input = tamanio_archivo_input

        print("Cargando información de los archivos ....")
        album_size, artist_size, track_size, catalog = loadData(tamanio_archivo_input)
        artistFirstThree, artistLastThree = controller.artistFirstThreeLastThree(catalog, artist_size)
        albumFirstThree, albumLastThree = controller.albumFirstThreeLastThree(catalog, album_size)
        trackFirstThree, trackLastThree = controller.trackFirstThreeLastThree(catalog, track_size)
        print('Albumes cargados: ' +str(album_size))
        print('Artistas cargados: ' +str(artist_size))
        print('Canciones cargados: ' +str(track_size))

        printArtists(artistFirstThree, artistLastThree)

    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        tipo = input("Escoje un tipo de ordenamiento (selection, insertion o shell): ")
        if tipo.lower() == "selection":
            tiempo, organizado = controller.ordenamientoSelection(control)
            print(f"El tiempo que tomo el ordenamiento Selection en organizar los datos fue {tiempo}")

        elif tipo.lower() == "insertion":
            tiempo, organizado = controller.ordenamientoInsetion(control)
            print(f"El tiempo que tomo el ordenamiento Insertion en organizar los datos fue {tiempo}")

        elif tipo.lower() == "shell":
            tiempo, organizado = controller.ordenamientoShell(control)
            print(f"El tiempo que tomo el ordenamiento Shell en organizar los datos fue {tiempo}")

    elif int(inputs[0]) == 7:
        pass
    elif int(inputs[0]) == 8:
        pass
    else:
        sys.exit(0)
sys.exit(0)
