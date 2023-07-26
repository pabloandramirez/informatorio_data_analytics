import requests
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from pandas import json_normalize
import datetime

# Configuración de la base de datos
#engine = create_engine('sqlite:///weather_data.db')
engine = create_engine('postgresql://postgres:nolocreo@localhost/weather_data')
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Definición de la tabla en la base de datos
class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    temperature = Column(Integer)
    description = Column(String)

# Creación de la base de datos
Base.metadata.create_all(engine)

# Obtención de datos meteorológicos de OpenWeatherMap
api_key = 'c8cfc85ff7481b57bd0c9f178cd4b0d0'
city = 'London,UK' # por ejemplo: 'London, UK'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(url)
data = response.json()
print(data)

normalized_data = json_normalize(data)

df = pd.DataFrame(normalized_data)

#nombre_csv = 'Resistencia_weather.csv'
#df.to_csv(nombre_csv, index=False)

#Guardado en la carpeta local
fecha_actual = datetime.datetime.now().strftime("%Y%m%d")
with open(f"Resistencia{fecha_actual}.csv", 'w') as output_file:
      df.to_csv(output_file, index=False)

print(f"El DataFrame ha sido guardado en {output_file}.")


# Extracción de los datos relevantes
temperature = data['main']['temp']
description = data['weather'][0]['description']

# Almacenamiento de los datos en la base de datos
session = Session()
weather_data = WeatherData(city=city, temperature=temperature, description=description)
session.add(weather_data)
session.commit()


print("Datos meteorológicos almacenados con éxito.")