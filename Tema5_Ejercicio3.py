'''
EJERCICIO 3

Se tiene un número de N cifras almacenado en una cadena de texto; por ejemplo, 
la cadena “1151451”. 

Diseñar un algoritmo que, mediante técnicas de Backtracking, encuentre todos los 
números  distintos  de  N  cifras  que  puedan  formarse  con  los  dígitos  de  la  cadena, 
sin alterar su orden relativo dentro de la misma. 

Por ejemplo, si N = 4, son números válidos 1151, 1511 y 1541, pero no 4551 o 5411, 
ya  que,  aunque  pueden  formarse  con  los  dígitos  de  la  cadena,  implican  una  
reordenación.
'''

def encontrar_combinaciones(cadena: str, n: int) -> set:

    resultados = set()

    def _backtrack(posicion_actual: int, combinacion_actual: list):
        # Si hemos formado un número de N cifras, lo añadimos al resultado
        if len(combinacion_actual) == n:
            resultados.add(''.join(combinacion_actual))
            return
        
        # Si ya no quedan suficientes dígitos, paramos
        if posicion_actual >= len(cadena):
            return
        
        for i in range(posicion_actual, len(cadena)):
            # Tomamos el dígito en la posición actual y seguimos buscando
            _backtrack(i + 1, combinacion_actual + [cadena[i]])
    
    # Comprobamos que tengan sentido los datos que estamos pidiendo:
    #  · Que el número de cifras de las cadenas pedidas sea menor o igual a la longitud de la cadena original (si no se cumple la condición, lanzamos error)
    try:
        assert n <= len(cadena)
    except AssertionError:
        print("Error. El valor de n no puede ser mayor que la longitud de la cadena")
    
    _backtrack(0, [])
    return sorted(resultados)
    

# Ejemplo de uso
def main():
    cadena = "1151451"
    N = 4
    combinaciones = encontrar_combinaciones(cadena, N)
    for numero in combinaciones:
        print(numero)


if __name__ == "__main__":
    main()



######################
#       TESTS        #
######################

def test_encontrar_combinaciones():
    cadena = "123"
    n = 2

    combinaciones = encontrar_combinaciones(cadena, n)
    assert len(combinaciones) == 3
    assert "12" == combinaciones[0]
    assert "13" == combinaciones[1]
    assert "23" == combinaciones[2]

def test_encontrar_combinaciones_lanza_excepcion():
    cadena = ""

    try:
        combinaciones = encontrar_combinaciones(cadena, 90)
        assert False
    except:
        pass

def test_timer_encontrar_combinaciones():
    import Tests_timer
    
    @Tests_timer.timer
    def _timer_encontrar_combinaciones(cadena: str, n: int):
        return encontrar_combinaciones(cadena, n)
    
    cadenaA = "12347653754344"
    Tests_timer.warmup()
    resultado = _timer_encontrar_combinaciones(cadenaA, 3)

    assert len(resultado[0]) == 133
    print(f'\n\nSe ha empleado un total de {resultado[1]} ms en la ejecución del programa.\n')