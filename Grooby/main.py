#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Modulos
import sys, pygame
from time import sleep
from pygame.locals import *
from jugador import *
from jugador2 import *
from enemigo1 import *
from enemigo2 import *
from enemigo3 import *
from enemigo4 import *
from enemigo5 import *
from estrella import *
from manzana import *
from menu import *
from vida import *
import random
#------------------------------------------------------------------------------
def carga_imagen(archivo, transparente=False):
    try: imagen = pygame.image.load(archivo)
    except pygame.error, message:
        raise SystemExit, message
    imagen = imagen.convert()
    if transparente:
        color = imagen.get_at((0,0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen

def mostrartexto(texto, posicion_x, posicion_y, color=(0,0,0)):
    #Cargamos la fuente para mostrar en pantalla
    fuente = pygame.font.Font('imagenes/VCR_OSD_MONO.ttf',25)
    #el texto lo pasamos por la fuente elegida
    salida = pygame.font.Font.render(fuente, texto ,1,color)
    #creamos un sprite para mostrarlo en pantalla
    salida_rect = salida.get_rect()
    #al sprite con el texto lo ponemos en una posicion
    #dentro de la pantalla
    salida_rect.centerx = posicion_x
    salida_rect.centery = posicion_y
    return salida,salida_rect

def mostrarpuntos(puntos, posicion_x, posicion_y, color=(0,0,0)):
    #Cargamos la fuente para mostrar en pantalla
    fuente = pygame.font.Font('imagenes/VCR_OSD_MONO.ttf',25)
    #el texto lo pasamos por la fuente elegida
    salida = pygame.font.Font.render(fuente,str(puntos),1,color)
    #creamos un sprite para mostrarlo en pantalla
    salida_rect = salida.get_rect()
    #al sprite con el texto lo ponemos en una posicion
    #dentro de la pantalla
    salida_rect.centerx = posicion_x
    salida_rect.centery = posicion_y
    return salida,salida_rect

#------------------------------------------------------------------------------
def main():
    #Pantalla
    pantalla = pygame.display.set_mode((600, 450), pygame.RESIZABLE)
    pygame.display.set_caption("Grooby Game")
    #Relo
    reloj = pygame.time.Clock()
    #Fondo
    imagen_fondo = carga_imagen('imagenes/mapa2.png')
    imagen_estrella = carga_imagen('imagenes/estrella1.png')
    color = imagen_estrella.get_at((0,0))
    imagen_estrella.set_colorkey(color, RLEACCEL)
    imagenPresent = pygame.image.load('imagenes/presentacion.png')
    rectanguloPresent = imagenPresent.get_rect()
    rectanguloPresent.top = 60
    rectanguloPresent.left = 80
    #jugador-enemigos
    jugador_grupo = pygame.sprite.Group()
    jugador_grupo = pygame.sprite.RenderPlain()
    all_sprites = pygame.sprite.Group()
    jugador = Jugador()
    jugador_grupo.add(jugador)
    all_sprites = pygame.sprite.RenderPlain()
    estrella_group = pygame.sprite.RenderPlain()
    manzana_group = pygame.sprite.RenderPlain()
    partidaEnMarcha = True
    #Menu
    menu = Menu()
    menu.set_colors((103,37,52), (255,133,154), (255,230,236))
    menu.init(['Comenzar','Controles','Salir'], pantalla)
    menu.move_menu(180, 330)
    pygame.mixer.music.load("musica/intro.mp3")
    pygame.mixer.music.play(1)
    Music_pause=False
    bucleprincipal=False
    while not bucleprincipal:
        entrarAlJuego = False
        while not entrarAlJuego:
            pantalla.fill( (0,0,0) )
            pantalla.blit(imagenPresent, (0,0))
            menu.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_UP:
                        menu.draw(-1)
                    if event.key == K_DOWN:
                        menu.draw(1)
                    if event.key == K_RETURN:
                        if menu.get_position() == 1:
                            finpausa = False
                            while not finpausa:
                                controls=carga_imagen('imagenes/Controles.png')
                                pantalla.blit(controls, (0,0))
                                pygame.display.flip()
                                pygame.time.wait(100)
                                for event in pygame.event.get(KEYUP):
                                    if event.key == K_RETURN:
                                        finpausa = True
                        if menu.get_position() == 2:
                            pygame.display.quit()
                            sys.exit()
                        if menu.get_position() == 0:
                            pygame.mixer.music.fadeout(1)
                            pygame.mixer.music.load("musica/groovy.mp3")
                            pygame.mixer.music.play()
                            sleep(3)
                            entrarAlJuego = True
                    if event.key == pygame.K_SPACE:
                        if Music_pause == True:
                            pygame.mixer.music.set_volume(1)
                            Music_pause = False
                        else:
                            pygame.mixer.music.set_volume(0)
                            Music_pause = True
                    if event.key == pygame.K_a:
                            pausafin2=False
                            while not pausafin2:
                                fin=carga_imagen('imagenes/acercade.png')
                                pantalla.blit(fin, (0,0))
                                pygame.display.flip()
                                pygame.time.wait(100)
                                for event in pygame.event.get(KEYUP):
                                    if event.key == K_RETURN:
                                        pausafin2 = True
                    if event.key == K_ESCAPE:
                        pygame.display.quit()
                        sys.exit()
                    pygame.display.update()
                elif event.type == QUIT:
                    pygame.display.quit()
                    sys.exit()
#------------------------------------------------------------------------------
        finhistoria = False
        pygame.mixer.music.fadeout(1)
        pygame.mixer.music.load("musica/historia.mp3")
        pygame.mixer.music.play(1)
        while not finhistoria:
                historia=carga_imagen('imagenes/historia.png')
                pantalla.blit(historia, (0,0))
                pygame.display.flip()
                pygame.time.wait(100)
                for event in pygame.event.get(KEYUP):
                    if event.key == K_RETURN:
                        pygame.mixer.music.stop()
                        finhistoria = True
                    if event.key == pygame.K_SPACE:
                        if Music_pause == True:
                            pygame.mixer.music.set_volume(1)
                            Music_pause = False
                        else:
                            pygame.mixer.music.set_volume(0)
                            Music_pause = True
#------------------------------------------------------------------------------
        Music_pause=False
        terminado = False
        velocidad=0
        n=1
        puntos=1
        cantestrellas=0
        movpantalla=0
        jugador.rect.centery=450/2
        jugador.rect.centerx=30
        pygame.mixer.music.load("musica/Green Greens.mp3")
        pygame.mixer.music.play(2)
        pygame.mixer.music.queue("musica/Vegetable Valley.mp3")
        while not terminado:
            keyy = pygame.key.get_pressed()
        # ---- Comprobar acciones del usuario ----
            key = pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminado = True
                    partidaEnMarcha = False
            time = reloj.tick(50)
            for boton in pygame.event.get():
                if boton.type == QUIT:
                    sys.exit(0)
                if boton.type == pygame.KEYUP:
                    if boton.key == pygame.K_RETURN:
                        finpausa = False
                        pausa_jug, pausa_jug_rect = mostrartexto('PAUSA', 300, 100)
                        pantalla.blit(pausa_jug, pausa_jug_rect)
                        pygame.display.flip()
                        while not finpausa:
                            pygame.time.wait(100)
                            for event in pygame.event.get(KEYUP):
                                if event.key == K_RETURN:
                                    finpausa = True
                    if boton.key == pygame.K_SPACE:
                        if Music_pause == True:
                            pygame.mixer.music.set_volume(1)
                            Music_pause = False
                        else:
                            pygame.mixer.music.set_volume(0)
                            Music_pause = True
                    if boton.key == K_ESCAPE:
                        pausaexit= False
                        pygame.mixer.music.set_volume(0)
                        pausa_jug, pausa_jug_rect = mostrartexto('Seguro que Desea Abandonar el Juego?', 300, 100)
                        pausa1_jug, pausa1_jug_rect = mostrartexto('S -Si     N - No', 300, 150)
                        pantalla.blit(pausa_jug, pausa_jug_rect)
                        pantalla.blit(pausa1_jug, pausa1_jug_rect)
                        pygame.display.flip()
                        while not pausaexit:
                            pygame.time.wait(100)
                            for event in pygame.event.get(KEYUP):
                                if event.key == K_s:
                                    pygame.display.quit()
                                    sys.exit()
                                if event.key == K_n:
                                    pygame.mixer.music.set_volume(1)
                                    pausaexit=True
#------------------------------------------------------------------------------
            if (puntos==500*n):
                velocidad+=1
                n=n+1
            if ((puntos % 200 == 0)or(puntos % 100 == 0)):
                nmr_random=random.randint(30,420)
                enemigo1 = Enemigo1(nmr_random, velocidad)
                all_sprites.add(enemigo1)               
            if ((puntos % 100 == 0)or(puntos  == 50)):
                nmr_random=random.randint(30,420)
                enemigo2 = Enemigo2(nmr_random,velocidad)
                all_sprites.add(enemigo2)
            if ((puntos % 300 == 0)or(puntos == 10)):
                nmr_random=random.randint(30,420)
                enemigo3 = Enemigo3(nmr_random,velocidad)
                all_sprites.add(enemigo3)
            if ((puntos % 100 == 0)or(puntos % 80 == 0)):
                nmr_random=random.randint(30,420)
                enemigo4 = Enemigo4(nmr_random,velocidad)
                all_sprites.add(enemigo4)
            if ((puntos % 350 == 0)or(puntos  == 400)):
                nmr_random=random.randint(30,420)
                enemigo5 = Enemigo5(nmr_random,velocidad)
                all_sprites.add(enemigo5)
            if (puntos % 703 == 0):
                nmr_random=random.randint(30,420)
                estrella = Estrella(nmr_random)
                estrella_group.add(estrella)
            if (puntos % 504 == 0):
                nmr_random=random.randint(30,420)
                manzana = Manzana(nmr_random)
                manzana_group.add(manzana)
#------------------------------------------------------------------------------
            if pygame.sprite.spritecollide(jugador, manzana_group, False):
                jugador.vidaa(1)
                manzana_group.remove(manzana)                
# agregado 2/3------
            if pygame.sprite.spritecollide(jugador, estrella_group, False):
                estrella_group.remove(estrella)
                cantestrellas=cantestrellas+1
            if pygame.sprite.spritecollide(jugador, all_sprites, False):
                if (jugador.vida > 0):#EN CASO DE SEGUIR VIVO
                    posicionx=jugador.rect.centerx
                    posiciony=jugador.rect.centery
                    n = 0
                    while (n<12):
                        jugador2=Jugador2(posicionx,posiciony)
                        pantalla.blit(jugador2.image, jugador2.rect)
                        pygame.display.flip()
                        jugador2.update()
                        pygame.time.delay(3)
                        n+=1
                    jugador.vidaa(0)
                else:#EN CASO DE MUERTE
                    pausa_jug, pausa_jug_rect = mostrartexto('FIN DEL JUEGO', 300, 50)
                    pausa1_jug, pausa1_jug_rect = mostrartexto('Su Puntaje es de:'+str(puntos), 300, 100)
                    pausa4_jug, pausa4_jug_rect = mostrartexto('Recolecto '+str(cantestrellas)+' Estrellas', 300, 150)
                    pausa2_jug, pausa2_jug_rect = mostrartexto('Precione Enter para Volver a Comenzar', 300, 250)
                    pausa3_jug, pausa3_jug_rect = mostrartexto('ESC / Exit', 500, 400)
                    posicionx=jugador.rect.centerx
                    posiciony=jugador.rect.centery
                    jugador2=Jugador2(posicionx,posiciony)
                    pausaexit=False
                    m=0
                    pygame.mixer.music.load("musica/dies.wav")
                    pygame.mixer.music.play(1)
                    while not pausaexit:
                        pantalla.blit(imagen_fondo,(-(movpantalla),0))
                        all_sprites.update()
                        jugador2.update()
                        all_sprites.draw(pantalla)
                        if (m<=30):
                            pantalla.blit(jugador2.image, jugador2.rect)
                            m=m+1
                        pantalla.blit(pausa_jug, pausa_jug_rect)
                        pantalla.blit(pausa1_jug, pausa1_jug_rect)
                        pantalla.blit(pausa2_jug, pausa2_jug_rect)
                        pantalla.blit(pausa3_jug, pausa3_jug_rect)
                        pantalla.blit(pausa4_jug, pausa4_jug_rect)
                        pygame.display.flip()
                        pygame.time.delay(50)
                        for event in pygame.event.get(KEYUP):
                            if event.key == K_RETURN:
                                pausaexit=True
                                puntos=0
                                movpantalla=0
                                cantestrellas=0
                                velocidad=2
                                all_sprites.empty()
                                estrella_group.empty()
                                jugador.vida = 100
                                jugador.rect.centery=450/2
                                jugador.rect.centerx=30
                                pygame.mixer.music.load("Musica/Green Greens.mp3")
                                pygame.mixer.music.play(2)
                                pygame.mixer.music.queue("musica/Vegetable Valley.mp3")
                            if event.key == K_ESCAPE:
                                pausaexit=True
                                terminado=True
                                all_sprites.empty()
                                estrella_group.empty()
                                pygame.mixer.music.load("musica/intro.mp3")
                                pygame.mixer.music.play(1)
                    
            
#------------------------------------------------------------------------------
            if (cantestrellas==20):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("musica/historia.mp3")
                pygame.mixer.music.play(1)
                all_sprites.empty()
                estrella_group.empty()
                fin=carga_imagen('imagenes/finpantalla.png')
                pausa1_jug, pausa1_jug_rect = mostrartexto('Felicidades!!', 200, 150)
                pausa2_jug, pausa2_jug_rect = mostrartexto('a Recuperado Todas las Estrellas', 320, 200)
                pausa4_jug, pausa4_jug_rect = mostrartexto('Su Puntaje Final es de:'+str(puntos), 300, 320)
                pausa3_jug, pausa3_jug_rect = mostrartexto('ENTER / Sig', 500, 420)
                pausa5_jug, pausa5_jug_rect = mostrartexto('A / Acerca', 100, 420)
                pantalla.blit(fin, (0,0))
                pantalla.blit(pausa1_jug, pausa1_jug_rect)
                pantalla.blit(pausa2_jug, pausa2_jug_rect)
                pantalla.blit(pausa3_jug, pausa3_jug_rect)
                pantalla.blit(pausa4_jug, pausa4_jug_rect)
                pantalla.blit(pausa5_jug, pausa5_jug_rect)
                pygame.display.flip()
                pygame.time.wait(100)
                pausafin=False
                while not pausafin:
                    for event in pygame.event.get(KEYUP):
                        if event.key == K_RETURN:
                            pygame.mixer.music.stop()
                            pausafin = True
                            terminado=True
                        if event.key == pygame.K_a:
                            pausafin2=False
                            while not pausafin2:
                                fin=carga_imagen('imagenes/acercade.png')
                                pantalla.blit(fin, (0,0))
                                pygame.display.flip()
                                pygame.time.wait(100)
                                for event in pygame.event.get(KEYUP):
                                    if event.key == K_RETURN:
                                        pygame.mixer.music.stop()
                                        pausafin = True
                                        terminado=True
                                        pausafin2 = True
#------------------------------------------------------------------------------
#agregado 2/3
            barrahp = Vida()
            barrahp.actualizar(jugador.vida)
            jugador.movimiento(keyy)
            jugador.update()
            jugador_grupo.update()
            estrella_group.update()
            manzana_group.update()
            all_sprites.update()
            puntos = puntos + 1
            movpantalla = movpantalla + 1
            puntos_jug, puntos_jug_rect = mostrarpuntos(puntos, 550, 30)
            puntos2_jug, puntos2_jug_rect = mostrartexto('x '+str(cantestrellas), 80, 30)
            if movpantalla>3346:
                movpantalla = 0
            pantalla.blit(imagen_fondo,(-(movpantalla),0))
            if (not(pygame.sprite.spritecollide(jugador, all_sprites, False))): #SI NO ESTA CHOCANDO CON ALGO
                pantalla.blit(jugador.image, jugador.rect)
            estrella_group.draw(pantalla)
            manzana_group.draw(pantalla)
            all_sprites.draw(pantalla)
            pantalla.blit(imagen_estrella, (10, 10))
            pantalla.blit(puntos_jug,puntos_jug_rect)
            pantalla.blit(puntos2_jug,puntos2_jug_rect)
            pantalla.blit(barrahp.imagen,(300,30)) 
            pygame.display.flip()
        all_sprites.empty()
    pygame.quit()

if __name__ == '__main__':
        pygame.init()
        main()