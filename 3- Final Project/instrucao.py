from PPlay.window import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.sound import *
import main

def instrucao(movimentoInimigo):
    # Instancio a janela
    janela = Window(1280,720)

    # Inicializo o teclado
    teclado = janela.get_keyboard()

    # Instancio o mouse
    mouseClick = janela.get_mouse()
    
    # Instancio as imagens dos botões
    playButton=Sprite("Images/Play.png",1)
    playButton.set_position(janela.width/2 - playButton.width/2, janela.height - 150)

    while True:
        # Volto pro menu
        if (teclado.key_pressed("ESC")):
            import menu
            menu.menu()
            
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(playButton)):
            if(movimentoInimigo==200):
                main.game(vidas=5,vidasInimigo=3,movimento=250,movimentoInimigo=movimentoInimigo,velProjetil=600,velProjetilInimigo=300,delay=0,delayInimigo=100)
            elif(movimentoInimigo==250):
                main.game(vidas=5,vidasInimigo=5,movimento=250,movimentoInimigo=movimentoInimigo,velProjetil=600,velProjetilInimigo=300,delay=0,delayInimigo=100)
            elif(movimentoInimigo==300):
                main.game(vidas=3,vidasInimigo=5,movimento=250,movimentoInimigo=movimentoInimigo,velProjetil=600,velProjetilInimigo=300,delay=0,delayInimigo=100)
        # Desenho o fundo
        janela.set_background_color([0,0,0])

        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Desenho as instrucoes
        janela.draw_text(("Instruçoes"), (janela.width / 2)-128, 100, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        janela.draw_text(("Alguns eventos no jogo dependem que certas condiçoes aconteçam."), 100, 150, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Portanto, um pop-up com um objetivo irá aparecer, após caminhar um pouco."), 100, 200, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Siga os objetivos e salve o reino."), 100, 250, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Controles"), (janela.width / 2)-128, 300, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        janela.draw_text(("Pressione 'W,A,S,D' ou as setas do teclado para andar."), 100, 350, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Pressione 'Space' para atirar."), 100, 400, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Pressione 'Left_Shift' para dar um dash para frente. Você pode juntar até 3 cargas."), 100, 450, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Pressione 'Left_Control' para criar um clone e desviar de seus inimigos."), 100, 500, size=28, font_name="Arial", bold=True,color=[255, 255, 255])

        # Desenho o botao
        playButton.draw()
        
        # Atualizo o gameLoop
        janela.update()
