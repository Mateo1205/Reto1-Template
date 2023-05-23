﻿"""
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
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
#from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(tipo_list):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(tipo_list)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")



def print_carga():

    #Solicita al usuario la cantidad de datos a usar
    print("-------------------------------------------Porcentaje de carga------------------------------------")
    print(" 1. small%")
    print(" 2. 5%")
    print(" 3. 10%")
    print(" 4. 20%")
    print(" 5. 30%")
    print(" 6. 50%")
    print(" 7. 80%")
    print(" 8. 100%")
    opc_1 = int(input("Seleccione el porcentaje de carga que desa realizar: \n"))
    porcentaje = None
    if opc_1 == 1:
        porcentaje = "small"
    elif opc_1 == 2:
        porcentaje = "5pct"
    elif opc_1 == 3:
        porcentaje = "10pct"
    elif opc_1 == 4:
        porcentaje = "20pct"
    elif opc_1 == 5:
        porcentaje = "30pct"
    elif opc_1 == 6:
        porcentaje = "50pct"
    elif opc_1 == 7:
        porcentaje = "80pct"
    elif opc_1 == 8:
        porcentaje = "large"


    #Solicita al usuario el tipo de lista (ARRAY_LIST, SINGLE_LIST)
    print("-----------------------------------Metodo de carga---------------------------------------------")
    print("1. ARRAY_LIST")
    print("2. SINGLE_LIST")
    opc_2 = int(input("Seleccione el metodo de carga: "))
    tip_carga = None
    if opc_2 == 1:
        tip_carga = "ARRAY_LIST"
    elif opc_2 == 2:
        tip_carga = "SINGLE_LINKED "


    #Solicita el tipo de ordenamiento
    print("-----------------------------------Metodo de ordenamiento--------------------------------------")
    print("1. Selection Sort")
    print("2. Insert Sort")
    print("3. Shell Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    opc_3 = int(input("Seleccione el metodo de ordenamiento que desea usar: "))
    print(opc_3)
    orden = None
    if opc_3 == 1:
        orden = "sele"
    elif opc_3 == 2:
        orden = "inser"
    elif opc_3 == 3:
        orden = "shel"
    elif opc_3 == 4:
        orden = "merg"
    elif opc_3 == 5:
        orden = "quick"

    return porcentaje, tip_carga, orden



    

def load_data(control, filename, orden):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    
    data = controller.load_data(control,filename,orden)
    
    return data


def print_data(primeros_ultimos_3):
    """
        Función que imprime un dato dado su ID
    """
    lista=[]
    lista_1 = []
    print(primeros_ultimos_3)
    for i in lt.iterator(primeros_ultimos_3):
        if lt.size(i) <= 6:
            for h in range(lt.size(i)):
                lista_1.append(lt.getElement(i,h))
            lista.append(lista_1)
            lista_1=[]
        else:
            
            for j in range(0,3):
                
                lista_1.append(lt.firstElement(i))
                lt.removeFirst(i)
                lista_1.append(lt.lastElement(i))
                lt.removeLast(i)
                
            
            lista.append(lista_1)
            lista_1=[]
            
    #TODO: Realizar la función para imprimir un elemento
    
    for i in lista:
       for j in i:
            print("---------------------------------------------------------------------")
            print(str(j["Año"])+ "     ||     " +str(j["Código actividad económica"]))
            print("---------------------------------------------------------------------")

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista


# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:

        
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:

                #Solicita al usuario toda la informacion para realizar la carga de datos
                print("Cargando información de los archivos ....\n")

                #Porcetaje de datos, tipo de lista y tipo de ordenamiento
                porcentaje, tipo_list, orden = print_carga()

                # conecta la funcion new_controller y envia el tipo de lista. Inicializa la estructuta de datos
                control = new_controller(tipo_list)
                
                #Realizar la carga de datos (inicio de la estructura de datos, nombre dela rchivo a cargar, tipo de orden)
                data = load_data(control,"DIAN/Salida_agregados_renta_juridicos_AG-" + porcentaje + ".csv",orden)
                
                
                primeros_ultimos_3 = controller.ejecutar_primeros_ultimos_3(control)
                
                print_data(primeros_ultimos_3)
                


            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
