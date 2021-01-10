import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    
    return mano

def es_escalera_real(mano):
    
    for i in range(len(mano)-1):
        if mano[i][0] != mano[i+1][0]: #Comparando palos
            return False
    valores_reales=['10','as','jota','reina','rey']
    valores_reales.sort()
    valores_mano=[]
    for carta in mano:
        valores_mano.append(carta[1])
    valores_mano.sort()
    if valores_mano == valores_reales:
        print(mano)
        return True
    else:
        return False
def es_escalera_color(mano):
    for i in range(len(mano)-1):
        if mano[i][0] != mano[i+1][0]: #Comparando palos
            return False
    for carta in mano:  #Obtenemos valores de cada carta
        valores_mano.append(carta[1])
    valores_mano.sort() ## ¿Como ordenarlos correctamente para comparar?         <--------
    for i in range(len(valores_mano)-1): ## Revisar que están ordenados.
        indice=VALORES.index(valores_mano[i])
        if VALORES[indice+1] != valores_mano[i+1] :
            return False
    return True

def es_poquer(mano):
    return False
def es_full(mano):
    return False
def es_color(mano):
    return False
def es_escalera(mano):
    return False
def es_tercia(mano):
    return False
def es_doble_par(mano):
    return False

def es_pares(mano):
    valores = []
    for carta in mano:
        valores.append(carta[1])

    counter = dict(collections.Counter(valores))
    for val in counter.values():
        if val == 2:
            return True
    return False
    
def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    escalera_real=0
    escalera_color=0
    poquer=0
    full=0
    color=0
    escalera=0
    tercia=0
    doble_par=0
    pares = 0
    for mano in manos:
        if(es_escalera_real(mano)):
            escalera_real+=1
        if(es_escalera_color(mano)):
            escalera_color+=1
        if(es_poquer(mano)):
            poquer+=1
        if(es_full(mano)):
            full+=1
        if(es_color(mano)):
            color+=1
        if(es_escalera(mano)):
            escalera+=1
        if(es_tercia(mano)):
            tercia+=1
        if(es_doble_par(mano)):
            doble_par+=1
        if(es_pares(mano)):
             pares+=1

    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')


if __name__ == '__main__':
    #tamano_mano = int(input('De cuantas barajas sera la mano: '))
    tamano_mano=5
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))
    #main(tamano_mano, intentos)