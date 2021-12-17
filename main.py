import streamlit as st
import pandas as pd
from src.cargar_datos import *
from src.streamlit import *
from data import *
from streamlit_folium import folium_static

st.write('''
# Skiing:
# Escoge tu estacion:
''')
data = cargardatos()
restdata = cargarrestaurantes()
estaciones = data['estacion']
#map = pd.read_json('data/kepler.gl.json')

input_nivel = ['elige','novato','principiante', 'medio', 'experto']
nivel = st.selectbox('Cual es tu nivel de skii: ', input_nivel)
if nivel == 'elige':
    st.stop()
    
input_snow = ['elige', 'S', 'N', 'indiferente']
snow = st.radio('¿Quieres que haya Snonwpark? ', input_snow)
if snow == 'elige':
    st.stop()


input_fam = ['elige', 'S', 'N']
fam = st.radio('Vas con tu familia: ', input_fam)
if fam == 'elige':
    st.stop()


respuesta = convinetor(nivel,snow,fam)
#print(respuesta)
#mapita(respuesta)
folium_static(mapita(respuesta))
respuesta
#detalles = mostrar(respuesta)
#detalles