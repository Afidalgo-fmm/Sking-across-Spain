import pandas as pd
def cargardatos():
    lectura = pd.read_csv('data/Datos.csv', index_col = 0)
    respuesta = pd.DataFrame(lectura)
    return respuesta

def cargarrestaurantes():
    lectura = pd.read_csv('data/Restaurantes.csv', index_col = 0)
    respuesta = pd.DataFrame(lectura)
    return respuesta