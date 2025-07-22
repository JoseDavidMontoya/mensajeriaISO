# main.py

from config import ISO_TIPO, FORMATO, API_URL, TOKEN
from db_mock import obtener_datos
from message_builder import construir_mensaje
from sender import enviar_mensaje


datos = obtener_datos()
mensaje = construir_mensaje(datos, ISO_TIPO, FORMATO)

print(f"\n--- MENSAJE ISO {ISO_TIPO.upper()} ({FORMATO.upper()}) ---\n")
print(mensaje)

# Enviar a API de prueba
enviar_mensaje(API_URL, TOKEN, mensaje, FORMATO)
