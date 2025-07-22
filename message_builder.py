# message_builder.py

import json
from lxml import etree

def construir_mensaje(datos, tipo, formato):
    plantilla = f"templates/iso{tipo}_template.{formato}"
    
    if formato == "xml":
        tree = etree.parse(plantilla)
        root = tree.getroot()

        for el in root.iter():
            if el.tag in datos:
                el.text = datos[el.tag]

        return etree.tostring(tree, pretty_print=True).decode()
    
    elif formato == "json":
        with open(plantilla) as f:
            data = json.load(f)

        for k in datos:
            if k in data:
                data[k] = datos[k]

        return json.dumps(data, indent=2)
