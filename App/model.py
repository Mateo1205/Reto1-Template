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
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos
def ejecutar_p_u_3(data_1):

    
    anio = "2012"
    
    filtro= lt.newList("ARRAY_LIST")
    lis_x_años = lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(data_1["data"]):

        if anio == i["Año"] :
            lt.addLast(lis_x_años,i)
        else: 
            anio =i["Año"]
            
            lt.addLast(filtro,lis_x_años)
            lis_x_años = lt.newList("ARRAY_LIST")
            lt.addLast(lis_x_años,i)
              
    lt.addLast(filtro, lis_x_años)
    return filtro
        


def new_data_structs(tip_list):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_struc = {
        "data" :None,
        "Años1":None
    }
    #TODO: Inicializar las estructuras de datos

    data_struc["data"] = lt.newList(datastructure= f"{tip_list}",
                                    cmpfunction=compare )
    data_struc["Años1"] = lt.newList(datastructure= f"{tip_list}",
                                    cmpfunction=compare )
    return data_struc




def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs["data"],data)



def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass



def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass



def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass



def  req_1(req_1):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    
    lista=lt.newList("ARRAY_LIST")
    lista_filtro = ["Año","Código actividad económica","Nombre actividad económica","Código sector económico"
                    ,"Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos",
                    "Total saldo a pagar","Total saldo a favor"]
    lista_1= lt.newList("ARRAY_LIST")
   
    for j in lt.iterator(req_1):
        mayor = 0
        info = None
        
        for h in lt.iterator(j):
            if int(h["Total saldo a pagar"]) > mayor: 
                info =h
                mayor =int(h["Total saldo a pagar"])
        
        lt.addLast(lista_1,info)
   
    for fil in lt.iterator(lista_1):
        lista_aux = lt.newList("ARRAY_LIST")
        for key in lista_filtro:
               lt.addLast(lista_aux,fil[key] )
        lt.addLast(lista,lista_aux["elements"])
    lt.addFirst(lista, lista_filtro)
        

    return lista





def req_2(req_2):
    """
    Función que soluciona el requerimiento 2
    """
    
    lista=lt.newList("ARRAY_LIST")
    lista_filtro = ["Año","Código actividad económica","Nombre actividad económica","Código sector económico"
                    ,"Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos",
                    "Total saldo a pagar","Total saldo a favor"]
    lista_1= lt.newList("ARRAY_LIST")
   
    for j in lt.iterator(req_2):
        mayor = 0
        info = None
        
        for h in lt.iterator(j):
            if int(h["Total saldo a favor"]) > mayor: 
                info =h
                mayor =int(h["Total saldo a favor"])
        
        lt.addLast(lista_1,info)
    
    for fil in lt.iterator(lista_1):
        lista_aux = lt.newList("ARRAY_LIST")
        for key in lista_filtro:
               lt.addLast(lista_aux,fil[key] )
        lt.addLast(lista,lista_aux["elements"])
    lt.addFirst(lista, lista_filtro)
    
    return lista





def req_3(req_3):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    #Organizado por año: Pocedemos a organizar cada año por sector y subsector

     
    for j in lt.iterator(req_3):
         se.sort(j,cmp_año_by_sector)

    lista = lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(req_3):
        
        lista_2 = lt.newList("ARRAY_LIST")
        Codigo_sub = lt.firstElement(i)["Código subsector económico"]
        
        total_retenciones= 0
        menor=None
        menor_total=None

        for h in lt.iterator(i):
            if Codigo_sub == h["Código subsector económico"]:
                lt.addLast(lista_2,h)
                total_retenciones += int(h["Total retenciones"])
                
            elif Codigo_sub != h["Código subsector económico"]:
                
                if (menor == None) or (total_retenciones < menor):
                    menor= total_retenciones
                    menor_total = lista_2
                    
                total_retenciones = 0
                Codigo_sub = h["Código subsector económico"]
                total_retenciones += int(h["Total retenciones"])
                
                

                lista_2 = lt.newList("ARRAY_LIST")

                lt.addLast(lista_2,h)
            
        if (total_retenciones < menor):
                menor_total = lista_2
                
            
        lt.addLast(lista,menor_total)

    impresion_1 = organizar_respuesta_3(lista)
    impresion_2 = organizar_respuesta_3_1(lista)

    return impresion_1, impresion_2
