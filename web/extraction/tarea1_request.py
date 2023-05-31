import json
from urllib import request
from web.models import Station


# URL SEMILLA
url = 'https://api.citybik.es/v2/networks/bikerio'

respuesta = request.urlopen(url)

json_obtenido = json.loads( respuesta.read().decode('utf-8') ) #JSON formateado

def obtener_informacion_api(contador):
    for station_data in json_obtenido["network"]["stations"]:
        # Verificar si el registro ya existe en la base de datos
        Station.objects.get_or_create(
            id=station_data["id"],
            defaults={
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
        )
        # Si el registro ya existía, puedes modificar los campos correspondientes (boeleano falso)
        # if not created:
        #     station.contador = contador
        #     station.empty_slots = station_data["empty_slots"]
        #     station.name = station_data["name"]
        #     station.free_bikes = station_data["free_bikes"]
        #     station.latitude = station_data["latitude"]
        #     station.longitude = station_data["longitude"]
        #     station.timestamp = station_data["timestamp"]
        #     station.address = station_data["extra"]["address"]
        #     station.normal_bikes = station_data["extra"]["normal_bikes"]
        #     station.payment = station_data["extra"]["payment"]
        #     #+ Actualizo los valores
        #     station = station.save()

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