# Modelos de intercambio cinético: De la física molecular a las ciencias sociales

**Marco Patriarca**\*  
Instituto Nacional de Física Química y Biofísica, Răvala 10, Tallin 15042, Estonia

**Anirban Chakraborti**†  
Laboratoire de Mathématiques Appliquées aux Systèmes, École Centrale Paris, 92290 Châtenay-Malabry, Francia

(Fecha: 27 de noviembre de 2024)

---

## RESUMEN

Discutimos varios modelos multiagente que tienen su origen en la teoría del intercambio cinético de la mecánica estadística y que han sido aplicados recientemente a una variedad de problemas en las ciencias sociales. Esta clase de modelos puede adaptarse fácilmente para simulaciones en áreas distintas de la física, como el modelado de las distribuciones de ingresos y riqueza en economía y la dinámica de opiniones en sociología.

---

## I. INTRODUCCIÓN

La aplicación de la teoría de probabilidades al estudio de los gases condujo a la formulación de la teoría cinética de los gases, preparó la base para la formulación de la distribución de velocidades de Maxwell y, más tarde, para el desarrollo de la mecánica estadística.¹⁻³ El triunfo inicial fue que las leyes empíricas de la termodinámica se obtuvieron a partir de las suposiciones básicas de la mecánica estadística. Hoy entendemos que el alcance de la mecánica estadística es mucho más amplio. Dado que dispone de las herramientas para tratar sistemas macroscópicos con un gran número de constituyentes microscópicos, puede aplicarse naturalmente a muchos tipos de sistemas.

Los modelos de intercambio cinético, tema de este artículo, son modelos estocásticos que tienen una interpretación directa en términos de intercambios de energía en un gas. Sin embargo, pueden adaptarse adecuadamente y utilizarse para estudiar problemas en las ciencias sociales, como lo ilustra el trabajo reciente.⁴⁻⁷ Las aplicaciones de los modelos de intercambio cinético a problemas en campos que van desde la física molecular hasta las ciencias sociales ilustran el vínculo histórico entre la mecánica estadística y las ciencias sociales. Recientemente, este vínculo ha sido redescubierto debido al desarrollo de la teoría de sistemas complejos y la dinámica social. De hecho, la estadística, que fue una base importante para el trabajo de Maxwell y Boltzmann y el fundamento de la mecánica estadística, se originó en el estudio de datos demográficos.⁸ La idea de que un gran número de moléculas y un gran grupo social tienen muchas características comunes importantes, en particular, que son predecibles debido al alto número de sus componentes a pesar de su carácter intrínsecamente aleatorio, fue compartida por muchos investigadores. Boltzmann escribió que "las moléculas son como tantos individuos, que tienen los más variados estados de movimiento", cuando escribía sobre los fundamentos de la mecánica estadística.⁸,⁹

Los modelos multiagente son una clase de modelos en los que las acciones e interacciones de agentes autónomos, que pueden representar individuos, organizaciones, sociedades, etc., pueden utilizarse para comprender el comportamiento del sistema en su conjunto. La formulación simple y la implementación numérica de los modelos de intercambio cinético los hacen atractivos en muchas disciplinas. Pueden considerarse como modelos prototípicos mínimos de sistemas complejos que consisten en un conjunto de unidades (posiblemente) heterogéneas que interactúan de acuerdo con leyes simples, y sin embargo son capaces de exhibir estados bien definidos con distribuciones de probabilidad robustas.

En este artículo nos centramos en la formulación, interpretación y simulación de algunos ejemplos representativos de modelos de intercambio cinético. También se resumen otras aplicaciones de los modelos de intercambio cinético en las ciencias sociales.

---

## II. MODELOS DE INTERCAMBIO CINÉTICO HOMOGÉNEOS

### A. Modelos de intercambio cinético en física molecular: Relajación térmica en *d* dimensiones

Introducimos la estructura general de un modelo de intercambio cinético mediante un ejemplo simple. Se supone que las *N* unidades (mínimamente) interactuantes {*i*}, con *i* = 1, 2, ..., *N*, son moléculas de un gas sin energía de interacción y las variables {*w*ᵢ} representan sus energías cinéticas, de modo que *w*ᵢ ≥ 0. La evolución temporal del sistema procede mediante una dinámica estocástica discreta. Se realizan una serie de actualizaciones de las energías cinéticas *w*ᵢ(*t*) en los tiempos discretos *t* = 0, 1, ... . Cada actualización tiene en cuenta el efecto de una colisión entre dos moléculas. El paso temporal, que puede fijarse en Δ*t* = 1 sin pérdida de generalidad, representa el intervalo de tiempo promedio entre dos colisiones moleculares consecutivas; es decir, en promedio, después de cada paso temporal Δ*t*, dos moléculas *i* y *j* experimentan un proceso de dispersión y se realiza una actualización de sus energías cinéticas *w*ᵢ y *w*ⱼ.

