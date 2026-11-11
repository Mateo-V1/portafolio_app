import streamlit as st
from PIL import Image

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');
        
        h1, h2, h3, p, div[data-testid="stMarkdownContainer"] {
            font-family: 'Montserrat', sans-serif !important;
        }
        
        [data-testid="stSidebar"] {
            background-color: #D0F5C8 !important;
        }

        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p {
            color: #222222 !important;
        }

        img {
            border-radius: 10px;
        }

        
    </style>
""", unsafe_allow_html=True)

st.title("Portafolio: Aplicaciones de Streamlit - Mateo Villada")

with st.sidebar:
  st.subheader("Portafolio: Aplicaciones de Streamlit")
  parrafo = (
    "En este portafolio encontrarás las aplicaciones de Streamlit en las que he trabajado "
    "a lo largo de las clases. Cada proyecto aborda diferentes temáticas como álgebra lineal, "
    "optimización, análisis de datos, modelos de regresión, series de tiempo, calidad del aire e Internet de las Cosas (IoT)."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/computacinavanzada/inicio?pli=1&authuser=0"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"[Enlace para páginas y ejercicios]({url_ia})")

col1, col2, col3 = st.columns(3)

with col1:
 st.subheader("1. Frut")
 image = Image.open('01_vectores_matrices.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace explorarás la aplicación interactiva de Frut.") 
 url = "https://frutasapp-m26a85z3nfzxbyf6gdsbaj.streamlit.app/"
 st.write(f"[Frut]({url})")

 st.subheader("4. Módulo 5 — Datos: preparación y estructur")
 image = Image.open('04_preparacion_datos.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás la preparación y estructura de los datos.") 
 url = "https://3yaxmzymshcffpoxausx6k.streamlit.app/"
 st.write(f"[Módulo 5 — Datos]({url})")

 st.subheader("7. Regresión — Conceptos clave")
 image = Image.open('06_regresion_lineal.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace explorarás los conceptos clave de la regresión.") 
 url = "https://regresionapp-dzsjavdxhd9farcata3sbk.streamlit.app/"
 st.write(f"[Regresión — Conceptos clave]({url})")

 st.subheader("10. 🌡️ Predictor de Sensación Térmica")
 image = Image.open('08_calidad_aire.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace podrás predecir la sensación térmica.") 
 url = "https://tiempoapp-vn7agnn6mw4wdtujtwps8y.streamlit.app/"
 st.write(f"[Predictor de Sensación Térmica]({url})")

with col2: 
 st.subheader("2. Gradientes")
 image = Image.open('02_calculo_gradiente.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás la optimización por gradiente descendente.") 
 url = "https://gradienteapp-hxaetjbaoeqwkmth3ylocw.streamlit.app/"
 st.write(f"[Gradientes]({url})")

 st.subheader("5. ¿Lloverá mañana? — Regresión Logística interactiva")
 image = Image.open('10_regresion_logistica.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás el paso de modelos lineales a clasificación logística.") 
 url = "https://regresionlogisticaapp-pv9ony8ndnayzywejady7f.streamlit.app/"
 st.write(f"[¿Lloverá mañana?]({url})")

 st.subheader("8. Eficiencia y paralelismo en Python")
 image = Image.open('05_app_preparacion_datos.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás técnicas de eficiencia y paralelismo en Python.") 
 url = "https://paralelismoapp-gcptmjqcg5lfke3hzxpmdu.streamlit.app/"
 st.write(f"[Eficiencia y paralelismo]({url})")

with col3: 
 st.subheader("3. Detector anomalias")
 image = Image.open('03_logica_bigo_vectorizacion.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás el detector de anomalías.") 
 url = "https://detectoranomaliasapp-wgtvagjqi8kpcgea6swnb6.streamlit.app/"
 st.write(f"[Detector anomalias]({url})")

 st.subheader("6. 🌡️ Series de Tiempo — Sensor IoT interactivo")
 image = Image.open('07_series_de_tiempo.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace podrás analizar series temporales de un sensor IoT.") 
 url = "https://serietiempoapp-qz3b6s96qssatejv5ffkin.streamlit.app/"
 st.write(f"[Series de Tiempo — Sensor IoT]({url})")

 st.subheader("9. Modelo de consumo energético")
 image = Image.open('09_sistema_iot.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace verás el modelo de consumo energético.") 
 url = "https://h7eea7chyodaji72ddhrmr.streamlit.app/"
 st.write(f"[Modelo de consumo energético]({url})")
