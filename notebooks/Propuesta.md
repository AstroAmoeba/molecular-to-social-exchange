# Propuesta de Proyecto Final con Justificación

Curso: Física Estadística (2027-1) — Facultad de Ciencias, UNAM
Profesor: Dr. Roberto Antonio Zamora Zamora
Fecha límite de entrega: 31 de Octubre.
Ponderación: 10% del Proyecto Final (40% de la calificación total del curso)

---

## 👥 Integrantes del Equipo (Individual)

1. Nombre completo: [Sonia María Pérez Portillo] —Correo: [perezportillos@ciencias.unam.mx]

---

## 1. 📖 Referencia del Artículo Científico Seleccionado

*   Título del Artículo: Kinetic exchange models: From molecular physics to social science
*   Autores: Marco Patriarca, Anirban Chakraborti
*   Revista, Volumen, Páginas y Año: American Journal of Physics 81, 618–623 (2013)
*   DOI / Enlace Permanente: https://doi.org/10.48550/arXiv.1305.0768

---

## 2. 🎯 Justificación Científica y Conexión con el Temario

### A. Relevancia y Conexión Temática

Los bloques relevantes del curso son principalmente el bloque 1, 2 y 5. El artículo plantea un modelo estocástico de intercambio aleatorio, por lo que los fundamentos revisados en la caminata aleatoria en el bloque 1 son fundamental, es para el entendimiento y el desarrollo del trabajo final desarrollado del artículo, en particular planteando un camino aleatorio en el espacio de energías, y los conceptos de valor medio y distribuciones.

Del bloque 2 del curso se recuperan los conceptos de ensamble canónico, espacio de fases y del principio de maximización de la entropía. Se hace uso y mención explícita de la distribución de Boltzmann-Gibbs para equilibrio $f(\omega) = \beta e^{-\beta \omega}$ y el teorema de equipartición $\left< \omega \right> = d k_B T / 2$ con $\alpha = d/2$.

Se recuperan también los conceptos de transiciones de fase y modelo de ising del bloque 5. La herramienta propuesta para la simulación (Monte Carlo) se describe también en este bloque.

Adicionalmente del bloque 6 y 7, se recupera del 6 conceptos como la relajación al equilibrio y ecuación de Langevin. La teoría cinética de gases desarrollada en el bloque 7 funge como motivación del artículo.

Los conceptos teóricos fundamentales para entender el contenido del artículo son los procesos estocásticos discretos (como los estudiados en el caminante aleatorio) el ensamble microcanónico y conservación de la energía, la distribución de equilibrio que contiene el factor de Boltzmann, el teorema de equipartición y las transiciones de fase.

### B. Pregunta Central y Motivación Física

El problema físico principal abordado por el artículo es la manera en la que emerge una condición de equilibrio estadístico a partir de una dinámica microscópica estocástica, con intercambio conservativo, entre múltiples agentes. Se plantea el problema en términos de N unidades que intercambian por pares ($\omega_i + \omega_j = cte$) una cantidad conservada, como energía o riqueza mediante colisiones binarias aleatorias, buscando determinar una distribución estacionaria $f(w)$, que denota la densidad de probabilidad de la cantidad conservada en estado estacionario.

Se establecen como hipótesis del modelo homogéneo la conservación de la cantidad intercambiada en cada colisión binaria, la dinámica estocástica discreta con elección aleatoria y uniforme de pares (considerando probabilidades a priori iguales y caos molecular), la localidad y Markovianidad de la regla de intercambio $\Delta w_{ij}$, que depende solo de las energías iniciales y de parámetros estocásticos; y ausencia de energía potencial (gas ideal, partículas descritas solo por su grado de libertad energético w).

### C. Metodología y Viabilidad

**Enfoque de trabajo**

Se propone un enfoque mixto, con especial énfasis en el aspecto numérico y computacional contenidos en el artículo, de tal manera que el aspecto teórico tenga principalmente un enfoque explicativo, interpretativo, contextualizador y justificativo sobre la parte computacional del proyecto.

