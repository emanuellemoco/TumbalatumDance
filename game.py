import pygame
from pygame.locals import * #usando todas as funções do pygame
from sys import exit
from random import randint

SCREEN_WIDTH = 956
SCREEN_HEIGHT = 560

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32) #configurações tela

#adicionando imagem de fundo e mudando a configuração 956,560 tamanho img
background_filename = 'pistadanca2.jpg'
background = pygame.image.load(background_filename).convert()

#adicionando a nave
#foi usado o método alpha pq ela tem partes transparentes

#lista_img = ['flechad.jpg','flechae.jpg','flechab.jpg','flechac.jpg']
lista_img = [
    pygame.image.load('flechad.jpg').convert_alpha(),
    pygame.image.load('flechae.jpg').convert_alpha(),
    pygame.image.load('flechab.jpg').convert_alpha(),
    pygame.image.load('flechac.jpg').convert_alpha()
]
lista_personagem1 = ['desenho.png','desenho2.png' ]

posicao_y = 460 
posicao_x = 0 

flechas = []
flechas_position = []

n_flechas = 600
for i in range(n_flechas):
    # Escolhe imagem aleatoria de flecha e poe na lista de imagens de flechas
    k = randint(0,3)
    img_flecha = lista_img[k]
    flechas.append(img_flecha)

    # Monta a posicao da flecha nova.
    flechas_position.append([0 - 200*i, posicao_y])


flecha0_position = [0,posicao_y] #posição inicial
flecha1_position = [0-200,posicao_y]
flecha2_position = [0-400,posicao_y]
flecha3_position = [0-600,posicao_y]
flecha4_position = [0-800,posicao_y]
flecha5_position = [0-1000,posicao_y]

personagem0_position = [200,50]

i = randint(0,3)
n = randint(0,3)
a = randint(0,3)
b  = randint(0,3)
c = randint(0,3)
d = randint(0,3)

pygame.display.set_caption('Tumbalatum Dance')
pygame.mixer.music.load('Shape_of_You.wav')
pygame.mixer.music.play(0) #toca

clock = pygame.time.Clock()

personagem0_filename = lista_personagem1[0]
personagem1_filename = lista_personagem1[1]

personagem0 = pygame.image.load(personagem0_filename).convert_alpha()
personagem1 = pygame.image.load(personagem1_filename).convert_alpha()

speed = 10

#loop para atualizar 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))

    for i in range(len(flechas_position)):
        flechas_position[i][0] += speed
        if flechas_position[i][0] > -100 and flechas_position[i][0] < SCREEN_WIDTH:
            screen.blit(flechas[i], flechas_position[i])



    screen.blit(personagem0, personagem0_position)
    screen.blit(personagem1, personagem0_position)

    pygame.display.update()
    time_passed = clock.tick(30)

