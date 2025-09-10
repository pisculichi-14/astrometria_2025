#%%

def suma(a, b, d = 0, e = 1):
    """
    Esta función hace la suma de a con b y hace opcionalmente d

    parámetros
     a:
     b:
     d (opcional:

    Devuelve:
     c

    Modo de uso:
     c = suma(1,2,d = 4)
    """
    c = a + b + d + e
    return c

#%%

def glc(n, x0, a=57, c=1, M=256)
    #n: cantidad de números aleatorios
    #x0: semilla
    #a: multiplicador
    #c: incremento
    #M: módulo

    números = []
    for i in range(n):
        x = (c + a*x0) % M
        números.append(x/M)
        X0 = x
    return números

#%%

def generador_congruencia_lineal(n, x0, a=1664525, c=1013904223, M=2**32):
    #n: cantidad de números aleatorios
    #x0: semilla
    #a: multiplicador
    #c: incremento
    #M: módulo

    números = []
    for i in range(n):
        x = (c + a*x0) % M
        números.append(x/M)
        X0 = x
    return números

#%%

def generador_congruencia_lineal_enteros(n, x0, a=1664525, c=1013904223, M=2**32):
    numeros = []
    for i in range(n):
        x = (c + a*x0) % M
        numeros.append(x)
        x0 = x
    return numeros

def generador_congruencia_lineal(n, x0, a=1664525, c=1013904223, M=2**32):
    return np.array(generador_congruencia_lineal_enteros(n, x0, a, c, M))/M

#%%


def generador_fibonacci_enteros(n, x0, a=1664525, c=1013904223, M=2**32):
    numeros=generador_congruencia_lineal_enteros(k, x0)
    for i in range(k, k+n):
        numeros.append((numeros[i-j] + numeros[i-k]) % m)
    return numeros[k:]

def generador_fibonacci(n, x0, j=24, k=55, m=2**32):
    return np.array(generador_fibonacci_enteros(n, x0, j, k, m))/m
# %%
