import os
import sys
import json
import pygame
import random
from threading import Thread
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
	class setting:
		LOOK_FPS = cfgd["LOOK_FPS"]
	MAX_FPS = cfgd["MAX_FPS"]

class temp:
	running_check_fps = False

if "-debag" in sys.argv:
	print("-" * 70)
	print(f"WINDOW:\n\tTITLE: \"{cfg.window.TITLE}\"\n\tSIZE: {cfg.window.WIDTH}x{cfg.window.HEIGHT}\nINFO:\n\tVERSION: {cfg.info.VERSION} ({cfg.info.VERSION_INT})\nSETTING:\n\tLOOK_FPS: {cfg.setting.LOOK_FPS}\nOTHER:\n\tMAX_FPS: {cfg.MAX_FPS}")
	print("-" * 70)

# Функции для работы
def fps_handler(fps: float):
	if fps >= 100:
		fps_str = str(fps)[:6]
	else:
		fps_str = str(fps)[:5]
	return fps_str

# Основа
rc_root = pygame.display.set_mode((cfg.window.WIDTH, cfg.window.HEIGHT))
pygame.display.set_caption(cfg.window.TITLE + " v" + str(cfg.info.VERSION))
clock = pygame.time.Clock()		

# Менюшки
def menu():
	# ГЛАВНОЕ МЕНЮ
	global OPERATION
	pygame.draw.rect(rc_root, (0, 0, 0), pygame.Rect(25, (cfg.window.HEIGHT - (cfg.window.HEIGHT / 4)), (cfg.window.WIDTH - 50), ((cfg.window.HEIGHT / 4) - 25)))
	rc_root.blit(
		pygame.transform.scale(
			pygame.image.load(
				f'image{prefix_path}world.png'), 
				(
					(int(cfg.window.HEIGHT / 4) - 50), 
					(int(cfg.window.HEIGHT / 4) - 50)
				)), 
				(50, ((cfg.window.HEIGHT - (cfg.window.HEIGHT / 4)) + 15) )
		)

# Переменые для определения менюшки
OPERATION = menu

# Начало работы
running = True
while running:
	clock.tick(cfg.MAX_FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	rc_root.fill((255, 255, 255))
	# Логика работы
	if cfg.setting.LOOK_FPS:
		rc_root.blit(pygame.font.Font(None, 20).render( "FPS: " + str(fps_handler(clock.get_fps())), True, pygame.Color('black')), (0, 0))
	OPERATION()
	# Конец
	pygame.display.update()
