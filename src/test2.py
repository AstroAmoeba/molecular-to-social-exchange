import numpy as np


def reshuffling_step(energies, rng):
    """Redistribuye la energía total de dos agentes elegidos al azar."""
    # Elegir dos agentes distintos.
    i, j = rng.choice(len(energies), size=2, replace=False)

    # La fracción epsilon determina cómo se reparte la energía conjunta.
    epsilon = rng.random()
    pair_energy = energies[i] + energies[j]

    # Repartir la energía conservando la suma de la pareja.
    energies[i] = epsilon * pair_energy
    energies[j] = (1 - epsilon) * pair_energy


def run_simulation(
    n_agents=1000,
    max_sweeps=2000,
    check_every_sweeps=20,
    tolerance=0.2,
    required_stable_checks=3,
    seed=42,
):
    """Simula intercambios hasta alcanzar el criterio de estacionariedad."""
    if n_agents < 2:
        raise ValueError("Se necesitan al menos dos agentes.")

    # Usar una semilla hace que la simulación se pueda reproducir.
    rng = np.random.default_rng(seed)

    # B2: iniciar a todos los agentes con energía igual a 1.
    energies = np.ones(n_agents, dtype=float)
    initial_total_energy = energies.sum()
    mean_energy = energies.mean()

    # Los histogramas usan energía expresada en unidades de la energía media.
    # Se agrega una categoría adicional para valores mayores que 10.
    histogram_edges = np.linspace(0, 10, 21)
    previous_histogram = None
    stable_checks = 0
    last_distance = None
    converged = False
    sweeps_completed = 0

    # Cada sweep contiene N colisiones aleatorias.
    for sweep in range(1, max_sweeps + 1):
        for _ in range(n_agents):
            reshuffling_step(energies, rng)

        sweeps_completed = sweep

        # Revisar si la distribución cambió poco desde el último control.
        if sweep % check_every_sweeps == 0:
            scaled_energies = energies / mean_energy
            counts, _ = np.histogram(scaled_energies, bins=histogram_edges)

            # Contar por separado las energías fuera del intervalo del histograma.
            overflow_count = np.count_nonzero(scaled_energies > histogram_edges[-1])
            current_histogram = np.append(counts, overflow_count) / n_agents

            if previous_histogram is not None:
                # Distancia entre distribuciones: 0 significa histogramas iguales.
                last_distance = 0.5 * np.abs(
                    current_histogram - previous_histogram
                ).sum()
                print(f"Sweep {sweep}: distancia = {last_distance:.4f}")

                if last_distance < tolerance:
                    stable_checks += 1
                else:
                    stable_checks = 0

                # Exigir varios controles consecutivos para evitar parar por azar.
                if stable_checks >= required_stable_checks:
                    converged = True
                    break

            previous_histogram = current_histogram

    # Comprobar numéricamente que la energía total se conservó.
    final_total_energy = energies.sum()
    energy_difference = final_total_energy - initial_total_energy
    assert np.isclose(
        final_total_energy,
        initial_total_energy,
        rtol=1e-12,
        atol=1e-10,
    ), "La energía total no se conservó."

    return (
        energies,
        sweeps_completed,
        converged,
        initial_total_energy,
        final_total_energy,
        last_distance,
    )


if __name__ == "__main__":
    (
        energies,
        sweeps,
        converged,
        initial_energy,
        final_energy,
        histogram_distance,
    ) = run_simulation()

    print(f"Sweeps realizados: {sweeps}")
    print(f"¿Criterio de estacionariedad alcanzado?: {converged}")
    print(f"Energía total inicial: {initial_energy:.12f}")
    print(f"Energía total final:   {final_energy:.12f}")
    print(f"Diferencia:            {final_energy - initial_energy:.3e}")
    if histogram_distance is not None:
        print(f"Distancia del último control: {histogram_distance:.4f}")