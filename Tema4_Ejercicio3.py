'''
Se tiene un sistema de billetes de distintos valores y ordenados de menor a mayor 
(por  ejemplo  1,  2,  5,  10,  20,  50  y  100  euros),  que  se  representan  mediante  los  
valores vi,  con  i ∈ {1, ..., N} (en  el  caso  anterior,  N = 7)  de  manera  que  de  cada  
billete  se  tiene  una  cantidad  finita,  mayor  o  igual  a  cero,  que  se  guarda  en  ci 
(siguiendo con el ejemplo, c3 = 6 representaría que hay 6 billetes de 5 euros).

Se quiere pagar exactamente una cierta cantidad de dinero D, utilizando para ello 
la menor cantidad de billetes posible. Se sabe que D ≤ ∑ ci*vi , pero puede que 
la cantidad exacta D no sea obtenible mediante los billetes disponibles. 

Diseñar  un  algoritmo  de  Programación  Dinámica  que  determine,  teniendo  como  
datos los valores ci, vi y D: 

 · Si la cantidad D puede devolverse exactamente o no. 
 · En  caso  afirmativo,  cuantos  billetes  de  cada  tipo  forman  la  descomposición  
óptima.
'''

import math

# Hemos metido el booleano "silenciar" para que al hacer los tests no se imprima el resultado todo el rato
def cambiar_dinero_min_billetes(tipoBilletes: list[int], cantidadBilletes: list[int], objetivo: int, silenciar: bool):

    N = len(tipoBilletes)  # número de tipos de billetes

    # Vector con el número de billetes necesarios para llegar al número de posicion de cada elemento
    dp = [math.inf] * (objetivo + 1)
    dp[0] = 0 

    # Tabla que guarda cuántos billetes de cada tipo se usaron para llegar a cada cantidad
    used = [[0] * N for _ in range(objetivo + 1)]

    for i in range(N):
        for x in range(objetivo, -1, -1):
            if dp[x] < math.inf:
                for k in range(1, cantidadBilletes[i] + 1):
                    nueva_cantidad = x + k * tipoBilletes[i]
                    if nueva_cantidad > objetivo:
                        break  # si nos pasamos, salimos del bucle

                    # Si encontramos una forma mejor (con menos billetes) de obtener esta cantidad, actualizamos los datos
                    if dp[x] + k < dp[nueva_cantidad]:
                        dp[nueva_cantidad] = dp[x] + k
                        used[nueva_cantidad] = used[x][:]  
                        used[nueva_cantidad][i] += k

    # Comprobación e interpretación de las soluciones
    if dp[objetivo] == math.inf:
        if not silenciar:
            print("No se puede pagar exactamente", objetivo, "euros con los billetes disponibles.")
        return None
    else:
        if not silenciar:
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

    cambiar_dinero_min_billetes(billetes, cantidades, 256, False)

if __name__ == "__main__":
    main()


######################
#       TESTS        #
######################

def test_cambiar_dinero_min_billetes1():
    billetes = [1, 2, 5, 10, 20, 50, 100]
    cantidades = [5, 5, 5, 2, 3, 5, 2]  
    objetivo = 28  

    resultado = cambiar_dinero_min_billetes(billetes, cantidades, objetivo, True)

    assert resultado is not None
    assert len(resultado) > 0 
    assert resultado[0] == 1 
    assert resultado[1] == 1
    assert resultado[2] == 1
    assert resultado[3] == 0
    assert resultado[4] == 1

def test_cambiar_dinero_min_billetes2():
    billetes = [1, 2, 5, 10, 20, 50, 100]
    cantidades = [1, 0, 0, 0, 0, 0, 0]  # Solo tenemos billetes de 1€
    objetivo = 3  # Queremos pagar 3€, pero solo tenemos 1 billete de 1€

    resultado = cambiar_dinero_min_billetes(billetes, cantidades, objetivo, True)

    assert resultado is None  # No podemos pagar exactamente 3€

def test_timer_cambiar_dinero_min_billetes():
    import Tests_timer

    @Tests_timer.timer
    def _timer_cambiar_dinero_min_billetes(tipoBilletes: list[int], cantidadBilletes: list[int], objetivo: int):
        return cambiar_dinero_min_billetes(tipoBilletes, cantidadBilletes, objetivo, True)
    
    billetes = [1, 3, 4]
    cantidades = [5, 3, 2]  
    objetivo = 10

    Tests_timer.warmup()
    resultado = _timer_cambiar_dinero_min_billetes(billetes, cantidades, objetivo)

    assert len(resultado[0]) > 0
    assert resultado[0][0] == 0
    assert resultado[0][1] == 2
    assert resultado[0][2] == 1

    print(f'\n\nSe ha empleado un total de {resultado[1]} ms en la ejecución del programa.\n')