# 02-knn.py
# Implementación del algoritmo k-vecinos más cercanos (k-NN)

inception = [0.2, 0.9, 0.0]
avengers  = [0.8, 0.3, 1.0]
dune      = [0.2, 0.9, 0.0]

def distancia(a,b):
    return sum([abs(x-y) for x,y in zip(a,b)])

print(distancia(inception, avengers))
print(distancia(inception, dune))

def knn(pelicula, dataset, k):
    distancias = []
    
    for nombre, features in dataset.items():
        dist = round(distancia(pelicula, features),4)
        distancias.append((nombre, dist))
    
    distancias.sort(key=lambda x: x[1])
    return distancias[:k]

peliculas = {
    "Inception":     [0.2, 0.9, 0.0],
    "Avengers":      [0.8, 0.3, 1.0],
    "Interstellar":  [0.1, 1.0, 0.0],
    "Matrix":        [0.3, 0.8, 0.1],
    "Titanic":       [0.1, 0.0, 0.0],
}

dune = [0.2, 0.9, 0.0]

print(knn(dune, peliculas, 3))