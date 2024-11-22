import pygame
from functions import att_tela
from functions import acelera
from functions import win1
from functions import win2
from functions import win3
from functions import teste

pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("Recursos/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
pygame.mixer.music.load("Recursos/trilha.mp3")
pygame.mixer.music.play(-1)

fundo = pygame.image.load("Recursos/fundo.png")
carro1 = pygame.image.load("Recursos/carro1.png")
carro2 = pygame.image.load("Recursos/carro2.png")
carro3 = pygame.image.load("Recursos/carro3.png")
win = pygame.image.load("Recursos/vitoria.jpg")

movXCar1 = 0
movXCar2 = 0
movXCar3 = 0
posYCar1 = 30
posYCar2 = 110
posYCar3 = 200

branco = (255,255,255)
preta = (0,0,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
azul = (0,0,255)

acabou = False
ganhou1 = False
ganhou2 = False
ganhou3 = False
somDaVitoria = False

vitoria = pygame.mixer.Sound("Recursos/vitoria.mp3")
vitoria.set_volume(0.5)
fonte = pygame.font.Font("freesansbold.ttf",60)
fonte1 = pygame.font.Font("freesansbold.ttf",20)
textoVermelho = fonte.render("Vermelho Ganhou!", True, preta)
textoAmarelo = fonte.render("Amarelo Ganhou!", True, preta)
textoAzul = fonte.render("Azul Ganhou!", True, preta)

while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
    
    if not acabou:
        lista = acelera(movXCar1, movXCar2, movXCar3)
        movXCar1 = lista[0]
        movXCar2 = lista[1]
        movXCar3 = lista[2]
        att_tela(carro1, movXCar1, posYCar1, carro2, movXCar2, posYCar2, carro3, movXCar3, posYCar3, fundo, tela)
    
    else:
        pygame.mixer.music.stop()
        tela.blit(win, (0,0))
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
        if ganhou1 == True:
            win1(movXCar1, movXCar2, movXCar3, tela, fonte1, vermelho)

        if ganhou2 == True:
            win2(movXCar1, movXCar2, movXCar3, tela, fonte1, amarelo)

        if ganhou3 == True:
            win3(movXCar1, movXCar2, movXCar3, tela, fonte1, azul)
    
    if movXCar1 > 1010:
        movXCar1 = -10
        posYCar1 = 350
        
    if movXCar2 > 1010:
        movXCar2 = -10
        posYCar2 = 420
    
    if movXCar3 > 1010:
        movXCar3 = -10
        posYCar3 = 500

    if posYCar1 == 350 and posYCar2 == 420 and posYCar3 == 500:
        alguma = teste(movXCar1, textoVermelho, tela, movXCar2, textoAmarelo, movXCar3, textoAzul, ganhou3, ganhou2, ganhou1)
        if alguma[0] == True:
            ganhou1 = True
            acabou = True
        if alguma[1] == True:
            ganhou2 = True
            acabou = True
        if alguma[2] == True:
            ganhou3 = True
            acabou = True

    pygame.display.update()
    clock.tick(60)
pygame.quit()