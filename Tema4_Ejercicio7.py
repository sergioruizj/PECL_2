def subsecuenciaLarga(subs1, subs2):
    """
    Calcula la longitud de la subsecuencia común más larga (LCS)
    entre dos listas de bits A y B, y devuelve también una
    subsecuencia concreta de esa longitud máxima.

    Parámetros:
    - A: lista de 0 y 1 (p. ej. [0,1,1,0,...])
    - B: lista de 0 y 1 (p. ej. [1,0,0,1,...])

    Devuelve:
    - lcs_length: entero, longitud de la LCS
    - lcs_sequence: lista de bits que es una subsecuencia común
    """

    # Longitudes de las secuencias
    n = len(subs1)
    m = len(subs2)

    # Creamos la tabla dp de (n+1) x (m+1), inicializada a 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Llenamos la tabla por filas y columnas (exceptiando la primera fila y columna)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Comparamos el i-ésimo bit de A (A[i-1]) con el j-ésimo de B (B[j-1])
            if subs1[i - 1] == subs2[j - 1]:
                # Caso “coinciden”: extendemos la LCS de los prefijos uno menos largos
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Caso “no coinciden”: descartamos uno o el otro
                # Elegimos el mejor de los dos:
                #   - descartar A[i-1] → dp[i-1][j]
                #   - descartar B[j-1] → dp[i][j-1]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 4) La longitud de la LCS está en dp[n][m]
    lcs_length = dp[n][m]

    # 5) Reconstrucción de la subsecuencia:
    #    Vamos desde (i=n, j=m) hasta (i=0 o j=0)
    i, j = n, m
    lcs_sequence = []  # aquí iremos guardando los bits (del final al principio)

    while i > 0 and j > 0:
        if subs1[i - 1] == subs2[j - 1]:
            # Si coinciden, formaron parte de la solución:
            lcs_sequence.append(subs1[i - 1])
            # Retrocedemos diagonalmente
            i -= 1
            j -= 1
        else:
            # Si no coinciden, vamos por donde el dp sea mayor
            if dp[i - 1][j] >= dp[i][j - 1]:
                # Mejor solución viene de “arriba” (descartando A[i-1])
                i -= 1
            else:
                # Mejor viene de “izquierda” (descartando B[j-1])
                j -= 1

    # Ahora lcs_sequence está al revés, porque empezamos por el final
    lcs_sequence.reverse()

    # 6) Devolvemos resultado
    return lcs_length, lcs_sequence



def main():
    A = [0,1,1,0,1,0,1,0,0,0,1]
    B = [1,0,1,0,0,1,0,0,1]

    length, seq = subsecuenciaLarga(A, B)
    print("Longitud máxima de subsecuencia común:", length)
    print("Una subsecuencia común de esa longitud:", seq)


if __name__ == "__main__":
    main()