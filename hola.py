import pygame, random, math, time
from pygame import mixer

#Initialize Pygame
switch = True
while switch:
	clock = pygame.time.Clock()
	started_once = "no"
	pygame.init()
	mixer.music.load("start.mp3")
	mixer.music.play()

	#The window
	screen = pygame.display.set_mode((800, 600))

	#Title of the window and icon
	pygame.display.set_caption("Flappy Bird")
	spear1 = pygame.image.load("spear2.png")
	spear2 = pygame.image.load("spear1.png")
	coin = pygame.image.load("coin.png")

	background = pygame.image.load("bg.png")

	#Player and placing the player
	playerImg = pygame.image.load("main.png")
	playerX = 370
	playerY = 20
	playerY_change = 0

	#Placing the obstacles and defining random spawning of them
	spear1X = 800
	spear1Y = random.randrange(200, 570)
	spear2X = spear1X
	spear2Y = spear1Y - 870
	spear11X = 801
	spear11Y = random.randrange(150, 400)
	spear22X = spear11X
	spear22Y = spear11Y - 1600

	def player(x, y):
		screen.blit(playerImg,(int(x), int(y))) #Blit means to draw

	def check(x, y):
		screen.blit(playerImg,(int(x), int(y))) #Blit means to draw
	
	def spear(x, y, x1, y1):
		screen.blit(spear1, (int(x), int(y)))
		screen.blit(spear2, (int(x1), int(y1)))

	def spear_LOL(x, y, x1, y1):
		screen.blit(spear1, (int(x), int(y)))
		screen.blit(spear2, (int(x1), int(y1)))

	start_text = pygame.font.Font("Amatic-bold.ttf", 100)
	def start_screen():
		starting = start_text.render("Welcome to Arup's", True, (100,20,40))
		starting2 = start_text.render("Flap Game!", True, (0,100, 255)) 
		starting1 =start_text.render("PRESS SPACE TO CONTINUE", True, (0,230,0))
		screen.blit(starting2, (235, 200))
		screen.blit(starting, (150, 100))
		screen.blit(starting1, (100, 400))
	
	end_text = pygame.font.Font("dog.ttf", 100)
	def END_SCREEN():
		screen.blit(coin, (310,215))
		score1 = end_text.render(str(x), True, (0,0,0))
		end_over = end_text.render("GAME OVER!", True, (255,0,0))
		end_restart = end_text.render("Press R to restart", True, (0,200,50))
		end_quit = end_text.render("Press Escape to quit", True, (0,0,200))
		screen.blit(end_over, (200, 80))
		screen.blit(end_restart, (120, 330))
		screen.blit(end_quit, (80,430))
		screen.blit(score1, (400, 200))

	score_text = pygame.font.Font("Inkfree.ttf", 64)
	def score_card():
		screen.blit(coin, (15, 20))
		score = score_text.render(str(x), True, (0, 0, 0))
		screen.blit(score, (100, 10))

	running = True
	
	on_start_screen = "yes"
	while on_start_screen == "yes":
		screen.blit(background, (0,0))
		start_screen()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				switch = False
				running = False
				on_start_screen = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					on_start_screen = False
		pygame.display.update()

	mixer.music.stop()
	x = 0 #This is score variable

	mixer.music.load("game.mp3")
	mixer.music.play() 
	game_over = "no"
	while running:

		#All of these define centres of all spears 
		centre_spear1X = (spear1X + (spear1X + 99))/2
		centre_spear1Y = (spear1Y + (spear1Y + 710))/2
		
		centre_spear11X = (spear11X + (spear11X + 99))/2
		centre_spear11Y = (spear11Y + (spear11Y + 710))/2
		
		centre_spear2X = (spear2X + (spear2X + 99))/2
		centre_spear2Y = (spear2Y + (spear2Y + 710))/2
		
		centre_spear22X = (spear22X + (spear22X + 99))/2
		centre_spear22Y = (spear22Y + (spear22Y + 710))/2

		centre_playerX = (playerX + (playerX + 64))/2
		centre_playerY = (playerY + (playerY + 64))/2
