from PPlay.window import*
from PPlay.keyboard import*
from PPlay.sound import*
import menu

def vitoria():
    # Instancio o tamanho da janela
    janela = Window(1280,720)
    
    # Inicializo o teclado
    teclado = janela.get_keyboard()
    
    # Adiciono musica
    pygame.mixer.music.load("Music/VictoryThemeSoundtrack.wav")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    while True:
        # Volto pro menu
        if (teclado.key_pressed("ESC")):
            pygame.mixer.music.stop()
            menu.menu()
        
        # Desenho os textos finais
        janela.draw_text(("Parabéns, nova Rainha. O reino está salvo desta criatura graças a você!"), (janela.width/2)-480, janela.height/2-100, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
        janela.draw_text(("Créditos:"), janela.width/2-100, janela.height-160, size=36, font_name="Arial", bold=True,color=[255, 255, 0])
        janela.draw_text(("Criadores: Gabriel Panza, João Vitor de Santana"), (janela.width/2)-360, janela.height-110, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
        janela.draw_text(("Colaboradores: Joao Vitor Moraes, Gustavo Medeiros"), (janela.width/2)-360, janela.height-60, size=28, font_name="Arial", bold=True,color=[255, 255, 0])

        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Finaliza o Gameloop
        janela.update()

def derrota():
    # Instancio o tamanho da janela
    janela = Window(1280,720)
    
    # Inicializo o teclado
    teclado = janela.get_keyboard()
    
    # Adiciono musica
    pygame.mixer.music.load("Music/DefeatThemeSoundtrack.wav")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    while True:
        # Volto pro menu
        if (teclado.key_pressed("ESC")):
            pygame.mixer.music.stop()
            menu.menu()
        
        # Desenho os textos finais
        janela.draw_text(("Eh... parece que você nao estava pronto mesmo. O reino sentirá sua falta, princesa!"), (janela.width/2)-555, janela.height/2-100, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
        janela.draw_text(("Créditos:"), janela.width/2-100, janela.height-160, size=36, font_name="Arial", bold=True,color=[255, 255, 0])
        janela.draw_text(("Criadores: Gabriel Panza, João Vitor de Santana"), (janela.width/2)-360, janela.height-110, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
        janela.draw_text(("Colaboradores: Joao Vitor Moraes, Gustavo Medeiros"), (janela.width/2)-360, janela.height-60, size=28, font_name="Arial", bold=True,color=[255, 255, 0])

        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Finaliza o Gameloop
        janela.update()