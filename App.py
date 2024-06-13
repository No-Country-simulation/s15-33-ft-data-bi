# import streamlit as st
# from API_partidos import obtener_partidos_por_jornada, obtener_tabla_posiciones
# from datetime import datetime, timedelta
# import pytz
# import pandas as pd

# st.set_page_config(
#     page_title="Partidos de Fútbol",
#     page_icon="⚽️"
# )


# # Función para convertir la zona horaria de UTC a Brasil
# def convertir_a_br(fecha_utc):
#     zona_br = pytz.timezone('America/Sao_Paulo')
#     fecha_br = datetime.fromisoformat(fecha_utc.replace('Z', '+00:00')).astimezone(zona_br)
#     return fecha_br.strftime('%Y-%m-%d'), fecha_br.strftime('%H:%M:%S')

# def mostrar_partidos_en_tabla(partidos):
#     if not partidos:
#         st.write("No se encontraron partidos.")
#     else:
#         data = []
#         for partido in partidos:
#             fecha_br, hora_br = convertir_a_br(partido['Fecha'])
#             data.append([partido['Local'], partido['Visitante'], fecha_br, hora_br])
#         df = pd.DataFrame(data, columns=['Local', 'Visitante', 'Fecha', 'Hora'])
#         st.table(df)

# st.image("img/bandera_brasil.png")

# # Seleccionar la jornada
# jornada = st.number_input("Seleccione la jornada", min_value=1, step=1, value=1)

# # Obtener los partidos para la jornada especificada
# partidos = obtener_partidos_por_jornada('2013', jornada)

# col1, col2 = st.columns([1, 3])
# with col1:
#     st.image("img/liga_brasil.png", width=100)
# with col2:
#     st.title("Brasileirao Serie A")

# st.header(f"Partidos de la jornada {jornada}")
# mostrar_partidos_en_tabla(partidos)


# def mostrar_tabla_posiciones(tabla_posiciones):
#     if not tabla_posiciones:
#         st.write("No se encontró la tabla de posiciones.")
#     else:
#         df = pd.DataFrame(tabla_posiciones, columns=['Posición', 'Equipo', 'Jugados', 'Ganados', 'Empatados', 'Perdidos', 'Puntos'])
#         df.set_index('Posición', inplace=True)  # Usar la columna "Posición" como índice
#         st.table(df)


# # Obtener y mostrar la tabla de posiciones
# st.header("Tabla de Posiciones")
# tabla_posiciones = obtener_tabla_posiciones('2013')
# mostrar_tabla_posiciones(tabla_posiciones)


import streamlit as st
from API_partidos import obtener_partidos_por_jornada, obtener_tabla_posiciones
from datetime import datetime
import pytz
import pandas as pd

st.set_page_config(
    page_title="Partidos de Fútbol",
    page_icon="⚽️"
)

# CSS personalizado para estilos avanzados
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
        color: #333;
        padding: 20px; /* Ajuste del padding */
    }
    .header {
        margin-bottom: 20px;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
    }
    .title {
        font-size: 2em;
        margin-bottom: 20px;
        text-align: center;
    }
    .subheader {
        font-size: 1.5em;
        margin-bottom: 10px;
        color: #4CAF50;
    }
    .table-container {
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .stTable {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
    }
    .stImage {
        margin: auto;
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Función para convertir la zona horaria de UTC a Brasil
def convertir_a_br(fecha_utc):
    zona_br = pytz.timezone('America/Sao_Paulo')
    fecha_br = datetime.fromisoformat(fecha_utc.replace('Z', '+00:00')).astimezone(zona_br)
    return fecha_br.strftime('%Y-%m-%d'), fecha_br.strftime('%H:%M:%S')

def mostrar_partidos_en_tabla(partidos):
    if not partidos:
        st.write("No se encontraron partidos.")
    else:
        data = []
        for partido in partidos:
            fecha_br, hora_br = convertir_a_br(partido['Fecha'])
            # Usar valores predeterminados para probabilidades
            prob_w = partido.get('Prob_W', 'N/A')
            prob_d = partido.get('Prob_D', 'N/A')
            prob_l = partido.get('Prob_L', 'N/A')
            data.append([
                hora_br, 
                fecha_br, 
                partido['Local'], 
                prob_w, 
                prob_d, 
                prob_l, 
                partido['Visitante']
            ])
        df = pd.DataFrame(data, columns=['Hora', 'Fecha', 'Local', 'Prob_W', 'Prob_D', 'Prob_L', 'Visitante'])
        st.table(df)

# Imagen de la bandera de Brasil
st.image("img/bandera_brasil.png", use_column_width=True, caption="Brasileirao")

# Seleccionar la jornada
jornada = st.number_input("Seleccione la jornada", min_value=1, step=1, value=1)

# Obtener los partidos para la jornada especificada
partidos = obtener_partidos_por_jornada('2013', jornada)

# Título y encabezado
st.markdown('<div class="header"><h1 class="title">Brasileirao Serie A</h1></div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="subheader">Partidos de la jornada {jornada}</h2>', unsafe_allow_html=True)
mostrar_partidos_en_tabla(partidos)

# Mostrar tabla de posiciones
def mostrar_tabla_posiciones(tabla_posiciones):
    if not tabla_posiciones:
        st.write("No se encontró la tabla de posiciones.")
    else:
        df = pd.DataFrame(tabla_posiciones, columns=['Posición', 'Equipo', 'Jugados', 'Ganados', 'Empatados', 'Perdidos', 'Puntos'])
        df.set_index('Posición', inplace=True)  # Usar la columna "Posición" como índice
        st.table(df)

st.markdown('<h2 class="subheader">Tabla de Posiciones</h2>', unsafe_allow_html=True)
tabla_posiciones = obtener_tabla_posiciones('2013')
mostrar_tabla_posiciones(tabla_posiciones)