#---------------------------------------------------------------------------------------
		
		#These calculate the present distance between the player and the centres of obstacles
		distance1 = math.sqrt((centre_spear2X - centre_playerX)**2 + (centre_spear2Y - centre_playerY)**2)
		distance2 = math.sqrt((centre_spear1X - centre_playerX)**2 + (centre_spear1Y - centre_playerY)**2)
		distance3 = math.sqrt((centre_spear22X - centre_playerX)**2 + (centre_spear22Y - centre_playerY)**2)
		distance4 = math.sqrt((centre_spear11X - centre_playerX)**2 + (centre_spear11Y - centre_playerY)**2)

#----------------------------------------------------------------------------------------
#-------This portion defines the parameters by which the game will stop
		if game_over == "no":
			if centre_playerX > (centre_spear1X - (49.5 + 32)) and (centre_playerX < centre_spear1X + (49.5 +32)):
				#Distance from each obstacle if lesser than 383...GAME OVER
				if distance1 < 383:
					spear1X_change = 0
					spear2X_change = 0
					game_over = "yes"
					mixer.music.stop()
					hit = mixer.Sound("hit.wav")
					hit.play()  

				if distance2 < 383:
					spear1X_change = 0
					spear2X_change = 0
					game_over = "yes"
					mixer.music.stop()
					hit = mixer.Sound("hit.wav")
					hit.play() 			

			if centre_playerX > (centre_spear11X - (49.5 + 32)) and (centre_playerX < centre_spear11X + (49.5 +32)):
				if distance3 < 383:
					spear1X_change = 0
					spear2X_change = 0
					game_over = "yes"	
					mixer.music.stop()
					hit = mixer.Sound("hit.wav")
					hit.play() 

				if distance4 < 383:
					spear1X_change = 0
					spear2X_change = 0
					game_over = "yes"
					mixer.music.stop()
					hit = mixer.Sound("hit.wav")
					hit.play()
			#If the player reaches the end of the screen....GAME OVER
			if playerY >= 540:  
				playerY_change = 0
				spear1X_change = 0 
				spear2X_change = 0
				game_over = "yes"
				mixer.music.stop()
				hit = mixer.Sound("hit.wav")
				hit.play()

	#-------This defines player falling... The higher the value, the faster it falls-----------------------------------
			screen.blit(background, (0,0))
			if game_over == "no":
				playerY_change += 0.1
				playerY += playerY_change
#-------------------------------------------------------------------------------------------------------------------
#-------This defines the pace with which player goes up when he presses up arrow
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					playerY_change += -5.5
#-----------------------------------------------------------------------------------------------------------------
		if game_over == "no":
			if spear1X == 380:
				spear11X = 800
				spear11Y = random.randrange(200, 570)
				spear22X = spear11X
				spear22Y = spear11Y - 870
			
			if spear11X == 380:
				spear1X = 800
				spear1Y = random.randrange(200, 570)
				spear2X = spear1X
				spear2Y = spear1Y - 870

			if spear11X <= 800:
				spear11X_change = -1.5
				spear22X_change = -1.5
				spear22X += spear22X_change
				spear11X += spear11X_change
			
			spearX_change = -1.5
			spear2X_change = -1.5
			spear2X += spear2X_change
			spear1X += spearX_change
		
		#This will check if the player has crossed the obstacle or not... If he has, it will play sound and increase score
		if centre_playerX > centre_spear1X + 45 and centre_playerX < centre_spear1X + 47:
			x += 1
			flap = mixer.Sound("lol.wav")
			flap.play() 

		if centre_playerX > centre_spear11X + 45 and centre_playerX < centre_spear11X + 47:
			x += 1 
			flap = mixer.Sound("lol.wav")
			flap.play()

		#These functions define where an image has to be... They have been defined in the beginning

		spear(spear1X,spear1Y, spear2X, spear2Y)
		spear_LOL(spear11X, spear11Y, spear22X, spear22Y)
		player(playerX, playerY)
		if game_over == "no":
			score_card()	
		if game_over == "yes":
			playerY_change == 0
			spear1X_change == 0
			spear2X_change == 0
			if started_once == "no":
				mixer.music.load("End.mp3")
				mixer.music.play()
				started_once = "yes"
			END_SCREEN()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					switch = False
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_r:
						running = False
					if event.key == pygame.K_ESCAPE:
						switch = False
						running = False
		clock.tick(140)
		pygame.display.update()
  