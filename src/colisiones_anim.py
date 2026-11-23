# Simulación de colisiones de partículas con Pygame y Pymunk
# para motivos ilustrativos

import math
import random
from pathlib import Path

import pygame
import pymunk
from PIL import Image, ImageSequence


# Dimensiones de la ventana en píxeles y propiedades de las partículas.
ANCHO, ALTO = 800, 600
CANTIDAD = 100
RADIO = 12
# El motor de física avanza en intervalos fijos de 1/120 segundos.
PASO_FISICA = 1 / 120
# La ruta se calcula desde este archivo para que no dependa de la carpeta actual.
RUTA_IMAGEN = Path(__file__).resolve().parent.parent / "figures" / "assets" / "walking_man.gif"


def cargar_sprite(ruta):
    """Carga los fotogramas de la imagen y sus duraciones en milisegundos."""
    fotogramas = []
    duraciones = []
    with Image.open(ruta) as imagen:
        for fotograma in ImageSequence.Iterator(imagen):
            # RGBA conserva el color y la transparencia del GIF.
            imagen_rgba = fotograma.convert("RGBA")
            superficie = pygame.image.frombytes(
                imagen_rgba.tobytes(), imagen_rgba.size, "RGBA"
            ).convert_alpha()
            # Cada imagen ocupa el mismo diámetro que su círculo de colisión.
            fotogramas.append(
                pygame.transform.smoothscale(superficie, (RADIO * 2, RADIO * 2))
            )
            # Si el archivo no indica duración, se usan 100 milisegundos.
            duraciones.append(max(1, fotograma.info.get("duration", 100) or 100))
    return fotogramas, duraciones


def main():
    # Prepara la ventana y un reloj que limita la velocidad de dibujo.
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Colisiones de partículas")
    reloj = pygame.time.Clock()

    # Todas las partículas comparten la misma animación y el mismo fotograma.
    fotogramas, duraciones = cargar_sprite(RUTA_IMAGEN)
    indice_fotograma = 0
    tiempo_fotograma = 0
    duracion_total = sum(duraciones)

    # El espacio contiene los cuerpos físicos; no se aplica gravedad.
    espacio = pymunk.Space()
    espacio.gravity = (0, 0)

    # Cuatro segmentos fijos forman los bordes del contenedor.
    paredes = [
        pymunk.Segment(espacio.static_body, inicio, fin, 0)
        for inicio, fin in [
            ((0, 0), (ANCHO, 0)),
            ((ANCHO, 0), (ANCHO, ALTO)),
            ((ANCHO, ALTO), (0, ALTO)),
            ((0, ALTO), (0, 0)),
        ]
    ]
    for pared in paredes:
        # Elasticidad 1 y fricción 0 hacen que los choques sean elásticos.
        pared.elasticity = 1.0
        pared.friction = 0.0
    espacio.add(*paredes)

    particulas = []
    columnas = 10
    filas = 10

    for indice in range(CANTIDAD):
        # Cada partícula tiene masa y momento de inercia de un círculo.
        masa = 1
        momento = pymunk.moment_for_circle(masa, 0, RADIO)
        cuerpo = pymunk.Body(masa, momento)
        # Se distribuyen inicialmente en una cuadrícula de 10 por 10.
        cuerpo.position = (
            (indice % columnas + 0.5) * ANCHO / columnas,
            (indice // columnas + 0.5) * ALTO / filas,
        )

        # Una dirección y rapidez aleatorias determinan la velocidad inicial.
        angulo = random.uniform(0, 2 * math.pi)
        rapidez = random.uniform(60, 150)
        cuerpo.velocity = (
            rapidez * math.cos(angulo),
            rapidez * math.sin(angulo),
        )

        # La forma circular determina las colisiones, no el contorno del GIF.
        forma = pymunk.Circle(cuerpo, RADIO)
        forma.elasticity = 1.0
        forma.friction = 0.0

        # El espacio simula el cuerpo y su forma; la lista permite dibujarlo.
        espacio.add(cuerpo, forma)
        particulas.append(cuerpo)

    acumulado = 0.0
    ejecutando = True

    while ejecutando:
        # Limita el dibujo a 60 FPS y evita saltos grandes en la física.
        tiempo_real = reloj.tick(60)
        tiempo = min(tiempo_real / 1000, 0.1)

        # Avanza el GIF respetando la duración de cada fotograma y lo repite.
        tiempo_fotograma = (tiempo_fotograma + tiempo_real) % duracion_total
        while tiempo_fotograma >= duraciones[indice_fotograma]:
            tiempo_fotograma -= duraciones[indice_fotograma]
            indice_fotograma = (indice_fotograma + 1) % len(fotogramas)
        sprite = fotogramas[indice_fotograma]

        # Detecta cuando se cierra la ventana.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            # Ejecuta los pasos de física necesarios según el tiempo transcurrido.
        acumulado += tiempo
        while acumulado >= PASO_FISICA:
            espacio.step(PASO_FISICA)
            acumulado -= PASO_FISICA

        # Limpia el fondo y dibuja el sprite centrado en cada cuerpo.
        pantalla.fill((24, 28, 35))

        for cuerpo in particulas:
            centro = (round(cuerpo.position.x), round(cuerpo.position.y))
            pantalla.blit(sprite, sprite.get_rect(center=centro))

        # Muestra el fotograma recién dibujado en la ventana.
        pygame.display.flip()

    # Libera los recursos de Pygame al cerrar la ventana.
    pygame.quit()


# Ejecuta la simulación solo cuando este archivo se inicia directamente.
if __name__ == "__main__":
    main()