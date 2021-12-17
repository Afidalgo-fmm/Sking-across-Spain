import pandas as pd
import numpy  as np
from src import cargar_datos as dat
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd


nivel_novato = [] # sin negras y muy pocas rojas
nivel_principiante = [] # principalmente que sean verdes y azules
nivel_medio = []  # un mix de todo pero sobre todo que haya rojas y azules
nivel_experto = [] # sin casi verdes ni azules sobre todo negras

my_data = dat.cargardatos()

for i,row in my_data.iterrows():
    if my_data.pistas_negras[i] == 0 and my_data.pistas_rojas[i] < my_data.pistas_verdes[i] and my_data.pistas_azules[i]:
        nivel_novato.append( my_data.estacion[i])
    elif my_data.pistas_azules[i] and my_data.pistas_verdes[i] > my_data.pistas_negras[i] and my_data.pistas_rojas[i]:
        nivel_principiante.append(my_data.estacion[i])
    elif my_data.pistas_rojas[i] and my_data.pistas_azules[i] > my_data.pistas_negras[i] and my_data.pistas_verdes[i]:
        nivel_medio.append(my_data.estacion[i])
    elif my_data.pistas_negras[i] and my_data.pistas_rojas[i] > my_data.pistas_azules[i] and my_data.pistas_verdes[i]:
        nivel_experto.append(my_data.estacion[i])
    

consnow = []
sinsnow = []
sudasnow = my_data['estacion']
for i,row in my_data.iterrows():
    if my_data.Snowpark[i] == 0:
        sinsnow.append(my_data.estacion[i])
    elif my_data.Snowpark[i] == 1:
        consnow.append(my_data.estacion[i])
    


confam = []
sinfam = []
for i,row in my_data.iterrows():
    if my_data.Familiar[i] == 0:
        sinfam.append(my_data.estacion[i])
    elif my_data.Familiar[i] == 1:
        confam.append(my_data.estacion[i])
    

print(sudasnow)
def convinetor(nivel,snow,familia):
    if nivel == 'novato':
        resnivel = nivel_novato
    elif nivel == 'principiante':
        resnivel = nivel_principiante
    elif nivel ==  'medio':
        resnivel = nivel_medio
    elif nivel == 'experto':
        resnivel = nivel_experto
        
    if snow == 'S':
        ressnow = consnow
    elif snow == 'N':
        ressnow = sinsnow
    elif snow == 'indiferente':
        ressnow = sudasnow
        
    if familia == 'S':
        resfam = confam
    elif familia == 'N':
        resfam = sinfam
    res = [value for value in resnivel if value in ressnow]
    resultado = [value for value in resfam if value in res]
    newdata = pd.DataFrame()

    for i, row in my_data.iterrows():
        if my_data.estacion[i] in resultado:
            newdata = newdata.append(row, ignore_index=True)
    #realdata = newdata[newdata['estacion','Estado_nieve','n_pistas', 'remontes','precio_adultos €', 'KM totales']]
    return newdata

def mapita (data_conv):
    inicial_lat = 40.463667
    inicial_long = -3.74922
    esp_map = folium.Map(location=[inicial_lat,inicial_long], zoom_start=6, tiles = 'Stamen Terrain')
    descripcion = []
    for i,row in data_conv.iterrows():
    #print([float(row.lat),float(row.long)])
    #print(row.estacion)
        marker1 = folium.Marker(location=[float(row.lat),float(row.long)], tooltip= row.estacion, icon=folium.Icon(icon='glyphicon glyphicon-asterisk'))
        marker1.add_to(esp_map)
    return esp_map
def mostrar(data_conv):
    resultado = pd.DataFrame()
    for i, row in data_conv.iterrows():
        pistas = int(row.n_pistas)
        estacion = row.estacion
        nieve = row.Estado_nieve
        remontes = int(row.remontes)
    resultado = resultado.append([estacion, pistas,remontes,nieve])
    return resultado