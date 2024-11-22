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