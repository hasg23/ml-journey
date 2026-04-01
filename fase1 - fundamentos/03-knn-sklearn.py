# 03-knn-sklearn.py
# Implementación del algoritmo k-vecinos más cercanos (k-NN) con scikit-learn
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

peliculas = { ... }

# Preparamos los datos
X = []
y = []
for nombre, features in peliculas.items():
    ...

# Creamos el modelo
modelo = KNeighborsClassifier(n_neighbors=3)
# Entrenamos el modelo
modelo.fit(X, y)
# Predecimos
print(modelo.predict([[0.2, 0.9, 0.0]]))