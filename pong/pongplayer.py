import pygame
#from __future__ import division


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, width=20, height=100, color=(255,255,255)):
       
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.height = height

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.x = x
        self.y = y

    def draw(self, screen):
    	screen.blit(self.image, (self.rect.x, self.rect.y))

class PongPlayer(Block):

	speed = 10

	def __init__(self, x, y):
		Block.__init__(self, x, y)
		self.change_y = 0
		self.score = 0

	def update(self, screen):
		self.draw(screen)
		self.move()
		if self.rect.y > screen.get_height() - self.height:
			self.rect.y = screen.get_height() - self.height 
		elif self.rect.y <= 0:
			self.rect.y = 1

	def move(self):
		self.rect.y += self.change_y

	def change_movement(self, number):
		self.change_y = PongPlayer.speed * number

class UserPlayer(PongPlayer):

	pass


class ComputerPlayer(PongPlayer):

	def compute_movement(self, pong_ball_y):
		if pong_ball_y <= self.rect.y and self.rect.y > 19:
			self.change_movement(-1)
		elif pong_ball_y >= self.rect.y + self.height and self.rect.y < 581:
			self.change_movement(1)
		else:
			self.change_movement(0)


class PongBall(Block):

	speed = 10

	def __init__(self, x=390, y=290, width=20, height=20):
		Block.__init__(self, x, y, width, height)
		self.change_x = 10
		self.change_y = 0

	def update(self, screen):
		self.draw(screen)
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		if not 0 <= self.rect.y < 580:
			self.hit_wall()
		if self.rect.y <= 0: 
			self.rect.y = 1
		elif self.rect.y >= 580:
			self.rect.y = 579

	def hit_wall(self):
		self.change_y *= -1

	def hit_player(self, hit, direction):
		self.change_x *=-1
		# Math to attempt pong ball movement based on paddle hit
		# this shit took way too long
		paddle_y = hit.rect.y
		paddle_center = ((hit.height/2)+paddle_y)
		paddle_end = hit.rect.y + hit.height
		ball_center = ((self.height/2)+self.rect.y)
		
		speed = 0
		
		x = -12
		for i in range(-20, 41, 10):
			
			if paddle_y + i <= self.rect.y <= paddle_y + i + 9:

				speed = x
				break
			x += 2

		x = 2
		for i in range(50, 111, 10):
			
			if paddle_y + i <= self.rect.y <= paddle_y + i + 9:

				speed = x
				break
			x += 2
		
		self.change_y = speed
		if self.rect.y + self.height <= paddle_y or self.rect.y >= paddle_end:
			self.change_y *= -1
			self.rect.x += self.change_x
			self.change_x *= -1

		











