import os
import json
import requests

API_KEY = os.getenv("eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjI5NzQ5NDgyNCwiYWFpIjoxMSwidWlkIjo0NDIyNjMxNiwiaWFkIjoiMjAyMy0xMS0yMFQxNzowNjozNC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTY4ODEzMjIsInJnbiI6ImV1YzEifQ.o1cqRb0B9pGxLS2PQQbU4_RkQlhW3GhGVkGUV3xiCxI")
BOARD_ID = 1939525964

# Mapear columnas por ID
COLUMNAS = {
    "nombre": "name",
    "telefono": "phone_mkqjgqhj",
    "correo": "email_mkqjt99t",
    "direccion": {
        "via": "dropdown_mkqjbykm",
        "nombre_via": "text_mkqjmeh1",
        "numero": "numeric_mkqjjj0g",
        "puerta": "text_mkqjwkmz",
        "cp": "numeric_mkqjwczq",
        "ciudad": "text_mkqjx0sz"
    },
    "tiempo": "numeric_mkqjs2kq"
}

PREGUNTA_IDS = [
    ("numeric_mkqje1xr", "text_mkqjynvd"),
    ("numeric_mkqj583y", "text_mkqjq3x5"),
    ("numeric_mkqjtmhs", "text_mkqjvc1p"),
    ("numeric_mkqjp912", "text_mkqj3t0k"),
    ("numeric_mkqjax81", "text_mkqjtv3j"),
    ("numeric_mkqj4hff", "text_mkqj5mt8"),
    ("numeric_mkqjx55q", "text_mkqjqx0q"),
    ("numeric_mkqjx2t", "text_mkqjbfd8"),
    ("numeric_mkqjyb6b", "text_mkqjx2qd"),
    ("numeric_mkqj34xs", "text_mkqj998e"),
    ("numeric_mkqjsyt6", "text_mkqjks1c"),
    ("numeric_mkqjbvax", "text_mkqjdwx5")
]

def enviar_resultados(datos, respuestas):
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    telefono = datos.get("telefono", "").strip()
    if telefono and not telefono.startswith("+"):
        telefono = f"+34{telefono}"

    column_values = {
        COLUMNAS["nombre"]: datos.get("nombre", "Candidato"),
        COLUMNAS["telefono"]: {"phone": telefono},
        COLUMNAS["correo"]: datos.get("correo", ""),
        COLUMNAS["tiempo"]: datos.get("tiempo", 0),
        COLUMNAS["direccion"]["via"]: {"labels": [datos.get("tipo_via", "")]},
        COLUMNAS["direccion"]["nombre_via"]: datos.get("nombre_via", ""),
        COLUMNAS["direccion"]["numero"]: datos.get("numero", ""),
        COLUMNAS["direccion"]["puerta"]: datos.get("puerta", ""),
        COLUMNAS["direccion"]["cp"]: datos.get("cp", ""),
        COLUMNAS["direccion"]["ciudad"]: datos.get("ciudad", "")
    }

    for i, r in enumerate(respuestas):
        if i < len(PREGUNTA_IDS):
            col_punt, col_eval = PREGUNTA_IDS[i]
            column_values[col_punt] = r["puntuacion"]
            column_values[col_eval] = r["evaluacion"]

    mutation_query = f"""
    mutation {{
      create_item (
        board_id: {BOARD_ID},
        item_name: "{datos.get("nombre", "Candidato")}",
        column_values: {json.dumps(json.dumps(column_values))}
      ) {{
        id
      }}
    }}
    """

    response = requests.post("https://api.monday.com/v2", json={"query": mutation_query}, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error al enviar datos a Monday: {response.text}")
    return response.json()
