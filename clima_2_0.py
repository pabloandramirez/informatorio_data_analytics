import requests
import json
import pandas as pd
from pandas import json_normalize
import datetime
import config

ciudades =  ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico City", "Dublin", "Tbilisi", "Bogota", "Tokio"]
coorList =   ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", 
              "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]
api_key = config.token
fecha_actual = datetime.datetime.now().strftime("%Y_%m_%d")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def clima_ciudades(coordenada):
    url = f"{BASE_URL}{coordenada}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        #Guardado en formato json
        response_json = response.json()

        ciudad = response_json["name"]
        ciudad_corregido = ciudad.replace(" ", "_")
        """with open(f"{ciudad}_weather.json", 'w') as output_file:
            json.dump(response_json, output_file)"""

        #print(response_json)

        # Normalizar el JSON de respuesta utilizando json_normalize, que ya lo pasa a DataFrame
        normalized_data = json_normalize(response_json)

        #print(normalized_data)

        #Pandas para DataFrame
        #df = pd.DataFrame(normalized_data)
        
        #Guardado en la carpeta local
        with open(f"data_analytics\openweather\{ciudad_corregido}{fecha_actual}.csv", 'w') as output_file:
            normalized_data.to_csv(output_file, index=False)

        print(f"El DataFrame ha sido guardado en {output_file}.")

def clima_por_ciudad(ciudad):
    url = f'{BASE_URL}q={ciudad}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        #Guardado en formato json
        response_json = response.json()
        """with open(f"{ciudad}_weather.json", 'w') as output_file:
            json.dump(response_json, output_file)"""

        #print(response_json)

        # Normalizar el JSON de respuesta utilizando json_normalize, que ya lo pasa a DataFrame
        normalized_data = json_normalize(response_json)

        #print(normalized_data)

        #Pandas para DataFrame
        #df = pd.DataFrame(normalized_data)
        
        #Guardado en la carpeta local
        ciudad_corregido = ciudad.replace(" ", "_")
        with open(f"data_analytics\openweather2\{ciudad_corregido}{fecha_actual}.csv", 'w') as output_file:
            normalized_data.to_csv(output_file, index=False)

        print(f"El DataFrame ha sido guardado en {output_file}.")


#Ese if indica que correra si ejecuto este script directo desde aca y no si lo corro importado en otro script
if __name__ == '__main__':
    for coordenada in coorList:
        clima_ciudades(coordenada)
    for ciudad in ciudades:
        clima_por_ciudad(ciudad)

