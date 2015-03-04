#Importa
import pygame
from pygame.locals import *
from creacion_sprites import spriteSheet
ANCHO = 600
ALTO = 400
#Jugador
class Jugador(pygame.sprite.Sprite):
    #Atributos------------------
    #Vida
    vida = None
    #velocidad
    velocidad_x = 2
    velocidad_y = -3
    #Vectores de movimiento
    v_sprites_d = []
    #Direccion
    image = None
    #Funciones------------------

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Carga de sprite sheet
        sprite_sheet = spriteSheet("imagenes/kirby.png")
        #Carga de imagenes DERECHAS
        image = sprite_sheet.carga_imagen(0, 0, 45, 45)
        self.v_sprites_d.append(image)
        image = sprite_sheet.carga_imagen(45, 0, 45, 45)
        self.v_sprites_d.append(image)
        #Imagen inicial
        self.image = self.v_sprites_d[0]
        #Saca el rect
        self.rect = self.image.get_rect()
        self.rect.centerx = 30
        self.rect.centery = ALTO/2
        self.vida = 100
#-----------------------------------------------------------------------------

    def movimiento(self,keyy):
        if keyy[K_UP]:
        #Mueve arriba
            if self.rect.top >= 2:
                pos_y = self.rect.centery + self.velocidad_y -5
                self.rect.centery = pos_y

    def update(self):
        #Mueve derecha
        if self.rect.centerx < 100:
            self.pos_x = self.rect.centerx + self.velocidad_x
            frame = (self.pos_x // 30) % len(self.v_sprites_d)
            self.image = self.v_sprites_d[frame]
            self.rect.centerx = self.pos_x
        else:
            frame = (self.pos_x // 30) % len(self.v_sprites_d)
            self.image = self.v_sprites_d[frame]
            self.pos_x = self.pos_x + self.velocidad_x
        #Mueve abajo
        if self.rect.centery < 425:
            self.pos_y = self.rect.centery + self.velocidad_y +5
            frame = (self.pos_y // 30) % len(self.v_sprites_d)
            self.image = self.v_sprites_d[frame]
            self.rect.centery = self.pos_y
            
#---------------------------------------------------------------------------------
# VIDA
#---------------------------------------------------------------------------------
    def vidaa(self,op):
        if (op == 1):
            if(self.vida < 100):
                self.vida += 30
                if (self.vida > 100):
                    self.vida = 100
        else:
            self.vida -=3 