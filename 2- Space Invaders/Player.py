from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
import pygame    

def player(janela,teclado,player,movimento):        
    if (teclado.key_pressed("A") or teclado.key_pressed("LEFT")):
        player.x -= movimento * janela.delta_time()
    if (teclado.key_pressed("D") or teclado.key_pressed("RIGHT")):
        player.x += movimento * janela.delta_time()
    if ((player.x+player.width/2)<0):
        player.set_position(janela.width-player.width/2, player.y)
    if ((player.x+player.width/2)>janela.width):
        player.set_position(0-player.width/2,player.y)