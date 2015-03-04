'''
Created on 3/3/2015

@author: akibara
'''
import pygame
from pygame.locals import *
from creacion_sprites import *
ANCHO = 600
ALTO = 400
class Vida(pygame.sprite.Sprite):
    '''
    Barra de vida
    '''   
    #Vector de barras de vida
    sprites_barra = []

    def __init__(self):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        #Carga de sprite sheet
        sprite_sheet = spriteSheet("imagenes/vida.png")
        #Carga de imagen LLENA
        imagen = sprite_sheet.carga_imagen(0, 0, 14, 28)
        self.sprites_barra.append(imagen)
        #Carga de imagen 75%
        imagen = sprite_sheet.carga_imagen(16, 0, 14, 28)
        self.sprites_barra.append(imagen)
        #Carga de imagen 50%
        imagen = sprite_sheet.carga_imagen(32, 0, 14, 28)
        self.sprites_barra.append(imagen)
        #Carga de imagen 25%
        imagen = sprite_sheet.carga_imagen(48, 0, 14, 28)
        self.sprites_barra.append(imagen)
        #Imagen inicial
        self.imagen = self.sprites_barra[0]
        
    def actualizar(self, vida):
        if (vida == 100):
            self.imagen = self.sprites_barra[0]
        elif(vida > 75):
            self.imagen = self.sprites_barra[1]
        elif(vida > 50):
            self.imagen = self.sprites_barra[2]
        elif(vida > 0):
            self.imagen = self.sprites_barra[3]
        