import streamlit as st
import pandas as pd
from src.cargar_datos import *
from src.streamlit import *

data = cargardatos()
restdata = cargarrestaurantes()
estaciones = data['estacion']
input_nivel = ['elige','novato','principiante', 'medio', 'experto']
'''

'''
nivel = input('Cual es tu nivel de skii: ')#, input_nivel)
#if nivel.lower() == 'elige':
 #   st.stop()
    
input_snow = ['elige', 'S', 'N', 'indiferente']
snow = input('¿Quieres que haya Snonwpark? ')#, input_snow)
#if snow.lower() == 'elige':
 #   st.stop()
#elif snow.lower() == 'indiferente':
#    snow = sudasnow

input_fam = ['elige', 'S', 'N']
fam = input('Vas con tu familia: ')#, input_fam)
#if fam.lower() == 'elige':
 #   st.stop()


respuesta = convinetor(nivel,snow,fam)
respuesta_final = []
for i in estaciones:
    if i in respuesta:
        respuesta_final.append(i)
print(respuesta_final)
