import pygame

def recarga(dificuldade,delay):
    if dificuldade=="facil":
        delay = 180
    if dificuldade=="medio":
        delay = 150
    if dificuldade=="dificil":
        delay = 120
    return delay
def recargaCultistaInimigo(dificuldade,delayInimigo):
    if dificuldade=="facil":
        delayInimigo = 150
    if dificuldade=="medio":
        delayInimigo = 125
    if dificuldade=="dificil":
        delayInimigo = 100
    return delayInimigo
