"""
Implementación del ejercicio 18 (método de congruencia lineal).

Este módulo define funciones para generar números pseudoaleatorios
uniformes en el intervalo [0,1] mediante un generador congruencial
lineal (LCG), calcular su periodo y evaluar momentos muestrales de
distintas órdenes.  El ejemplo de uso en el bloque principal
imprime el periodo y los momentos de orden 1, 3 y 7 para N = 10,
100 y 1000 muestras.
"""

import numpy as np

def lcg_stream(a: int = 57, c: int = 1, m: int = 256, seed: int = 10, size: int = 1) -> np.ndarray:
    """Devuelve una secuencia de números pseudoaleatorios uniformes usando un LCG.

    Args:
        a: multiplicador del LCG.
        c: incremento del LCG.
        m: módulo del LCG.
        seed: valor inicial X0.
        size: longitud de la secuencia a generar.

    Returns:
        Un arreglo de `size` valores en el intervalo [0, 1).
    """
    x = seed % m
    u = np.empty(size, dtype=float)
    for i in range(size):
        x = (a * x + c) % m
        u[i] = x / m
    return u


def lcg_period(a: int = 57, c: int = 1, m: int = 256, seed: int = 10) -> int:
    """Calcula el periodo del LCG con los parámetros dados.

    El periodo se define como la longitud de la secuencia antes de que el
    generador vuelva a un valor previamente visitado.

    Args:
        a: multiplicador del LCG.
        c: incremento del LCG.
        m: módulo del LCG.
        seed: valor inicial X0.

    Returns:
        El periodo del generador.
    """
    x = seed % m
    seen = set()
    period = 0
    while x not in seen:
        seen.add(x)
        x = (a * x + c) % m
        period += 1
    return period


def sample_moments(u: np.ndarray, orders: list[int]) -> dict[int, float]:
    """Calcula momentos muestrales de la secuencia `u` para los órdenes dados.

    Args:
        u: arreglo de números en [0, 1).
        orders: lista de enteros que representan los órdenes de los momentos.

    Returns:
        Un diccionario que mapea cada orden al valor del momento muestral.
    """
    moments = {}
    for k in orders:
        moments[k] = float(np.mean(u ** k))
    return moments


if __name__ == "__main__":
    # Calcular el periodo del generador
    periodo = lcg_period()
    print(f"Período del LCG: {periodo}")

    # Evaluar momentos para N = 10, 100 y 1000
    tamaños = [10, 100, 1000]
    for N in tamaños:
        muestra = lcg_stream(size=N)
        momentos = sample_moments(muestra, [1, 3, 7])
        print(f"N = {N}: momentos = {momentos}")