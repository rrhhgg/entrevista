import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Entrevistas Grupo Gómez", page_icon="🍽️", layout="centered")

# Logo centrado
logo = Image.open("utilidades/logo gg.png")
st.image(logo, width=250)

st.markdown("## Entrevistas Automáticas Grupo Gómez")
st.markdown("Selecciona el puesto para iniciar la entrevista:")

# Botones centrados y funcionales
col1, col2 = st.columns(2)

with col1:
    if st.button("🍽️ Camarero"):
        switch_page("entrevista_camarero_v1")

with col2:
    if st.button("🔪 Cocinero"):
        switch_page("entrevista_demo")

# Resto de roles deshabilitados
st.markdown("### Próximamente:")
st.button("👨‍🍳 Jefe de Cocina", disabled=True)
st.button("👔 Director", disabled=True)
st.button("🧼 Friegaplatos", disabled=True)
st.button("🚚 Repartidor", disabled=True)
st.button("👩‍✈️ Hostess", disabled=True)