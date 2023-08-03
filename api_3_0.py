import requests
import json
import pandas as pd
from pandas import json_normalize
import datetime
from datetime import timedelta
import config

coordList =   ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", 
              "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", 
              "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

ciudades =  ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", 
             "Mexico City", "Dublin", "Tbilisi", "Bogota", "Tokio"]

api_key = config.token

responses = []
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

for j in range(5):
    url = f"{BASE_URL}{coordList[i]}&dt={int(ts)}&appid={api_key}&units=metric"
    timestamp = ts
    #Convertir datetime a unix para leer fecha
    dt = datetime.now()
    date = dt.strftime("%Y-%m-%d")
    ts = ts + 86400 #aca ya tiene un día más
    response = requests.get(url).json()
    responses.append(response)
    with open(f"{ciudades[i]}_{date}_weather.json", 'w') as outfile:
        json.dump(response, outfile, indent=4, separators=(',',': '))

"""for i in range(len(ciudades)):"""



def obtener_datos_climaticos_ultimos_5_dias(ciudad, coords, api_key):
    datos_climaticos = []
    fecha_actual = datetime.utcnow()
    for i in range(1, 6):
        fecha_consulta = fecha_actual - timedelta(days=i)
        timestamp_consulta = int(fecha_consulta.timestamp())
        url = f"{BASE_URL}{coords}&q={ciudad}&dt={timestamp_consulta}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        datos_climaticos.append(data)
    return datos_climaticos


#https://api.openweathermap.org/data/2.5/forecast?units=metric&cnt=40&
#https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API}

#dt = datetime.fromtimestamp( timestamp, tz=timezone.utc )

