
from borracho import BorrachoDeIzquierda
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure,show

def caminata(campo,borracho,pasos):
    inicio  = campo.obtener_coordenada(borracho)
    x_arr=[]
    y_arr=[]
    x_arr.append(inicio.x)
    y_arr.append(inicio.y)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        x_arr.append(campo.obtener_coordenada(borracho).x)
        y_arr.append(campo.obtener_coordenada(borracho).y)

    graficar(x_arr,y_arr)
    
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos,numero_de_intentos,tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0,0)
    distancias=[]

    for _ in range(numero_de_intentos):
        campo=Campo()
        campo.anadir_borracho(borracho,origen)
        distancia_caminata=caminata(campo,borracho,pasos)
        distancias.append( round(distancia_caminata,1) )

    return distancias
def graficar(x,y):
    grafica= figure(title='Camino aleatorio',x_axis_label='eje x',y_axis_label='eje y')
    grafica.line(x,y)
    show(grafica)

def main(num_pasos,numero_de_intentos,tipo_de_borracho):
    distancias_medias_por_caminata=[]
    
    for pasos in num_pasos:
        distancias = simular_caminata(pasos,numero_de_intentos,tipo_de_borracho)
        distancia_media = round(sum(distancias)/len(distancias), 4)
        distancias_medias_por_caminata.append(distancia_media)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_de_borracho.__name__} caminata aletaria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'MAX   = {distancia_maxima}')
        print(f'Min   = {distancia_minima}')


if __name__ == "__main__":
    
    num_pasos = [1000000]
    numero_de_intentos = 1


    main(num_pasos,numero_de_intentos,BorrachoDeIzquierda)