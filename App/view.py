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
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController():

    control = controller.newController()
    return control

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar los albumes en un periodo de tiempo")
    print("3- Encontrar los artistas mas pouplares")
    print("4- Encontrar las canciones mas populares")
    print("5- Encontrar la canción mas popular de un artista")
    print("6- Encontrar la discografía de un artista")
    print("7- Clasificar las canciones con mayor distribución")
    print("0- Salir")

def loadData():

    album, artist, track, catalogo = controller.loadData(control)
    return album, artist, track, catalogo

control = newController()
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        al, ar, tr, cat = loadData()
        artistFirst3Last3Data = controller.artistFirst3Last3(cat)
        albumFirst3Last3Data = controller.albumFirst3Last3(cat)
        trackFirst3Last3Data = controller.trackFirst3Last3(cat)
        print('Albumes cargados: ' +str(al))
        print('Artistas cargados: ' +str(ar))
        print('Canciones cargados: ' +str(tr))
        print("\n - - artistas - - \n" + 
        f"1 | nombre: {artistFirst3Last3Data[0]['nombre']}, géneros: {artistFirst3Last3Data[0]['generos']}, popularidad: {artistFirst3Last3Data[0]['popularidad']}, número de seguidores: {artistFirst3Last3Data[0]['seguidores']}\n" +
        f"2 | nombre: {artistFirst3Last3Data[1]['nombre']}, géneros: {artistFirst3Last3Data[1]['generos']}, popularidad: {artistFirst3Last3Data[1]['popularidad']}, número de seguidores: {artistFirst3Last3Data[1]['seguidores']}\n" +
        f"3 | nombre: {artistFirst3Last3Data[2]['nombre']}, géneros: {artistFirst3Last3Data[2]['generos']}, popularidad: {artistFirst3Last3Data[2]['popularidad']}, número de seguidores: {artistFirst3Last3Data[2]['seguidores']}\n" +
        "...\n" + 
        "...\n" + 
        "...\n" +
        f"-3 | nombre: {artistFirst3Last3Data[-3]['nombre']}, géneros: {artistFirst3Last3Data[-3]['generos']}, popularidad: {artistFirst3Last3Data[-3]['popularidad']}, número de seguidores: {artistFirst3Last3Data[-3]['seguidores']}\n" + 
        f"-2 | nombre: {artistFirst3Last3Data[-2]['nombre']}, géneros: {artistFirst3Last3Data[-2]['generos']}, popularidad: {artistFirst3Last3Data[-2]['popularidad']}, número de seguidores: {artistFirst3Last3Data[-2]['seguidores']}\n" +
        f"-1 | nombre: {artistFirst3Last3Data[-1]['nombre']}, géneros: {artistFirst3Last3Data[-1]['generos']}, popularidad: {artistFirst3Last3Data[-1]['popularidad']}, número de seguidores: {artistFirst3Last3Data[-1]['seguidores']}\n" +
        "\n - - álbumes - - \n" +
        f"1 | nombre del álbum: {albumFirst3Last3Data[0]['nombre']}, tipo de álbum: {albumFirst3Last3Data[0]['tipo']}, mercados en que está disponible el álbum: {albumFirst3Last3Data[0]['disp']}, fecha de lanzamiento: {albumFirst3Last3Data[0]['lanz']}\n" +
        f"2 | nombre del álbum: {albumFirst3Last3Data[1]['nombre']}, tipo de álbum: {albumFirst3Last3Data[1]['tipo']}, mercados en que está disponible el álbum: {albumFirst3Last3Data[1]['disp']}, fecha de lanzamiento: {albumFirst3Last3Data[1]['lanz']}\n" +
        f"3 | nombre del álbum: {albumFirst3Last3Data[2]['nombre']}, tipo de álbum: {albumFirst3Last3Data[2]['tipo']}, mercados en que está disponible el álbum: {albumFirst3Last3Data[2]['disp']}, fecha de lanzamiento: {albumFirst3Last3Data[2]['lanz']}\n" +
        "...\n" + 
        "...\n" + 
        "...\n" +
        f"-3 | nombre del álbum: {albumFirst3Last3Data[-3]['nombre']}, tipo de álbum: {albumFirst3Last3Data[-3]['tipo']}, mercados en que está disponible el álbum: {albumFirst3Last3Data[-3]['disp']}, fecha de lanzamiento: {albumFirst3Last3Data[-3]['lanz']}\n" +
        f"-2 | nombre del álbum: {albumFirst3Last3Data[-2]['nombre']}, tipo de álbum: {albumFirst3Last3Data[-2]['tipo']}, mercados en que está disponible el álbum: {albumFirst3Last3Data[-2]['disp']}, fecha de lanzamiento: {albumFirst3Last3Data[-2]['lanz']}\n" +
        f"-1 | nombre del álbum: {albumFirst3Last3Data[-1]['nombre']}, tipo de álbum: {albumFirst3Last3Data[-1]['tipo']}, mercados en que está disponible el álbum: {albumFirst3Last3Data[-1]['disp']}, fecha de lanzamiento: {albumFirst3Last3Data[-1]['lanz']}\n" +
        "\n - - canciones - - \n" + 
        f"1 | nombre de la canción: {trackFirst3Last3Data[0]['nombre']}, países en los que está disponible la canción: {trackFirst3Last3Data[0]['disponibilidad']}, duración en milisegundos: {trackFirst3Last3Data[0]['duracion']},  número de la canción en el álbum: {trackFirst3Last3Data[0]['numero_cancion']}\n" +
        f"2 | nombre de la canción: {trackFirst3Last3Data[1]['nombre']}, países en los que está disponible la canción: {trackFirst3Last3Data[1]['disponibilidad']}, duración en milisegundos: {trackFirst3Last3Data[1]['duracion']},  número de la canción en el álbum: {trackFirst3Last3Data[1]['numero_cancion']}\n" +
        f"3 | nombre de la canción: {trackFirst3Last3Data[2]['nombre']}, países en los que está disponible la canción: {trackFirst3Last3Data[2]['disponibilidad']}, duración en milisegundos: {trackFirst3Last3Data[2]['duracion']},  número de la canción en el álbum: {trackFirst3Last3Data[2]['numero_cancion']}\n" +
        "...\n" + 
        "...\n" + 
        "...\n" +
        f"-3 | nombre de la canción: {trackFirst3Last3Data[-3]['nombre']}, países en los que está disponible la canción: {trackFirst3Last3Data[-3]['disponibilidad']}, duración en milisegundos: {trackFirst3Last3Data[-3]['duracion']},  número de la canción en el álbum: {trackFirst3Last3Data[-3]['numero_cancion']}\n" +
        f"-2 | nombre de la canción: {trackFirst3Last3Data[-2]['nombre']}, países en los que está disponible la canción: {trackFirst3Last3Data[-2]['disponibilidad']}, duración en milisegundos: {trackFirst3Last3Data[-2]['duracion']},  número de la canción en el álbum: {trackFirst3Last3Data[-2]['numero_cancion']}\n" +
        f"-1 | nombre de la canción: {trackFirst3Last3Data[-1]['nombre']}, países en los que está disponible la canción: {trackFirst3Last3Data[-1]['disponibilidad']}, duración en milisegundos: {trackFirst3Last3Data[-1]['duracion']},  número de la canción en el álbum: {trackFirst3Last3Data[-1]['numero_cancion']}\n")

    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
