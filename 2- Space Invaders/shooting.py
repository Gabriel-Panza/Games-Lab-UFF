from PPlay.sprite import*
from PPlay.collision import*
import pygame
import random

def criaProjNave(player,listaProjeteis):
    # Crio o projetil
    projetil = Sprite("projetil.png",1)
    projetil.x = player.x + 50
    projetil.y = player.y - projetil.height
    listaProjeteis.append(projetil)

def tiroPlayer(janela,listaProjeteis,velProjetil):
    for i in listaProjeteis:
        i.y -= velProjetil*janela.delta_time()
        i.draw()
        if (i.y<-50):
            listaProjeteis.remove(i)

def criaProjInimigo(inimigo,listaProjeteisInimigos):
    # Crio o projetil
    projetilInimigo = Sprite("projetil2.png",1)
    projetilInimigo.x = inimigo[0].x + 50
    projetilInimigo.y = inimigo[0].y + projetilInimigo.height + 50
    if (random.random() < 0.3 and len(listaProjeteisInimigos)==0):
        listaProjeteisInimigos.append(projetilInimigo)

def tiroInimigo(janela,listaProjeteisInimigos,velProjetilInimigo):
    for i,projetilAlien in enumerate(listaProjeteisInimigos):
        projetilAlien.y += velProjetilInimigo*janela.delta_time()
        projetilAlien.draw()
        if (projetilAlien.y>janela.height):
            listaProjeteisInimigos.pop(i)

def delay(delay,linha):
    if linha==4:    
        delay = 40
    if linha==5:
        delay = 35
    if linha>=6:
        delay = 25
    return delay
def delayInimigo(delayInimigo,linha):
    if linha==4:
        delayInimigo = 100
    if linha==5:
        delayInimigo = 110
    if linha>=6:
         delayInimigo = 120
    return delayInimigo
