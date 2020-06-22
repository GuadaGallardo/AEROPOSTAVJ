# funciones del scroll

def jugadorGolpeaMoneda(rectanguloJugador, monedas):
    for moneda in monedas:
        if rectanguloJugador.colliderect(moneda['rect']):
            monedas.remove(moneda)
            return True
    return False

def jugadorGolpeaNube(superficie, rectanguloJugador, nubes):
    for nube in nubes:
        if rectanguloJugador.colliderect(nube['rect']):
            #cambia la imagen de la nube
            superficie.blit(nube['superficie2'], nube['rect'])
            return True
    return False

def jugadorGolpeaEdificio(superficie, rectanguloJugador, edificios):
    for edificio in edificios:
        if rectanguloJugador.colliderect(edificio['rect']):
            #cambia la imagen del edificio
            superficie.blit(edificio['superficie2'], edificio['rect'])
            return True
    return False

if __name__ == '__main__':
    jugadorGolpeaMoneda()
    jugadorGolpeaNube()
    jugadorGolpeaEdificio()
