import random


def calcular_pi(n):
    points_in_circle=0
    for _ in range(n):
        x=random.random()
        y=random.random()
        distance=(x**2 + y**2)**0.5
        if distance<=1:
            points_in_circle+=1
    
    return 4*points_in_circle/n



if __name__ == "__main__":
    pi=calcular_pi(10000000)
    print(f'pi = {pi}')