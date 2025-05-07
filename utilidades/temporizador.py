
import streamlit as st
import time

def temporizador(key, max_time=120):
    start_time_key = f"{key}_start"
    respuesta_key = f"{key}_respuesta"

    if start_time_key not in st.session_state:
        st.session_state[start_time_key] = time.time()

    tiempo_pasado = time.time() - st.session_state[start_time_key]

    if tiempo_pasado > max_time:
        return st.session_state.get(respuesta_key, "")

    respuesta = st.text_area("Tu respuesta", key=respuesta_key)
    if st.button("Enviar respuesta"):
        return respuesta

    return None
