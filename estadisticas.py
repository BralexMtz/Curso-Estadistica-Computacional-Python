import math


def media(X):
   return sum(X)/len(X)

def varianza(X):
    suma=0
    mu=media(X)
    for x in X:
        suma+=(x - mu)**2
    return suma/len(X)

def desviacion_estandar(X):
    return math.sqrt(varianza(X))
