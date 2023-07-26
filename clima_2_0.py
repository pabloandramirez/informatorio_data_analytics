import requests
import json
import pandas as pd
from pandas import json_normalize
import datetime

ciudades =  ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
coorList =   ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

def clima_ciudades(coordenada, ciudad):
    api_key = "c8cfc85ff7481b57bd0c9f178cd4b0d0"
    url = f"https://api.openweathermap.org/data/2.5/weather?{coordenada}&appid={api_key}&units=metric"
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
        fecha_actual = datetime.datetime.now().strftime("%Y_%m_%d")
        with open(f"data_analytics\openweather\{ciudad}{fecha_actual}.csv", 'w') as output_file:
            normalized_data.to_csv(output_file, index=False)

        print(f"El DataFrame ha sido guardado en {output_file}.")

if __name__ == '__main__':
    for (coordenada, ciudad) in zip(coorList, ciudades):
        clima_ciudades(coordenada, ciudad.replace(" ", "_"))

