import json
from urllib import request
from web.models import Station


# URL SEMILLA
url = 'https://api.citybik.es/v2/networks/bikerio'

respuesta = request.urlopen(url)

json_obtenido = json.loads( respuesta.read().decode('utf-8') ) #JSON formateado

def obtener_informacion_api(contador):
    for station_data in json_obtenido["network"]["stations"]:
        defaults = {
            "contador": contador,
            "empty_slots": station_data["empty_slots"],
            "name": station_data["name"],
            "free_bikes": station_data["free_bikes"],
            "latitude": station_data["latitude"],
            "longitude": station_data["longitude"],
            "timestamp": station_data["timestamp"],
            "address": station_data["extra"]["address"],
            "normal_bikes": station_data["extra"]["normal_bikes"],
            "payment": station_data["extra"]["payment"],
        }
        
        obj, created = Station.objects.get_or_create(
            id = station_data["id"],
            defaults = defaults
        )
        
        # Comprobar si hay modificaciones y actualizar el objeto existente si es necesario
        if not created:
            is_updated = False
            for field, value in defaults.items():
                if getattr(obj, field) != value:
                    setattr(obj, field, value)
                    is_updated = True

            if is_updated:
                obj.save()

        print(contador, "-. ", station_data["name"])

        contador += 1
    print("----------------------------------------------\n Recorrido listo \n----------------------------------------------\n")



# Solo mostrar, sin guardar en BDD
#info = []
    # for station in json_obtenido["network"]["stations"]:
    #     # Diccionario que le paso la lista
    #     station_data = {
    #         "contador": contador,
    #         "empty_slots": station["empty_slots"],
    #         "id": station["id"],
    #         "name": station["name"],
    #         "free_bikes": station["free_bikes"],
    #         "latitude": station["latitude"],
    #         "longitude": station["longitude"],
    #         "timestamp": station["timestamp"],
    #         "address": station["extra"]["address"],
    #         "normal_bikes": station["extra"]["normal_bikes"],
    #         "payment": station["extra"]["payment"],
    #     }

    #     info.append( station_data )

    #     print(contador, "-. ", station_data["name"])
    # return info


    # station_id = station_data["id"]

    #     station, created = Station.objects.get_or_create(id=station_id)

    #     if not created:
    #         if any(
    #             getattr(station, field) != station_data[field]
    #             for field in ["empty_slots", "name", "free_bikes", "latitude", "longitude", "timestamp", "address", "normal_bikes", "payment"]
    #         ):
    #             for field in ["empty_slots", "name", "free_bikes", "latitude", "longitude", "timestamp", "address", "normal_bikes", "payment"]:
    #                 setattr(station, field, station_data[field])
    #             station.save()