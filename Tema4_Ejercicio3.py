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

def cambiar_dinero_min_billetes(tipoBilletes: int, cantidadBilletes: int, objetivo: int):

    N = len(tipoBilletes)  # número de tipos de billetes

    # Inicializamos la tabla dp con infinito
    dp = [math.inf] * (objetivo + 1)
    dp[0] = 0 

    # Esta tabla guarda cuántos billetes de cada tipo se usaron para llegar a cada cantidad
    used = [[0] * N for _ in range(objetivo + 1)]

    # Recorremos cada tipo de billete
    for i in range(N):
        # Vamos desde D hasta 0 para no reutilizar el mismo billete más veces de las permitidas
        for x in range(objetivo, -1, -1):
            if dp[x] < math.inf:
                # Probamos usar de 1 hasta c[i] billetes del tipo i
                for k in range(1, cantidadBilletes[i] + 1):
                    nueva_cantidad = x + k * tipoBilletes[i]
                    if nueva_cantidad > objetivo:
                        break  # si nos pasamos, salimos del bucle

                    # Si encontramos una forma mejor (con menos billetes) de obtener esta cantidad
                    if dp[x] + k < dp[nueva_cantidad]:
                        dp[nueva_cantidad] = dp[x] + k
                        # Copiamos la solución previa y añadimos k billetes del tipo i
                        used[nueva_cantidad] = used[x][:]  # copiar lista
                        used[nueva_cantidad][i] += k

    # Al final, comprobamos si pudimos formar la cantidad D
    if dp[objetivo] == math.inf:
        print("No se puede pagar exactamente", objetivo, "euros con los billetes disponibles.")
        return None
    else:
        print("Se puede pagar exactamente", objetivo, "euros.")
        print("Número mínimo de billetes usados:", dp[objetivo])
        print("Distribución de billetes usados:")
        for i in range(N):
            if used[objetivo][i] > 0:
                print(f"  · {used[objetivo][i]} billetes de {tipoBilletes[i]}€")
        return used[objetivo]


def main():
    billetes = [1, 2, 5, 10, 20, 50, 100, 200]
    cantidades = [5, 600, 0, 20, 4, 30, 80, 20]

    cambiar_dinero_min_billetes(billetes, cantidades, 9789)

if __name__ == "__main__":
    main()


######################
#       TESTS        #
######################