# Modelos de intercambio cinético

Proyecto final de Física Estadística, Facultad de Ciencias, UNAM. Explora cómo una distribución de equilibrio puede emerger de intercambios aleatorios de energía entre agentes.

El proyecto se basa en *Kinetic exchange models: From molecular physics to social science*, de Marco Patriarca y Anirban Chakraborti. El artículo también estudia aplicaciones de estos modelos a la distribución de riqueza y la dinámica de opiniones.

## Modelo

La simulación parte de $N = 1000$ agentes con una unidad de energía cada uno. En cada interacción se eligen dos agentes y se redistribuye su energía:

$$
E_i' = \varepsilon(E_i + E_j), \qquad
E_j' = (1-\varepsilon)(E_i + E_j),
$$

donde $\varepsilon$ se elige aleatoriamente entre 0 y 1. La energía total de la pareja se conserva.

El objetivo es comparar la distribución obtenida con la distribución exponencial de Boltzmann-Gibbs:

$$
P(E) = \beta e^{-\beta E},
\qquad \beta = \frac{1}{\langle E\rangle}.
$$

## Estado del proyecto

- La simulación de intercambios verifica numéricamente la conservación de la energía y utiliza un criterio práctico de estabilidad del histograma.
- La comparación gráfica con la distribución exponencial y el análisis de resultados están pendientes.
- La animación de colisiones es ilustrativa e independiente del modelo de intercambio de energía.

## Instalación

Con Python instalado, desde la raíz del repositorio:

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

Los comandos de activación corresponden a Windows.

## Uso

Ejecutar la simulación numérica:

```cmd
python src\test2.py
```

El programa muestra las distancias entre histogramas, el número de rondas realizadas, el resultado del criterio de estacionariedad y la energía total inicial y final. Cada ronda o *sweep* consiste en 1000 intercambios aleatorios con los parámetros predeterminados.

Ejecutar la animación ilustrativa:

```cmd
python src\colisiones_anim.py
```

La animación abre una ventana y utiliza el GIF de `walking_man.gif`.

## Contenido

- `test2.py`: simulación de intercambios.
- `colisiones_anim.py`: animación ilustrativa.
- `Simulacion.md`: explicación del código numérico.
- `Propuesta.md`: objetivos y metodología.
- `Bitacora.md`: avances y tareas pendientes.
- `guion.md` y `Escaleta.md`: materiales para el video.
- `Declaracion_uso_de_IA.md`: declaración de uso de IA.
- `files_plantilla_jupyter.ipynb`: plantilla de trabajo en Jupyter.

## Referencia

Patriarca, M. y Chakraborti, A. (2013). *Kinetic exchange models: From molecular physics to social science*. American Journal of Physics, 81, 618–623. [Prepublicación en arXiv](https://doi.org/10.48550/arXiv.1305.0768).

