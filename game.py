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

    # заготова сферры

    angle_player = 0
    pr_player = False
    pr_player_left = False
    pr_player_right = False

    mvsp = 3.5  # Скорость курсора
    mvsp_baelle = 4
    spawn_count = 150

    zeit_zaehler = 0

    clock = pygame.time.Clock()
    fps = 50
    time_count = 0

    x = 1
    x2 = 1
    end = 0

    # Все основные константы объявлены
    # Начало цикла для заглавного окна
    while x2 == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    x = 0
                    x2 = 0
                    game = 0

                if event.key == K_SPACE:
                    x2 = 0

                if event.key == K_DOWN and difficult != "Easy":
                    if difficult == "Hard":
                        difficult = "Normal"
                    else:
                        difficult = "Easy"

                if event.key == K_UP and difficult != "Hard":
                    if difficult == "Easy":
                        difficult = "Normal"
                    else:
                        difficult = "Hard"
        # Вверху выбираем уровень сложности. Уровень на английском, так как русские аналоги большие по длине.

        if difficult == "Easy":
            spawn_count = 250
            diff_bg = (0, 255, 0)

        if difficult == "Normal":
            spawn_count = 150
            diff_bg = (255, 255, 0)

        if difficult == "Hard":
            diff_bg = (255, 0, 0)
            spawn_count = 50

        fenster.fill((255, 175, 0))
        text_title = pygame.font.SysFont(None, 125)
        text_subt = pygame.font.SysFont(None, 75)
        text_subt2 = pygame.font.SysFont(None, 25)

        title = text_title.render("Курсор", True, black)
        fenster.blit(title, (50, 50))

        subt1 = text_subt.render("Жми пробел, чтобы начать", True, black, (255, 250, 0))
        subt2 = text_subt.render("Нвжми esc для выхода", True, black, (255, 100, 0))
        subt3 = text_subt.render(difficult, True, black, diff_bg)
        subt4 = text_subt2.render("Используй стрелки, что бы изменить", True, black)
        subt5 = text_subt.render("Слоность:", True, black)

        fenster.blit(subt1, (100, 325))
        fenster.blit(subt2, (100, 400))
        fenster.blit(subt3, (500, 100))
        fenster.blit(subt4, (500, 210))
        fenster.blit(subt5, (500, 10))  # (325, 100))

        pygame.draw.polygon(fenster, black, ((500, 90), (525, 65), (550, 90)))
        pygame.draw.polygon(fenster, black, ((500, 167), (525, 192), (550, 167)))

        pygame.display.update()
        # Вывели все основные надписи
        # Начало основного цикла
        while x == 1:
            time_count += 1  # время
            # print(angle_player)

            if pr_player_left:
                angle_player += 5
            if pr_player_right:
                angle_player -= 5

            if pr_player:
                b = math.cos(
                    math.radians(angle_player)) * mvsp  # Длинна прилижащего катета

                a = math.sin(
                    math.radians(angle_player)) * mvsp  # Длинна противополжного катета

                # if player.top >= 0 and player.bottom <= wh:
                player.top += round(b)
                # if player.left >= 0 and player.right <= ww:
                player.left += round(a)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    x = 0

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        x = 0
                    if event.key == K_UP or event.key == K_w:
                        pr_player = True

                    if event.key == K_LEFT or event.key == K_a:
                        pr_player_left = True

                    if event.key == K_RIGHT or event.key == K_d:
                        pr_player_right = True

                if event.type == KEYUP:
                    if event.key == K_UP or event.key == K_w:
                        pr_player = False
                    if event.key == K_LEFT or event.key == K_a:
                        pr_player_left = False
                    if event.key == K_RIGHT or event.key == K_d:
                        pr_player_right = False
            # обработка нажати
