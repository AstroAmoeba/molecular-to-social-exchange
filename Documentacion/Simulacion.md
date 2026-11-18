# Sobre la simulación

actualmente alojada en src/test2.py

El objetivo de la simulacion es ....

## Qué se esta simulando


Se plantea un sistema tal que... en relacion.... con el articulo "zzz" de xyz     
https://doi.org/10.48550/arXiv.1305.0768

## Cómo funciona el código

Se simulan intercambios aleatorios de energía entre agentes. Cada interacción conserva la energía total de la pareja, pero la reparte al azar entre sus dos integrantes. La simulación se detiene al alcanzar un número máximo de rondas o cuando la distribución de energía cambia poco durante varios controles consecutivos.

### 1. `reshuffling_step(energies, rng)`

Esta función realiza una interacción:

1. `rng.choice(..., size=2, replace=False)` escoge dos agentes distintos.
2. `rng.random()` genera `epsilon`, un número aleatorio entre 0 y 1.
3. Suma las energías de ambos: `pair_energy = energies[i] + energies[j]`.
4. Reparte esa suma así:
   ```python
   energies[i] = epsilon * pair_energy
   energies[j] = (1 - epsilon) * pair_energy
   ```
   $$
E_i' = \varepsilon(E_i + E_j), \quad\quad (1)
$$
$$
E_j' = (1 - \varepsilon)(E_i + E_j), \quad\quad (2)
$$

La suma no cambia: `epsilon * pair_energy + (1 - epsilon) * pair_energy = pair_energy`. Por ejemplo, si la pareja tiene 2 unidades y `epsilon` vale 0.3, queda con 0.6 y 1.4 unidades.

### 2. `run_simulation(...)`

Esta función configura y ejecuta la simulación. Sus parámetros principales son:

- `n_agents=1000`: cantidad de agentes.
- `max_sweeps=2000`: máximo de rondas.
- `check_every_sweeps=20`: cada cuántas rondas se revisa la distribución.
- `tolerance=0.2`: cambio máximo aceptado entre controles.
- `required_stable_checks=3`: controles consecutivos que deben quedar bajo la tolerancia para considerar que se alcanzó la estacionariedad.
- `seed=42`: semilla para que los números aleatorios —y, por tanto, el resultado— sean reproducibles.

Primero comprueba que haya al menos dos agentes, ya que cada interacción requiere elegir una pareja. Luego crea el generador aleatorio y asigna una unidad de energía a cada agente:

```python
energies = np.ones(n_agents, dtype=float)
```

Así, con los valores predeterminados, la energía total inicial es 1000 y la energía media es 1.

### 3. Qué es un *sweep*

El ciclo exterior recorre las rondas. En cada *sweep* se hacen `n_agents` intercambios:

```python
for _ in range(n_agents):
    reshuffling_step(energies, rng)
```

No significa que cada agente participe exactamente una vez: las parejas se vuelven a elegir al azar y un agente puede participar varias veces, o ninguna, durante una ronda.

### 4. Cómo decide si la distribución se estabilizó

Cada `check_every_sweeps` rondas, el código compara la distribución actual de energías con la del control anterior.

- Divide cada energía por `mean_energy`. Esto expresa las energías en unidades de la energía media, facilitando la interpretación de los intervalos.
- Construye un histograma con bordes entre 0 y 10, en pasos de 0.5.
- Cuenta por separado los valores mayores que 10 como una categoría de “desbordamiento”.
- Divide las cantidades por el número de agentes para obtener proporciones.

En el primer control solo guarda un histograma de referencia, así que todavía no calcula una distancia. En los controles siguientes calcula:

```python
0.5 * np.abs(current_histogram - previous_histogram).sum()
```

Es una distancia entre distribuciones: vale 0 si las proporciones de todas las categorías son iguales; cuanto mayor es, más cambiaron. Si queda por debajo de `tolerance`, incrementa `stable_checks`; si no, vuelve a cero el contador. Cuando alcanza `required_stable_checks` consecutivos, marca `converged = True` y termina.

**Importante:** esto es un criterio práctico de estabilidad del histograma, no una prueba matemática de que el sistema haya alcanzado un equilibrio definitivo. Además, el histograma agrupa valores en intervalos, así que puede no reflejar cambios pequeños dentro de cada intervalo.

### 5. Comprobación de conservación y resultados

Al terminar, el código vuelve a sumar las energías y calcula la diferencia respecto de la suma inicial. La instrucción `assert np.isclose(...)` verifica que la diferencia sea suficientemente pequeña para tratarse de errores de redondeo numérico. Si no se cumple, lanza un error indicando que no se conservó la energía.

La función devuelve una tupla con:

1. `energies`: energía final de cada agente.
2. `sweeps_completed`: rondas realizadas.
3. `converged`: si se cumplió el criterio de estabilidad.
4. `initial_total_energy`: energía total inicial.
5. `final_total_energy`: energía total final.
6. `last_distance`: última distancia calculada, o `None` si no hubo comparación.

### 6. Bloque de ejecución

El bloque `if __name__ == "__main__":` se ejecuta cuando el archivo se corre directamente, pero no cuando se importa desde otro módulo. Ejecutándolo directamente, llama a `run_simulation()` con los valores predeterminados y muestra las rondas realizadas, el resultado del criterio de estacionariedad y las energías inicial y final.

Es un modelo aleatorio simplificado de redistribución de energía que estudia cómo cambia una distribución cuando se intercambia energía conservando el total.