inception = [0.2, 0.9, 0.0]
avengers  = [0.8, 0.3, 1.0]
dune      = [0.2, 0.9, 0.0]

def distancia(a,b):
    return sum([abs(x-y) for x,y in zip(a,b)])

print(distancia(inception, avengers))
print(distancia(inception, dune))