La evolución del sistema se lleva a cabo mediante los siguientes pasos en cada tiempo *t*.

1. Elegir aleatoriamente un par de moléculas *i* y *j* (*i* ≠ *j* y 1 ≤ *i*, *j* ≤ *N*), con energías cinéticas *w*ᵢ y *w*ⱼ, respectivamente; representan las moléculas que experimentan una colisión.

2. Calcular la cantidad neta Δ*w*ᵢⱼ de energía cinética que se intercambiará entre las moléculas; su valor es una función de las energías cinéticas iniciales *w*ᵢ y *w*ⱼ y depende del modelo considerado.

3. Realizar el intercambio de energía entre *i* y *j* actualizando sus energías cinéticas,

$$w_i \rightarrow w_i - \Delta w_{ij} \quad (1a)$$

$$w_j \rightarrow w_j + \Delta w_{ij}. \quad (1b)$$

La energía cinética total se conserva durante una interacción.

4. Fijar *t* → *t*+1 e ir al paso 1.

La forma de la función Δ*w*ᵢⱼ define el modelo específico. Los modelos de intercambio cinético describen la dinámica a nivel microscópico, basándose en colisiones moleculares individuales. Tal representación puede ser óptima en términos de simplicidad y eficiencia computacional cuando el foco está en la dinámica de la energía, porque las partículas se describen solo por su grado de libertad energético *w*, en lugar de por el conjunto completo de sus 2*d* coordenadas de posición y momento, para un sistema *d*-dimensional.

Como primer ejemplo simple, considérese la regla de redistribución: *w*ᵢ → ε(*w*ᵢ + *w*ⱼ), *w*ⱼ → (1−ε)(*w*ᵢ + *w*ⱼ), donde ε es una variable estocástica extraída como un número aleatorio uniforme entre 0 y 1. Esta regla corresponde a Δ*w*ᵢⱼ = (1−ε)*w*ᵢ − ε*w*ⱼ. En este caso, el algoritmo que hemos esbozado conduce desde condiciones iniciales arbitrarias a la distribución de energía de Boltzmann-Gibbs en equilibrio, *f*(*w*) = β exp(−β*w*), donde β = 1/⟨*w*⟩ y ⟨*w*⟩ representa la energía media de una sola molécula. Las derivaciones teóricas de este resultado utilizando la ecuación de transporte de Boltzmann, o el principio de maximización de la entropía, o argumentos probabilísticos simples, pueden encontrarse en la mayoría de los libros de texto estándar de mecánica estadística.

Como ejemplo más general, considérese la relajación en el espacio de energía de un gas en *d* dimensiones. Suponemos que *d* > 1 porque las distribuciones de momento y energía de un gas unidimensional (donde solo ocurren colisiones frontales) no cambian con el tiempo. Aunque el modelo puede concebirse más fácilmente para un gas en tres dimensiones, las características más sorprendentes de los modelos de intercambio cinético aparecen para un gas en un número arbitrario de dimensiones, un caso relevante para el tratamiento de sistemas heterogéneos en la Sec. III. Para un gas en *d* dimensiones, la forma de la regla de actualización, y en particular de Δ*w*ᵢⱼ, puede derivarse exactamente de la conservación de energía y momento durante una colisión entre dos partículas *i* y *j*. Si los respectivos vectores *d*-dimensionales de los momentos iniciales de las partículas son **p**ᵢ y **p**ⱼ, encontramos¹⁰

$$\Delta w_{ij} = r_i w_i - r_j w_j \quad (2)$$

$$r_k = \cos^2 \alpha_k \quad (k = i, j) \quad (3)$$

$$\cos \alpha_k = \frac{\mathbf{p}_k \cdot \Delta \mathbf{p}_{ij}}{|\mathbf{p}_k| |\Delta \mathbf{p}_{ij}|}, \quad (4)$$

donde cos αₖ es el coseno director del momento **p**ₖ (*k* = *i*, *j*) con respecto a la dirección del momento transferido Δ**p**ᵢⱼ = **p**ᵢ − **p**ⱼ. Las direcciones de las dos partículas que colisionan pueden suponerse aleatorias utilizando la hipótesis del caos molecular.³

