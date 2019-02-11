# Zeit wird gezaehlt
import math
import pygame
import random
import time
from pygame.locals import *

pygame.init()

# bg = (255, 255, 255)
bg = (20, 20, 50)
black = (0, 0, 0)

diff_bg = (255, 255, 0)

ww = 800
wh = 600

fenster = pygame.display.set_mode((ww, wh), FULLSCREEN)
pygame.mouse.set_visible(0)
fenster.fill(bg)
pygame.display.set_caption("Не получай урон от кужков!")

pygame.display.update()

spieler = pygame.image.load("player_1.png")
# Загружаем игрока
player_x = ww / 2
player_y = wh / 2
player = pygame.Rect(player_x, player_y, spieler.get_rect().width, spieler.get_rect().height)

pygame.mixer.music.load("noise.mp3")  # добавим музыку

difficult = "Normal"
hels = 1  # количество жизней
game = True  # позволит в будущем выйти из игры
while game == True:
    ball_rot = pygame.image.load("ball_rot.png")
    rot_rect = pygame.Rect(random.randint(0, ww - ball_rot.get_rect().width),
                           random.randint(0, wh - ball_rot.get_rect().height), ball_rot.get_rect().width,
                           ball_rot.get_rect().height)

    ball_gruen = pygame.image.load("ball_gruen.png")
    gruen_rect = pygame.Rect(random.randint(0, ww - ball_gruen.get_rect().width),
                             random.randint(0, wh - ball_gruen.get_rect().height), ball_gruen.get_rect().width,
                             ball_gruen.get_rect().height)

    ball_blau = pygame.image.load("ball_blau.png")
    blau_rect = pygame.Rect(random.randint(0, ww - ball_blau.get_rect().width),
                            random.randint(0, wh - ball_blau.get_rect().height), ball_blau.get_rect().width,
                            ball_blau.get_rect().height)

    explosion = pygame.image.load("explosion.png")

    angle_rot = random.randint(0, 360)
    angle_gruen = random.randint(0, 360)
    angle_blau = random.randint(0, 360)

    bilder_baelle = [ball_rot, ball_gruen, ball_blau]
    baelle = [rot_rect, gruen_rect, blau_rect]
    angle_baelle = [angle_rot, angle_gruen, angle_blau]

    # заготова сфер