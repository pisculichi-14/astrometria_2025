
import numpy as np
import matplotlib.pyplot as plt

# Generador LCG
def lcg_stream(a=1664525, c=1013904223, m=2**32, seed=123456, N=40000):
    x = seed % m
    arr = np.empty(N, dtype=float)
    for i in range(N):
        x = (a * x + c) % m
        arr[i] = x / m
    return arr

# Generador Fibonacci con retardo (24,55)
class LaggedFibonacci:
    def __init__(self, j=24, k=55, m=2**32, seed=0):
        self.j, self.k, self.m = j, k, m
        # inicializar estado con LCG
        base = lcg_stream(seed=seed, N=k)
        self.state = (base * m).astype(np.uint64)
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

# Cálculo de la correlación de Pearson
def pearson_correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Longitudes distintas")
    mx = np.mean(x)
    my = np.mean(y)
    num = np.sum((x - mx) * (y - my))
    den = np.sqrt(np.sum((x - mx)**2) * np.sum((y - my)**2))
    return 0.0 if den == 0 else num / den

def corr_por_retardos(u, lags=(1,2,3,5,7,10)):
    return {L: float(pearson_correlation(u[:-L], u[L:])) for L in lags}

if __name__ == "__main__":
    # Secuencia con LCG y LFG
    u_lcg = lcg_stream(N=40000)
    lf = LaggedFibonacci(seed=7)
    u_fibo = np.array([lf.random() for _ in range(40000)])

    lags = (1,2,3,5,7,10)
    c_lcg = corr_por_retardos(u_lcg, lags)
    c_fibo = corr_por_retardos(u_fibo, lags)

    # Función de graficado
    def plot_corr(cdict, fname, titulo):
        L = sorted(cdict.keys())
        r = [cdict[l] for l in L]
        plt.figure(figsize=(5,3.5))
        plt.plot(L, r, '-s', color='red', lw=2, ms=5)
        plt.title(titulo)
        plt.xlabel("retardo")
        plt.ylabel("r")
        plt.grid(True, alpha=0.3)
        plt.xticks(L)
        # Densidad de ticks en y
        ymin, ymax = min(r), max(r)
        if ymin == ymax:
            ticks_y = [ymin]
        else:
            ticks_y = np.linspace(ymin, ymax, 6)
        plt.yticks(ticks_y)
        plt.tight_layout()
        plt.savefig(fname, dpi=200)
        plt.close()

    plot_corr(c_lcg, "ej_20_corr_lcg.png", "Correlación (LCG)")
    plot_corr(c_fibo, "ej_20_corr_fibo.png", "Correlación (Fibonacci)")
