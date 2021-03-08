import os
import sys
import json
import pygame
import random
import rc_config.rcb as rcb
import rc_LanguagePack.text_main.errors as LP_TEXT_ERRORS
# Инициализация
pygame.init()
pygame.mixer.init()

# Дополнительная настройка
if sys.platform == "win32":
	prefix_path = "\\"
	import ctypes
elif sys.platform == "linux":
	prefix_path = "/"
else:
	exit()

# Загрузка конфигураций
try:
	with open(f"rc_config{prefix_path}config_basic.cfg") as cfgd_file:
		cfgd = json.load(cfgd_file)
except:
	if sys.platform == "win32":
		ctypes.windll.user32.MessageBoxW(0, LP_TEXT_ERRORS.ERROR_LOAD_CONFIG_FILE[1], LP_TEXT_ERRORS.ERROR_LOAD_CONFIG_FILE[0], LP_TEXT_ERRORS.ERROR_LOAD_CONFIG_FILE[3])
	raise OSError(LP_TEXT_ERRORS.ERROR_LOAD_CONFIG_FILE[1])

# Конфирурации
class cfg:
	class window:
		TITLE = rcb.root.window.TITLE
		WIDTH = cfgd["ROOT"]["WIDTH"]
		HEIGHT = cfgd["ROOT"]["HEIGHT"]
	class info:
		VERSION = rcb.info.VERSION
		VERSION_INT = rcb.info.VERSION_INT
	MAX_FPS = cfgd["MAX_FPS"]

if "-debag" in sys.argv:
	print(f"WINDOW:\n\tTITLE: \"{cfg.window.TITLE}\"\n\tSIZE: {cfg.window.WIDTH}x{cfg.window.HEIGHT}\nINFO:\n\tVERSION: {cfg.info.VERSION} ({cfg.info.VERSION_INT})")

# Основа
rc_root = pygame.display.set_mode((cfg.window.WIDTH, cfg.window.HEIGHT))
pygame.display.set_caption(cfg.window.TITLE + " v" + str(cfg.info.VERSION))
clock = pygame.time.Clock()

running = True
while running:
	clock.tick(cfg.MAX_FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	rc_root.fill((255, 255, 255))
	pygame.display.flip()
