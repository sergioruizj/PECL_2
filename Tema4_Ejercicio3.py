'''
Se tiene un sistema de billetes de distintos valores y ordenados de menor a mayor 
(por  ejemplo  1,  2,  5,  10,  20,  50  y  100  euros),  que  se  representan  mediante  los  
valores vi,  con  i ∈ {1, ..., N} (en  el  caso  anterior,  N = 7)  de  manera  que  de  cada  
billete  se  tiene  una  cantidad  finita,  mayor  o  igual  a  cero,  que  se  guarda  en  𝑐𝑐𝑖𝑖 
(siguiendo con el ejemplo, c3 = 6 representaría que hay 6 billetes de 5 euros). 
Se quiere pagar exactamente una cierta cantidad de dinero D, utilizando para ello 
la menor cantidad de billetes posible. Se sabe que D ≤ ∑ ci*vi , pero puede que 
la cantidad exacta D no sea obtenible mediante los billetes disponibles. Diseñar  un  algoritmo  de  Programación  Dinámica  que  determine,  teniendo  como  
datos los valores ci, vi y D: 
 Si la cantidad D puede devolverse exactamente o no. 
 En  caso  afirmativo,  cuantos  billetes  de  cada  tipo  forman  la  descomposición  
óptima.
'''

import math

def cambiar_dinero_min_billetes(v, c, D):
    """
    v: lista de valores de billetes (por ejemplo [1, 2, 5, 10, 20, 50, 100])
    c: lista de cantidades disponibles para cada billete (por ejemplo [3, 1, 1, 1, 2, 0, 1])
    D: cantidad que se quiere pagar (por ejemplo 43)
    """

    N = len(v)  # número de tipos de billetes

    # Inicializamos la tabla dp con infinito (significa que no se puede alcanzar esa cantidad)
    dp = [math.inf] * (D + 1)
    dp[0] = 0  # Para obtener 0€, se necesitan 0 billetes

    # Esta tabla guarda cuántos billetes de cada tipo se usaron para llegar a cada cantidad
    used = [[0] * N for _ in range(D + 1)]

    # Recorremos cada tipo de billete
    for i in range(N):
        # Vamos desde D hasta 0 para no reutilizar el mismo billete más veces de las permitidas
        for x in range(D, -1, -1):
            if dp[x] < math.inf:
                # Probamos usar de 1 hasta c[i] billetes del tipo i
                for k in range(1, c[i] + 1):
                    nueva_cantidad = x + k * v[i]
                    if nueva_cantidad > D:
                        break  # si nos pasamos, salimos del bucle

                    # Si encontramos una forma mejor (con menos billetes) de obtener esta cantidad
                    if dp[x] + k < dp[nueva_cantidad]:
                        dp[nueva_cantidad] = dp[x] + k
                        # Copiamos la solución previa y añadimos k billetes del tipo i
                        used[nueva_cantidad] = used[x][:]  # copiar lista
                        used[nueva_cantidad][i] += k

    # Al final, comprobamos si pudimos formar la cantidad D
    if dp[D] == math.inf:
        print("No se puede pagar exactamente", D, "euros con los billetes disponibles.")
        return None
    else:
        print("Se puede pagar exactamente", D, "euros.")
        print("Número mínimo de billetes usados:", dp[D])
        print("Distribución de billetes usados:")
        for i in range(N):
            if used[D][i] > 0:
                print(f"  {used[D][i]} billetes de {v[i]}€")
        return used[D]


def main():
    billetes = [1, 2, 5, 10, 20, 50, 100]
    cantidades = [2, 4, 5, 2, 3, 5, 2]

    cambiar_dinero_min_billetes(billetes, cantidades, 49)

if __name__ == "__main__":
    main()