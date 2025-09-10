import numpy as np
import matplotlib.pyplot as plt

"""
Distribución de la suma de dos dados equilibrados.

Se calcula la distribución teórica de la variable aleatoria suma S=d1+d2,
con d1 y d2 dados equilibrados de seis caras.  Luego se generan valores
de S según la distribución teórica y mediante una simulación de lanzamientos,
comparando las distribuciones resultantes.
"""

# Distribución teórica de S (sumas 2..12) y probabilidades
def distribucion_teorica() -> tuple[np.ndarray, np.ndarray]:
    conteos = {suma: 0 for suma in range(2, 13)}
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            conteos[d1 + d2] += 1
    sums = np.array(sorted(conteos.keys()))
    probs = np.array([conteos[s] / 36.0 for s in sums])
    return sums, probs


if __name__ == "__main__":
    # Obtiene distribución teórica
    sums, probs = distribucion_teorica()
    # Generar muestra a partir de la distribución teórica
    n_teo = 20000
    muestras_teo = np.random.choice(sums, size=n_teo, p=probs)
    # Simulación de lanzamientos de dos dados
    n_exp = 20000
    dados1 = np.random.randint(1, 7, size=n_exp)
    dados2 = np.random.randint(1, 7, size=n_exp)
    muestras_exp = dados1 + dados2
    # Cálculo de frecuencias relativas
    freqs_teo = np.array([np.mean(muestras_teo == s) for s in sums])
    freqs_exp = np.array([np.mean(muestras_exp == s) for s in sums])
    # Imprimir valores para referencia
    print("Distribución teórica (probabilidades):")
    for s, p in zip(sums, probs):
        print(f"  S={s}: {p:.3f}")
    # Gráfico de distribución teórica
    plt.figure(figsize=(5,3.5))
    plt.bar(sums, freqs_teo, color='red')
    plt.title("Distribución teórica de S = d_1 + d_2")
    plt.xlabel("suma")
    plt.ylabel("frecuencia")
    plt.grid(axis='y', alpha=0.3)
    # Ticks densos en el eje x (2..12)
    plt.xticks(sums)
    plt.yticks(np.linspace(0, max(freqs_teo)*1.1, 6))
    plt.tight_layout()
    plt.savefig("./ej_23_teo.png", dpi=200)
    plt.close()
    # Gráfico de distribución experimental
    plt.figure(figsize=(5,3.5))
    plt.bar(sums, freqs_exp, color='orange')
    plt.title("Distribución experimental de S = d_1 + d_2")
    plt.xlabel("suma")
    plt.ylabel("frecuencia")
    plt.grid(axis='y', alpha=0.3)
    plt.xticks(sums)
    plt.yticks(np.linspace(0, max(freqs_exp)*1.1, 6))
    plt.tight_layout()
    plt.savefig("./ej_23_exp.png", dpi=200)
    plt.close()