from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
import main

def difficult():
        janela = Window(1280,720)

        teclado = janela.get_keyboard()

        mouseClick = janela.get_mouse()

        facil = Sprite("facil.png", 1)
        medio = Sprite("medio.png", 1)
        dificil = Sprite("dificil.png", 1)

        while (True):
            if(teclado.key_pressed("ESC")):
                import menu
                menu.MainMenu()
                
            if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(facil)):
                velInimigo = 1
                main.game(vidas=5, movimento=200,movimentoInimigo=100*velInimigo,velProjetil=900,velProjetilInimigo=300,delay=0,delayInimigo=100,linha=4)
            elif(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(medio)):
                velInimigo = 1.2
                main.game(vidas=5, movimento=200,movimentoInimigo=100*velInimigo,velProjetil=900,velProjetilInimigo=300,delay=0,delayInimigo=125,linha=4)
            elif(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(dificil)):
                velInimigo = 1.5
                main.game(vidas=5, movimento=200,movimentoInimigo=100*velInimigo,velProjetil=900,velProjetilInimigo=300,delay=0,delayInimigo=150,linha=4)
            
            facil.set_position(492, 400)
            medio.set_position(490, 460)
            dificil.set_position(508, 520)
            
            janela.draw_text(("DIFICULDADES"), (janela.width / 2)-225, 150, size=48, font_name="Arial", bold=True,color=[255, 255, 255])
            facil.draw()
            medio.draw()
            dificil.draw()
            
            janela.set_title("Space Invaders")

            janela.update()