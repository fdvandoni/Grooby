import pygame
from pygame.locals import *

if not pygame.display.get_init():
    pygame.display.init()

if not pygame.font.get_init():
    pygame.font.init()


class Menu:
    lista = []
    pola = []
    font_size = 24
    font_path = 'imagenes/VCR_OSD_MONO.ttf'
    font = pygame.font.Font
    dest_surface = pygame.Surface
    ilosc_pol = 0
    background_color = (51,51,51)
    text_color =  (255, 255, 153)
    color_selection = (153,102,255)
    item_selection = 0
    position_paste = (0,0)
    menu_width = 0
    menu_height = 0

    class Pole:
        text = ''
        pole = pygame.Surface
        pole_rect = pygame.Rect
        selection_rect = pygame.Rect

    def move_menu(self, top, left):
        self.position_paste = (top,left)

    def set_colors(self, text, selection, background):
        self.background_color = background
        self.text_color =  text
        self.color_selection = selection

    def set_fontsize(self,font_size):
        self.font_size = font_size

    def set_font(self, path):
        self.font_path = path

    def get_position(self):
        return self.item_selection

    def init(self, lista, dest_surface):
        self.lista = lista
        self.dest_surface = dest_surface
        self.ilosc_pol = len(self.lista)
        self.stworz_structure()

    def draw(self,przesun=0):
        if przesun:
            self.item_selection += przesun
            if self.item_selection == -1:
                self.item_selection = self.ilosc_pol - 1
            self.item_selection %= self.ilosc_pol
        menu = pygame.Surface((self.menu_width, self.menu_height))
        menu.fill(self.background_color)
        selection_rect = self.pola[self.item_selection].selection_rect
        pygame.draw.rect(menu,self.color_selection,selection_rect)


        for i in xrange(self.ilosc_pol):
            menu.blit(self.pola[i].pole,self.pola[i].pole_rect)
        self.dest_surface.blit(menu,self.position_paste)
        return self.item_selection

    def stworz_structure(self):
        shift = 0
        self.menu_height = 0
        self.font = pygame.font.Font(self.font_path, self.font_size)
        for i in xrange(self.ilosc_pol):
            self.pola.append(self.Pole())
            self.pola[i].text = self.lista[i]
            self.pola[i].pole = self.font.render(self.pola[i].text, 1, self.text_color)

            self.pola[i].pole_rect = self.pola[i].pole.get_rect()
            shift = int(self.font_size * 0.2)

            height = self.pola[i].pole_rect.height
            self.pola[i].pole_rect.left = shift
            self.pola[i].pole_rect.top = shift+(shift*2+height)*i

            width = self.pola[i].pole_rect.width+shift*2
            height = self.pola[i].pole_rect.height+shift*2
            left = self.pola[i].pole_rect.left-shift
            top = self.pola[i].pole_rect.top-shift

            self.pola[i].selection_rect = (left,top ,width, height)
            if width > self.menu_width:
                    self.menu_width = width
            self.menu_height += height
        x = self.dest_surface.get_rect().centerx - self.menu_width / 2
        y = self.dest_surface.get_rect().centery - self.menu_height / 2
        mx, my = self.position_paste
        self.position_paste = (x+mx, y+my)