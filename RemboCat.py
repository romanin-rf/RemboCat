import os
import sys
import json
import pygame
import random
import tempfile
from threading import Thread
# Дополнительные пакеты
import rc_config.rcb as RCB
import rc_LanguagePack.text_main.errors as LP_TEXT_ERRORS
import rc_libs.func.wstr as WORK_STR
import rc_libs.rc_engine as RC_ENGINE
import rc_libs.rc_cryptor as RC_CRYPTOR
import rc_LanguagePack.menu as LP_MENU
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
		TITLE = RCB.root.window.TITLE
		WIDTH = cfgd["ROOT"]["WIDTH"]
		HEIGHT = cfgd["ROOT"]["HEIGHT"]
	class info:
		VERSION = RCB.info.VERSION
		VERSION_INT = RCB.info.VERSION_INT
	class setting:
		LOOK_FPS = cfgd["LOOK_FPS"]
	MAX_FPS = cfgd["MAX_FPS"]

class TEMP:
	class in_ram:
		pass
	if not("rc_TEMP" in os.listdir()):
		os.mkdir((str(os.getcwd()) + f"{prefix_path}rc_TEMP"))
	if not("graphics" in os.listdir("rc_TEMP")):
		os.mkdir((str(os.getcwd()) + f"{prefix_path}rc_TEMP{prefix_path}graphics"))
	class Graphics:
		# Image = tempfile.NamedTemporaryFile(dir = (str(os.getcwd()) + f"{prefix_path}rc_TEMP{prefix_path}graphics"))
		pass
	TimeData = tempfile.NamedTemporaryFile(dir = (str(os.getcwd()) + f"{prefix_path}rc_TEMP"))

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
	global OPERATION, TEMP
	if ("WELCOME" in dir(TEMP.in_ram)) and ((TEMP.in_ram.WELCOME / cfg.MAX_FPS) < 15):
		TEMP.in_ram.WELCOME += 1
	else:
		if not("WELCOME" in dir(TEMP.in_ram)):
			TEMP.in_ram.WELCOME = 0
	
	if not("IMAGE_WORLD" in dir(TEMP.in_ram)):
		TEMP.in_ram.IMAGE_WORLD = pygame.image.load(f'image{prefix_path}world.png')

	if (TEMP.in_ram.WELCOME / cfg.MAX_FPS) < 3:
		RC_ENGINE.create_dialog(rc_root, (25, 123, 166), TEMP.in_ram.IMAGE_WORLD, str(LP_MENU.WELCOME1))
	elif (TEMP.in_ram.WELCOME / cfg.MAX_FPS) < 6:
		RC_ENGINE.create_dialog(rc_root, (25, 123, 166), TEMP.in_ram.IMAGE_WORLD, str(LP_MENU.WELCOME2))
	elif (TEMP.in_ram.WELCOME / cfg.MAX_FPS) < 9:
		RC_ENGINE.create_dialog(rc_root, (25, 123, 166), TEMP.in_ram.IMAGE_WORLD, str(LP_MENU.WELCOME3))
	elif (TEMP.in_ram.WELCOME / cfg.MAX_FPS) < 12:
		RC_ENGINE.create_dialog(rc_root, (25, 123, 166), TEMP.in_ram.IMAGE_WORLD, str(LP_MENU.WELCOME4))
	elif (TEMP.in_ram.WELCOME / cfg.MAX_FPS) < 15:
		RC_ENGINE.create_dialog(rc_root, (25, 123, 166), TEMP.in_ram.IMAGE_WORLD, str(LP_MENU.WELCOME5))
	else:
		pass

# Переменые для определения менюшки
OPERATION = menu

# Инициализация движка
RC_ENGINE.init(cfg.window.WIDTH, cfg.window.HEIGHT)
if "-debag" in sys.argv:
	WORK_out_user_commands = True
	def out_user_commands():
		global cfg, rc_root, rc_clock
		while WORK_out_user_commands:
			command = str(input(">>> "))
			try:
				out = eval(command)
			except:
				try:
					out = exec(command)
				except:
					out = "Error command..."
			print(out)
	Thread(target = out_user_commands, args = (), daemon = True).start()

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
		RC_ENGINE.fps_looker(rc_root, rc_clock, (0, 0))
	OPERATION()
	# Конец
	pygame.display.update()