Ahora podemos estudiar la evolución temporal eligiendo aleatoriamente en cada paso temporal dos nuevos valores para *r*ₖ en la Ec. (2), en lugar de mantener una lista de coordenadas de momento, como se hace comúnmente en una simulación de dinámica molecular. Luego usamos la Ec. (1) para calcular las nuevas energías de las partículas *w*ᵢ y *w*ⱼ. Obsérvese que las *r*ₖ no están distribuidas uniformemente en (0, 1), por lo que la forma de su función de distribución de probabilidad debe elegirse con cierta prudencia. De hecho, su distribución depende fuertemente de la dimensión espacial *d*, siendo su valor promedio ⟨*r*ₖ⟩ = 1/*d*; véase la Ref. 10 para más detalles. Esta dependencia de ⟨*r*ₖ⟩ con *d* puede entenderse intuitivamente desde la teoría cinética: cuanto mayor es el valor de *d*, más improbable se vuelve que *r*ₖ asuma valores cercanos a *r*ₖ = 1 (correspondiente a una colisión frontal de tipo unidimensional). Por lo tanto, una elección simple y computacionalmente eficiente es una distribución aleatoria uniforme *f*(*r*ₖ), limitada en el intervalo (0, 2/*d*), tal que el valor promedio ⟨*r*ₖ⟩ = 1/*d*.

Las simulaciones de este sistema modelo utilizando números aleatorios en lugar de las *r*ᵢ en la Ec. (2), para *d* = 2, dan la distribución de equilibrio de Boltzmann-Gibbs: *f*(*w*) = β exp(−β*w*), donde β = 1/⟨*w*⟩, como antes. Para *d* > 2, obtenemos la generalización *d*-dimensional de la distribución de Boltzmann estándar,¹⁰⁻¹² es decir, la distribución Gamma (Γ)¹³,¹⁴ caracterizada por un parámetro de forma α igual a la mitad de la dimensión espacial,

$$f(w, \alpha, \theta) = \frac{w^{\alpha-1} e^{-w/\theta}}{\theta^{\alpha} \Gamma(\alpha)} \quad (5)$$

$$\alpha = d/2 \quad (6)$$

$$\theta = \langle w \rangle / \alpha. \quad (7)$$

El parámetro de escala θ de la distribución Γ queda fijado, por definición, por la Ec. (7).¹³,¹⁴ A partir del teorema de equipartición en mecánica estadística clásica, *w* = *d k*_B *T*/2. Por lo tanto, vemos que la Ec. (7) identifica el parámetro de escala θ como la temperatura absoluta (en unidades de energía) dada por θ ≡ *k*_B *T* = 1/β. Por consiguiente, el mismo factor de Boltzmann, exp(−*w*/θ), está presente en la distribución de equilibrio independientemente de la dimensión *d*, y el prefactor *w*^{α−1} depende de *d*, porque tiene en cuenta el volumen del espacio de fases proporcional a *p*^d ∝ *w*^{d/2}, donde *p* es el módulo del momento.

### B. Modelado de la distribución de la riqueza

Además de su interpretación en el contexto de la física, los modelos de intercambio cinético son aplicables a problemas en las ciencias sociales como la dinámica de opiniones y el modelado de sistemas económicos. Estos últimos modelos demuestran su adaptabilidad y promesa, particularmente en su aplicación a las distribuciones de riqueza. En esta sección consideramos cómo algunos modelos de intercambio cinético describen la formación de la distribución de la riqueza observada en una sociedad, como consecuencia de intercambios binarios de riqueza entre individuos. Suponemos aquí que la definición estándar de riqueza es el conjunto de todas aquellas cosas con algún valor monetario o de cambio. La forma de una distribución típica de la riqueza es compleja, con un comportamiento de Boltzmann-Gibbs (exponencial) en los valores bajos e intermedios de riqueza, *w* < *w*_c, y una cola de ley de potencias (Pareto) en los valores de riqueza más grandes, *w* ≥ *w*_c, donde *w*_c es un valor de cruce que depende del ajuste numérico de los datos. La ley de Pareto se expresa como:

$$f(w) \sim w^{-\alpha-1} \quad (w \ge w_c), \quad (8)$$

donde *f*(*w*) es la densidad de probabilidad, y el exponente α es el exponente de Pareto, que tiene un valor entre 1 y 3. La Referencia 16 ofrece relatos concisos de estudios empíricos, numéricos y analíticos sobre este tema. La Figura 1 muestra un gráfico de la distribución de probabilidad acumulada para datos de riqueza. Es más práctico representar la distribución de probabilidad acumulada *C*(*w*) = ∫_w^∞ *f*(*w*′) *dw*′ en función de la riqueza *w*, en lugar de *f*(*w*), porque los datos estadísticos suelen presentarse en intervalos no uniformes de *w*. Curiosamente, cuando *f*(*w*) es una función exponencial o de ley de potencias, entonces la correspondiente *C*(*w*) también es una función exponencial o de ley de potencias. Para más detalles sobre los modelos cinéticos de intercambio de riqueza, véanse las Refs. 4, 5 y 7.

**FIG. 1.** Distribución de probabilidad acumulada de la riqueza neta, compuesta por activos (incluyendo efectivo, acciones, propiedades y bienes del hogar) y pasivos (incluyendo hipotecas y otras deudas) en el Reino Unido, mostrada en escalas log-log (panel principal) y log-lineal (recuadro). Los puntos representan los datos del Inland Revenue, y las líneas sólidas son ajustes a las distribuciones de Boltzmann-Gibbs (exponencial) y Pareto (potencia).¹⁵

