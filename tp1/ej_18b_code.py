
import numpy as np
import matplotlib.pyplot as plt

def walk_mean_R(K=10, N=1000, seed=0):
    rng = np.random.default_rng(seed)
    acc = np.zeros(N)
    for k in range(K):
        x = np.cumsum(rng.uniform(-np.sqrt(2), np.sqrt(2), N))
        y = np.cumsum(rng.uniform(-np.sqrt(2), np.sqrt(2), N))
        acc += np.sqrt(x**2 + y**2)
    return acc / K

if __name__ == "__main__":
    N = 1000
    mean_R = walk_mean_R(K=10, N=N, seed=123)
    n = np.arange(1, N + 1)
    plt.figure(figsize=(5,3.2))
    plt.plot(n, mean_R, lw=2)
    plt.title("Distancia media vs N")
    plt.xlabel("N")
    plt.ylabel("E[R]")
    plt.tight_layout()
    plt.savefig("ej_18b_R_vs_N.png", dpi=200)
    plt.close()

    plt.figure(figsize=(5,3.2))
    plt.plot(np.sqrt(n), mean_R, lw=2)
    plt.title("Distancia media vs sqrt(N)")
    plt.xlabel("sqrt(N)")
    plt.ylabel("E[R]")
    plt.tight_layout()
    plt.savefig("ej_18b_R_vs_sqrtN.png", dpi=200)
    plt.close()
