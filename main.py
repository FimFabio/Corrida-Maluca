import pygame
import random
from functions import final_position

pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("Recursos/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preta = (0,0,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
azul = (0,0,255)
fundo = pygame.image.load("Recursos/fundo.png")
carro1 = pygame.image.load("Recursos/carro1.png")
carro2 = pygame.image.load("Recursos/carro2.png")
carro3 = pygame.image.load("Recursos/carro3.png")

movXCar1 = 0
movXCar2 = 0
movXCar3 = 0
posYCar1 = 30
posYCar2 = 110
posYCar3 = 200

vitoria = pygame.mixer.Sound("Recursos/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("Recursos/trilha.mp3")
pygame.mixer.music.play(-1) #-1 looping, 1,2 3 vezes
acabou = False
ganhou1 = False
ganhou2 = False
ganhou3 = False
somDaVitoria = False

fonte = pygame.font.Font("freesansbold.ttf",60)
fonte1 = pygame.font.Font("freesansbold.ttf",20)
textoVermelho = fonte.render("Vermelho Ganhou!", True, branco)
textoAmarelo = fonte.render("Amarelo Ganhou!", True, branco)
textoAzul = fonte.render("Azul Ganhou!", True, branco)

while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
   
    
    if not acabou:
        movXCar1 = movXCar1 + random.randint(0,10)
        movXCar2 = movXCar2 + random.randint(0,8)
        movXCar3 = movXCar3 + random.randint(0,11)
        tela.blit(fundo, (0,0))
        tela.blit(carro1, (movXCar1,posYCar1))
        tela.blit(carro2, (movXCar2,posYCar2))
        tela.blit(carro3, (movXCar3,posYCar3))
    
    else:
        pygame.mixer.music.stop()
        tela.blit(carro1, (movXCar1,posYCar1))
        tela.blit(carro2, (movXCar2,posYCar2))
        tela.blit(carro3, (movXCar3,posYCar3))
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
        if ganhou1 == True:
            diferenca1 = movXCar1 - movXCar2
            diferenca2 = movXCar1 - movXCar3
            if diferenca1 > diferenca2:
                diferenca3 = movXCar3 - movXCar2
                tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca2) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, vermelho), (20,250))
            else:
                diferenca3 = movXCar2 - movXCar3
                tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca1) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, vermelho), (20,250))

        if ganhou2 == True:
            diferenca1 = movXCar2 - movXCar1
            diferenca2 = movXCar2 - movXCar3
            if diferenca1 > diferenca2:
                diferenca3 = movXCar3 - movXCar1
                tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca2) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, amarelo), (20,250))
            else:
                diferenca3 = movXCar1 - movXCar3
                tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca1) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, amarelo), (20,250))
        if ganhou3 == True:
            diferenca1 = movXCar3 - movXCar1
            diferenca2 = movXCar3 - movXCar2
            if diferenca1 > diferenca2:
                diferenca3 = movXCar2 - movXCar1
                tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca2) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, azul), (20,250))
            else:
                diferenca3 = movXCar1 - movXCar2
                tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca1) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, azul), (20,250))

    
    if movXCar1 > 1010:
        movXCar1 = 0
        posYCar1 = 350
        
    if movXCar2 > 1010:
        movXCar2 = 0
        posYCar2 = 420
    
    if movXCar3 > 1010:
        movXCar3 = 0
        posYCar3 = 500
    

    
    if posYCar1 == 350 and posYCar2 == 420 and posYCar3 == 500:
        ganhou1 = final_position(movXCar1, textoVermelho, ganhou1, tela)
        ganhou2 = final_position(movXCar2, textoAmarelo, ganhou2, tela)
        ganhou3 = final_position(movXCar3, textoAzul, ganhou3, tela)
        if ganhou1 == True:
            acabou = True
        if ganhou2 == True:
            acabou = True
        if ganhou3 == True:
            acabou = True

    pygame.display.update()
    clock.tick(5000)
pygame.quit()
    

