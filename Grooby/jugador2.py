#Importa
import pygame
from creacion_sprites import spriteSheet
ANCHO = 600
ALTO = 400
#Jugador
class Jugador2(pygame.sprite.Sprite):
    #Atributos------------------

    #velocidad
    velocidad_x = 5
    velocidad_y = -5
    #Vectores de movimiento
    v_sprites_d = []
    #Direccion
    image = None

    #Funciones------------------

    def __init__(self, posicionx,posiciony):
        pygame.sprite.Sprite.__init__(self)
        #Carga de sprite sheet
        sprite_sheet = spriteSheet("imagenes/kirbydanio.png")
        image = sprite_sheet.carga_imagen(0, 0, 45, 45)
        self.v_sprites_d.append(image)
        image = sprite_sheet.carga_imagen(45, 0, 45, 45)
        self.v_sprites_d.append(image)
        image = sprite_sheet.carga_imagen(90, 0, 45, 45)
        self.v_sprites_d.append(image)
        self.image = self.v_sprites_d[0]
        #Saca el rect
        self.rect = self.image.get_rect()
        self.rect.centerx = posicionx
        self.rect.centery = posiciony
#-----------------------------------------------------------------------------
    def update(self):
        if self.rect.centerx > 0:
            self.pos_x = self.rect.centerx + self.velocidad_x
            frame = (self.pos_x // 30) % len(self.v_sprites_d)
            self.image = self.v_sprites_d[frame]
            self.rect.centerx = self.pos_x