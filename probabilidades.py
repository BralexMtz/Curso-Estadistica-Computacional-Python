import random

def tirar_dado(num_lanzamientos,dados):
    sequencia_de_tiros=[]
    for _ in range(num_lanzamientos):
        suma=0
        for _ in range(dados):
            suma += random.choice([1,2,3,4,5,6])
        sequencia_de_tiros.append(suma)
    return sequencia_de_tiros

def obtener_probabilidad(tiros,numero_de_repeticiones):
    # Probabilidad de que haya un 1 en N tiros del dado
    tiros_acertados=0
    for tiro in tiros:
        if valor in tiro: # Condicion de probabilidad
            tiros_acertados+=1

    probabilidad= tiros_acertados/numero_de_repeticiones
    return probabilidad

def main(num_lanzamientos,numero_de_repeticiones,dados,valor):
    
    probabilidad=0
    for paso in range(100):
        tiros=[]
        for _ in range(numero_de_repeticiones):
            sequencia_de_tiros=tirar_dado(num_lanzamientos,dados)
            tiros.append(sequencia_de_tiros)
        
        probabilidad += obtener_probabilidad(tiros,numero_de_repeticiones) 
    probabilidad/=100

    print(f'Probabilidad de obtener un {valor} en {num_lanzamientos} tiros : {probabilidad}')

if __name__ == "__main__":
    dados = int(input('Cuantos dados: '))
    valor = int(input('Valor que queremos validar: ')) 
    num_lanzamientos = int(input('Cuantos lanzamientos de los dados: '))
    numero_de_repeticiones = int(input('Cuantas veces repetimos la simulacion: '))
    main(num_lanzamientos,numero_de_repeticiones,dados,valor)
