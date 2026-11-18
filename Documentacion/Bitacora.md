# Lista de pendientes y productos prometidos


## A. Productos Entregables ?
### A1. Productos del Proyecto Final (calificación)
1. **Simulación computacional funcional** en Python que reproduzca la emergencia de Boltzmann-Gibbs a partir de la regla de reshuffling.
2. **Verificación numérica de conservación de energía** ($E_{tot}=\sum E_i$ constante).
3. **Histograma de energías** en estado estacionario.
4. **Comparación numérica vs. distribución exponencial** $P(E)=\beta e^{-\beta E}$ con $\beta=1/\langle E\rangle$.
5. **Comparación de histogramas antes y después** de los intercambios (evolución al equilibrio).
6. **Explicación de la relación** entre la distribución obtenida y la distribución de Boltzmann.
7. **Repositorio en GitHub** con:
   - Código alojado y versionado con git.
   - Documentación (README).
   - Entorno de trabajo configurado.
8. **Notebooks** (Google Colab / JupyterLab / VS Code) con bloques de texto que expliquen brevemente las simulaciones.

### A2. Productos del Video
9. **Video entregable** de divulgación (audiencia: público general).
   - Tono accesible, analogías, situaciones cotidianas.
   - Recursos gráficos: animaciones metafóricas y lúdicas.
   - Detalles técnicos delegados al repositorio.
10. **Guion del video** (redacción en paralelo a la simulación).

### A3. Productos de gestión/declaración
11. **Documento de propuesta** (ya entregado el 31 de octubre).
12. **Declaración de uso de IA** 

---

## B. TAREAS PARA PRODUCIR LOS PRODUCTOS

### B1. Configuración (Semana 1)
- [x] Crear repositorio en GitHub.
- [x] Configurar git en el entorno local (VS Code).
- [x] Configurar entorno tipo Colab en VS Code (extensión Jupyter + kernel Python).
- [x] Crear estructura de carpetas (`/src`, `/notebooks`, `/figures`).
- [x] Crear `README.md` inicial.
- [x] Crear `requirements.txt`.
- [x] Primer commit.

### B2. Simulación base (Semanas 1–2)
- [ ] Definir sistema: $N=1000$ partículas, $E_i=1$ inicial.
- [ ] Implementar selección aleatoria de pares.
- [ ] Implementar regla de redistribución:
  - $E'_i=\varepsilon(E_i+E_j)$
  - $E'_j=(1-\varepsilon)(E_i+E_j)$ con $\varepsilon\sim U(0,1)$.
- [ ] Definir y documentar qué cuenta como "un paso" (colisión vs. sweep).
- [ ] Iterar hasta distribución aproximadamente estacionaria.
- [ ] Verificar numéricamente $E_{tot}=\sum E_i$ constante.

### B3. Análisis y figuras (Semanas 2–3)
- [ ] Construir histograma de energías tras muchos intercambios.
- [ ] Calcular $\beta=1/\langle E\rangle$.
- [ ] Ajustar/comparar con $P(E)=\beta e^{-\beta E}$.
- [ ] Graficar histogramas antes y después de los intercambios.
- [ ] Redactar explicación de la relación con Boltzmann.
- [ ] Documentar todo en notebook con celdas markdown.

### B4. Validación y robustez (Semana 3)
- [ ] Repetir con distintas semillas.
- [ ] Probar distintas condiciones iniciales.
- [ ] (Opcional) Estudio de tiempo de relajación.
- [ ] Commit y documentación de resultados.

### B5. Extensión opcional (Semana 4)
- [ ] Implementar modelo con ahorro (Ec. 9) y comparar con Gamma.
- [ ] (Solo si el núcleo está cerrado.)

### B6. Video (Semanas 4–5)
- [ ] Redactar guion (en paralelo desde antes).
- [ ] Diseñar analogías y animaciones.
- [ ] Grabar.
- [ ] Editar.
- [ ] Verificar que el nivel sea divulgativo.

### B7. Cierre (Semana 6)
- [ ] Limpiar y documentar repositorio.
- [ ] Verificar todos los entregables de la sección A.
- [ ] Ensayo final / revisión.

---

## C. TABLA DE TRAZABILIDAD (producto → tarea → semana)

| # | Producto prometido | Tarea(s) que lo produce(n) | Semana |
|---|---|---|---|
| 1 | Simulación funcional | B1, B2 | 1–2 |
| 2 | Verificación conservación $E_{tot}$ | B2 | 1–2 |
| 3 | Histograma estacionario | B3 | 2 |
| 4 | Comparación con exponencial | B3 | 2 |
| 5 | Histogramas antes/después | B3 | 2–3 |
| 6 | Explicación Boltzmann | B3 | 2–3 |
| 7 | Repositorio GitHub documentado | B1, B7 | 1 y 6 |
| 8 | Notebooks explicativos | B2, B3 | 2–3 |
| 9 | Video divulgativo | B6 | 4–5 |
| 10 | Guion del video | B6 | 4–5 |
| 11 | Propuesta | — | Hecho |
| 12 | Declaración IA | — | xd |


17/11/26

Se realizo una primera version de B2, llamada test2.py
despues de iterar con varios seeds y aumentar el numero maximo de sweeps no se ha llegado a una condicion de equilibrio, por lo que se optó por reguistrar la distancia entre cada revision con

68 print(f"Sweep {sweep}: distancia = {last_distance:.4f}")

Se redujo el numero de intervalos "bins" de 50 a 20

histogram_edges = np.linspace(0, 10, 21)

No se logró llegar a la condicion de equilibrio, no siquiera aumentando el parametro de tolerancia de 0.2 a 0.5