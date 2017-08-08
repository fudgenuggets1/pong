import pygame
from player_input import player_input
from game import new_game
from functions import text_to_screen
from pongplayer import UserPlayer

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
FPS = 60
total_frames = 0

# Making my own buttons gdi
class Button():

	def __init__(self, msg, x, y, w, h, action, action_index = 1, color = (128, 128, 128), highlight=(200, 200, 200)):

		self.msg = msg
		self.x, self.y = x, y
		self.w, self.h = w, h
		self.regular_color, self.highlight_color = color, highlight
		self.action = action
		self.color = self.regular_color
		self.mouse_on = False
		self.action_index = action_index

	@staticmethod
	def update(screen, list):

		for button in list:
			pygame.draw.rect(screen, button.color, (button.x, button.y, button.w, button.h))       
			x = button.w / 2
			y = button.h / 2
			text_to_screen(screen, button.msg, button.x+x, button.y+y, 20)

	def mouse_over(self):
		self.color = self.highlight_color
		self.mouse_on = True
	def mouse_off(self):
		self.color = self.regular_color
		self.mouse_on = False
	def do_action(self):
		global home
		home.pong_game = self.action(self.action_index)

# Home screen
class HomeScreen():

	def __init__(self):
		self.pong_game = False
		buttons = [
			["1 Player", 200, 200, 125, 50, new_game, 1],
			["2 Player", 475, 200, 125, 50, new_game, 2],
		]
		self.buttons = []
		for item in buttons:
			self.buttons.append(Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

	def update(self, screen):
		if not self.pong_game:
			Button.update(screen, self.buttons)
		else:
			self.pong_game.update(screen)

	def reset(self):
		self.pong_game = False

home = HomeScreen()

while True:

	screen.fill((150,150,150))

	player_input(screen, home)
	home.update(screen)

	pygame.display.set_caption("Pong")
	pygame.display.flip()
	clock.tick(FPS)
	total_frames += 1