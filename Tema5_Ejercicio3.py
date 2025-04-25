def encontrar_combinaciones(cadena, N):
    resultados = set()

    def backtrack(indice, camino):
        # Si hemos formado un número de N cifras, lo añadimos al resultado
        if len(camino) == N:
            resultados.add(''.join(camino))
            return
        # Si ya no quedan suficientes dígitos, paramos
        if indice >= len(cadena):
            return
        for i in range(indice, len(cadena)):
            # Tomamos el dígito en la posición actual y seguimos buscando
            backtrack(i + 1, camino + [cadena[i]])

    backtrack(0, [])
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