# This is a sample Python script.
import random
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import sqlite3
import pygame

pygame.init()
pygame.font.init()

Nb_Col = 40
Nb_Row = 30
Cell_Size = 32

screen = pygame.display.set_mode(size=(Nb_Col * Cell_Size, Nb_Row * Cell_Size))
timer = pygame.time.Clock()

class Menu:
    def __init__(self):
        self.menu = pygame.Surface((Nb_Col * Cell_Size, Nb_Row * Cell_Size))

    def draw_menu(self):
        screen.blit(self.menu,(0,0))
        self.menu.fill(pygame.Color("grey"))
        self.Title_rect = pygame.Rect(0, 0, (Nb_Col * Cell_Size), (Nb_Row * Cell_Size)/3)
        pygame.draw.rect(screen, pygame.Color("black"), self.Title_rect)
        self.Run_rect = pygame.Rect(0, (Nb_Row * Cell_Size)/3, (Nb_Col * Cell_Size / 2), (Nb_Row * Cell_Size)/3)
        pygame.draw.rect(screen, pygame.Color("blue"), self.Run_rect)
        self.Amelio_rect = pygame.Rect((Nb_Col * Cell_Size / 2), (Nb_Row * Cell_Size) / 3, (Nb_Col * Cell_Size / 2), (Nb_Row * Cell_Size) / 3)
        pygame.draw.rect(screen, pygame.Color("green"), self.Amelio_rect)
        self.Save_rect = pygame.Rect(0, (Nb_Row * Cell_Size * 2) / 3, (Nb_Col * Cell_Size), (Nb_Row * Cell_Size) / 3)
        pygame.draw.rect(screen, pygame.Color("white"), self.Save_rect)

menu=Menu()
conn = sqlite3.connect('ma_base.db')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color('white'))
    menu.draw_menu()
    pygame.display.update()
    timer = pygame.time.Clock()
