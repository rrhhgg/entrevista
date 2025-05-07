import streamlit as st
from PIL import Image

st.set_page_config(page_title="Entrevistas Grupo Gómez", page_icon="🍽️", layout="centered")

# Estilos en línea
st.markdown("""
    <style>
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 2em;
    }
    .botonera {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1.2em;
    }
    .botonera a {
        text-decoration: none;
    }
    .botonera button {
        background-color: #ff914d;
        color: white;
        border: none;
        padding: 0.8em 1.8em;
        font-size: 1.2em;
        border-radius: 1.5em;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .botonera button:hover {
        background-color: #ff7a26;
    }
    .botonera button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
    }
    </style>
""", unsafe_allow_html=True)

# Logo centrado
logo = Image.open("utilidades/logo gg.png")
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.image(logo, width=250)
st.markdown('</div>', unsafe_allow_html=True)

# Título
st.markdown("## Entrevistas Automáticas Grupo Gómez")
st.markdown("Selecciona el puesto para iniciar la entrevista:")

# Botones
st.markdown("""
<div class="botonera">
    <a href="https://entrevista-rrhhgg.streamlit.app/entrevista_camarero_v1" target="_self">
        <button>🍽️ Camarero</button>
    </a>
    <a href="https://entrevista-rrhhgg.streamlit.app/entrevista_demo" target="_self">
        <button>🔪 Cocinero</button>
    </a>
    <button disabled>👨‍🍳 Jefe de Cocina</button>
    <button disabled>👔 Director</button>
    <button disabled>🧼 Friegaplatos</button>
    <button disabled>🚚 Repartidor</button>
    <button disabled>👩‍✈️ Hostess</button>
</div>
""", unsafe_allow_html=True)