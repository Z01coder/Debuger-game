import pygame
import random

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("img/map.jpg")

font = pygame.font.SysFont("Digital-7 Mono", 47)

pygame.mixer.music.load("music/dbgr8.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

hit_sound = pygame.mixer.Sound("sounds/explosion.wav")
hit_sound.set_volume(0.3)

pygame.display.set_caption("Ыгра")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_images = [
    pygame.image.load("img/b1.png"),
    pygame.image.load("img/b2.png"),
    pygame.image.load("img/b3.png"),
    pygame.image.load("img/b4.png"),
    pygame.image.load("img/b5.png"),
]

target_img = random.choice(target_images)
target_width = 78
target_height = 78

hits = 0
previous_hits = 0
start_ticks = pygame.time.get_ticks()

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

hits = 0
start_ticks = pygame.time.get_ticks()

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                hits += 1
                target_img = random.choice(target_images)
                hit_sound.play()

    seconds = (pygame.time.get_ticks() - start_ticks) // 1000  # Перевод времени в секунды

    # Если прошло 30 секунд, перезапуск игры
    if seconds >= 30:
        previous_hits = hits
        hits = 0  # Обнуление счётчика попаданий
        start_ticks = pygame.time.get_ticks()

    hits_text = font.render(f"y6pato: {hits}", True, (27, 91, 0))
    previous_hits_text = font.render(f"pekop9: {previous_hits}", True, (27, 91, 0))


    screen.blit(background, (0, 0))
    screen.blit(target_img, (target_x, target_y))
    screen.blit(hits_text, (100, 20))
    screen.blit(previous_hits_text, (SCREEN_WIDTH - previous_hits_text.get_width() - 90, 20))

    pygame.display.update()

pygame.quit()