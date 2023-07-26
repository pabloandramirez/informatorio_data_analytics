import numpy as np
import pandas as pd

df = pd.read_csv('calls.csv')

df2 = pd.read_csv("data_analytics\openweather\Bogota2023_07_26.csv" , encoding='latin-1')

df2.to_excel('Bogota2023_07_26.xlsx', index=False)

df.to_excel('calls.xlsx', index=False)


print(df.head(n=50))
df.info()
df.shape
#agrupa el promedio de las duraciones de las llamadas por el id del agente
#print(df[['agentid', 'duration']].groupby(['agentid']).mean())

#agrupa el promedio de las duraciones de las llamadas por el id del agente pero de forma ascendente
#print(df[['agentid', 'duration']].groupby(['agentid']).mean().sort_values(by=['duration']))

#agrupa el promedio de las duraciones de las llamadas por el id del agente pero de forma descendente
print(df[['agentid', 'duration']].groupby(['agentid']).mean().sort_values(by=['duration'], ascending=False))

