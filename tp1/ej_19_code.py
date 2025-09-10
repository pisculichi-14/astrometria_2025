
import numpy as np
import matplotlib.pyplot as plt

# Generador congruencial lineal (LCG) para inicializar el estado
def lcg(seed, size, m=2**32, a=1664525, c=1013904223):
    x = seed % m
    arr = np.empty(size, dtype=np.uint64)
    for i in range(size):
        x = (a * x + c) % m
        arr[i] = x
    return arr

# Generador de Fibonacci con retardo: j=24, k=55, m=2**32, suma
class LaggedFibonacci:
    def __init__(self, j=24, k=55, m=2**32, seed=0):
        self.j, self.k, self.m = j, k, m
        self.state = lcg(seed, k, m)
        self.idx = 0
    def rand_uint(self):
        i = self.idx
        j_idx = (i - self.j) % self.k
        k_idx = (i - self.k) % self.k
        val = (int(self.state[j_idx]) + int(self.state[k_idx])) % self.m
        self.state[i] = val
        self.idx = (i + 1) % self.k
        return val
    def random(self):
        return self.rand_uint() / self.m

if __name__ == "__main__":
    n = 10000
    seed = 12122002
    lf = LaggedFibonacci(seed=seed)
    valores_fibo = np.array([lf.random() for _ in range(n)])

    np.random.seed(42)
    valores_np = np.random.random(n)

    mean_fibo = float(np.mean(valores_fibo))
    var_fibo  = float(np.var(valores_fibo, ddof=1))
    mean_np   = float(np.mean(valores_np))
    var_np    = float(np.var(valores_np, ddof=1))

    print("Media (Fibo)", mean_fibo)
    print("Varianza (Fibo)", var_fibo)
    print("Media (NumPy)", mean_np)
    print("Varianza (NumPy)", var_np)

    # Histograma de la secuencia Fibonacci: la densidad de un uniforme en [0,1] no debe superar 1.
    plt.figure(figsize=(5, 3.5))
    plt.hist(valores_fibo, bins=40, density=True, color='red', alpha=0.8)
    plt.title("Histograma (Fibonacci)")
    plt.xlabel("valor")
    plt.ylabel("densidad")
    plt.grid(True, alpha=0.3)
    plt.xticks(np.linspace(0, 1, 11))
    # Limitar el eje y entre 0 y 1 para reflejar la densidad teórica
    plt.ylim(0, 1)
    plt.yticks(np.linspace(0, 1, 6))
    plt.tight_layout()
    plt.savefig("ej_19_hist_fibo.png", dpi=200)
    plt.close()

    plt.figure(figsize=(5, 3.5))
    plt.hist(valores_np, bins=40, density=True, color='red', alpha=0.8)
    plt.title("Histograma (NumPy)")
    plt.xlabel("valor")
    plt.ylabel("densidad")
    plt.grid(True, alpha=0.3)
    plt.xticks(np.linspace(0, 1, 11))
    plt.ylim(0, 1)
    plt.yticks(np.linspace(0, 1, 6))
    plt.tight_layout()
    plt.savefig("ej_19_hist_np.png", dpi=200)
    plt.close()
