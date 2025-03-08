import pygame
from pantalla_inicio_final import mostrar_pantalla_de_inicio

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 600, 400
TAMANO_CELDA = 40
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laberinto en Pygame")

mostrar_pantalla_de_inicio(pantalla)
# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Mapa del laberinto (1 = pared, 0 = camino)
laberinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Posición inicial del jugador
jugador_x, jugador_y = 1, 1

# Bucle del juego
reloj = pygame.time.Clock()
jugando = True

while jugando:
    pantalla.fill(BLANCO)
    
    # Capturar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
    
    # Capturar teclas presionadas
    teclas = pygame.key.get_pressed()
    
    # Movimiento del jugador
    nueva_x, nueva_y = jugador_x, jugador_y
    if teclas[pygame.K_UP]:
        nueva_y -= 1
    if teclas[pygame.K_DOWN]:
        nueva_y += 1
    if teclas[pygame.K_LEFT]:
        nueva_x -= 1
    if teclas[pygame.K_RIGHT]:
        nueva_x += 1

    # Verificar colisión con paredes
    if laberinto[nueva_y][nueva_x] == 0:
        jugador_x, jugador_y = nueva_x, nueva_y

    # Dibujar el laberinto
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            if laberinto[fila][columna] == 1:
                pygame.draw.rect(
                    pantalla, NEGRO, 
                    (columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                )

    # Dibujar el jugador
    pygame.draw.rect(
        pantalla, AZUL, 
        (jugador_x * TAMANO_CELDA, jugador_y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
    )

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(20)

pygame.quit()