def organizar_respuesta_3(impresion_1):
    lista = lt.newList("ARRAY_LIST")
    lista_filtra=["Año","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico"]
    
    for i in lt.iterator(impresion_1):
        l= lt.firstElement(i)
        lista_aux = lt.newList("ARRAY_LIST")
        total_rete=0
        total_ingresos_n=0
        total_cost_gas=0
        total_sald_pagar=0
        total_saldo_favor=0
        for k in lt.iterator(i):
           total_rete+= int(k["Total retenciones"])
           total_ingresos_n += int(k["Total ingresos netos"])
           total_cost_gas += int(k["Total costos y gastos"])
           total_sald_pagar += int(k["Total saldo a pagar"])
           total_saldo_favor += int(k["Total saldo a favor"])
        
        for key in lista_filtra:
            lt.addLast(lista_aux,l[key])

        lt.addLast(lista_aux,total_rete)
        lt.addLast(lista_aux,total_ingresos_n)
        lt.addLast(lista_aux,total_cost_gas)
        lt.addLast(lista_aux,total_sald_pagar)
        lt.addLast(lista_aux,total_saldo_favor)
        lt.addLast(lista,lista_aux["elements"])

    param2 = ["Año","Código sector económico","Nombre sector económico","Código subsector económico",
             "Nombre subsector económico","Total retenciones del subsector económico",
             "Total ingresos netos del subsector económico","Total costos y gastos del subsector económico",
             "Total saldo a pagar del subsector económico","Total saldo a favor del subsector económico"]
        
    lt.addFirst(lista,param2)
    
    return lista 
