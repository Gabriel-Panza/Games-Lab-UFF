from PPlay.window import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.gameimage import*
from PPlay.sound import *
import instrucao

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
            diff(janela)
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(leaveButton)):
            sair(janela)
        
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
def diff(janela):
    teclado = janela.get_keyboard()

    mouseClick = janela.get_mouse()

    facil = Sprite("Images/facil.png", 1)
    medio = Sprite("Images/medio.png", 1)
    dificil = Sprite("Images/dificil.png", 1)
    while (True):
        if(teclado.key_pressed("ESC")):
            import menu
            menu.menu()
        
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(facil)):
            instrucao.instrucao(movimentoInimigo=200)
        elif(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(medio)):
            instrucao.instrucao(movimentoInimigo=250)
        elif(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(dificil)):
            instrucao.instrucao(movimentoInimigo=300)
        
        facil.set_position(520, 250)
        medio.set_position(520, 300)
        dificil.set_position(535, 350)
        
        janela.draw_text(("DIFICULDADES"), (janela.width / 2)-210, 50, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        facil.draw()
        medio.draw()
        dificil.draw()
        
        janela.set_title("Space Invaders")

        janela.update()

def diff(janela):
    teclado = janela.get_keyboard()

    mouseClick = janela.get_mouse()

    facil = Sprite("Images/facil.png", 1)
    medio = Sprite("Images/medio.png", 1)
    dificil = Sprite("Images/dificil.png", 1)
    while (True):
        if(teclado.key_pressed("ESC")):
            import menu
            menu.menu()
        
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(facil)):
            instrucao.instrucao(movimentoInimigo=200)
        elif(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(medio)):
            instrucao.instrucao(movimentoInimigo=250)
        elif(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(dificil)):
            instrucao.instrucao(movimentoInimigo=300)
        
        facil.set_position(520, 250)
        medio.set_position(520, 300)
        dificil.set_position(535, 350)
        
        janela.draw_text(("DIFICULDADES"), (janela.width / 2)-210, 50, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        facil.draw()
        medio.draw()
        dificil.draw()
        
        janela.set_title("Space Invaders")

        janela.update()

def sair(janela):
    teclado = janela.get_keyboard()

    mouseClick = janela.get_mouse()

    simButton = Sprite("Images/Sim.png", 1)
    naoButton = Sprite("Images/Nao.png", 1)
    while (True):
        if(teclado.key_pressed("ESC")):
            menu()
        
        janela.draw_text(("DESEJA MESMO SAIR?"), (janela.width / 2)-280, 100, size=48, font_name="Arial", bold=True,color=[255, 0, 255])
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(simButton)):
            janela.close()
        if((mouseClick.is_button_pressed(1) and mouseClick.is_over_object(naoButton)) or (teclado.key_pressed("ESC"))):
            import menu
            menu()
        
        simButton.set_position((janela.width/2) -120, (janela.height/2)-50)
        naoButton.set_position((janela.width/2) -120, (janela.height/2)+110)
        
        simButton.draw()
        naoButton.draw()
        
        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Atualizo o Gameloop
        janela.update()

