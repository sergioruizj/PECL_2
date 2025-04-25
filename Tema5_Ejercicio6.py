# Tabla de sustitución como diccionario de diccionarios
M = {
    'a': {'a': 'b', 'b': 'b', 'c': 'a', 'd': 'd'},
    'b': {'a': 'c', 'b': 'a', 'c': 'd', 'd': 'a'},
    'c': {'a': 'b', 'b': 'a', 'c': 'c', 'd': 'c'},
    'd': {'a': 'd', 'b': 'd', 'c': 'd', 'd': 'b'},
}

# Función de Backtracking
def backtrack(cadena, objetivo, camino=[]):
    if len(cadena) == 1:
        if cadena == objetivo:
            print(" → ".join(camino + [cadena]))  # Mostrar solución
            return True
        return False

    for i in range(len(cadena) - 1):
        par = cadena[i:i+2]
        reemplazo = M[par[0]][par[1]]
        nueva_cadena = cadena[:i] + reemplazo + cadena[i+2:]
        if backtrack(nueva_cadena, objetivo, camino + [cadena]):
            return True
    
    return False

# Ejemplo de uso
cadena_inicial = "acabada"
objetivo = "d"
print(f"Buscando forma de reducir '{cadena_inicial}' a '{objetivo}':")
if not backtrack(cadena_inicial, objetivo):
    print("No es posible reducir la cadena al carácter objetivo.")
