import numpy as np
import matplotlib.pyplot as plt

"""
Simulación del problema de Monty Hall.

Se consideran tres puertas, una con un premio (auto) y dos con cabras.  El
participante elige una puerta al azar; el presentador abre una de las
otras puertas que tiene una cabra y se ofrecen dos estrategias: cambiar
de elección a la otra puerta cerrada o mantener la elección inicial.

Esta rutina estima la probabilidad de ganar bajo cada estrategia mediante
simulación Monte Carlo.
"""

# Devuelve las probabilidades de ganar si se cambia o si se mantiene.
def monty_hall(simulaciones: int = 200_000) -> tuple[float, float]:
    ganar_cambiar = 0
    ganar_mantener = 0
    # Ejecuta la simulación simulaciones veces
    for _ in range(simulaciones):
        premio = np.random.randint(3)    # Puerta con el auto
        eleccion = np.random.randint(3)  # Elección inicial del jugador
        # Seleccionar una puerta que no sea la elegida ni la del premio para abrir
        posibles = [p for p in range(3) if p != eleccion and p != premio]
        abierta = np.random.choice(posibles)
        # Estrategia de cambiar: elegir la única puerta cerrada restante
        nueva = next(p for p in range(3) if p not in (eleccion, abierta))
        # Se gana al cambiar si la nueva puerta tiene el premio
        if nueva == premio:
            ganar_cambiar += 1
        # Se gana al mantener si la puerta elegida inicialmente tiene el premio
        if eleccion == premio:
            ganar_mantener += 1
    return ganar_cambiar / simulaciones, ganar_mantener / simulaciones


if __name__ == "__main__":
    # Ejecutar simulación
    p_cambiar, p_mantener = monty_hall()
    print(f"Probabilidad de ganar si cambia: {p_cambiar:.4f}")
    print(f"Probabilidad de ganar si mantiene: {p_mantener:.4f}")
    # Crear gráfico de barras con los resultados
    estrategias = ["Cambiar", "Mantener"]
    probabilidades = [p_cambiar, p_mantener]
    plt.figure(figsize=(4.5, 3.5))
    plt.bar(estrategias, probabilidades, color=['red', 'orange'])
    plt.ylim(0, 1)
    plt.title("Probabilidad de ganar")
    plt.xlabel("Estrategia")
    plt.ylabel("probabilidad")
    plt.grid(axis='y', alpha=0.3)
    # ticks en el eje y con separación uniforme
    plt.yticks(np.linspace(0, 1, 6))
    plt.tight_layout()
    plt.savefig("./ej_21.png", dpi=200)
    plt.close()