import pandas as pd
import numpy  as np
from src import cargar_datos as dat

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
    return f'Estas son las estaciones que te recomiendo {resultado}'