Entre los primeros ejemplos de modelos de intercambio cinético de mercados propuestos por no físicos, mencionamos el trabajo de Angle, un sociólogo.¹⁷⁻²⁰ En la primera versión del modelo¹⁷,¹⁸ la riqueza intercambiada en un encuentro entre dos agentes tiene la forma de la Ec. (2), donde *r*ᵢ = εκη y *r*ⱼ = (1 − ε)κη. Aquí κ representa la fracción máxima de riqueza que puede perderse, ε es un número aleatorio uniforme en (0, 1), y η es una variable estocástica con los valores 0 o 1 con una distribución de probabilidad que depende de la diferencia entre la riqueza de los dos agentes *w*ᵢ − *w*ⱼ. En el segundo modelo de Angle, denominado proceso de desigualdad de un parámetro,¹⁹,²⁰ *r*ᵢ = κη y *r*ⱼ = κ(1 − η), con un significado similar para κ y η. En contraste, en la versión básica de los modelos²¹⁻²³ introducidos anteriormente por el economista Bennati, Δ*w*ᵢⱼ es una constante, independiente de otros parámetros.

Independientemente de los esfuerzos de modelado anteriores por parte de científicos sociales, los físicos también habían realizado varios estudios. El primer tipo de modelos, tanto con intercambios multiplicativos como aditivos, fue propuesto por Ispolatov, Krapivski y Redner.²⁴ En los modelos de intercambio cinético introducidos posteriormente, consideramos primero el trabajo de Dragulescu y Yakovenko,²⁵ donde *r*ᵢ = 1 − *r*ⱼ = ε, correspondiente a un esquema de redistribución aleatoria de la riqueza total de los dos agentes. A continuación consideramos un modelo prototípico simple de intercambio cinético con una distribución de equilibrio Γ, que fue introducido por Chakraborti y Chakrabarti²⁶ para describir la actividad comercial entre *N* entidades (por ejemplo, agentes, empresas y compañías) empleando un criterio de ahorro al realizar sus transacciones. Las transacciones se representan mediante intercambios de riqueza por pares con la dinámica dada por la Ec. (1) con

$$\Delta w_{ij} = \kappa(\bar{\epsilon} w_i - \epsilon w_j) = (1 - \lambda)(\bar{\epsilon} w_i - \epsilon w_j), \quad (9)$$

donde ε̄ = 1 − ε. El parámetro de intercambio κ ∈ (0, 1) (o el parámetro de ahorro λ = 1 − κ) define la fracción máxima de la riqueza *w* en el proceso de intercambio (o la fracción mínima de *w* preservada durante el intercambio). El parámetro κ (o λ) también determina la escala temporal del proceso de relajación, así como el valor medio ⟨*w*⟩ en equilibrio.²⁷ La distribución de riqueza de equilibrio del sistema se describe bien mediante la distribución Γ de la Ec. (5), donde un ajuste sugiere la fórmula empírica

$$\alpha = \frac{1 + 2\lambda}{1 - \lambda} = \frac{3}{\kappa} - 2, \quad (10)$$

que relaciona el parámetro de forma α con el parámetro de ahorro λ. Obsérvese que para λ → 0 (o κ → 1), α → 1, correspondiente a la función exponencial. En todos los diversos modelos que hemos mencionado, la distribución de equilibrio se ajusta bien mediante una distribución Γ. Esta forma de la distribución de equilibrio muestra un buen acuerdo con las distribuciones empíricas de riqueza en valores pequeños e intermedios¹⁵,²⁸ (véase la Fig. 1).

Los resultados numéricos del modelo definido por la Ec. (9) se comparan en la Fig. 2 con un ajuste basado en la distribución Γ. Se obtuvieron utilizando 10⁴ agentes y 10⁴ pasos temporales. La convergencia al equilibrio es rápida y un tiempo de simulación tan largo se utilizó solo para acumular estadísticas (cada 100 pasos temporales). Obsérvese que aquí un paso temporal es en realidad un bucle sobre *N* intercambios. El número de agentes empleados debe elegirse suficientemente grande para garantizar suficientes estadísticas — lo que implica una buena calidad del histograma de riqueza — en la escala de frecuencia deseada, de lo contrario puede aparecer un histograma muy irregular en los valores más pequeños y más grandes de *w*. El valor *N* = 10⁵ sigue siendo manejable computacionalmente, pero suficientemente grande para ver claramente frecuencias tan pequeñas como 10⁻⁵.

**FIG. 2.** (Color en línea) Distribuciones de riqueza de equilibrio del modelo introducido en la Ref. 26 y definido por la Ec. (9) para diferentes valores del parámetro de ahorro λ para escalas lineal (arriba) y semilogarítmica (abajo).

### C. Otras aplicaciones en ciencias sociales

