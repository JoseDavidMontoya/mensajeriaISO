# mensajeriaISOindeval

Herramienta automatizada para construir y enviar mensajes ISO 15022 e ISO 20022 (XML o JSON) a un API REST, usando datos desde una base de datos Oracle (mock en esta fase).

## Características

- Construcción de mensajes ISO 15022/20022
- Envío a API REST (con soporte para Bearer Token)
- Soporte para pruebas con `pytest` y reportes HTML
- Preparado para integración con pipelines CI/CD (AWS)

## Instalación

```bash
pip3 install -r requirements.txt



# Ejecución

python3 main.py

# Ejecutar pruebas

python3 -m pytest test_envio.py --html=report.html
