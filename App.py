import streamlit as st
from API_partidos import obtener_partidos
from datetime import datetime, timedelta
import pytz

st.set_page_config(
    page_title="Partidos de Fútbol",
    page_icon="⚽️"
)

# Función para convertir la zona horaria de UTC a Brasil
def convertir_a_br(fecha_utc):
    # Establecer la zona horaria de Brasil
    zona_br = pytz.timezone('America/Sao_Paulo')
    # Convertir la fecha UTC a la zona horaria de Brasil
    fecha_br = datetime.fromisoformat(fecha_utc.replace('Z', '+00:00')).astimezone(zona_br)
    return fecha_br.strftime('%Y-%m-%d'), fecha_br.strftime('%H:%M:%S')

def mostrar_partidos_en_tabla(partidos):
    if not partidos:
        st.write("No se encontraron partidos.")
    else:
        data = []
        for partido in partidos:
            fecha_br, hora_br = convertir_a_br(partido['Fecha'])
            data.append([partido['Local'], partido['Visitante'], fecha_br, hora_br])
        st.table(data)

# Obtener la fecha ingresada por el usuario
fecha = st.date_input("Seleccione la fecha", datetime.today())

# Calcular la fecha de fin (al día siguiente)
fecha_fin = fecha + timedelta(days=1)

# Obtener los partidos para el rango de fechas especificado
partidos = obtener_partidos(fecha.strftime('%Y-%m-%d'), fecha_fin.strftime('%Y-%m-%d'), '2013')

# Mostrar los partidos en Streamlit
st.title("Partidos de Fútbol de la Liga de Brasil")
st.header(f"Partidos del {fecha.strftime('%Y-%m-%d')} al {fecha_fin.strftime('%Y-%m-%d')}")
mostrar_partidos_en_tabla(partidos)










