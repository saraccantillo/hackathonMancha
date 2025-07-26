import pandas as pd

# Leer el archivo CSV
data = pd.read_csv('Dataset_Talento.csv')

# Limpieza de columnas [temperatura, humedad, vibración, tiempo_ciclo]
# Temperatura
data['temperatura'] = data['temperatura'].astype("string")
data['temperatura'] = data['temperatura'].str.replace('.', '', regex=False)
data['temperatura'] = data['temperatura'].str[:3] 
data['temperatura'] = data['temperatura'].str[:2] + '.' + data['temperatura'].str[2]
data['temperatura'] = data['temperatura'].astype(float)

# Humedad
data['humedad'] = data['humedad'].astype("string")
data['humedad'] = data['humedad'].str.replace('.', '', regex=False)
data['humedad'] = data['humedad'].str[:3] 
data['humedad'] = data['humedad'].str[:2] + '.' + data['humedad'].str[2]
data['humedad'] = data['humedad'].astype(float)

# Vibración
data['vibración'] = data['vibración'].astype("string")
data['vibración'] = data['vibración'].str.replace('.', '', regex=False)
data['vibración'] = data['vibración'].str[:2] 
data['vibración'] = data['vibración'].str[:1] + '.' + data['vibración'].str[1]
data['vibración'] = data['vibración'].astype(float)

# Tiempo_ciclo
data['tiempo_ciclo'] = data['tiempo_ciclo'].astype("string")
data['tiempo_ciclo'] = data['tiempo_ciclo'].str.replace('.', '', regex=False)
data['tiempo_ciclo'] = data['tiempo_ciclo'].str[:3] 
data['tiempo_ciclo'] = data['tiempo_ciclo'].str[:2] + '.' + data['tiempo_ciclo'].str[2]
data['tiempo_ciclo'] = data['tiempo_ciclo'].astype(float)

# Eficiencia porcentual
data['eficiencia_porcentual'] = data['eficiencia_porcentual'].astype("string")
data['eficiencia_porcentual'] = data['eficiencia_porcentual'].str.replace('.', '', regex=False)
data['eficiencia_porcentual'] = data['eficiencia_porcentual'].str[:3] 
data['eficiencia_porcentual'] = data['eficiencia_porcentual'].str[:2] + '.' + data['eficiencia_porcentual'].str[2]
data['eficiencia_porcentual'] = data['eficiencia_porcentual'].astype(float)

# ----------------------------------------
# Limpieza de campos vacíos
# Mostrar las columnas con datos nulos
print(data.isnull().sum())

# Eliminar filas con valores nulos en columnas clave
data = data.dropna(subset=['vibración'])
data = data.dropna(subset=['temperatura'])
data = data.dropna(subset=['humedad'])
data = data.dropna(subset=['tiempo_ciclo'])
data = data.dropna(subset=['eficiencia_porcentual'])

# Mostrar conteo de valores únicos
print(data['vibración'].value_counts())
print(data['temperatura'].value_counts())
print(data['humedad'].value_counts())
print(data['tiempo_ciclo'].value_counts())
print(data['eficiencia_porcentual'].value_counts())

# Rellenar campos vacíos
data['tipo_fallo'] = data['tipo_fallo'].fillna("No especifica")
data['observaciones'] = data['observaciones'].fillna("No especifica")

# Exportar el DataFrame limpio a Excel
data.to_excel('Dataset_Talento_limpio.xlsx', index=False)