def organizar_respuesta_3_1(impresion_2):

    lista = lt.newList("ARRAY_LIST")
    lista_quitar=[ "Código actividad económica","Nombre actividad económica","Total retenciones","Total ingresos netos",
                  "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    for i in lt.iterator(impresion_2):
       lista_1 = lt.newList("ARRAY_LIST")
       dicc={}
       for k in lt.iterator(i):
           for key in lista_quitar:
               dicc[key] = k[key]
           lt.addLast(lista_1,dicc)
           dicc = {}
           
       if lt.size(i) <= 6:
          lt.addLast(lista,lista_1)
       else:
            for y in range(3):
               x= lt.firstElement(lista_1)
               lt.addFirst(lista,x)
               lt.removeFirst(lista_1)

               y = lt.lastElement(lista_1)
               lt.addLast(lista,y)
               lt.removeLast(i)
            
    return lista






def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass






def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass







def  req_6(impresion_1, anio):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    lista_anio = sacar_info_año(impresion_1,anio)
    
    se.sort(lista_anio,cmp_año_by_sector)
    
    lista_grup = agrupar_6(lista_anio)
    lista_sec_aportes,lista_sub_mayor, lista_sub_menor = establer_subsectores_mas_aporte(lista_grup)
    lista_final_sub = organizar_sub_act_aportes(lista_sub_mayor,lista_sub_menor)

    return lista_sec_aportes

def sacar_info_año(impresion_1,anio):
    
    for ip in lt.iterator(impresion_1):
        k = lt.firstElement(ip)
      
        if int(k["Año"]) == anio:
           return ip      
def agrupar_6(lista):

    lista_organizada = lt.newList("ARRAY_LIST")
    lista_sec = lt.newList("ARRAY_LIST")
    lista_sub = lt.newList("ARRAY_LIST")
    lista_act = lt.newList("ARRAY_LIST")
    primero = lt.firstElement(lista)
    for elem in lt.iterator(lista):
        if elem["Código sector económico"] == primero["Código sector económico"]:
            if elem["Código subsector económico"] == primero["Código subsector económico"]:
                lt.addLast(lista_sub,elem)

                if elem["Código"]





            else:
                lt.addLast(lista_sec,lista_sub)
                lista_sub=lt.newList("ARRAY_LIST")
                lt.addLast(lista_sub,elem)
                primero = elem

        else:
            lt.addLast(lista_sec,lista_sub)
            lista_sub=lt.newList("ARRAY_LIST")
            lt.addLast(lista_sub,elem)

            lt.addLast(lista_organizada,lista_sec)
            lista_sec=lt.newList("ARRAY_LIST")
            primero= elem

    lt.addLast(lista_sec,lista_sub)
    lt.addLast(lista_organizada,lista_sec)


    
    return lista_organizada
def establer_subsectores_mas_aporte(lista_grup):
    lista_final_1 = lt.newList("ARRAY_LIST")
    lista_filtro = ["Código sector económico","Nombre sector económico","Total ingresos netos del sector económico"
                    ,"Total costos y gastos del sector económico","Total saldo por pagar del sector económico"
                    ,"Total saldo a favor del sector económico","Subsector economico que mas aporto","Subsector economico que menos aporto"]
    lt.addLast(lista_final_1,lista_filtro)

    lista_sub_mayor =lt.newList("ARRAY_LIST")
    lista_sub_menor =lt.newList("ARRAY_LIST")
    for sector in lt.iterator(lista_grup):
        lista_aux =lt.newList("ARRAY_LIST")
        total_ingresos_sec = 0
        total_cos_gastos_sec = 0
        total_sal_pagar_sec = 0
        total_sal_favor_sec = 0
        info_menor = None
        info_mayor = None
        mayor=0
        menor=None
        x = lt.firstElement(lt.firstElement(sector))
        for sub_sector in lt.iterator(sector):
            
            actual_ingre_sec = total_ingresos_sec
            for cada_sub in lt.iterator(sub_sector):
                total_ingresos_sec += int(cada_sub["Total ingresos netos"])
                total_cos_gastos_sec += int(cada_sub["Total costos y gastos"])
                total_sal_pagar_sec += int(cada_sub["Total saldo a pagar"])
                total_sal_favor_sec += int(cada_sub["Total saldo a favor"])
            comparar_ingresos_suc= total_ingresos_sec-actual_ingre_sec
            if comparar_ingresos_suc > mayor:
                mayor = comparar_ingresos_suc
                info_mayor = sub_sector   
            if (menor==None) or (comparar_ingresos_suc < menor):
                menor = comparar_ingresos_suc
                info_menor = sub_sector
        lt.addLast(lista_aux,x["Código sector económico"])
        lt.addLast(lista_aux,x["Nombre sector económico"])
        lt.addLast(lista_aux,total_ingresos_sec)
        lt.addLast(lista_aux,total_cos_gastos_sec)
        lt.addLast(lista_aux,total_sal_pagar_sec)
        lt.addLast(lista_aux,total_sal_favor_sec)
        lt.addLast(lista_sub_mayor,info_mayor)
        lt.addLast(lista_sub_menor,info_menor)
        j=lt.firstElement(info_mayor)
        b=lt.firstElement(info_menor)
        lt.addLast(lista_aux, j["Código subsector económico"])
        lt.addLast(lista_aux, b["Código subsector económico"])
        lt.addLast(lista_final_1,lista_aux["elements"])
        
    return lista_final_1,lista_sub_mayor, lista_sub_menor
def organizar_sub_act_aportes(lista_sub_mayor, lista_sub_menor):
    
    
    
    lista_filtro = ["Código subsector económico","Nombre subsector económico","El total ingresos netos para el subsector","El total costos y gastos para el subsector",
                   "El total saldo por pagar para el subsector","El total saldo a favor para el subsector"]
    

    for sub in lt.iterator(lista_sub_mayor):

        lt_sub_mayor = lt.newList("ARRAY_LIST")
        total_ingresos_sub = 0
        total_cos_gastos_sub = 0
        total_sal_pagar_sub = 0
        total_sal_favor_sub = 0
        act_mayor = 0
        act_menor = 0

        for act in lt.iterator(sub):

            now_ingr_sub = total_ingresos_sub
            total_ingresos_sub += int(act["Total ingresos netos"])
            total_cos_gastos_sub += int(act["Total costos y gastos"])
            total_sal_pagar_sub += int(act["Total saldo a pagar"])
            total_sal_favor_sub += int(act["Total saldo a favor"])
        
            comp_ingr_sub = total_ingresos_sub - now_ingr_sub

            if comp_ingr_sub > act_mayor:
                act_mayor = comp_ingr_sub
                info_acti_mayor = act

            if (act_menor == None) or (comp_ingr_sub < act_menor):
                act_menor = comp_ingr_sub
                info_act_menor =act
        


        lt.addLast(lt_sub_mayor,lista_filtro)
        lt.addLast(lt_sub_mayor,sub["Código subsector económico"])
        lt.addLast(lt_sub_mayor,sub["Nombre subsector económico"])
        lt.addLast(lt_sub_mayor,total_ingresos_sub)
        lt.addLast(lt_sub_mayor,total_cos_gastos_sub)
        lt.addLast(lt_sub_mayor,total_sal_pagar_sub)
        lt.addLast(lt_sub_mayor,total_sal_favor_sub)




def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass






def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass






def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass

def sort(data_structs,orden):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    if orden == "sele":
        se.sort(data_structs["data"],cmp_impuesto_by_año)
    elif orden == "inser":
        ins.sort(data_structs["data"],cmp_impuesto_by_año)
    elif orden == "shel":
        sa.sort(data_structs["data"],cmp_impuesto_by_año)
    elif orden == "merg":
        merg.sort(data_structs["data"],cmp_impuesto_by_año)
    elif orden == "quick":
        quk.sort(data_structs["data"],cmp_impuesto_by_año)

def cmp_impuesto_by_año(unidad_1, unidad_2):
    
    #criterio de ordenamiento por año
    if unidad_1["Año"] == unidad_2["Año"]:
        sub_1 = unidad_1["Código actividad económica"]
        sub_2 = unidad_2["Código actividad económica"]
        return float(sub_1) > float(sub_2)
    else:
        return int(unidad_1["Año"]) < float(unidad_2["Año"])

def cmp_año_by_sector(unidad_1,unidad_2):
    
    if unidad_1["Código sector económico"] == unidad_2["Código sector económico"]:
        if unidad_1["Código subsector económico"] == unidad_2["Código subsector económico"]:
            sub_1 = unidad_1["Código actividad económica"]
            sub_2 = unidad_2["Código actividad económica"]
            return float(sub_1) < float(sub_2)
        else:
            unidad_1["Código subsector económico"] < unidad_2["Código subsector económico"]
    else:
        return int(unidad_1["Código sector económico"]) < float(unidad_2["Código sector económico"])
    
def cmp_by_total_saldo_pagar(unidad_1,unidad_2):

    if unidad_1["Año"] == unidad_2["Año"]:
        sub_1 = unidad_1["Total saldo a pagar"]
        sub_2 = unidad_2["Total saldo a pagar"]
        return float(sub_1) < float(sub_2)
    else:
        return int(unidad_1["Total saldo a pagar"]) < float(unidad_2["Total saldo a pagar"])
    
def cmp_sector_subsector_actividad(unidad_1,unidad_2):
    if unidad_1["Código sector económico"] == unidad_2["Código sector económico"]:
        if unidad_1["Código subsector económico"] == unidad_2["Código subsector económico"]:
            if unidad_1["Código actividad económica"] == unidad_2["Código actividad económica"]:
                sub_1 = unidad_1["Total ingresos netos"]
                sub_2 = unidad_2["Total ingresos netos"]
                return float(sub_1) < float(sub_2)

            else:
                return str(unidad_1["Código actividad económica"]) < str(unidad_2["Código actividad económica"])   
        else:
           return float(unidad_1["Código subsector económico"])< int(unidad_2["Código subsector económico"])
    else:
        return int(unidad_1["Código sector económico"]) < float(unidad_2["Código sector económico"])