import pygame
from pygame.locals import * #usando todas as funções do pygame
from sys import exit
from random import randint
import time



black = (0,0,0)
white = (255,255,255)
blue = (0, 0, 200)
yellow = (200, 200, 0)
red = (200,0,0)
green = (0, 200, 0)
pink = (200,0,127)
blue_ed = (51, 153, 200)

bright_red = (255,0,0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
bright_yellow = (255, 255, 0)
bright_pink = (255,0,127)
bright_blue_ed = (51, 153, 255)



SCREEN_WIDTH = 956
SCREEN_HEIGHT = 560

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32) #configurações tela

#adicionando imagem de fundo e mudando a configuração 956,560 tamanho img
background_filename = '.\\imagens\\imagem_inicial.png'
background = pygame.image.load(background_filename).convert()


conta_tempo_pers = 0
conta_desenho_pers = 0

posicao_y = 460 
posicao_x = 0 

##

font = pygame.font.SysFont(None, 25) 
smallText = pygame.font.Font("freesansbold.ttf",20)

#opções de musica para o jogo
som_opcao1 = ('.\\musicas\\Explosao.wav') 
som_opcao2 = ('.\\musicas\\Despacito.wav') 
som_opcao3 = ('.\\musicas\\Rihanna.wav') 
som_opcao4 = ('.\\musicas\\Musica_teste.wav') 

#som_opcao4 = ('.\\musicas\\Shape_of_You.wav') 

lista_personagem1 = [
		'.\\imagens\\mcvovozona1.png',
		'.\\imagens\\mcvovozona2.png',
		'.\\imagens\\mcvovozona3.png',
		'.\\imagens\\mcvovozona4.png',
		'.\\imagens\\mcvovozona5.png',
		'.\\imagens\\mcvovozona6.png',
		'.\\imagens\\mcvovozona7.png',
		#'.\\imagens\\mcvovozona8.png',
		#'.\\imagens\\mcvovozona9.png',
		#'.\\imagens\\mcvovozona10.png',
		#'.\\imagens\\mcvovozona11.png'
		# '.\\imagens\\mcvovozona12.png',
		# '.\\imagens\\mcvovozona13.png',
		# '.\\imagens\\mcvovozona14.png',
		# '.\\imagens\\mcvovozona15.png',
		# '.\\imagens\\mcvovozona16.png',
		# '.\\imagens\\mcvovozona17.png'
	]

lista_personagem2 = [
		'.\\imagens\\robocop1.png',
		'.\\imagens\\robocop2.png',
		'.\\imagens\\robocop3.png',
		'.\\imagens\\robocop4.png',
		'.\\imagens\\robocop5.png',
		'.\\imagens\\robocop6.png'
	]

lista_personagem3 = [
		'.\\imagens\\estranha1.png',
		'.\\imagens\\estranha2.png',
		'.\\imagens\\estranha3.png',
		'.\\imagens\\estranha4.png',
		'.\\imagens\\estranha5.png',
		'.\\imagens\\estranha6.png'
	]

lista_personagem4 = [
		'.\\imagens\\estranho1.png',
		'.\\imagens\\estranho2.png',
		'.\\imagens\\estranho3.png',
		'.\\imagens\\estranho4.png',
		'.\\imagens\\estranho5.png',
		'.\\imagens\\estranho6.png'
	]

velocidade_easy = 9
velocidade_medium = 13
velocidade_hard = 18

def message_to_screen(msg, color, msg_pos_x, msg_pos_y):
	screen_text = font.render(msg, True, color)
	#screen.blit(screen_text, [400, 200])
	screen.blit(screen_text, [msg_pos_x, msg_pos_y])

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()


def button (msg, x,y,w,h,ic,ac):  #largura, altura, cor inativa e ativa
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	botao_clicado = False

	#desenhar um botão na tela
	if (x + w) > mouse [0] > x and (y + h) > mouse[1] > y:
		pygame.draw.rect(screen, ac, (x, y, w, h))
		if click[0] == 1:
			botao_clicado = True
			time.sleep(0.1)  #amem david delay para ignorar duplo clique
	else:
		pygame.draw.rect(screen, ic, (x, y, w, h))

	#para escrever no botão
	textSurf, TextRect = text_objects(msg, smallText)
	#para escrever no meio
	TextRect.center = ((x+(w/2), (y + (h/2))))
	screen.blit(textSurf, TextRect)

	return botao_clicado
