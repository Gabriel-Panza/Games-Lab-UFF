from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import*
import pygame
from pygame import mixer

def rank():
    janela = Window(1280,720)

    teclado = janela.get_keyboard()

    espaco = GameImage("Image/espaço.jpg")

    # Organizo o arquivo txt em ordem decrescente
    pontuacao = translate('Pontuacao.txt')
    pontuacao.reverse()
    
    # Desenho o fundo
    espaco.draw()
    
    # Desenho a pontuacao
    altura = 150
    limite=0
    for i,conteudo in enumerate(pontuacao):
        if i==0:
            continue
        if limite<5:
            janela.draw_text(str(i), (janela.width/2)-120, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
            janela.draw_text(("."), (janela.width/2)-100, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
            janela.draw_text(str(conteudo), (janela.width/2)-80, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
            altura+=45
            limite+=1
        
    while (True):
        # Volto pro menu
        if(teclado.key_pressed("ESC")):
            import menu
            menu.MainMenu()
        
        # Desenho o texto titulo na janela
        janela.draw_text(("RANKING"), (janela.width / 2)-130, 50, size=48, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Defino o titulo do jogo
        janela.set_title("Space Invaders")
        
        # Atualizo o GameLoop
        janela.update()

def fimDoJogoDerrota(score):
    janela = Window(1280,720)
    
    teclado = janela.get_keyboard()
    
    espaco = GameImage("Image/espaço.jpg")
    
    nome = input("Entre com o seu nome: ")
    
    # Instancio o som da Derrota
    mixer.music.load("Music/NarutoSadThemeFlute.wav")
    mixer.music.set_volume(0.4)
    mixer.music.play(-1)
    
    # Abro o arquivo (leitura)
    arquivo = open('Pontuacao.txt', 'r')
    conteudo = arquivo.readlines()

    # Insiro o conteúdo
    conteudo.append(str(score) + " - " + nome + ".")
    arquivo.close()
    
    # Abre novamente o arquivo (escrita)
    arquivo = open('Pontuacao.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
    
    while (True):
        # Desenho o fundo
        espaco.draw()

        # Volto pro menu
        if(teclado.key_pressed("ESC")):
            mixer.music.stop()
            import menu
            menu.MainMenu()
            
        janela.draw_text(("Você foi derrotado pela invasão! Boa sorte na proxima vez, recruta!"), (janela.width/2) - 400, janela.height/2 - 200, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Aperte 'ESC' para voltar ao menu"), (janela.width/2) - 250, (janela.height/2) - 100, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Instancio o titulo da janela  
        janela.set_title("Space Invaders")
        
        # Atualizo o GameLoop
        janela.update()
        
def translate(file):
    arquivo = open(file)
    pontuacao = []
    for elemento in arquivo:
        temp = elemento.split(".")
        for i in temp:
            pontuacao.append(i)
    arquivo.close()
    return pontuacao