Lallouache et al.⁶ construyeron un modelo homogéneo para la dinámica colectiva de formación de opinión en una sociedad modificando la dinámica de intercambio cinético estudiada en el contexto de los mercados. En este modelo, la opinión del *i*-ésimo agente se representa mediante una variable continua *w*ᵢ ∈ (−1, +1). Se supone que las interacciones entre agentes que modifican sus opiniones tienen lugar mediante encuentros aleatorios de dos cuerpos, con una dinámica definida por

$$w_i \rightarrow \lambda[w_i + \epsilon w_j] \quad (11a)$$

$$w_j \rightarrow \lambda[w_j + \epsilon' w_i], \quad (11b)$$

donde λ ∈ (0, 1) es el parámetro de "convicción" (constante) y ε, ε′ ∈ (0, 1) son procesos estocásticos no correlacionados distribuidos uniformemente. Obsérvese que no hay conservación paso a paso de la opinión, a diferencia de los modelos de riqueza precedentes. Sorprendentemente, se encuentra que aparece polaridad o consenso, partiendo de un desorden aleatorio inicial (donde las *w*ᵢ están distribuidas uniformemente con valores positivos y negativos). En el lenguaje de la física, hay una "transición espontánea de ruptura de simetría" en el sistema: partiendo del valor medio de *w*ᵢ, *w̄*(0) = 0, el sistema evoluciona ya sea al estado "para" con *w̄*(*t* > τ) = 0, donde todos los agentes tienen opinión cero (para valores de λ ≤ 2/3), o al estado de "simetría rota", con *w̄*(*t* > τ) ≠ 0, donde todos los agentes tienen opiniones todas positivas o todas negativas (para λ ≥ 2/3). El tiempo *t* > τ, donde τ es el tiempo de relajación del sistema. El comportamiento de relajación del sistema muestra una divergencia crítica de τ en λ = λ_c = 2/3. Sen²⁹ generalizó el modelo de Lallouache et al. introduciendo un parámetro adicional μ para representar la capacidad de influencia de los individuos y estudió las transiciones de fase correspondientes.

En un contexto diferente, similar en espíritu al trabajo presentado en las Refs. 30 y 31, Ghosh et al.³² consideraron un modelo económico en el que existe un umbral de pobreza θ > 0 tal que en cualquier tiempo *t*, al menos uno de los dos agentes que interactúan es "pobre"; es decir, su riqueza satisface *w* < θ. El papel central asignado a los comerciantes pobres produce diversas características nuevas, como una forma diferente de la distribución de equilibrio y una transición de fase en la fracción de agentes pobres en función de θ. Estos modelos de intercambios cinéticos, que se inspiran en diversos contextos socioeconómicos, también pueden servir para introducir las ideas de transiciones de fase y fenómenos críticos en la física estadística.

---

## III. MODELOS DE INTERCAMBIO CINÉTICO HETEROGÉNEOS

Una generalización interesante de los modelos de intercambio cinético homogéneos que hemos discutido hasta ahora es la introducción de heterogeneidad. Probablemente la aplicación más relevante de los modelos de intercambio cinético heterogéneos en las ciencias sociales es la predicción de una forma realista para la distribución de la riqueza que incluya la ley de potencias de Pareto en los valores de riqueza más grandes (véase la Fig. 1 y la Sec. II B).

Consideramos de nuevo el modelo definido por la Ec. (9) e introducimos heterogeneidad diversificando el parámetro κ o, equivalentemente, el parámetro de ahorro λ, lo que significa que cada término κ*w*ᵢ (o λ*w*ᵢ) se reemplaza por κᵢ*w*ᵢ (o λᵢ*w*ᵢ), obteniéndose así³³

$$\Delta w_{ij} = \bar{\epsilon} \kappa_i w_i - \epsilon \kappa_j w_j = \bar{\epsilon}(1 - \lambda_i) w_i - \epsilon(1 - \lambda_j) w_j. \quad (12)$$

Como ejemplo simple, consideramos un conjunto de agentes heterogéneos con parámetros κᵢ distribuidos uniformemente en el intervalo (0, 1). Repitiendo las simulaciones usando la Ec. (12), se encuentra que la forma de las distribuciones de riqueza de equilibrio separadas *f*ᵢ(*w*) de cada agente sigue siendo una distribución Γ. Sin embargo, hay una sorpresa en la distribución de riqueza del sistema *f*(*w*), dada por la suma de las distribuciones de riqueza de los agentes individuales, *f*(*w*) = Σᵢ *f*ᵢ(*w*). Como también han mostrado otros estudios analíticos y numéricos, *f*(*w*) tiene una forma exponencial hasta valores intermedios de *w*, y una ley de potencias de Pareto se desarrolla en los valores más grandes de *w* (véase la Fig. 3).³⁴,³⁵ Tal forma es similar a las distribuciones reales de riqueza como la mostrada en la Fig. 1. Esta forma de la distribución de riqueza de equilibrio *f*(*w*) es robusta con respecto a los detalles del sistema y a los valores de los otros parámetros, siempre que los valores de los κᵢ estén suficientemente dispersos en todo el intervalo κ = (0, 1). Es el grupo de agentes con κ ≈ 0 (λ ≈ 1) el que es crucial para la aparición de una ley de potencias. No todos los agentes tienen que diferir entre sí, como se ilustra mejor repitiendo la simulación utilizando una distribución diferente para los parámetros κ o las λ, en la que el 99% de la población de agentes tiene λ = 0.2, y solo el 1% de la población es heterogénea con λ en el intervalo (0, 1) (véase la Fig. 4).

El modelo heterogéneo utiliza necesariamente un corte superior finito λ_max < 1, al considerar la distribución del parámetro de ahorro, que determina directamente el corte *w*_max de la distribución de riqueza, análogo al corte observado en las distribuciones reales: cuanto más cerca está λ_max de uno, mayor es *w*_max y más amplio es el intervalo en el que se observa la ley de potencias.³⁶

El corte λ está estrechamente relacionado con el proceso de relajación, cuyas escalas temporales para el agente *i* son proporcionales a 1/(1 − λᵢ).²⁷ Por lo tanto, la tasa de convergencia más lenta está determinada por 1 − λ_max. El corte finito λ utilizado en las simulaciones de modelos de intercambio cinético heterogéneos no es una limitación del modelo, sino que refleja una característica importante de las distribuciones reales de riqueza.

**FIG. 3.** (Color en línea) Distribución de riqueza *f*(*w*) para κᵢ (o λᵢ) distribuidos uniformemente en el intervalo (0, 1); *f*(*w*) se descompone en distribuciones parciales *f*ᵢ(*w*), donde cada *f*ᵢ(*w*) se obtiene contando las estadísticas de aquellos agentes con parámetro λᵢ en un subintervalo específico (de la Ref. 36). (a) Descomposición de *f*(*w*) en diez distribuciones parciales en los subintervalos λ (0, 0.1), (0.1, 0.2) ... (0.9, 1). (b) La última distribución de (a) en el intervalo λ (0.9, 1) se descompone en distribuciones parciales obtenidas contando las estadísticas de agentes con subintervalos λ (0.9, 0.91), (0.91, 0.92) ... (0.99, 1). Obsérvese cómo la ley de potencias aparece como consecuencia de la superposición de las distribuciones parciales.

---

## IV. COMENTARIOS

Existen varios estudios analíticos que complementan las simulaciones y los estudios empíricos. Remitimos al lector a la Ref. 16, que ofrece relatos concisos de estudios sobre este tema, junto con una lista exhaustiva de referencias.

La dinámica de los modelos de intercambio cinético a veces se critica por basarse en un enfoque alejado de una perspectiva económica real. Sin embargo, tal dinámica también puede derivarse de la teoría microeconómica.³⁷ Aunque la teoría económica estándar supone que las actividades de los agentes individuales están impulsadas por el principio de maximización de la utilidad, la imagen alternativa que hemos descrito es que los agentes pueden verse como partículas que intercambian "riqueza", en lugar de energía, y comercian en dispersiones de dos cuerpos que conservan la riqueza (energía), como en la maximización de la entropía basada en la teoría cinética de los gases.³⁴ Esta analogía cualitativa entre los dos principios de maximización no es nueva — tanto economistas como físicos la han notado en muchos contextos, pero esta equivalencia ha ganado terreno más firme solo recientemente.³⁷

**FIG. 4.** (Color en línea) Ejemplo de una distribución realista de riqueza, de la Ref. 36. Curva continua: distribución de riqueza obtenida mediante simulaciones de una población mixta de agentes, tal que el 1% de los agentes tienen propensiones de ahorro λᵢ ∈ (0, 1) distribuidas uniformemente y el otro 99% de los agentes tienen λᵢ = 0.2. Curva punteada: distribución exponencial de riqueza ∝ exp(−*w*/⟨*w*⟩), con la misma riqueza promedio, representada para comparación con la distribución en la región de riqueza intermedia. Curva discontinua: ley de potencias de Pareto ∝ *w*⁻², representada para comparación con la parte de altos ingresos de la distribución.

---

## V. PROBLEMAS SUGERIDOS

Los modelos de intercambio de riqueza que hemos discutido son mínimos y se prestan a diversas generalizaciones y modificaciones para estudiar el efecto de características adicionales. Elíjase el modelo de intercambio cinético, por ejemplo, definido por: *w*ᵢ → *w*ᵢ − Δ*w*ᵢⱼ y *w*ⱼ → *w*ⱼ + Δ*w*ᵢⱼ, con Δ*w*ᵢⱼ = (1 − ε)*w*ᵢ − ε*w*ⱼ. Realícense las simulaciones y compruébese si se alcanza la correspondiente distribución de equilibrio de Boltzmann-Gibbs *f*(*w*) = β exp(−β*w*), donde β = 1/⟨*w*⟩, partiendo de cualquier distribución inicial arbitraria de *w* entre los agentes. A continuación, realícense las simulaciones para *w*ᵢ → *w*ᵢ − Δ*w*ᵢⱼ y *w*ⱼ → *w*ⱼ + Δ*w*ᵢⱼ, cuando la forma de Δ*w*ᵢⱼ o las ecuaciones dinámicas se modifican, como se sugiere a continuación.

- **Diferentes reglas de intercambio:** Verifíquese que la distribución final de riqueza de equilibrio sigue siendo la distribución de Boltzmann-Gibbs, cuando se emplea la regla de que en cada paso se intercambia una cantidad constante arbitraria [Δ*w*ᵢⱼ = *w*₀], o en cada paso se intercambia una fracción de la riqueza promedio del sistema.²⁵ Sin embargo, si en cambio se utiliza la riqueza mínima entre los dos agentes como cantidad intercambiada [Δ*w*ᵢⱼ = min(*w*ᵢ, *w*ⱼ)], se producirá la condensación de la riqueza total en manos de un solo agente.³⁸

- **Impuestos sobre las transacciones:** Modifíquense las ecuaciones dinámicas añadiendo un término que tome como impuesto una cantidad fija de riqueza δ*w*₀ o un porcentaje fijo de la riqueza intercambiada Δ*w*ᵢⱼ de los agentes *i* y *j*, y lo redistribuya uniformemente entre todos los demás.²⁵

- **Deuda:** Modifíquense las ecuaciones dinámicas de modo que se permita a los agentes pedir prestado o tomar préstamos hasta una cantidad máxima *w*_max, de modo que su riqueza pueda volverse negativa pero no menor que −*w*_max. Esta modificación puede implementarse incrementando la riqueza total en una cantidad adicional *w*_max.²⁵

- **Ahorro fijo:** Añádase al modelo un ahorro fijo *w*₀ para cada uno de los dos agentes, de modo que la riqueza total se reduzca en una cantidad 2*w*₀.³⁸

- **Interacciones de muchos agentes:** Establézcase una nueva regla dinámica en la que la riqueza se redistribuya en encuentros entre más de dos agentes, por ejemplo, entre tres agentes *i*, *j* y *k*. Los demás detalles de la transacción deben ser similares a los de una transacción por pares entre los agentes *i* y *j*. Debe tenerse cierto cuidado para definir adecuadamente las respectivas fracciones aleatorias de riqueza asignadas a cada agente para hacer el proceso simétrico con respecto a todos los agentes involucrados en el encuentro.

---

## AGRADECIMIENTOS

Agradecemos a todos nuestros colaboradores y estudiantes. M.P. agradece el apoyo financiero del proyecto de financiación específica SF0690030s09 y de la Fundación Estonia para la Ciencia mediante la subvención n.º 9462.

\* marco.patriarca@kbfi.ee  
† anirban.chakraborti@ecp.fr

---

## REFERENCIAS

¹ L. Boltzmann, *Lectures on Gas Theory*, Dover, NY (1964).

² J. P. Sethna. *Statistical Mechanics*, Oxford University Press, Oxford (2006).

³ D. ter Haar, *Elements of Statistical Mechanics*, Butterworth-Heinemann, Oxford (1995).

⁴ A. Chakraborti, I. Muni Toke, M. Patriarca y F. Abergel, "Econophysics review: II. Agent-based models," *Quantitative Finance* **11**, 1013–1041 (2011).

⁵ A. Chatterjee y B. K. Chakrabarti, "Kinetic exchange models for income and wealth distributions," *Eur. Phys. J. B* **60**, 135–149 (2007).

⁶ M. Lallouache, A. S. Chakrabarti, A. Chakraborti y B. K. Chakrabarti, "Opinion formation in kinetic exchange models: Spontaneous symmetry-breaking transition," *Phys. Rev. E* **82**, 056112-1–5 (2010).

⁷ M. Patriarca, E. Heinsalu y A. Chakraborti, "Basic kinetic wealth-exchange models: common features and open problems," *Eur. J. Phys. B* **73**, 145–153 (2010).

⁸ P. Ball, "The physical modelling of society: a historical perspective," *Physica A* **314**, 1–14 (2002).

⁹ L. Boltzmann, "Weitere Studien über das Wärmegleichegewicht unter Gasmolekulen," *Akad. Wiss. Wein* **66**, 275–370 (1872).

¹⁰ A. Chakraborti y M. Patriarca, "Gamma-distribution and wealth inequality," *Pramana J. Phys.* **71** (2), 233–243 (2008).

¹¹ M. Patriarca, A. Chakraborti y K. Kaski, "Gibbs versus non-Gibbs distributions in money dynamics," *Physica A* **340**, 334–339 (2004).

¹² M. Patriarca, A. Chakraborti y K. Kaski, "Statistical model with a standard gamma distribution," *Phys. Rev. E* **70**, 016104-1–5 (2004).

¹³ N. L. Johnson, S. Kotz y N. Balakrishnan, *Continuous Univariate Distributions*, Wiley, Nueva York (1994), Vol. 1.

¹⁴ M. Abramowitz e I. A. Stegun, *Handbook of Mathematical Functions*, Dover, Nueva York (1972).

¹⁵ A. Dragulescu y V. M. Yakovenko, "Evidence for the exponential distribution of income in the USA," *Eur. Phys. J. B* **20**, 585–589 (2001).

¹⁶ A. Chakraborti, I. Muni Toke, M. Patriarca y F. Abergel, "Econophysics review: I. Empirical facts," *Quantitative Finance* **11**, 991–1012 (2011).

¹⁷ J. Angle, "The surplus theory of social stratification and the size distribution of personal wealth," *Soc. Forces* **65**, 293–326 (1986).

¹⁸ J. Angle, "The inequality process as a wealth maximizing process," *Physica A* **367**, 388–414 (2006).

¹⁹ J. Angle, "Deriving the size distribution of personal wealth from 'the rich get richer, the poor get poorer'," *J. Math. Sociol.* **18**, 27–46 (1993).

²⁰ J. Angle, "The one-parameter inequality process," *Physica A* **367**, 388–414 (2006).

²¹ E. Bennati, "Un modello probabilistico per la distribuzione del reddito," en *Atti della Prima Riunione Scientifica della Società Italiana di Statistica*, 1978, pp. 1–14.

²² E. Bennati, "La distribuzione funzionale del reddito: un modello probabilistico," *Rivista di Politica Economica* **6**, 3–28 (1988).

²³ E. Bennati, "Un modello probabilistico per la distribuzione del reddito," *Statistica* **48**, 283–296 (1988).

²⁴ S. Ispolatov, P. L. Krapivsky y S. Redner, "Wealth distributions in asset exchange models," *Eur. Phys. J. B* **2**, 267–276 (1998).

²⁵ A. Dragulescu y V. M. Yakovenko, "Statistical mechanics of money," *Eur. Phys. J. B* **17**, 723–729 (2000).

²⁶ A. Chakraborti y B. K. Chakrabarti, "Statistical mechanics of money: how saving propensity affects its distribution," *Eur. Phys. J. B* **17**, 167–170 (2000).

²⁷ M. Patriarca, A. Chakraborti y G. Germano, "Influence of saving propensity on the power-law tail of the wealth distribution," *Physica A* **369**, 723–736 (2006).

²⁸ A. Dragulescu y V. M. Yakovenko, "Exponential and power-law probability distributions of wealth and income in the United Kingdom and the United States," *Physica A* **299**, 213–221 (2001).

²⁹ P. Sen, "Phase transitions in a kinetic model of opinion formation," *Phys. Rev. E* **84**, 042101 (2011).

³⁰ A. Chatterjee, B. K. Chakrabarti y S. S. Manna, "Pareto law in a kinetic model of market with random saving propensity," *Physica A* **335**, 155–163 (2004).

³¹ G. Katona y J. Kertész, "Pareto's law and the power-law distribution of wealth in a stochastic exchange model," *Physica A* **387**, 1865–1871 (2008).

³² A. Ghosh, A. Chakraborti y B. K. Chakrabarti, "A poverty threshold model of wealth distribution," *Physica A* **390**, 2830–2839 (2011).

³³ A. Chakraborti y M. Patriarca, "Gamma-distribution and wealth inequality," *Pramana J. Phys.* **71**, 233–243 (2008).

³⁴ M. Patriarca, A. Chakraborti y K. Kaski, "Statistical model with a standard gamma distribution," *Phys. Rev. E* **70**, 016104 (2004).

³⁵ A. Chatterjee, S. Yarlagadda y B. K. Chakrabarti, "Kinetic exchange models of income and wealth distributions," en *Econophysics of Wealth Distributions*, editado por A. Chatterjee, S. Yarlagadda y B. K. Chakrabarti, Springer, Milán (2005), pp. 37–55.

³⁶ M. Patriarca, A. Chakraborti y G. Germano, "Influence of saving propensity on the power-law tail of the wealth distribution," *Physica A* **369**, 723–736 (2006).

³⁷ A. Chakraborti, "Distributions of money in model markets of economy," *Int. J. Mod. Phys. C* **13**, 1315–1321 (2002).

³⁸ A. Chatterjee, B. K. Chakrabarti y S. S. Manna, "Pareto law in a kinetic model of market with random saving propensity," *Physica A* **335**, 155–163 (2004).

---

*Nota: Las referencias 36–38 se han completado con la información bibliográfica estándar correspondiente a las citas del texto original; en el documento fuente aparecían parcialmente truncadas.*