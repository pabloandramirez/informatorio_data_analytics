import requests
import json
import pandas as pd
from pandas import json_normalize
import datetime

if __name__ == '__main__':
    lat = "-27.451100"
    lon = "-58.986600"
    api_key = "c8cfc85ff7481b57bd0c9f178cd4b0d0"
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    response = requests.get(url)
if response.status_code == 200:
    #Guardado en formato json
    response_json = response.json()
    with open("Resistencia_weather.json", 'w') as output_file:
        json.dump(response_json, output_file)

    print(response_json)

    # Normalizar el JSON de respuesta utilizando json_normalize, que ya lo pasa a DataFrame
    normalized_data = json_normalize(response_json)

    print(normalized_data)

    #Pandas para DataFrame
    #df = pd.DataFrame(normalized_data)
    
    #Guardado en la carpeta local
    fecha_actual = datetime.datetime.now().strftime("%Y_%m_%d")
    with open(f"data_analytics\openweather\Resistencia{fecha_actual}.csv", 'w') as output_file:
        normalized_data.to_csv(output_file, index=False)

    print(f"El DataFrame ha sido guardado en {output_file}.")