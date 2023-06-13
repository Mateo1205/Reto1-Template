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

import config as cf
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(tip_list):
    """
    Crea una instancia del modelo
    """
    #Crea el diccionario con la llave model
    control ={
             "model" : None
             
    }

    control["model"] = model.new_data_structs(tip_list)
  
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    return control 


# Funciones para la carga de datos

def load_data(control, filename, orden):
    """
    Carga los datos del reto
    """
    catalog = control["model"]
    dianfile = cf.data_dir + filename
    input_file = csv.DictReader(open(dianfile, encoding = "utf-8"))
    for contect in input_file:
        model.add_data(catalog,contect)
    # ordenamiento
    sort(catalog,orden)

    control["model"]["Años1"] = model.ejecutar_p_u_3(control["model"])
    





# Funciones de ordenamiento

def sort(catalog, orden):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    model.sort(catalog, orden)
    

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(req_1):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    res_1 = model.req_1(req_1["Años1"])
    
    return res_1




def req_2(req_2):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    
    res_2 = model.req_2(req_2["Años1"])
    return res_2




def req_3(req_3):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
   
    impresion_1, impresion_2 = model.req_3(req_3["Años1"])

    return impresion_1, impresion_2







def req_4(req_4):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    



def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass





def req_6(control, anio):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    
    impresion_1 = model.req_6(control["Años1"],anio)

    return impresion_1





def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass





def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass




# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
