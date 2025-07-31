# test_envio.py

import requests
from config import API_URL, TOKEN, FORMATO, ISO_TIPO
from db_mock import obtener_datos
from message_builder import construir_mensaje
from sender import _es_mt548


def test_envio_mensaje_exitoso():
    datos = obtener_datos()
    mensaje = construir_mensaje(datos, ISO_TIPO, FORMATO)

    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/xml" if FORMATO == "xml" else "application/json"
    }

    response = requests.post(API_URL, data=mensaje.encode('utf-8'), headers=headers)

    print("\nRespuesta:\n", response.text)

    assert response.status_code == 200, "La API respondió con error"
    assert "data" in response.text, "La respuesta no contiene el payload esperado"
    assert _es_mt548(response.text), "La respuesta no es un mensaje MT548"