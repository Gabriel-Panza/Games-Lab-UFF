from PPlay.window import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.gameimage import*
from PPlay.sound import *
import instrucao
import diff
import sair

def menu():    
    # Instancio a janela
    janela = Window(1280,720)

    # Instancio o mouse
    mouseClick = janela.get_mouse()
    
    # Instancio as imagens dos botões
    playButton=Sprite("Images/Play.png",1)
    diffButton=Sprite("Images/Dificuldade.png",1)
    leaveButton=Sprite("Images/Sair.png",1)

    # Instancio o fundo
    fundo = GameImage("Images/FundoInicial.jpg")
    
    while (True):
        # Desenho  o fundo
        fundo.draw()
        
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(playButton)):
            instrucao.instrucao(movimentoInimigo=250)
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(diffButton)):
            diff.diff(janela)
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(leaveButton)):
            sair.sair(janela)
        
        playButton.set_position(525, 260)
        diffButton.set_position(525, 400)
        leaveButton.set_position(525, 540)
        
        playButton.draw()
        diffButton.draw()
        leaveButton.draw()
        
        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        janela.draw_text(("A Ascensão da Feiticeira"), (janela.width / 2)-290, 50, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        
        # Atualizo o Gameloop
        janela.update()
menu()