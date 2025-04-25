import time
import copy

RESULT = 0
TIME = 1

def timer(function): 
    """ Decorador para calcular el tiempo de ejecución """
    def wrap(*args, **kwargs):
        num_times = 10
        suma = 0
        for _ in range(num_times):
            new_args = copy.deepcopy(args)
            new_kwargs = copy.deepcopy(kwargs)
            start = time.time_ns() / 1e6
            result= function(*new_args, **new_kwargs)
            end = time.time_ns() / 1e6
            suma += end - start
        avg_time = suma / num_times
        return result, avg_time
    return wrap
  
@timer
def countdown(n): 
    """ Bucle mientras n sea mayor que 0 """
    while n > 0: 
        n -= 1

def warmup():
    """ Aumenta la precisión si se ejecuta antes de medir tiempos """
    return countdown(1000000)
