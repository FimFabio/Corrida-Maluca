def final_position(movXCar, texto, ganhou, tela):
 if movXCar > 900:
    tela.blit(texto, (270,180))
    ganhou = True
    return ganhou