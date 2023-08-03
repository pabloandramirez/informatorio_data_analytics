import requests
import json
import pandas as pd
from pandas import json_normalize
import datetime
import config
import os

ciudadesList =  ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico City", "Dublin", "Tbilisi", "Bogota", "Tokio"]
coorList =   ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", 
              "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]
API_KEY = config.token
FECHA_ACTUAL = datetime.datetime.now().strftime("%Y%m%d")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


def obtener_datos_climaticos_ciudades(ciudades):
    d = {'ids' : [], 'cities': [], 'weather' : [], 'temp_max': [], 'temp_min': []}
    for i in ciudades:
        url = f"{BASE_URL}q={i}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            id = data['id']
            name = data['name']
            weather = data['weather'][0]['main']
            temp_max = data['main']['temp_max']
            temp_min = data['main']['temp_min']
            d["ids"].append(id)
            d["cities"].append(name)
            d["weather"].append(weather)
            d["temp_max"].append(temp_max)
            d["temp_min"].append(temp_min)
        else:
            print(f"Error al obtener los datos de la ciudad de {name}: codigo {response.status_code}")
    df = pd.DataFrame(data=d)
    output_dir = "data_analytics/openweather"
    os.makedirs(output_dir, exist_ok=True)
    csv_file_path = os.path.join(output_dir, f"tiempodiario_{FECHA_ACTUAL}.csv")
    xlsx_file_path = os.path.join(output_dir, f"tiempodiario_{FECHA_ACTUAL}.xlsx")
    df.to_csv(csv_file_path, index=False)
    df.to_excel(xlsx_file_path, index=False, engine='openpyxl')
    return df

if __name__ == '__main__':
    obtener_datos_climaticos_ciudades(ciudadesList)
