import pygame
import random

class NPC:
    def __init__(self, x, y, color, tamano_celda, laberinto):
        self.x = x
        self.y = y
        self.color = color
        self.tamano_celda = tamano_celda
        self.laberinto = laberinto

    def mover(self):
        # Posibles direcciones: arriba, abajo, izquierda, derecha
        direcciones = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(direcciones)  # Mezclar direcciones para moverse aleatoriamente

        for dx, dy in direcciones:
            nueva_x, nueva_y = self.x + dx, self.y + dy
            if self.laberinto[nueva_y][nueva_x] == 0:  # Verificar si no es una pared
                self.x, self.y = nueva_x, nueva_y
                break  # Mueve solo en la primera dirección válida encontrada

    def dibujar(self, pantalla):
        pygame.draw.rect(
            pantalla, self.color, 
            (self.x * self.tamano_celda, self.y * self.tamano_celda, self.tamano_celda, self.tamano_celda)
        )
