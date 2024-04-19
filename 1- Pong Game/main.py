from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from PPlay.keyboard import *

################################################################################################################################
################################################ Inicializações / Start() ######################################################
################################################################################################################################

# Instancio o tamanho da janela
janela = Window(1280,720)

# Inicializo o teclado
teclado = janela.get_keyboard()

# Instancio as imagens q serão sobrepostas na minha janela
fundo = GameImage("sprites/Stadium.jpg")
bola = Sprite("sprites/bola.png",1)
padE = Sprite("sprites/padE.png",1)
padD = Sprite("sprites/padD.png",1)

# Instancio a posição inicial da bola para que ela fique no centro da tela
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2

padE.y= janela.height/2 - padE.height/2
padE.x= +25
padD.y= janela.height/2 - padD.height/2
padD.x= (janela.width - padD.width/2) - 40

# Defino a velocidade dos gameObjects
vBola_x = 0
vBola_y = 0
vPadE = 550
vPadD = 500

# Defino o tempo inicial pro deltaTime
tempoInicial = time.time()
frames=0

# Defino a pontuação inicial
pontEsquerdo = 0
pontDireito = 0

################################################################################################################################
##################################################### Game Loop / Update() #####################################################
################################################################################################################################
while(True):
    # Crio o deltaTime
    tempoAtual = time.time()
    deltaTime = tempoAtual - tempoInicial
    tempoInicial = tempoAtual
    
    # Gero o framerate a ser desenhado
    if frames==0:
        frames=300
        framerate = deltaTime  
    if frames>0:
        frames-=1
          
    # Inicio o jogo com a bola parada no meio
    if ((bola.x == janela.width/2 - bola.width/2) and (teclado.key_pressed("space"))):
        vBola_x = 800
        vBola_y = 800
    
    # Faço a bola acompanhar o pad após tomar gol
    if ((vBola_x == 0) and (bola.y == padE.y)):
        if (teclado.key_pressed("w")):
            bola.y -= vPadE * deltaTime
        if (teclado.key_pressed("s")):
            bola.y += vPadE * deltaTime
            
    # Se a bola ta parada, adicione a velocidade
    if (teclado.key_pressed("space")):
        if (bola.y == padE.y):
            vBola_x = 800
            vBola_y = 800
        if (bola.y == padD.y):
            vBola_x = -800
            vBola_y = -800
    
    # Atualizo a posição da bola a cada frame
    bola.x += vBola_x * deltaTime
    bola.y += vBola_y * deltaTime
    
    # Adiciono os inputs do teclado e a AI no programa
    if (teclado.key_pressed("w")) and (padE.y>0):
        padE.y -= vPadE * deltaTime
    if (teclado.key_pressed("s")) and (padE.y <= janela.height - padE.height):
        padE.y += vPadE * deltaTime
        
    if (padD.y > bola.y and abs(padD.y - bola.y) > 10) and (padD.y>0): 
        padD.y -= vPadD * deltaTime
    if (padD.y < bola.y and abs(padD.y - bola.y) > 10) and (padD.y <= janela.height - padE.height):
        padD.y += vPadD * deltaTime
        
    # Colisão da bola com a janela
    if (bola.y < -5) or (bola.y + bola.height > janela.height+5):
        vBola_y *= -1
        
    if (bola.x < +5):
        bola.x = padD.x - 65
        bola.y = padD.y
        vBola_x = 0
        vBola_y = 0
        pontEsquerdo+=1

    if (bola.x + bola.width > janela.width-5):
        bola.x = padE.x + 65
        bola.y = padE.y
        vBola_x = 0
        vBola_y = 0
        pontDireito+=1

    # Colisão da bola com o pad
    if bola.collided(padE):
        bola.x += 1
        vBola_x *= -1
    if bola.collided(padD):
        bola.x -= 1
        vBola_x *= -1
        
    # Finaliza o programa ao alcançar certa pontuação
    if pontEsquerdo>=5 or pontDireito>=5:
        time.sleep(1)
        janela.close()
    
    # Define um titulo pra janela
    janela.set_title("PokePong")
    
    # Chamo/Desenho as imagens instanciadas no começo
    fundo.draw()
    bola.draw()
    padE.draw()
    padD.draw()
    
    # Pontuação
    janela.draw_text(str(pontDireito), (janela.width / 2) - 75, 60, size=48, font_name="Arial", bold=True,color=[0, 0, 0])
    janela.draw_text(str(pontEsquerdo), (janela.width / 2) + 60, 60, size=48, font_name="Arial", bold=True,color=[0, 0, 0])
    
    # Fps
    janela.draw_text(("FPS: "), 0, 0, size=24, font_name="Arial", bold=True,color=[0, 0, 0])
    janela.draw_text(str(int(framerate*10000)), 65, 0, size=24, font_name="Arial", bold=True,color=[0, 0, 0])

    #Finaliza o Gameloop
    janela.update()