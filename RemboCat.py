import os
import sys
import json
import pygame
import random
from threading import Thread
# Дополнительные пакеты
import rc_config.rcb as rcb
import rc_LanguagePack.text_main.errors as LP_TEXT_ERRORS
import rc_libs.func.wstr as WORK_STR
import rc_libs.rc_engine as RC_ENGINE
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

# Дополнительный костыль
class temp:
	pass

# Для проверки
if "-debag" in sys.argv:
	print("-" * 70)
	print(f"WINDOW:\n\tTITLE: \"{cfg.window.TITLE}\"\n\tSIZE: {cfg.window.WIDTH}x{cfg.window.HEIGHT}\nINFO:\n\tVERSION: {cfg.info.VERSION} ({cfg.info.VERSION_INT})\nSETTING:\n\tLOOK_FPS: {cfg.setting.LOOK_FPS}\nOTHER:\n\tMAX_FPS: {cfg.MAX_FPS}")
	print("-" * 70)

# Основа
rc_root = pygame.display.set_mode((cfg.window.WIDTH, cfg.window.HEIGHT))
pygame.display.set_caption(cfg.window.TITLE + " v" + str(cfg.info.VERSION))
rc_clock = pygame.time.Clock()

# Менюшки
def menu():
	# ГЛАВНОЕ МЕНЮ
	global OPERATION
	RC_ENGINE.create_dialog(rc_root, (25, 123, 166), f'image{prefix_path}world.png', "[ГОЛОС]: Привет, мой друг! Давай познакомню тебя с этим миром! 1234567890-1234567890-123")

# Переменые для определения менюшки
OPERATION = menu

# Инициализация движка
RC_ENGINE.init(cfg.window.WIDTH, cfg.window.HEIGHT)

# Начало работы
running = True
while running:
	rc_clock.tick(cfg.MAX_FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	rc_root.fill((255, 255, 255))
	# Логика работы
	if cfg.setting.LOOK_FPS:
		RC_ENGINE.fps_looker(rc_root, rc_clock,(0, 0))
	OPERATION()
	# Конец
	pygame.display.update()
