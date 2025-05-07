import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Entrevistas Grupo Gómez", page_icon="🍽️")

logo = Image.open("utilidades/logo gg.png")
st.image(logo, width=200)

st.title("Entrevistas Automáticas Grupo Gómez")

st.markdown("Selecciona el puesto para iniciar la entrevista:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🍽️ Camarero"):
        switch_page("entrevista_camarero_v1")

with col2:
    if st.button("🔪 Cocinero"):
        switch_page("entrevista_demo")

with col3:
    st.button("👨‍🍳 Jefe de Cocina", disabled=True)

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    st.button("👔 Director", disabled=True)

with col5:
    st.button("🧼 Friegaplatos", disabled=True)

with col6:
    st.button("🚚 Repartidor", disabled=True)

st.markdown("👩‍✈️ Hostess (próximamente)", unsafe_allow_html=True)