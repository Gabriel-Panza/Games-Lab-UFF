from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.gameimage import *
import instrucao

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