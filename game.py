import pygame
from pygame.locals import * #usando todas as funções do pygame
from sys import exit
from random import randint
import time
import json

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
pygame.joystick.init()
# ######### SE TIVER JOYSTICK
# joystick = pygame.joystick.Joystick(0)
# joystick.init()
###########

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32) #configurações tela

#para ficar a tela cheia
#tela1111 = pygame.display.set_mode((956,560),pygame.FULLSCREEN) 


#CARREGANDO AS IMAGENS DE FUNDO
#adicionando imagem de fundo e mudando a configuração 956,560 tamanho img
background_filename = '.\\imagens\\imagem_inicial.png'
background_inicial = pygame.image.load(background_filename).convert()

background_nivel_filename = '.\\imagens\\imagem_nivel.png'
background_nivel = pygame.image.load(background_filename).convert()

background_filename = '.\\imagens\\imagem_infos.png'
background_infos = pygame.image.load(background_filename).convert()

background_filename = '.\\imagens\\imagem_personagem.png'
background_personagem = pygame.image.load(background_filename).convert()

background_filename = '.\\imagens\\imagem_som.png'
background_som = pygame.image.load(background_filename).convert()

background_filename = '.\\imagens\\imagem_gameover.png'
background_gameover = pygame.image.load(background_filename).convert()

background_filename = '.\\imagens\\pistadanca2.jpg'
background_pista = pygame.image.load(background_filename).convert()

background_filename = '.\\imagens\\imagem_fim_jogo.png'
background_fim_jogo = pygame.image.load(background_filename).convert()

background_filename = '.\\imagens\\imagem_about.png'
background_about = pygame.image.load(background_filename).convert()

background_filename = '.\\imagens\\imagem_highscore.png'
background_highscore = pygame.image.load(background_filename).convert()

quadrado_rosa = pygame.image.load('.\\imagens\\quadrado2.png').convert_alpha()
img_perfect = pygame.image.load('.\\imagens\\img_perfect.png').convert_alpha()
img_bad = pygame.image.load('.\\imagens\\img_bad.png').convert_alpha()



conta_tempo_pers = 0
conta_desenho_pers = 0

posicao_y = 460 
posicao_x = 0 

font = pygame.font.SysFont(None, 25)
smallText = pygame.font.Font("freesansbold.ttf",20)

#MUSICAS COM MENOS TEMPO
som_opcao1 = ('.\\musicas\\Explosao2.wav') 
som_opcao2 = ('.\\musicas\\Despacito2.wav') 
som_opcao3 = ('.\\musicas\\Rihanna2.wav') 
som_opcao4 = ('.\\musicas\\Shape_of_You2.wav')  

