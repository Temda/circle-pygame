import pygame
import sys
import random

import math

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")

WHITE = (255, 255, 255)
BG_COLOR = (38, 38, 38)

character_img = pygame.image.load('anime.gif').convert_alpha()
character_img = pygame.transform.scale(character_img, (100, 100))

character_x = 10
character_y = 485
character_change_x = 0
character_change_y = 0
speed = 0.8 # ? ปรับ speed 0.3 กำลังดี

power_sword_x = -100
power_sword_y = -100
power_sword_active = False


score = 0


power_sword_img = pygame.image.load('power_sword.png').convert_alpha() # ? พลังที่ต้องเดินเก็บ
power_sword_img = pygame.transform.scale(power_sword_img, (50, 50))


font = pygame.font.Font('freesansbold.ttf', 32)


sword = pygame.image.load('fire-sword.gif').convert_alpha() # ! ดาบที่หมุนรอบตัว
sword = pygame.transform.scale(sword, (100, 50))

sword_update = pygame.image.load('power_sword_update.png').convert_alpha() # ! ดาบที่หมุนรอบตัว
sword_update = pygame.transform.scale(sword_update, (100, 50))


pygame.mixer.music.load('powers.mp3')
pygame.mixer.music.set_volume(0.2)

# radius = 100
# angle = 0

def show_score(x, y):
    score_display = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_display, (x, y))


def character(x, y, score):
    screen.blit(character_img, (x, y))

    if score > 0 :
        for i in range(score):
            angle = i * (360 / score)

            if score > 10:
                sword_x = x + character_img.get_width()/2 + (70 * math.cos(math.radians(angle))) - sword_update.get_width()/2
                sword_y = y + character_img.get_height()/2 + (70 * math.sin(math.radians(angle))) - sword_update.get_height()/2
                screen.blit(sword_update, (sword_x, sword_y))
            else:
                sword_x = x + character_img.get_width()/2 + (70 * math.cos(math.radians(angle))) - sword.get_width()/2
                sword_y = y + character_img.get_height()/2 + (70 * math.sin(math.radians(angle))) - sword.get_height()/2
                screen.blit(sword, (sword_x, sword_y))


running = True
while running:
    screen.fill(BG_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_change_x = -speed
            elif event.key == pygame.K_RIGHT:
                character_change_x = speed
            elif event.key == pygame.K_UP:
                character_change_y = -speed
            elif event.key == pygame.K_DOWN:
                character_change_y = speed
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                character_change_x = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                character_change_y = 0

    character_x += character_change_x
    character_y += character_change_y

    character_x = max(0, min(screen_width - 100, character_x))
    character_y = max(0, min(screen_height - 100, character_y))

    if not power_sword_active and random.randint(0, 1000) > 995:
        power_sword_x = random.randint(0, screen_width - 50)
        power_sword_y = random.randint(0, screen_height - 50)
        power_sword_active = True

    character_rect = pygame.Rect(character_x, character_y, 100, 100)
    power_sword_rect = pygame.Rect(power_sword_x, power_sword_y, 50, 50)
    if power_sword_active and character_rect.colliderect(power_sword_rect):
        score += 1
        power_sword_active = False
        power_sword_x = -100
        power_sword_y = -100
        pygame.mixer.music.play()


    if power_sword_active:
        screen.blit(power_sword_img, (power_sword_x, power_sword_y))

    character(character_x, character_y, score)

    show_score(10, 10)

    pygame.display.update()


pygame.quit()
sys.exit()