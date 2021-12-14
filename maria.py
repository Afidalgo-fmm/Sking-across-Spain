import streamlit as st
import pandas as pd
import src.manage_data as dat
from PIL import Image


def app():
    st.write("""
    # Perrinder:
    ## Haz *match* con tu perrete
    """)

    data = dat.cargadata()
    data = data.sort_values('Behaviour', ascending = False)

    

    input_size = ["Elige" , "Grande", "Mediano", "Pequeño"]

    
    
    size = st.selectbox("¿De qué tamaño te gustaría adoptar tu pero?", input_size)
    if size == "Elige":
        st.stop()
    
    #st.stop()

    input_alergia = ["Elige", "Sí", "No"]
    alergia  = st.selectbox("¿Eres alérgicx al pelo de perro?", input_alergia)
    if alergia == "Elige":
        st.stop()
    
    input_tiempo  = ["Elige", "Mucho", "Intermedio", "Poco"]
    tiempo = st.selectbox("¿Cuánto tiempo tienes para pasear?", input_tiempo)
    if tiempo == "Elige":
        st.stop()
    
    input_ninos  = ["Elige", "Sí", "No"]
    ninos = st.selectbox("¿Tienes hijos pequeños?", input_ninos)
    if ninos == "Elige":
        st.stop()

    input_perros_otro  = ["Elige", "Sí", "No"]
    perros_otro = st.selectbox("¿Tienes ya otro perro? ", input_perros_otro)
    if perros_otro == "Elige":
            st.stop()

    #formula

    if size == "Grande":
        tamano = [4,5]
    elif size == "Mediano":
        tamano = [3]
    else:
        tamano = [1,2]
    volumen = data[data.Size.isin(tamano)]
    

    if alergia == "Sí":
        pelo = [1,2]
    else: 
        pelo = [1,2,3,4,5]    
    pelete = volumen[volumen['Amount Of Shedding'].isin(pelo)]


    if tiempo == "Mucho":
        horas = [1,2,3,4,5]
    elif tiempo == "Intermedio":
        horas = [1,2,3]
    else:
        horas = [1,2]        
    paseo = pelete[pelete['Exercise Needs'].isin(horas)]
    

    if ninos == "Sí":
        hijo = [4,5]
    else:
        hijo = [1,2,3,4,5]        
    nino = paseo[paseo['Kid-Friendly'].isin(hijo)]
    

    if perros_otro == "Sí":
        otro = [4,5]
    else:
        otro = [1,2,3,4,5]        
    perro = nino[nino['Dog Friendly'].isin(otro)]

    st.write("""
    ## Primeras sugerencias:
    """)
    if len(perro.Name) == 0:
        st.write("""
        No hemos podido encontrar perretes con estas características
        """)
    else:
        st.dataframe(perro.head(4).Name)

    
   

    
    st.write("""
    ### Por si te queda alguna duda
    """)

    try:

        eleccion2 = data.loc[(data.Groups == cluster)]
        for i in range(0,c):
            eleccion2 = eleccion2[eleccion2.Name != lista[i]]

        eleccion2 = eleccion2.head(4).Name
        st.dataframe(eleccion2)    
    except:
        st.write("""
        No hemos podido encontrar perretes con estas características
        """)

    finada = Image.open("images/pepa8.jpg")
    st.image(finada, use_column_width=True)