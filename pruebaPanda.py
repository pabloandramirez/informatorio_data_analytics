import pandas as pd

# Extracción: Leer datos CSV en un DataFrame
df = pd.read_csv('calls.csv')

# Transformación: Aplicar alguna transformación a los datos
df['total'] = df['duration'] * df['customerid']  # Calcular el total de cada venta

# Carga: Guardar el DataFrame transformado en un nuevo archivo CSV
df.to_csv('datos_ventas_transformados.csv', index=False)