lista_personagem1 = [
		'.\\imagens\\mcvovozona1.png',
		'.\\imagens\\mcvovozona2.png',
		'.\\imagens\\mcvovozona3.png',
		'.\\imagens\\mcvovozona4.png',
		'.\\imagens\\mcvovozona5.png',
		'.\\imagens\\mcvovozona6.png'
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

velocidade_easy = 5
velocidade_medium = 9
velocidade_hard = 13

##########
#código compartilhado com o grupo da manoela 
letras={}
letras[K_a]='a'
letras[K_b]='b'
letras[K_c]='c'
letras[K_d]='d'
letras[K_e]='e'
letras[K_f]='f'
letras[K_g]='g'
letras[K_h]='h'
letras[K_i]='i'
letras[K_j]='j'
letras[K_k]='k'
letras[K_l]='l'
letras[K_m]='m'
letras[K_n]='n'
letras[K_o]='o'
letras[K_p]='p'
letras[K_q]='q'
letras[K_r]='r'
letras[K_s]='s'
letras[K_t]='t'
letras[K_u]='u'
letras[K_v]='v'
letras[K_w]='w'
letras[K_x]='x'
letras[K_y]='y'
letras[K_z]='z'
##############################

#amém manu 
########codigo compartilhado com o grupo da manoela
with open('highscore.json','r') as arquivo:
	dados = json.load(arquivo)

myfont2 = pygame.font.SysFont('Lucida Console', 25)

#myfont2 = pygame.font.Font('Cosmos.otf', 45)

#função que salva o jogo que o jogador iniciou(personagens e insperdex)
def save(dadossalvo):
	with open('highscore.json','w') as dados_salvos:
		dados_salvos.writelines(json.dumps(dados))

def organizadados(dados):
	highscore = sorted(dados.items(), key=lambda x: x[1], reverse=True)
	dadosorg = []
	for y, z in highscore:
		pontos = myfont2.render('{0} : {1}'.format(y,z) , False, (255,255,255))
		dadosorg.append(pontos)
	print(dadosorg)
	return dadosorg

def lerpontos(dadosorg,screen):
	#para aparecer os usuarios e pontos do high score na tela 
	pos_x = 270
	pos_x2 = 575
	screen.blit(dadosorg[0],(pos_x,253))
	screen.blit(dadosorg[1],(pos_x,313))
	screen.blit(dadosorg[2],(pos_x,376))
	screen.blit(dadosorg[3],(pos_x,433))
	screen.blit(dadosorg[4],(pos_x,496))
	screen.blit(dadosorg[5],(pos_x2,253))
	screen.blit(dadosorg[6],(pos_x2,313))
	screen.blit(dadosorg[7],(pos_x2,376))
	screen.blit(dadosorg[8],(pos_x2,433))
	screen.blit(dadosorg[9],(pos_x2,496))

############################
def message_to_screen(msg, color, msg_pos_x, msg_pos_y):
	screen_text = font.render(msg, True, color)
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

def cria_ranking (dicionario):
	nome = dicionario[0]
	score = dicionario [nome]

def inicia_posicao_flechas(n_flechas, lista_img, posicao_y):
	flechas = []
	flechas_position = []
	flechas_tipo = []

	for i in range(n_flechas):
		# Escolhe imagem aleatoria de flecha e poe na lista de imagens de flechas
		k = randint(0,3)
		img_flecha = lista_img[k]
		flechas.append(img_flecha)

		# Monta a posicao da flecha nova.
		flechas_position.append([0 - 200*i, posicao_y])
		# Guarda tambem o tipo de flecha
		flechas_tipo.append(k)

	return (flechas, flechas_position, flechas_tipo)

#MUSICA DA TELA INICIAL
pygame.display.set_caption('Tumbalatum Dance')

pygame.mixer.music.load('.\\musicas\\Tumbalatum.wav') 
pygame.mixer.music.play(-1) #toca infinitamente

clock = pygame.time.Clock()

#loop para atualizar 
tela = "inicial"


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

n_flechas = 600

score = 0
novo_score = 0 
novo_score1 = 0 
novo_score_erro = 0

flechas, flechas_position, flechas_tipo = inicia_posicao_flechas(n_flechas, lista_img, posicao_y)

contador_acertos = 0
contador_erros = 0
contador_bad = 0
mostrando_perf = False
mostrando_bad = False
contador_tempo = 0
contador_tempo_erro = 0
comecou_musica_jogo = False
comecou_musica_gameover = False
contador = 0
score_seta_fora = 0

nome = ""
pause = False

dadosorg = organizadados(dados)
jogo = True
while jogo:
	tecla = None

	for event in pygame.event.get():
		print(event)
		if event.type == QUIT:
			exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or \
			   event.key == pygame.K_LEFT or \
			   event.key == pygame.K_UP or \
			   event.key == pygame.K_DOWN:
				tecla = event.key
			contador = 0	
############# para o joystick funcionar
			if event.key == pygame.K_ESCAPE: #para sair quando apertar esc
				jogo = False
		if event.type == pygame.JOYBUTTONDOWN:
			if event.button == 3:
				tecla = pygame.K_RIGHT
			if event.button == 0:
				tecla = pygame.K_LEFT
			if event.button == 2:
				tecla = pygame.K_UP
			if event.button == 1:
				tecla = pygame.K_DOWN
			contador = 0
##################
		if event.type == pygame.USEREVENT:   #evento para acaba o jogo quando a musica termina
			tela = "fim_jogo"
			print('kbo')

		if event.type == QUIT:
			exit()

	if tela == "inicial":
		score = 0
		novo_score = 0
		screen.blit(background_inicial, (0,0))
		comecou_musica_gameover = False
		comecou_musica_jogo = False
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
			comecou_musica_jogo = False

	elif tela == "info":
		screen.blit(background_infos, (0,0))
		#para desenhar o botão com uma def
		botao_voltar_clicado = button ("Voltar", 825, 500, 100, 50, pink, bright_pink)
		if botao_voltar_clicado:
			tela = "inicial"
			screen.blit(background_inicial, (0,0))

	elif tela == "about":
		pygame.display.update()
		screen.blit(background_about, (0,0))
		botao_voltar_clicado = button ("Voltar", 825, 500, 100, 50, green, bright_green)
		if botao_voltar_clicado:
			tela = "inicial"
			screen.blit(background_inicial, (0,0))

		pygame.display.update()
		time_passed = clock.tick(30)


	elif tela == "highscore":
		screen.blit(background_highscore, (0,0))

		dadosorg = organizadados(dados)
		lerpontos(dadosorg,screen)

		botao_voltar_clicado = button ("Voltar", 845, 500, 100, 50, pink, bright_pink)
		if botao_voltar_clicado:
			tela = "inicial"		

	elif tela == "level":
		pygame.display.update()
		screen.blit(background_nivel, (0,0))

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

	elif tela == "personagem":
		pygame.display.update()
		screen.blit(background_personagem, (0,0))
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
			tela = "level"      
			screen.blit(background_nivel, (0,0))

	elif tela == "musica":
		screen.blit(background_som, (0,0))

		botao_ed_clicado = button ("Ed Sheeran", 300, 250, 115, 50, blue_ed, bright_blue_ed)
		botao_despacito_clicado = button ("Despacito", 300, 420, 115, 50, green, bright_green)
		botao_kevinho_clicado = button ("Kevinho", 600, 250, 115, 50, yellow, bright_yellow)
		botao_rihanna_clicado = button ("Rihanna", 600, 420, 115, 50, red, bright_red)
		botao_voltar3_clicado = button ("Voltar", 825, 500, 100, 50, pink, bright_pink)

		if botao_ed_clicado or botao_despacito_clicado or botao_kevinho_clicado or botao_rihanna_clicado or botao_voltar3_clicado:
			tela = "jogo"
			flechas, flechas_position, flechas_tipo = inicia_posicao_flechas(n_flechas, lista_img, posicao_y)

			if botao_ed_clicado:
				musica = som_opcao4
			elif botao_despacito_clicado:
				musica = som_opcao2
			elif botao_kevinho_clicado:
				musica = som_opcao1
			elif botao_rihanna_clicado:
				musica = som_opcao3

		elif botao_voltar3_clicado:
			tela = "personagem"
			screen.blit(background_personagem, (0,0))

	elif tela == "jogo":
		contador += 1
		pygame.display.update()

		#amem japa
		if not comecou_musica_jogo:
			pygame.mixer.music.load(musica) 
			pygame.mixer.music.set_endevent(pygame.USEREVENT)
			pygame.mixer.music.play(0)
			comecou_musica_jogo = True

		screen.blit(background_pista, (0,0))        

		personagens = []
		for filename in personagem:
			novo_personagem = pygame.image.load(filename).convert_alpha()
			personagens.append(novo_personagem)

		personagem_position = [375,75]

		screen.blit(background_pista, (0,0))
		message_to_screen ("{0}".format(score), white, 800, 50)

		if contador > 350:
			score -=30
			novo_score1 -= 30
			if score < 0:
				score = 0
			if novo_score1 < -500:
				tela = "game_over"
				comecou_musica_jogo = False
				score = 0
				novo_score1 = 0
		    
		seta_no_quadrado = False

		for i in range(len(flechas_position)):
			flechas_position[i][0] += velocidade

			pos_x = flechas_position[i][0]
			if pos_x > -100 and pos_x < SCREEN_WIDTH:
				screen.blit(flechas[i], flechas_position[i])

			if pos_x > 700 and pos_x < 800:
				seta_no_quadrado = True
				score_seta_fora = 0
				contador_erros = 0

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
						contador_acertos += 1
						print(contador_acertos)
						contador_erros = 0

					elif pos_x > 720 and pos_x < 780:
						print("Good!")
						score+=70
						print(score)
						screen.blit(quadrado_rosa, (735,455))
						contador_acertos += 1
						print(contador_acertos)
						contador_erros = 0

					else:
						print("Ok!")
						score+=50
						print(score)
						screen.blit(quadrado_rosa, (735,455))
						contador_acertos += 1
						print(contador_acertos)
						contador_erros = 0

					conta_desenho_pers = (conta_desenho_pers + 1) % len(personagens)
				elif tecla != None:
					print("Errou!")
					score -= 30
					novo_score_erro -=30
					contador_erros += 1
					print("contador erro: {0}".format(contador_erros))
					print (novo_score_erro)
					if score < 0: #para o score nao ficar negativo
						score = 0
						print(novo_score_erro)
						if novo_score_erro < -120:
							tela = "game_over" 
							print("deu game")
							score = 0
							novo_score_erro = 0
					contador_acertos = 0
					print (contador_acertos)

					#para aparecer perfect
				if contador_acertos >= 5 :
					print ("muito bem!")
					contador_acertos = 0
					mostrando_perf = True
					contador_tempo = 0


				if mostrando_perf:
					screen.blit(img_perfect, (730,400))
					contador_tempo += 1
					if contador_tempo == 10:
						mostrando_perf = False

#amem japa2
		if not seta_no_quadrado:
			if tecla == pygame.K_RIGHT or \
			   tecla == pygame.K_LEFT or \
			   tecla == pygame.K_DOWN or \
			   tecla == pygame.K_UP:
			   score -= 30
			   score_seta_fora -= 30
			   contador_erros -= 1
			   print ("score :{0}".format(score))
			   print ("score seta fora: {0}".format(score_seta_fora))
			   if score < 0:
			   	score = 0
			   if score_seta_fora < -180:
			   	tela = "game_over"
			   	score_seta_fora = 0

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

		while pause == True: # pausa
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
			tela = "jogo"
			score = 0
			novo_score = 0
			flechas, flechas_position, flechas_tipo = inicia_posicao_flechas(n_flechas, lista_img, posicao_y)
			pygame.mixer.music.load(musica) 
			pygame.mixer.music.set_endevent(pygame.USEREVENT)
			pygame.mixer.music.play(0)
			comecou_musica_jogo = True
			
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
			pygame.mixer.music.play(-1) #toca

	elif tela == "game_over":
		screen.blit(background_gameover, (0,0))
		score = 0
		novo_score = 0
		contador_acertos = 0 

		if not comecou_musica_gameover:
			pygame.mixer.music.load('.\\musicas\\gameover.wav')
			pygame.mixer.music.play(-1)
			comecou_musica_gameover = True

		botao_voltar_clicado = button ("MENU", 420, 420, 100, 50, red, bright_red)	
		if botao_voltar_clicado:
			tela = "inicial"
			pygame.mixer.music.load('.\\musicas\\Tumbalatum.wav') 
			pygame.mixer.music.play(-1) #toca

	elif tela == "fim_jogo":
		screen.blit(background_fim_jogo, (0,0))
		novo_score = 0
		if event.type == pygame.KEYDOWN:
			if event.key in letras:
				letra=letras[event.key]
				nome+=letra
				time.sleep(0.15) 
		message_to_screen ("{0}".format(nome), white, 440, 470)
							   
		botao_inserir_clicado = button ("Inserir", 620, 455, 115, 50, blue_ed, bright_blue_ed)
		botao_voltar_clicado = button ("MENU", 825, 500, 100, 50, pink, bright_pink)		
		message_to_screen ("{0}".format(score), white, 395, 325)

		if botao_voltar_clicado:
			tela = "inicial"
			pygame.mixer.music.load('.\\musicas\\Tumbalatum.wav') 
			pygame.mixer.music.play(-1) #toca

		elif botao_inserir_clicado:
			dados[nome] = score
			save(dados)
			tela = "inicial"
			nome = ""
			pygame.mixer.music.load('.\\musicas\\Tumbalatum.wav') 
			pygame.mixer.music.play(-1) #toca

	pygame.display.update()
	time_passed = clock.tick(30)