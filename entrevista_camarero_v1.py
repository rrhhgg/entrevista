import streamlit as st
import json
import time
from enviar_a_monday import enviar_resultados
from utilidades.temporizador import temporizador
from utilidades.evaluador import evaluar_respuesta
from utilidades.datos_utils import recoger_datos_entrevistado

# Cargar preguntas
with open("estructura/preguntas_generales.json", "r", encoding="utf-8") as f:
    preguntas_generales = json.load(f)

with open("estructura/preguntas_camarero.json", "r", encoding="utf-8") as f:
    preguntas_especificas = json.load(f)

# Configuración de la app
st.set_page_config(page_title="Entrevista Camarero", layout="centered")
st.title("Entrevista Camarero")

# Recoger datos del entrevistado
if "datos" not in st.session_state:
    datos = recoger_datos_entrevistado()
    if datos:
        st.session_state.datos = datos
        st.session_state.pregunta_actual = 0
        st.session_state.respuestas = []
        st.experimental_rerun()
else:
    preguntas = preguntas_generales + preguntas_especificas
    total_preguntas = len(preguntas)
    idx = st.session_state.pregunta_actual

    if idx < total_preguntas:
        pregunta = preguntas[idx]
        st.markdown(f"### Pregunta {idx+1} de {total_preguntas}")
        st.markdown(f"**{pregunta['texto']}**")
        st.markdown("⏱️ Tiempo máximo para responder: 120 segundos")

        respuesta = temporizador(f"respuesta_{idx}", 120)

        if respuesta is not None:
            with st.spinner("Analizando respuesta..."):
                evaluacion = evaluar_respuesta(pregunta["codigo"], pregunta["texto"], respuesta)
            st.session_state.respuestas.append({
                "codigo": pregunta["codigo"],
                "pregunta": pregunta["texto"],
                "respuesta": respuesta,
                "evaluacion": evaluacion["evaluacion"],
                "puntuacion": evaluacion["puntuacion"]
            })
            st.session_state.pregunta_actual += 1
            st.experimental_rerun()
    else:
        with st.spinner("Enviando los resultados a Monday..."):
            enviar_resultados(st.session_state.datos, st.session_state.respuestas)
        st.success("¡Gracias por completar la entrevista!")
        st.markdown("Nos pondremos en contacto contigo si avanzas a la siguiente fase. 🫶")
        st.stop()
