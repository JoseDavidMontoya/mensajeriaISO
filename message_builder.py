import json
from lxml import etree

def construir_mensaje(datos, iso_tipo, formato):
    tipo = iso_tipo.lower()
    formato = formato.lower()

    if tipo.startswith("mt"):
        carpeta = "mt"
    elif tipo.startswith("mx"):
        carpeta = "mx"
    else:
        raise ValueError("Tipo ISO no soportado. Debe comenzar con 'mt' o 'mx'")

    ruta_plantilla = f"templates/{carpeta}/{tipo}_template.{formato}"

    if formato == "xml":
        tree = etree.parse(ruta_plantilla)
        root = tree.getroot()

        for el in root.iter():
            if el.tag in datos:
                el.text = datos[el.tag]

        return etree.tostring(tree, pretty_print=True).decode()

    elif formato == "json":
        with open(ruta_plantilla) as f:
            template_data = json.load(f)

        for k in datos:
            if k in template_data:
                template_data[k] = datos[k]

        return json.dumps(template_data, indent=2)

    elif formato == "txt":
        with open(ruta_plantilla, "r") as f:
            plantilla_txt = f.read()
        return plantilla_txt.format(**datos)

    else:
        raise ValueError("Formato no soportado. Usa 'xml', 'json' o 'txt'")