### fim def_button

pygame.display.set_caption('Tumbalatum Dance')
#MUSICA DA TELA INICIAL

pygame.mixer.music.load('.\\musicas\\Tumbalatum.wav') 
pygame.mixer.music.play(-1) #toca

effect_wrong = pygame.mixer.Sound('.\\musicas\\sound_wrong.wav')
effect_correct = pygame.mixer.Sound('.\\musicas\\teste.wav')





clock = pygame.time.Clock()

#loop para atualizar 
tela = "inicial"




background_nivel_filename = '.\\imagens\\imagem_nivel.png'
background_nivel = pygame.image.load(background_filename).convert()


lista_img = [
		pygame.image.load('.\\flechas\\flechad.png').convert_alpha(),
		pygame.image.load('.\\flechas\\flechae.png').convert_alpha(),
		pygame.image.load('.\\flechas\\flechab.png').convert_alpha(),
		pygame.image.load('.\\flechas\\flechac.png').convert_alpha()
	]


conta_tempo_pers = 0
conta_desenho_pers = 0

posicao_y = 460 
posicao_x = 0 

flechas = []
flechas_position = []
flechas_tipo = []

n_flechas = 600

score = 0


for i in range(n_flechas):
	# Escolhe imagem aleatoria de flecha e poe na lista de imagens de flechas
	k = randint(0,3)
	img_flecha = lista_img[k]
	flechas.append(img_flecha)

	# Monta a posicao da flecha nova.
	flechas_position.append([0 - 200*i, posicao_y])
	# Guarda tambem o tipo de flecha
	flechas_tipo.append(k)





