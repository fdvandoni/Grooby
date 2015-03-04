#Importa
import pygame
from creacion_sprites import spriteSheet
ANCHO = 600
ALTO = 450

class Manzana(pygame.sprite.Sprite):
    #velocidad
    velocidad_x = 2
    #Vectores de movimiento
    v_sprites_d = []
    #Direccion
    image = None

    def __init__(self, posicion_random):
        pygame.sprite.Sprite.__init__(self)
        #Carga de sprite sheet
        sprite_sheet = spriteSheet("imagenes/manzana.png")
        #Carga de imagenes DERECHAS
        image = sprite_sheet.carga_imagen(0, 0, 30, 30)
        self.v_sprites_d.append(image)
        image = sprite_sheet.carga_imagen(30, 0, 30, 30)
        self.v_sprites_d.append(image)
        image = sprite_sheet.carga_imagen(60, 0, 30, 30)
        self.v_sprites_d.append(image)
        image = sprite_sheet.carga_imagen(90, 0, 30, 30)
        self.v_sprites_d.append(image)
        #Imagen inicial
        self.image = self.v_sprites_d[0]
        #Saca el rect
        self.rect = self.image.get_rect()
        self.rect.centerx = 600
        self.rect.centery = posicion_random
#-------------------------------------------------------------------------

    def update(self):
        #Mueve derecha
        if self.rect.centerx < 601:
            self.pos_x = self.rect.centerx - self.velocidad_x
            frame = (self.pos_x // 30) % len(self.v_sprites_d)
            self.image = self.v_sprites_d[frame]
            self.rect.centerx = self.pos_x
