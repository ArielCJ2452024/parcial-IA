import pygame

def mostrar_pantalla_de_inicio(pantalla):

    pantalla.fill((0,0,0)) #fondo color negro
    fuente = pygame.font.Font(None,36)
    texto=fuente.render("precione para iniciar",True, (255,255,255))
    rect_texto = texto.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2))

    pantalla.blit(texto, rect_texto)
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit
        if evento.type == pygame.KEYDOWN:
                esperando = False  # Sale del bucle cuando se presiona una tecla
    