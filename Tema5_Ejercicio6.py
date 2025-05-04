'''
En una cadena cualquiera, dos caracteres consecutivos se pueden sustituir por el 
valor que aparece en la tabla, utilizando el primer carácter como fila y el segundo 
como columna. Por ejemplo, se puede cambiar la secuencia “ca” por una “b”, ya 
que M[c][a]=b. 

Implementar un algoritmo Backtracking que, a partir de una cadena de texto, sea 
capaz de encontrar la forma de realizar las sustituciones para reducir la cadena a 
un solo carácter dado, si es posible. 

Ejemplo:  Dada  la  cadena  “acabada”  y  el  carácter  “d”,  una  posible  forma  de  
sustitución es la siguiente: acabada -> acacda -> abcda -> abcd -> bcd -> bc -> d.
'''


# Función de Backtracking
def simplificar_cadena(cadena: str, objetivo: str, camino: list, M: set) -> list:
    if len(cadena) == 1:
        if cadena == objetivo:
            return camino + [cadena]
        return []

    for i in range(len(cadena) - 1):
        par = cadena[i:i+2]
        reemplazo = M[par[0]][par[1]]
        nueva_cadena = cadena[:i] + reemplazo + cadena[i+2:]
        resultado = simplificar_cadena(nueva_cadena, objetivo, camino + [cadena], M)
        if resultado:
            return resultado
    
    return []

# Ejemplo de uso
def main():
    M = {
    'a': {'a': 'b', 'b': 'b', 'c': 'a', 'd': 'd'},
    'b': {'a': 'c', 'b': 'a', 'c': 'd', 'd': 'a'},
    'c': {'a': 'b', 'b': 'a', 'c': 'c', 'd': 'c'},
    'd': {'a': 'd', 'b': 'd', 'c': 'd', 'd': 'b'},
    }

    cadena_inicial = "aaabbbcccddd"
    objetivo = "d"
    print(f"Buscando forma de reducir '{cadena_inicial}' a '{objetivo}':")
    resultado = simplificar_cadena(cadena_inicial, objetivo, [], M)
    if not resultado:
        print("No es posible reducir la cadena al carácter objetivo.")
    else:
        print(" → ".join(resultado))

if __name__ == "__main__":
    main()


######################
#       TESTS        #
######################

def test_simplificar_cadena1():
    M = {
    'a': {'a': 'b', 'b': 'b', 'c': 'a', 'd': 'd'},
    'b': {'a': 'c', 'b': 'a', 'c': 'd', 'd': 'a'},
    'c': {'a': 'b', 'b': 'a', 'c': 'c', 'd': 'c'},
    'd': {'a': 'd', 'b': 'd', 'c': 'd', 'd': 'b'},
    }

    cadena = "acabbadaadd"
    objetivo = "a"
    resultado = simplificar_cadena(cadena, objetivo, [], M)
    
    assert resultado[0] == "acabbadaadd"
    assert resultado [-1] == "a"
    assert len(resultado) > 1

def test_simplificar_cadena2():
    M = {
    'a': {'a': 'b', 'b': 'b', 'c': 'a', 'd': 'd'},
    'b': {'a': 'c', 'b': 'a', 'c': 'd', 'd': 'a'},
    'c': {'a': 'b', 'b': 'a', 'c': 'c', 'd': 'c'},
    'd': {'a': 'd', 'b': 'd', 'c': 'd', 'd': 'b'},
    }

    cadena = "acabada"
    objetivo = "r"
    resultado = simplificar_cadena(cadena, objetivo, [], M)
    
    assert resultado == []


def test_timer_simplificar_cadena():
    import Tests_timer

    @Tests_timer.timer
    def _timer_simplificar_cadena(cadena: str, objetivo: str, camino: list, M: set):
        return simplificar_cadena(cadena, objetivo, camino, M)
    
    M = {
    'a': {'a': 'b', 'b': 'b', 'c': 'a', 'd': 'd'},
    'b': {'a': 'c', 'b': 'a', 'c': 'd', 'd': 'a'},
    'c': {'a': 'b', 'b': 'a', 'c': 'c', 'd': 'c'},
    'd': {'a': 'd', 'b': 'd', 'c': 'd', 'd': 'b'},
    }

    cadena = "aaabbbccccdcdaabcdbacdbbadcbadddd"
    objetivo = "d"
    Tests_timer.warmup()
    resultado = _timer_simplificar_cadena(cadena, objetivo, [], M)

    assert resultado[0][0] == "aaabbbccccdcdaabcdbacdbbadcbadddd"
    assert resultado [0][-1] == "d"
    assert len(resultado[0]) > 1

    print(f'\n\nSe ha empleado un total de {resultado[1]} ms en la ejecución del programa.\n')
