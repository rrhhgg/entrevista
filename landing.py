import streamlit as st
from PIL import Image

st.set_page_config(page_title="Entrevistas Grupo Gómez", page_icon="🍽️", layout="centered")

# Cargar y centrar logo
logo = Image.open("utilidades/logo gg.png")
st.image(logo, width=300)

st.markdown("## Entrevistas Automáticas Grupo Gómez")
st.markdown("Selecciona el puesto para iniciar la entrevista:")

# Botones con enlaces a apps individuales
st.markdown("""
<div style='display: flex; justify-content: center; gap: 1.5em; flex-wrap: wrap; margin-top: 2em;'>
    <a href="https://entrevista-rrhhgg.streamlit.app/entrevista_camarero_v1" target="_self">
        <button style="font-size:1.2em; padding: 0.7em 1.5em;">🍽️ Camarero</button>
    </a>
    <a href="https://entrevista-rrhhgg.streamlit.app/entrevista_demo" target="_self">
        <button style="font-size:1.2em; padding: 0.7em 1.5em;">🔪 Cocinero</button>
    </a>
    <button style="font-size:1.2em; padding: 0.7em 1.5em;" disabled>👨‍🍳 Jefe de Cocina</button>
    <button style="font-size:1.2em; padding: 0.7em 1.5em;" disabled>👔 Director</button>
    <button style="font-size:1.2em; padding: 0.7em 1.5em;" disabled>🧼 Friegaplatos</button>
    <button style="font-size:1.2em; padding: 0.7em 1.5em;" disabled>🚚 Repartidor</button>
    <button style="font-size:1.2em; padding: 0.7em 1.5em;" disabled>👩‍✈️ Hostess</button>
</div>
""", unsafe_allow_html=True)