En particular, el objetivo del desarrollo será reproducir la emergencia de Boltzmann-Gibbs a partir de la regla de reshuffling y verificar la conservación de la energía. Para esto se propone el uso de python como lenguaje de programación para realizar las simulaciones, alojando el código en un repositorio en Github configurado con git al entorno de trabajo y con su respectiva documentación. Se considera también el uso de Google Collab, JupyterLab o notebooks en VS Code para generar documentos con bloques de texto que expliquen brevemente las simulaciones.

#### Actividades propuestas:

**Objetivo:**
Estudiar mediante una simulación sencilla cómo una distribución estadística de equilibrio puede emerger a partir de intercambios aleatorios entre los componentes de un sistema.

**Actividades a reproducir:**

* Considerar un sistema de \(N = 1000\) partículas, cada una con energía inicial \(E_i = 1\). Seleccionar aleatoriamente pares de partículas y redistribuir su energía mediante

$$
E_i' = \varepsilon(E_i + E_j), \quad\quad (12)
$$
$$
E_j' = (1 - \varepsilon)(E_i + E_j), \quad\quad (13)
$$

donde \(\varepsilon\) es un número aleatorio uniforme entre 0 y 1.
Implementar este procedimiento en Python y repetirlo hasta obtener una distribución aproximadamente estacionaria.

* Construir un histograma de las energías de las partículas después de un número suficientemente grande de intercambios.
Comparar la distribución numérica con la distribución exponencial,

$$
P(E) = \beta e^{-\beta E}, \quad\quad (14)
$$

donde

$$
\beta = \frac{1}{\langle E \rangle}. \quad\quad (15)
$$

Explicar la relación entre la distribución obtenida y la distribución de Boltzmann.

* Verificar numéricamente que la energía total del sistema permanece constante,

$$
E_{\text{tot}} = \sum_{i=1}^{N} E_i. \quad\quad (16)
$$

Comparar los histogramas de energía antes y después de los intercambios y explicar cómo el sistema evoluciona hacia una distribución de equilibrio.


**Herramientas a utilizar**

Las herramientas a utilizar son simulación de Monte Carlo (considerando conservación de energía), procesos estocásticos en la interpretación de la evolución de las energías como un caminante aleatorio en el espacio de energías e Histogramas de $E_i$.

**Factibilidad**

El proyecto es factible en el periodo restante al final del semestre debido a que utiliza un modelo computacional de alcance delimitado, basado en intercambios aleatorios entre pares de partículas. Su implementación requiere herramientas gratuitas y recursos de cómputo convencionales. Además, dispone de predicciones teóricas explícitas (conservación de la energía y distribución aproximadamente exponencial en equilibrio) que permiten verificar los resultados.

Considerando una planificación en el que se busque realizar la simulación computacional en un lapso de 3 a 4 semanas considerando la validación y análisis de la simulación, con la redacción en paralelo del guión del video. Y considerando un espacio de dos a una semanas para la realización del mismo, se prevé que los tiempos sean adecuados para la realización y entrega del proyecto final.

---

## 3. Audiencia del Video 

*   **Audiencia objetivo del video:** 

    *   **Pares (compañeros del curso):** Lenguaje técnico del nivel del curso, asumiendo familiaridad con los bloques previos.
    *   **Profesores / Comité evaluador:** Énfasis en rigor, profundidad y análisis crítico. 
    *   **Público general / Divulgación:** Explicaciones accesibles, analogías, mínimo uso de jerga técnica.

*   **Justificación breve (2–3 oraciones):** ¿Por qué eligieron esa audiencia y cómo adaptarán el tono, nivel de detalle y recursos visuales del video?

