import pygame
from pongplayer import *
from functions import *

class PongGame():

	def __init__(self, players):

		if players == 1:
			self.player1 = ComputerPlayer(30, 250)
			self.mode = 1
		else:	
			self.player1 = UserPlayer(30, 250)
			self.mode = 2
		self.player2 = player2=UserPlayer(750, 250)
		self.players = pygame.sprite.Group(self.player1, self.player2)
		self.pong_ball = PongBall()
		self.gameover = False

	def update(self, screen):

		self.play_game(screen)
		if not (self.player1.score == 10 or self.player2.score == 10):
			self.pong_ball.update(screen)
		else:
			text_to_screen(screen, "(Space)", 400, 300)
			self.gameover=True
		self.check_ball()

	def play_game(self, screen):
		text_to_screen(screen, "%s     %s" % (self.player1.score, self.player2.score), 400, 100, 100)
		self.players.update(screen)
		
		if self.mode == 1:
			self.player1.compute_movement(self.pong_ball.rect.y)
			
		hits = pygame.sprite.spritecollide(self.pong_ball, self.players, False)
		for hit in hits:
			
			if hit == self.player1:	
				self.pong_ball.hit_player(hit, 1)
			else:
				self.pong_ball.hit_player(hit, -1)

	def update_player_movement(self, player, number):
		player.change_movement(number)

	def check_ball(self):
		if -100 > self.pong_ball.rect.x:
			self.player2.score += 1
			self.pong_ball.rect.x = 300
			self.pong_ball.change_x *= -1
		elif 880 < self.pong_ball.rect.x:
			self.player1.score += 1
			self.pong_ball.rect.x = 400
			self.pong_ball.change_x *= -1
		
def new_game(players = 1):
	return PongGame(players)







