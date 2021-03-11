import pygame

class size:
	class win:
		WIDTH = 1024
		HEIGHT = 768

class settings:
	class pos_dialog:
		pass

def init(WIDTH: int, HEIGHT: int):
	global size, settings
	size.win.HEIGHT = HEIGHT
	size.win.WIDTH = WIDTH
	settings.pos_dialog.RECT =	[
				[25, (size.win.HEIGHT - (size.win.HEIGHT / 4))],
				[(size.win.WIDTH - 50), ((size.win.HEIGHT / 4) - 25)]
			]
	settings.pos_dialog.IMAGE =	[
				[(int(size.win.HEIGHT / 4) - 50), (int(size.win.HEIGHT / 4) - 50)], 
				[50, ((size.win.HEIGHT - (size.win.HEIGHT / 4)) + 15)]
			]
	settings.pos_dialog.TEXT =	[
				[(75 + (int(size.win.HEIGHT / 4) - 50)), ((size.win.HEIGHT - (size.win.HEIGHT / 4)) + 15)]
			]

def fps_looker(root, clock, pos: tuple, color_fg = pygame.Color('black')):
	root.blit(pygame.font.Font(None, 20).render( "FPS: " + str(clock.get_fps())[:6], True, color_fg), pos)

def create_dialog(root, color_bg: tuple, fileicon, text: str, color_fg = pygame.Color('black')):
	pygame.draw.rect(root, color_bg, pygame.Rect(settings.pos_dialog.RECT[0][0], settings.pos_dialog.RECT[0][1], settings.pos_dialog.RECT[1][0], settings.pos_dialog.RECT[1][1]))
	root.blit(pygame.transform.scale(fileicon, (settings.pos_dialog.IMAGE[0][0], settings.pos_dialog.IMAGE[0][1])), (settings.pos_dialog.IMAGE[1][0], settings.pos_dialog.IMAGE[1][1]))
	root.blit(pygame.font.Font(None, 24).render(text, True, color_fg), (settings.pos_dialog.TEXT[0][0], settings.pos_dialog.TEXT[0][1]))