La audiencia objetivo del video será el público en general / de corte divulgativo. Ya que se considera que el tema a tratar es atractivo y novedoso al público en general al tratarse de relaciones no triviales entre ciencias sociales y ciencias físicas y matemáticas. Se planea adaptar el nivel de la información presentada mediante el uso de analogías, acercamiento a situaciones cotidianas y uso de recursos gráficos como animaciones de carácter metafórico y lúdico. El nivel de detalle sobre los aspectos más técnicos de la simulación serán delegados a el repositorio abierto con código y texto explicativo.

---

## 4. Declaración de Uso de Inteligencia Artificial (IA)

Se hizo uso de DeepSeek y Notebook LLM, previamente entrenados con el contenido del artículo y del temario del curso para la elaboración de los apartados de la justificación A y B documento. Se introdujeron los mismos prompts en ambos modelos de lenguaje a modo de realizar una comparativa entre las respuestas. Posteriormente, se hizo uso únicamente de DeepSeek a modo de consulta para el apartado C de la justificación y GitHub copilot para la selección de stack y planeación del proyecto en el lapso restante del semestre. La redacción del documento en sí es de autoría propia.

**Apartados A y B:**

*   **Prompts utilizados y propósito:**

1.  **Prompt 1:** "Este es el temario del curso y este es un artículo en el que planeo trabajar, me puedes ayudar a responder ¿Con qué bloque(s) del curso se vincula directamente este artículo (ej. Bloques 1, 2, 3, 4, 5, 6 u 8)?" — *(Propósito: Comparar el output de ambos LLM para identificar los bloques pertinentes al trabajo y comparar con lo recabado en la lectura del artículo.)*
2.  **Prompt 2:** "¿Qué conceptos teóricos del curso son el punto de partida para entender el modelo o fenómeno estudiado?" — *(Propósito: Comparar el output de ambos LLM para identificar los conceptos teóricos revisados en el curso, verificar los conceptos y su relación con los bloques temáticos pertinentes al trabajo y comparar con lo recabado en la lectura del artículo.)*
3.  **Prompt 3:** "¿Cuál es el problema físico principal que aborda el artículo?¿Cuáles son las hipótesis físicas fundamentales y las ecuaciones clave que se derivarán o analizarán?" — *(Propósito: Comparar el output de ambos LLM y la información recabada de la lectura del artículo para identificar el problema principal y delimitarlo al resto de los problemas que se abordan en el artículo.)*

**Apartado C**

4.  **Prompt 4:** "Este es el desarrollo propuesto para mi proyecto final basado en este artículo, me puedes ayudar a darme algunas ideas sobre los siguientes puntos? Enfoque de trabajo: Teórico / Analítico: Profundización en deducciones matemáticas, soluciones asintóticas y límites físicos. Numérico / Computacional: Reproducción de simulaciones, figuras o cálculos en Google Colab (Python / Julia). Mixto: Combinación de análisis analítico y código numérico complementario. Herramientas a utilizar: (ej. Simulación Monte Carlo / Metropolis, caminatas aleatorias, diagonalización exacta, cálculo simbólico, etc.) Factibilidad: ¿Por qué es viable completar este proyecto en lo que resta del semestre? " — *(Propósito: recabar ideas sobre las actividades a realizar, como realizarlas y cuáles con las herramientas conceptuales pertinentes)* 
5.  **Prompt 5:** "Basado en el artículo del archivo MD, quiero hacer una serie de actividades. Cual sería un buen flujo de trabajo y stack para hacerlo? En especial, se puede configurar un entorno en VS Code que funcione similar a Google Collab" — *(Propósito: Considerar propuestas de stack tecnológico para realizar el trabajo, particularmente la integración de VS Code con git y github para llevar registro y respaldo del proyecto)*


**Planeación a 6 semanas (Github Copilot):**

6.  **Prompt 6:** "Tengo aprox 6 semanas para hacer las actividades anteriormente mencionadas y hacer un video entregable. ¿Cómo puedo justificar la factibilidad de hacer esto y cómo me puedo organizar para lograrlo? " — *(Propósito: Generar un plan tentativo para poder realizar el proyecto, a manera de considerar acotar, reducir o expandir el alcance de este)*