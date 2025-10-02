from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
import main
import ranking

def MainMenu():
    # Instancio a janela
    janela = Window(1280,720)

    # Instancio o mouse
    mouseClick = janela.get_mouse()
    
    # Instancio as imagens dos botões
    espaco = GameImage("Image/espaço.jpg")
    playButton=Sprite("Image/Play.png")
    diffButton=Sprite("Image/Dificuldade.png")
    rankingButton=Sprite("Image/Ranking.png")
    leaveButton=Sprite("Image/Sair.png")
    
    while (True):
        # Desenho o fundo
        espaco.draw()
        
        if (mouseClick.is_button_pressed(1)):
            if (mouseClick.is_over_object(playButton)):
                main.game(vidas=5,movimento=200,movimentoInimigo=100,velProjetil=900,velProjetilInimigo=300,delay=0,delayInimigo=100,linha=4)
            if (mouseClick.is_over_object(diffButton)):
                difficult()
            if (mouseClick.is_over_object(rankingButton)):
                ranking.rank()
            if (mouseClick.is_over_object(leaveButton)):
                sair()
        
        playButton.set_position(520, 250)
        diffButton.set_position(520, 325)
        rankingButton.set_position(520, 400)
        leaveButton.set_position(520, 475)
        
        janela.draw_text(("SPACE INVADERS"), (janela.width / 2)-225, 100, size=48, font_name="Arial", bold=True,color=[200, 200, 255])
        playButton.draw()
        diffButton.draw()
        rankingButton.draw()
        leaveButton.draw()
        
        janela.set_title("Space Invaders")

        janela.update()

def difficult():
    # Instancio a janela
    janela = Window(1280,720)

    # Instancio o teclado
    teclado = janela.get_keyboard()

    # Instancio o mouse
    mouseClick = janela.get_mouse()

    # Instancio as imagens dos botões
    facil = Sprite("Image/facil.png", 1)
    medio = Sprite("Image/medio.png", 1)
    dificil = Sprite("Image/dificil.png", 1)
    
    # Retiro o bug de doubleClick
    retBug = 300
    
    while (True):
        if(teclado.key_pressed("ESC")):
            MainMenu()
            
        if (mouseClick.is_button_pressed(1) and retBug==0):
            if (mouseClick.is_over_object(facil)):
                main.game(vidas=5, movimento=200,movimentoInimigo=100,velProjetil=900,velProjetilInimigo=300,delay=0,delayInimigo=100,linha=4)
            elif(mouseClick.is_over_object(medio)):
                main.game(vidas=5, movimento=200,movimentoInimigo=120,velProjetil=900,velProjetilInimigo=300,delay=0,delayInimigo=125,linha=4)
            elif(mouseClick.is_over_object(dificil)):
                main.game(vidas=5, movimento=200,movimentoInimigo=150,velProjetil=900,velProjetilInimigo=300,delay=0,delayInimigo=150,linha=4)
        
        if retBug>0:
            retBug-=1
        
        facil.set_position(492, 250)
        medio.set_position(490, 350)
        dificil.set_position(508, 450)
        
        janela.draw_text(("DIFICULDADES"), (janela.width / 2)-225, 100, size=48, font_name="Arial", bold=True,color=[200, 200, 255])
        facil.draw()
        medio.draw()
        dificil.draw()
        
        janela.set_title("Space Invaders")

        janela.update()

def sair():
    # Instancio a janela
    janela = Window(1280,720)

    # Instancio o teclado
    teclado = janela.get_keyboard()

    # Instancio o mouse
    mouseClick = janela.get_mouse()

    # Instancio as imagens dos botões
    simButton = Sprite("Image/sim.png", 1)
    naoButton = Sprite("Image/nao.png", 1)

    while (True):
        janela.draw_text(("DESEJA MESMO SAIR?"), (janela.width / 2)-275, 150, size=48, font_name="Arial", bold=True,color=[255, 255, 255])
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(simButton)):
            janela.close()
        if((mouseClick.is_button_pressed(1) and mouseClick.is_over_object(naoButton)) or (teclado.key_pressed("ESC"))):
            MainMenu()
        
        simButton.set_position((janela.width/2) -300, (janela.height/2)+100)
        naoButton.set_position((janela.width/2) +100, (janela.height/2)+100)
        
        simButton.draw()
        naoButton.draw()
        
        janela.update()
MainMenu()