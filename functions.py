import random
def final_position(movXCar, texto, ganhou, tela):
 if movXCar > 900:
    tela.blit(texto, (270,180))
    ganhou = True
    return ganhou
 
def att_tela(carro1, movXCar1, posYCar1, carro2, movXCar2, posYCar2, carro3, movXCar3, posYCar3, fundo, tela):
      tela.blit(fundo, (0,0))
      tela.blit(carro1, (movXCar1,posYCar1))
      tela.blit(carro2, (movXCar2,posYCar2))
      tela.blit(carro3, (movXCar3,posYCar3))

def acelera(movXCar1, movXCar2, movXCar3):
   movXCar1 = movXCar1 + random.randint(0,10)
   movXCar2 = movXCar2 + random.randint(0,10)
   movXCar3 = movXCar3 + random.randint(0,10)
   return [movXCar1, movXCar2, movXCar3]

def win1(movXCar1, movXCar2, movXCar3, tela, fonte1, vermelho):
   diferenca1 = movXCar1 - movXCar2
   diferenca2 = movXCar1 - movXCar3
   if diferenca1 > diferenca2:
         diferenca3 = movXCar3 - movXCar2
         tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca2) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, vermelho), (20,250))
   else:
         diferenca3 = movXCar2 - movXCar3
         tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca1) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, vermelho), (20,250))

def win2(movXCar1, movXCar2, movXCar3, tela, fonte1, amarelo):
   diferenca1 = movXCar2 - movXCar1
   diferenca2 = movXCar2 - movXCar3
   if diferenca1 > diferenca2:
      diferenca3 = movXCar3 - movXCar1
      tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca2) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, amarelo), (20,250))
   else:
      diferenca3 = movXCar1 - movXCar3
      tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca1) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, amarelo), (20,250))

def win3(movXCar1, movXCar2, movXCar3, tela, fonte1, azul):
   diferenca1 = movXCar3 - movXCar1
   diferenca2 = movXCar3 - movXCar2
   if diferenca1 > diferenca2:
      diferenca3 = movXCar2 - movXCar1
      tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca2) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, azul), (20,250))
   else:
      diferenca3 = movXCar1 - movXCar2
      tela.blit(fonte1.render("Distância entre o primerio e o segundo é de " + str(diferenca1) + ", a Distância entre o segundo e o terceiro é de " + str(diferenca3), True, azul), (20,250))

def teste(movXCar1, textoVermelho, tela, movXCar2, textoAmarelo, movXCar3, textoAzul, posYCar1, posYCar2, posYCar3, ganhou3, ganhou2, ganhou1):
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
   return [ganhou1, ganhou2, ganhou3]