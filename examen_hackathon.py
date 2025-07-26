# Importar librerías
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_excel(r'datasetLimpio.xlsx')


#mostrar las columnas con datos Null o faltantes
df.isnull().sum()

# Eliminar filas con valores nulos en la columna 'vibración'
df = df.dropna(subset=['vibración'])

# Mostrar la cantidad de valores únicos
df['vibración'].value_counts()

df = df.dropna(subset=['temperatura'])

# Mostrar la cantidad de valores únicos en 'temperatura'
df['temperatura'].value_counts()

# Eliminar filas con valores nulos en la columna 'humedad'
df = df.dropna(subset=['humedad'])

# Mostrar la cantidad de valores únicos en 'humedad'
df['humedad'].value_counts()

df['temperatura'].value_counts()

# Eliminar filas con valores nulos en la columna 'tiempo ciclo'
df = df.dropna(subset=['tiempo_ciclo'])

# Mostrar la cantidad de valores únicos en 'tiempo ciclo'

df['tiempo_ciclo'].value_counts()

#------------------------------------------------------------------------------------------------------------------

