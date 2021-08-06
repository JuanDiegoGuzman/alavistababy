#!/usr/bin/env python

import pandas as pd 
def avgcity(city, my_csv):
    citypop = {}
    for line in my_csv:
        mycity = line["loc"] #identificamos la localidad 
        pop = float(line["pop"])# identificamos la poblacion y transformamos a un numero float
        if line["cases"] != "NA": # en este caso NA es el punto clave ya que decimos que se cree una funcion
                                  #donde si es que en las lineas no tiene el NA, REALIZE LA FUNCIONDE ABAJO. 
            cases =float(line["cases"])
            citypop[mycity] = citypop.get(mycity, [0,0,0]) #GENERAMOS RESPUES QUE TENGAN 3 NIVELES: EN EL PRIMERO GUARDAMOS LA POBLACION, EN EL 2 IDENTIFICADOR GUARDAMOS LOS CASOSY EN EL ULTIMO IDENTIFICADOR GUARDAMOS EL CONTEO.
            citypop[mycity][0] = citypop[mycity][0] + pop
            citypop[mycity][1] = citypop[mycity][1] + cases
            citypop[mycity][2] = citypop[mycity][2] + 1
            
        for key in citypop:
            if key == city:
                avg_cases = 100000*citypop[key][2]/citypop[key][1] #CALCULAMOS EL PORCENTAJE DE CASO: en este caso multiplicamos por 1000 para tener un numero legible, lo que quieres decir que sera por 100000 habitantes
                return print (key, avg_cases)
            