
import openai

def evaluar_respuesta(codigo, pregunta, respuesta):
    prompt = f"Pregunta: {pregunta}\nRespuesta: {respuesta}\nEvalúa la respuesta del 1 al 10 y da una breve explicación."
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un evaluador de entrevistas."},
            {"role": "user", "content": prompt}
        ]
    )
    contenido = completion.choices[0].message["content"]

    import re
    puntuacion = 5
    match = re.search(r"([1-9]|10)", contenido)
    if match:
        puntuacion = int(match.group(1))

    return {
        "evaluacion": contenido,
        "puntuacion": puntuacion
    }