comecou_musica_jogo = False
pause = False
while True:
	tecla = None
	for event in pygame.event.get():
		#print(eveventent)
		if event.type == QUIT:
			exit()

	if tela == "inicial":
		background_filename = '.\\imagens\\imagem_inicial.png'
		background = pygame.image.load(background_filename).convert()
		screen.blit(background, (0,0))

		#para desenhar o botão com uma def
		botao_play_clicado = button ("Play", 150, 180, 110, 50, green, bright_green)
		botao_info_clicado = button ("Infos", 150, 280, 110, 50, red, bright_red)
		botao_about_clicado = button ("About", 150, 380, 110, 50, blue, bright_blue)
		botao_highscore_clicado = button ("High Score", 150, 480, 110, 50, pink, bright_pink)

		if botao_play_clicado:
			tela = "level"
		elif botao_info_clicado:
			tela = "info"
		elif botao_about_clicado:
			tela = "about"
		elif botao_highscore_clicado:
			tela = "highscore"

	elif tela == "info":
		background_filename = '.\\imagens\\imagem_infos.png'
		background = pygame.image.load(background_filename).convert()
		screen.blit(background, (0,0))

		#para desenhar o botão com uma def
		botao_voltar_clicado = button ("Voltar", 825, 500, 100, 50, pink, bright_pink)
		if botao_voltar_clicado:
			tela = "inicial"
			background_filename = '.\\imagens\\imagem_inicial.png'
			background = pygame.image.load(background_filename).convert()
		pygame.display.update()
		time_passed = clock.tick(30) 


	elif tela == "about":
		pygame.display.update()
		background_filename = '.\\imagens\\imagem_about.png'
		background = pygame.image.load(background_filename).convert()
		screen.blit(background, (0,0))
		#message_to_screen ("Choose your level", white, 300, 150)
		#para desenhar o botão com uma def
		botao_voltar_clicado = button ("Voltar", 825, 500, 100, 50, green, bright_green)
		if botao_voltar_clicado:
			tela = "inicial"
			background_filename = '.\\imagens\\imagem_inicial.png'
			background = pygame.image.load(background_filename).convert()
		pygame.display.update()
		time_passed = clock.tick(30)


	elif tela == "highscore":
		background_filename = '.\\imagens\\imagem_highscore.png'
		background = pygame.image.load(background_filename).convert()
		screen.blit(background, (0,0))

		botao_voltar_clicado = button ("Voltar", 845, 500, 100, 50, pink, bright_pink)

	

	elif tela == "level":
		pygame.display.update()
		background_filename = '.\\imagens\\imagem_nivel.png'
		background = pygame.image.load(background_filename).convert()
		screen.blit(background, (0,0))

		#para desenhar o botão com uma def
		botao_easy_clicado = button ("Easy", 150, 250, 100, 50, green, bright_green)
		botao_medium_clicado = button ("Medium", 150, 350, 100, 50, yellow, bright_yellow)
		botao_hard_clicado = button ("Hard", 150, 450, 100, 50, red, bright_red)
		botao_voltar1_clicado = button ("Voltar", 825, 500, 100, 50, pink, bright_pink)

		if botao_easy_clicado:
			velocidade = velocidade_easy
			tela = "personagem"
		elif botao_medium_clicado:
			velocidade = velocidade_medium
			tela = "personagem"
		elif botao_hard_clicado:
			velocidade = velocidade_hard
			tela = "personagem"
		elif botao_voltar1_clicado:
			tela = "inicial"
		pygame.display.update()
		time_passed = clock.tick(30) 

		#print(botao_easy_clicado, botao_medium_clicado, botao_hard_clicado, botao_voltar_clicado, tela)


	elif tela == "personagem":
		pygame.display.update()
		#print("Voce escolheu o modo {0}".format(velocidade))

		background_filename = '.\\imagens\\imagem_personagem.png'
		background = pygame.image.load(background_filename).convert()
		screen.blit(background, (0,0))
		botao_vovozona_clicado = button ("Vovózona", 200, 240, 100, 50, red, bright_red)
		botao_robocop_clicado = button ("Robôcop", 520, 240, 100, 50, red, bright_red)
		botao_beyonce_clicado = button ("Beyonce", 520, 440, 100, 50, red, bright_red)
		botao_kleyton_clicado = button ("Kleyton", 200, 440, 100, 50, red, bright_red)
		botao_voltar2_clicado = button ("Voltar", 825, 500, 100, 50, pink, bright_pink)

		if botao_vovozona_clicado:
			personagem = lista_personagem1
			tela = "musica"
		elif botao_robocop_clicado:
			personagem = lista_personagem2
			tela = "musica"
		elif botao_beyonce_clicado:
			personagem = lista_personagem3
			tela = "musica"
		elif botao_kleyton_clicado:
			personagem = lista_personagem4
			tela = "musica"
		elif botao_voltar2_clicado:
			tela = "level"       #NAO TA VOLTANDO PRO LEVEL 
			background_filename = '.\\imagens\\imagem_inicial.png'
			background = pygame.image.load(background_filename).convert()



	elif tela == "musica":
		#print("Voce escolheu a velocudade {0}".format(velocidade))

		background_filename = '.\\imagens\\imagem_som.png'
		background = pygame.image.load(background_filename).convert()
		screen.blit(background, (0,0))

		botao_ed_clicado = button ("Ed Sheeran", 300, 250, 115, 50, blue_ed, bright_blue_ed)
		botao_despacito_clicado = button ("Despacito", 300, 420, 115, 50, green, bright_green)
		botao_kevinho_clicado = button ("Kevinho", 600, 250, 115, 50, yellow, bright_yellow)
		botao_rihanna_clicado = button ("Rihanna", 600, 420, 115, 50, red, bright_red)
		botao_voltar3_clicado = button ("Voltar", 825, 500, 100, 50, pink, bright_pink)




		if botao_ed_clicado:
			musica = som_opcao4
			tela = "jogo"

		elif botao_despacito_clicado:
			musica = som_opcao2
			tela = "jogo"
		elif botao_kevinho_clicado:
			musica = som_opcao1
			tela = "jogo"
		elif botao_rihanna_clicado:
			musica = som_opcao3
			tela = "jogo"

		elif botao_voltar3_clicado:
			tela = "personagem"
			background_filename = '.\\imagens\\imagem_personagem.png'
			background = pygame.image.load(background_filename).convert()


	elif tela == "jogo":
		pygame.display.update()
		#pygame.mixer.music.stop()

		#amem japa
		if not comecou_musica_jogo:
			pygame.mixer.music.load(musica) 
			pygame.mixer.music.play(0)
			comecou_musica_jogo = True
	
		#print("Voce escolheu a musica {0}".format(musica))


		background_filename = '.\\imagens\\pistadanca2.jpg'
		background = pygame.image.load(background_filename).convert()
		screen.blit(background, (0,0))        
		quadrado_rosa = pygame.image.load('.\\imagens\\quadrado2.png').convert_alpha()

		personagens = []
		for filename in personagem:
			novo_personagem = pygame.image.load(filename).convert_alpha()
			personagens.append(novo_personagem)

		personagem_position = [375,75]

		tecla = None
	   
		for event in pygame.event.get():
			print (event)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT or \
				   event.key == pygame.K_LEFT or \
				   event.key == pygame.K_UP or \
				   event.key == pygame.K_DOWN:
					tecla = event.key

			if event.type == QUIT:
				exit()

		screen.blit(background, (0,0))
		message_to_screen ("{0}".format(score), white, 800, 50)
		   
		for i in range(len(flechas_position)):
			flechas_position[i][0] += velocidade

			pos_x = flechas_position[i][0]
			if pos_x > -100 and pos_x < SCREEN_WIDTH:
				screen.blit(flechas[i], flechas_position[i])

			if pos_x > 700 and pos_x < 800:
				tipo = flechas_tipo[i]

				if (tipo == 0 and tecla == pygame.K_RIGHT) or \
				   (tipo == 1 and tecla == pygame.K_LEFT) or \
				   (tipo == 2 and tecla == pygame.K_DOWN) or \
				   (tipo == 3 and tecla == pygame.K_UP):

					if pos_x > 740 and pos_x < 760:
						print("Perfect!")
						score+=100
						print(score)
						screen.blit(quadrado_rosa, (735,455))
						#effect_correct.play()

					elif pos_x > 720 and pos_x < 780:
						print("Good!")
						score+=70
						print(score)
						screen.blit(quadrado_rosa, (735,455))
						#effect_correct.play()

					else:
						print("Ok!")
						score+=50
						print(score)
						screen.blit(quadrado_rosa, (735,455))
						#effect_correct.play()

					conta_desenho_pers = (conta_desenho_pers + 1) % len(personagens)
				elif tecla != None:
					print("Errou!")
					score -= 30
					if score < 0: #para o score nao ficar negativo
						score = 0
					print(score)
					#effect_wrong.play()

		screen.blit(personagens[conta_desenho_pers], personagem_position)

		botao_reiniciar_clicado = button ("Reiniciar", 50, 30, 110, 50, green, bright_green)
		botao_voltar4_clicado = button ("Voltar", 50, 100, 110, 50, yellow, bright_yellow)
		botao_menu_clicado = button ("MENU", 50, 170, 110, 50, pink, bright_pink)

		if event.type == pygame.KEYDOWN:
			  if event.key == pygame.K_SPACE: #se o usuário apertar a tecla espaço pausa o joog
				  pygame.mixer.music.pause()

				  print("STOP")
				  pause = True
				  time.sleep(0.1)
				  #TEM QUE PARAR A TELA INTEIRA

			  if event.key == pygame.K_RETURN: #apertar a tecla enter, volta o jogo
				  pygame.mixer.music.unpause()
				  print ("play")


		while pause == True: # pausa se der errado aqui está 
			for event in pygame.event.get():
				if event.type == QUIT:
					exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						pause = False
						time.sleep(0.1)
						pygame.mixer.music.unpause()



		if botao_reiniciar_clicado:
			pygame.display.update()
			#tela = "jogo" colocando em comentario para testar a tela fim_jogo
			pygame.display.update()
			score = 0
			tela="fim_jogo"
			#erro, tem que fazer reiniciar o jogo
		elif botao_voltar4_clicado:
			pygame.display.update()
			tela = "musica" 
			comecou_musica_jogo = False
			pygame.mixer.music.load('.\\musicas\\Tumbalatum.wav') 
			pygame.mixer.music.play(-1) #toca
			score = 0     
		elif botao_menu_clicado:
			tela = "inicial"
			comecou_musica_jogo = False
			score = 0
			pygame.mixer.music.load('.\\musicas\\Tumbalatum.wav') 


	elif tela == "fim_jogo":
		#print("Voce escolheu a velocudade {0}".format(velocidade))

		background_filename = '.\\imagens\\imagem_fim_jogo.png'
		background = pygame.image.load(background_filename).convert()
		screen.blit(background, (0,0))

		botao_inserir_clicado = button ("Inserir", 620, 455, 115, 50, blue_ed, bright_blue_ed)
		botao_voltar_clicado = button ("MENU", 825, 500, 100, 50, pink, bright_pink)		
		message_to_screen ("{0}".format(score), white, 395, 325)

		if botao_voltar_clicado:
			tela = "inicial"

		elif botao_inserir_clicado:
			""
			#tem que inserir o nome na lista do high score




  
	pygame.display.update()
	time_passed = clock.tick(30)