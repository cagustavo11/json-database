import json


def clearJSON(jsonName):
    # Creo la estructura basica y por defecto con la lista vacia
    data = {
        "results": []
    }
    # Abro el archivo json  y además establezco la acción de 'write', que significa escritura.
    openJson = open(f'{jsonName}.json', 'w')
    # Ejecuto el método write que me permite pasarle un string para escribir sobre el json
    # en el interior del método write ejecuto otro método que es el json.dumps que me permite convertir la sintaxis de python a formato json.
    openJson.write(json.dumps(data, indent=4))
    openJson.close()
