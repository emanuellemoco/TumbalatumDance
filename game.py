import pygame
from pygame.locals import * #usando todas as funções do pygame
from sys import exit
from random import randint


black = (0,0,0)
white = (255,255,255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (200,0,0)
green = (0, 200, 0)


bright_red = (255,0,0)
bright_green = (0, 255, 0)


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
som_opcao4 = ('.\\musicas\\Shape_of_You.wav') 

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




def loop_game(som_opcao, personagem_opcao):
    #adicionando imagem de fundo e mudando a configuração 956,560 tamanho img
    background_filename = '.\\imagens\\pistadanca2.jpg'
    background = pygame.image.load(background_filename).convert()

    #adicionando as setas
    #foi usado o método alpha pq ela tem partes transparentes

    #lista_img = ['flechad.jpg','flechae.jpg','flechab.jpg','flechac.jpg']
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

    
    pygame.mixer.music.load(som_opcao) 
    #pygame.mixer.music.load('.\\musicas\\Explosao.wav') 
    pygame.mixer.music.play(0) #toca

    clock = pygame.time.Clock()

    personagens = []
    for filename in personagem_opcao:
        novo_personagem = pygame.image.load(filename).convert_alpha()
        personagens.append(novo_personagem)

    personagem_position = [375,75]

    speed = 10


    #loop para atualizar 
    while True:
        tecla = None
       
        # if not event in pygame.event.get():
        #     contador +=1 
        #     if contador % 5 == 0:
        #         score = -10
        #         if score <= 0:
        #             score = 0
        #             break

        for event in pygame.event.get():
            contador = 0
            #print (event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or \
                   event.key == pygame.K_LEFT or \
                   event.key == pygame.K_UP or \
                   event.key == pygame.K_DOWN:
                    tecla = event.key

            if event.type == QUIT:
                exit()

        screen.blit(background, (0,0))
        message_to_screen ("{0}".format(score), white)
           
        for i in range(len(flechas_position)):
            flechas_position[i][0] += speed

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
                      #  message_to_screen (score, white)
                    elif pos_x > 720 and pos_x < 780:
                        print("Good!")
                        score+=70
                        print(score)
                      #  message_to_screen (score, white)
                    else:
                        print("Ok!")
                        score+=50
                        print(score)
                     #   message_to_screen (score, white)
                    conta_desenho_pers = (conta_desenho_pers + 1) % len(personagens)
                elif tecla != None:
                    print("Errou!")
                    score -= 30
                    print(score)
                  #  message_to_screen (score, white)

        screen.blit(personagens[conta_desenho_pers], personagem_position)


      #para desenhar o botão com uma def
        button ("GO! ", 200, 30, 100, 50, green, bright_green, "gooo")
        button ("AAAA ", 600, 30, 100, 50, red, bright_red, "aaaa")

      
        pygame.display.update()
        time_passed = clock.tick(30)

############ fim def loop_game()

def escolher_personagem():
    background_filename = '.\\imagens\\imagem_inicial.png'
    background = pygame.image.load(background_filename).convert()
    while True:
      #para desenhar o botão com uma def
        # button ("GO! ", 200, 30, 100, 50, green, bright_green, "gooo")
        # button ("AAAA ", 600, 30, 100, 50, red, bright_red, "aaaa")
        pygame.display.update()
        time_passed = clock.tick(30)



def message_to_screen(msg, color):
    #essa def ta com problema
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [900, 30])
   # screen.blit(screen_text, [SCREEN_WIDTH/2, SCREEN_HEIGHT/2])
##

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button (msg, x,y,w,h,ic,ac, action=None):  #largura, altura, cor inativa e ativa
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print (click)
    #print(mouse)

    #desenhar um botão na tela
    if x+w > mouse [0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click [0] == 1 and action != None:
            print ("apertou")
            ##
            #chama o loop_game (no caso, com a musica som_opcao1)
            loop_game(som_opcao4, lista_personagem2)
            ###

            #escolher_personagem()

            # if action == "play": 
            # #exec (open python teste.py)
            #     print ("teste")
          
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    #para escrever no botão
    textSurf, TextRect = text_objects(msg, smallText)
    #para escrever no meio
    TextRect.center = ((x+(w/2), (y + (h/2))))
    screen.blit(textSurf, TextRect)

### fim def_button

pygame.display.set_caption('Tumbalatum Dance')
#MUSICA DA TELA INICIAL
pygame.mixer.music.load('.\\musicas\\Rihanna.wav') 
pygame.mixer.music.play(0) #toca

clock = pygame.time.Clock()

speed = 10

#loop para atualizar 
while True:
    tecla = None
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))
    message_to_screen ("mensagem para aparece na tele", white)

  #para desenhar o botão com uma def
    button ("GO! ", 200, 200, 100, 50, green, bright_green, "gooo")
    button ("AAAA ", 200, 300, 100, 50, red, bright_red, "aaaa")

  
    pygame.display.update()
    time_passed = clock.tick(30)

