
import streamlit as st

def recoger_datos_entrevistado():
    st.header("Datos del entrevistado")

    tipo_via = st.selectbox("Tipo de vía", ["Calle", "Avenida", "Plaza", "Camino", "Carretera"])
    nombre_via = st.text_input("Nombre de la vía")
    numero = st.text_input("Número")
    puerta = st.text_input("Puerta")
    cp = st.text_input("Código Postal")
    ciudad = st.text_input("Ciudad")
    telefono = st.text_input("Teléfono (sin prefijo)")
    correo = st.text_input("Correo electrónico")
    dni = st.text_input("DNI/NIE")
    ss = st.text_input("Número de la Seguridad Social")

    if st.button("Empezar entrevista"):
        telefono = telefono.strip()
        if not telefono.startswith("+"):
            telefono = f"+34{telefono}"
        return {
            "direccion": f"{tipo_via} {nombre_via}, {numero}, {puerta}, {cp}, {ciudad}",
            "telefono": telefono,
            "correo": correo,
            "dni": dni,
            "nss": ss
        }
    return None
