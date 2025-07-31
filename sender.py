import requests

def enviar_mensaje(api_url, token, payload, formato):
    headers = {
        "Authorization": token,
        "Content-Type": _obtener_content_type(formato)
    }

    try:
        response = requests.post(api_url, data=payload.encode('utf-8'), headers=headers)
        print("\n--- RESPUESTA DEL ENDPOINT ---")
        print(f"Status Code: {response.status_code}")
        print("Cuerpo:")
        print(response.text)
        if _es_mt548(response.text):
            print("La respuesta es un mensaje MT548.")
        else:
            print("La respuesta NO es un mensaje MT548.")
        return response
    except requests.exceptions.RequestException as e:
        print("Error al enviar el mensaje:", e)
        return None

def _obtener_content_type(formato):
    if formato == "xml":
        return "application/xml"
    elif formato == "json":
        return "application/json"
    else:
        return "text/plain"


def _es_mt548(texto_respuesta):
    # Busca el identificador MT548 en el texto de la respuesta
    return "MT548" in texto_respuesta or ":548:" in texto_respuesta