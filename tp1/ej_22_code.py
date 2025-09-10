import numpy as np
import matplotlib.pyplot as plt

"""
Generación de tipos de galaxias con probabilidades dadas.

Se utilizan cuatro tipos: elíptica, espiral, enana e irregular con
probabilidades 0.4, 0.3, 0.2 y 0.1 respectivamente.  Se genera una muestra
de tamaño grande para estimar las frecuencias y se grafica un histograma
de barras con dichas frecuencias.
"""

# Función que devuelve un arreglo de tipos de galaxias según las probabilidades
def generar_tipos(n: int = 20000, semilla: int = 42) -> np.ndarray:
    np.random.seed(semilla)
    # Números aleatorios uniformes en [0,1)
    u = np.random.random(n)
    # Umbrales acumulativos
    umbrales = [0.4, 0.7, 0.9, 1.0]
    tipos = np.empty(n, dtype=object)
    for i, x in enumerate(u):
        if x < umbrales[0]:
            tipos[i] = 'elíptica'
        elif x < umbrales[1]:
            tipos[i] = 'espiral'
        elif x < umbrales[2]:
            tipos[i] = 'enana'
        else:
            tipos[i] = 'irregular'
    return tipos


if __name__ == "__main__":
    # Generar muestra de tipos
    tipos = generar_tipos()
    # Calcular frecuencias
    categorias, counts = np.unique(tipos, return_counts=True)
    freqs = counts / counts.sum()
    print("Frecuencias relativas:")
    for c, f in zip(categorias, freqs):
        print(f"{c}: {f:.4f}")
    # Paleta de colores caliente
    cmap = plt.get_cmap('hot')
    colores = cmap(np.linspace(0.3, 0.8, len(categorias)))
    # Gráfico de barras
    plt.figure(figsize=(5,3.5))
    plt.bar(categorias, freqs, color=colores)
    plt.ylim(0, 0.5)
    plt.title("Frecuencias de tipos de galaxias")
    plt.xlabel("tipo")
    plt.ylabel("frecuencia")
    plt.grid(axis='y', alpha=0.3)
    plt.yticks(np.linspace(0, 0.5, 6))
    plt.tight_layout()
    plt.savefig("./ej_22.png", dpi=200)
    plt.close()