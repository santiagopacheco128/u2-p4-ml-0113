import pandas as pd
import numpy as np
# santiago pacheco nc 0113
n_filas=5
n_columnas=5
tags_columna=tuple("ABCDE") # etiquetas para las columnas
print(tags_columna)
matriz = np.random.randint(1, 6, size=(n_filas, n_columnas))
print("genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# la varaiables df es DataFrame
df = pd.DataFrame(matriz, columns=tags_columna)
print("----- La tabla o dataframe ------NC  = 0113")
print(df)
print("----- santiago pacheco nc 0113 ------")