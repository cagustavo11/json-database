import json


def readJSON(jsonName):

    openJson = open(f'{jsonName}.json', 'r').read()
    # en caso de que el json esté vacio creo la estructura basica y por defecto con la lista vacia y retornamos la lista
    if len(openJson) == 0:
        data = {
            "results": []
        }
        return data.get('results')
    # en caso contrario simplemente ejecuto el método json.loads que me permite transformar de formato a json a algo entendible por python y su vez cojo los results
    listData = json.loads(openJson).get('results')
    # retorno la lista
    return listData
