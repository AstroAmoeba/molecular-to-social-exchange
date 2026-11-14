import numpy as np

def reshuffling_step(E, rng):
    N = len(E)
    i, j = rng.choice(N, size=2, replace=False)
    eps = rng.random()
    s = E[i] + E[j]
    E[i] = eps * s
    E[j] = (1 - eps) * s
    return E

