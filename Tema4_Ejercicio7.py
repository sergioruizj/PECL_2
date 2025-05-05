'''
Se  define  una  secuencia  de  bits  A como  una  sucesión A= {F1, F2, ... , Fn}  donde 
cada  Fi puede  tomar  el  valor  0  o  1 .  A  partir  de  una  secuencia  se  define  una  
subsecuencia  X de  A como  X = {x1, x2, ... , xk} ,  siendo  k ≤ n,  de  forma  que  X 
puede obtenerse eliminando algún elemento de A pero respetando el orden en que 
aparecen  los  bits;  por  ejemplo,  si  A = {1,0,1,1,0,0,1}  podríamos  obtener  como 
subsecuencias  {1,1,1,0,1} ,  {1,0,1}  o  {1,1,0,0}  entre  otras,  pero  nunca  se  podría 
conseguir la subsecuencia {1,0,0,1,1}. 

Dadas  dos  secuencias  A  y  B,  se  denomina  a  X  una  subsecuencia  común  de  A  y  B 
cuando X es  subsecuencia  de  A y  además  es  subsecuencia  de  B (aunque  puede  
que se hayan obtenido quitando distintos elementos en A que B, e incluso distinta 
cantidad). Suponiendo las secuencias A = {0,1,1,0,1,0,1,0} y B = {1,0,1,0,0,1,0,0,1} 
una subsecuencia común sería X = {1,1,0,1}, pero no podría serlo X = {0,1,1,1,0}. 

Se desea determinar la subsecuencia común de dos secuencias A y B que tenga la 
longitud máxima, para lo que se pide: 
 · Explicar con detalle la forma de resolver el problema. 
 · Hacer un algoritmo de Programación Dinámica que obtenga la longitud máxima 
   posible y una secuencia común de dicha longitud.
'''

def maxima_subsecuencia(cadena1: list, cadena2: list):
    """
    Calcula la longitud de la subsecuencia común más larga
    entre dos listas de bits A y B, y devuelve también una
    subsecuencia concreta de esa longitud máxima.
    """

    n = len(cadena1)
    m = len(cadena2)

    # Creamos la tabla dp de (n+1) x (m+1), inicializada a 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Llenamos la tabla por filas y columnas (exceptuando la primera fila y columna)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Comparamos el i-ésimo bit de A (A[i-1]) con el j-ésimo de B (B[j-1])
            if cadena1[i - 1] == cadena2[j - 1]: # Coinciden
                dp[i][j] = dp[i - 1][j - 1] + 1
            else: # No coinciden
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


    # Interpretación de las soluciones
    lcs_length = dp[n][m]

    i, j = n, m
    max_subsecuencia = []  

    while i > 0 and j > 0:
        if cadena1[i - 1] == cadena2[j - 1]: # Coinciden
            max_subsecuencia.append(cadena1[i - 1])
            i -= 1
            j -= 1
        else: # No coinciden
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    max_subsecuencia.reverse()

    return lcs_length, max_subsecuencia



def main():
    A = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]
    B = [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1]

    length, seq = maxima_subsecuencia(A, B)
    print("Longitud máxima de subsecuencia común:", length)
    print("Una subsecuencia común de esa longitud:", seq)


if __name__ == "__main__":
    main()



######################
#       TESTS        #
######################

def test_maxima_subsecuencia1():
    A = [0, 1, 1, 0, 1, 0, 1, 0]
    B = [1, 0, 1, 0, 0, 1, 0, 0, 1]
    longitud, subsecuencia = maxima_subsecuencia(A, B)

    assert longitud == len(subsecuencia)
    assert subsecuencia == [0, 1, 1, 0, 0, 1]

def test_maxima_subsecuencia2():
    A = [1, 1, 1, 1, 1, 1]
    B = [0, 0, 0, 0, 0, 0, 0]
    longitud, subsecuencia = maxima_subsecuencia(A, B)

    assert longitud == 0
    assert subsecuencia == []

def test_timer_maxima_subsecuencia():
    import Tests_timer

    @Tests_timer.timer
    def _timer_maxima_subsecuencia(cadena1: list, cadena2: list):
        return maxima_subsecuencia(cadena1, cadena2)
    

    A = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]
    B = [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1]

    Tests_timer.warmup()
    resultado, tiempo = _timer_maxima_subsecuencia(A, B)

    assert resultado[0] == 14
    assert resultado[1] == [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1]

    print(f'\n\nSe ha empleado un total de {tiempo} ms en la ejecución del programa.\n')

