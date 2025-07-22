# sender.py

import requests

def enviar_mensaje(api_url, token, mensaje, formato):
    headers = {
        "Content-Type": "application/xml" if formato == "xml" else "application/json",
        "Authorization": token
    }

    try:
        response = requests.post(api_url, data=mensaje.encode('utf-8'), headers=headers)
        print("\n--- RESPUESTA DEL API ---")
        print("Código de estado:", response.status_code)
        print("Contenido:")
        print(response.text)
        return response
    except requests.exceptions.RequestException as e:
        print("Error al enviar el mensaje:", e)
        return None
