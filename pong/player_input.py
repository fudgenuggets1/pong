import pygame, sys

def player_input(screen, home):

	Mpos = pygame.mouse.get_pos()
	mouse_x = Mpos[0] 
	mouse_y = Mpos[1]
	#print Mpos

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()

		# I love making spaghetti 
		if home.pong_game:	
			pong_game = home.pong_game
			player1 = pong_game.player1
			player2 = pong_game.player2
			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_DOWN:
					pong_game.update_player_movement(player2, 1)
				elif event.key == pygame.K_UP:
					pong_game.update_player_movement(player2, -1)
				
				if event.key == pygame.K_s:
					pong_game.update_player_movement(player1, 1)
				elif event.key == pygame.K_w:
					pong_game.update_player_movement(player1, -1)

				# gameover
				if event.key == pygame.K_SPACE and pong_game.gameover:
					home.reset()
					return
			
			elif event.type == pygame.KEYUP:
				
				if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
					pong_game.update_player_movement(player2, 0)
				if event.key == pygame.K_s or event.key == pygame.K_w:
					pong_game.update_player_movement(player1, 0)

			state = pygame.key.get_pressed()
			if not state[pygame.K_DOWN] and not state[pygame.K_UP]:
				pong_game.update_player_movement(player2, 0)
			if state[pygame.K_DOWN]:
				pong_game.update_player_movement(player2, 1)
			if state[pygame.K_UP]:
				pong_game.update_player_movement(player2, -1)
			
			if not state[pygame.K_s] and not state[pygame.K_w]:
				pong_game.update_player_movement(player1, 0)
			if state[pygame.K_s]:
				pong_game.update_player_movement(player1, 1)
			if state[pygame.K_w]:
				pong_game.update_player_movement(player1, -1)

		elif home.buttons:
			for button in home.buttons:
				if button.x+button.w > mouse_x > button.x and button.y+button.h > mouse_y > button.y:
					button.mouse_over()
				else:
					button.mouse_off()

			if event.type == pygame.MOUSEBUTTONDOWN:
				for button in home.buttons:
					if button.mouse_on:
						button.do_action()








