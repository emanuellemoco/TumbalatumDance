import pygame
from pygame.locals import * #usando todas as funções do pygame
from sys import exit
from random import randint

SCREEN_WIDTH = 956
SCREEN_HEIGHT = 560

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32) #configurações tela

#adicionando imagem de fundo e mudando a configuração 956,560 tamanho img
background_filename = '.\\imagens\\pistadanca2.jpg'
background = pygame.image.load(background_filename).convert()

#adicionando a nave
#foi usado o método alpha pq ela tem partes transparentes

#lista_img = ['flechad.jpg','flechae.jpg','flechab.jpg','flechac.jpg']
lista_img = [
    pygame.image.load('.\\flechas\\flechad.png').convert_alpha(),
    pygame.image.load('.\\flechas\\flechae.png').convert_alpha(),
    pygame.image.load('.\\flechas\\flechab.png').convert_alpha(),
    pygame.image.load('.\\flechas\\flechac.png').convert_alpha()
]
lista_personagem1 = ['desenho.png','desenho2.png' ]
conta_tempo_pers = 0
conta_desenho_pers = 0

posicao_y = 460 
posicao_x = 0 

flechas = []
flechas_position = []
flechas_tipo = []

n_flechas = 600
for i in range(n_flechas):
    # Escolhe imagem aleatoria de flecha e poe na lista de imagens de flechas
    k = randint(0,3)
    img_flecha = lista_img[k]
    flechas.append(img_flecha)

    # Monta a posicao da flecha nova.
    flechas_position.append([0 - 200*i, posicao_y])

    # Guarda tambem o tipo de flecha
    flechas_tipo.append(k)

pygame.display.set_caption('Tumbalatum Dance')
#pygame.mixer.music.load('Shape_of_You.wav')
pygame.mixer.music.load('.\\musicas\\Explosao.wav') 
pygame.mixer.music.play(0) #toca

clock = pygame.time.Clock()

personagens = []
for filename in lista_personagem1:
    novo_personagem = pygame.image.load(filename).convert_alpha()
    personagens.append(novo_personagem)

personagem_position = [200,50]

speed = 10

#loop para atualizar 
while True:
    tecla = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or \
               event.key == pygame.K_LEFT or \
               event.key == pygame.K_UP or \
               event.key == pygame.K_DOWN:
                tecla = event.key

        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))

    for i in range(len(flechas_position)):
        flechas_position[i][0] += speed

        pos_x = flechas_position[i][0]
        if pos_x > -100 and pos_x < SCREEN_WIDTH:
            screen.blit(flechas[i], flechas_position[i])

        if pos_x > 800 and pos_x < 900:
            tipo = flechas_tipo[i]

            if (tipo == 0 and tecla == pygame.K_RIGHT) or \
               (tipo == 1 and tecla == pygame.K_LEFT) or \
               (tipo == 2 and tecla == pygame.K_DOWN) or \
               (tipo == 3 and tecla == pygame.K_UP):
                if pos_x > 840 and pos_x < 860:
                    print("Perfect!")
                elif pos_x > 820 and pos_x < 880:
                    print("Good!")
                else:
                    print("Ok!")
                conta_desenho_pers = (conta_desenho_pers + 1) % len(personagens)
            elif tecla != None:
                print("Errou!")

    screen.blit(personagens[conta_desenho_pers], personagem_position)

    pygame.display.update()
    time_passed = clock.tick(30)
