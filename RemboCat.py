import os
import sys
import json
import pygame
import random
import rc_config.rcb as rcb
# Инициализация
pygame.init()
pygame.mixer.init()

# Подговтовка
if sys.platform == "win32":
	prefix_path = "\\"
elif sys.platform == "linux":
	prefix_path = "/"
else:
	exit()

# Загрузка конфигураций
with open(f"rc_config{prefix_path}config_basic.cfg") as cfgd_file:
	cfgd = json.load(cfgd_file)

# Конфирурации
class cfg:
	class window:
		TITLE = rcb.root.window.TITLE
		WIDTH = rcb.root.window.WIDTH
		HEIGHT = rcb.root.window.HEIGHT
	MAX_FPS = cfgd["MAX_FPS"]

# Основа
rc_root = pygame.display.set_mode((cfg.window.WIDTH, cfg.window.HEIGHT))
pygame.display.set_caption(cfg.window.TITLE)
clock = pygame.time.Clock()

running = True
while running:
	clock.tick(cfg.MAX_FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	rc_root.fill((255, 255, 255))
	pygame.display.flip()
