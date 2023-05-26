import json
from urllib import request


# URL SEMILLA
url = 'https://api.citybik.es/v2/networks/bikerio'

respuesta = request.urlopen(url)

json_obtenido = json.loads( respuesta.read().decode('utf-8') ) #JSON formateado

info = []

def obtener_informacion_api(contador):
    for station in json_obtenido["network"]["stations"]:
        # Diccionario que le paso la lista
        station_data = {
            "contador": contador,
            "empty_slots": station["empty_slots"],
            "id": station["id"],
            "name": station["name"],
            "free_bikes": station["free_bikes"],
            "latitude": station["latitude"],
            "longitude": station["longitude"],
            "timestamp": station["timestamp"],
            "address": station["extra"]["address"],
            "normal_bikes": station["extra"]["normal_bikes"],
            "payment": station["extra"]["payment"],
        }

        info.append( station_data )

        print(contador, "-. ", station_data["name"])

        contador += 1

    return info