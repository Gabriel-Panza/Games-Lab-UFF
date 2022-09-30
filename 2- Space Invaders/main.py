from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.sound import*
import menu
import Player 
import enemy
import ranking
import shooting
from pygame import mixer

################################################################################################################################
################################################ Inicializações / Start() ######################################################
################################################################################################################################
def game(vidas,movimento,movimentoInimigo,velProjetil,velProjetilInimigo,delay,delayInimigo,linha):
    # Instancio o tamanho da janela
    janela = Window(1280,720)

    # Instancio o teclado
    teclado = janela.get_keyboard()

    # Instancio os objetos do jogo
    espaco = GameImage("Image/espaço.jpg")
    player = Sprite("Image/nave.png",1)
    playerInvencible = Sprite("Image/naveInvencivel.png",1)
    
    # Defino a posiçao do player
    player.x = janela.width/2
    player.y = janela.height - player.height - 20
    
    # Instancio o som do jogo
    mixer.music.load("Music/Megalovania.wav")
    mixer.music.set_volume(0.4)
    mixer.music.play(-1)
       
    # Defino o frame per second
    FPS = 60
    clock = pygame.time.Clock()

    # Crio o vetor de projeteis inimigos
    listaProjeteisInimigos = []
    listaProjeteis = []
    listaProjeteisNavemae = []
    
    # Crio o vetor de inimigos
    matrizDeInimigos = []
    spawnNaveMae = 600
    movimentoInimigoBase = movimentoInimigo
    
    # Crio a pontuaçao que os aliens dão e o delay de invencibilidade
    score = 0
    delayInvencible = 0
    TomeiDano=False
    
    ################################################################################################################################
    ################################################ Gameloop / Update() ###########################################################
    ################################################################################################################################
    while (True):
        # Desenho o fundo
        espaco.draw()
                
        # Conto o fps
        clock.tick(FPS)
    
        # Volto pro menu do jogo
        if (teclado.key_pressed("ESC")):
            mixer.music.stop()
            menu.MainMenu()
            
        # Faço a movimentação do personagem
        Player.player(janela,teclado,player,movimento)
        
        # Crio os inimigos
        if (len(matrizDeInimigos)==0):
            enemy.spawn(linha,matrizDeInimigos)

        # Recrio a matriz apos matar todos os aliens
        for i in matrizDeInimigos:
            if (len(i)==0):
                vazio = True
            else:
                vazio = False
                break
        if vazio:    
            matrizDeInimigos.clear()
            movimentoInimigo=movimentoInimigoBase
            player.x= janela.width/2-player.width/2
            delayInvencible=180
            if linha<5:
                linha+=1
                movimentoInimigo*=1.03
                movimentoInimigoBase*=1.03
                enemy.spawn(linha,matrizDeInimigos)
            else:
                naveMae = enemy.spawn(linha,matrizDeInimigos)
        
        # Faço o movimento dos inimigos
        movimentoInimigo = enemy.moveInimigos(janela, matrizDeInimigos, movimentoInimigo)
        
        # Faço o movimento da nave mae
        if linha>=6:
            if spawnNaveMae>0:
                spawnNaveMae-=1
            else:
                if naveMae.y>0:
                    naveMae.draw()
                    naveMae.x += 100*janela.delta_time()
                    score = enemy.killNavemae(listaProjeteis,score,naveMae)

        # Chamo a funçao que irá lidar com a criaçao dos tiros
        if (teclado.key_pressed("SPACE") and delay==0):
            shooting.criaProjNave(player,listaProjeteis)
            delay = shooting.delay(delay,linha)
        if (delayInimigo==0):
            for i in matrizDeInimigos:
                for j in i:
                    shooting.criaProjInimigo(j,listaProjeteisInimigos)
            delayInimigo = shooting.delayInimigo(delayInimigo,linha)
            
        # Faço o movimento dos tiros
        shooting.tiroPlayer(janela,listaProjeteis,velProjetil)
        shooting.tiroInimigo(janela,listaProjeteisInimigos,velProjetilInimigo)
        if delay>0:
            delay-=1
        if delayInimigo>0:
            delayInimigo-=1
        
        if delayInvencible>0:
            delayInvencible-=1
            playerInvencible.x = player.x
            playerInvencible.y = player.y
            playerInvencible.draw()
        else:
            player.draw()
        
        # Verifico se alguem tomou hit
        vidasAntes = vidas
        score, movimentoInimigo = enemy.kill(listaProjeteis,matrizDeInimigos,score,linha,movimentoInimigo)
        if (vidas>0 and delayInvencible==0):
            for i in matrizDeInimigos:
                vidas = enemy.hit(vidas, player, i, listaProjeteisInimigos,listaProjeteisNavemae,score)
                if vidas != vidasAntes:
                    TomeiDano=True
        if TomeiDano:
            player.x= janela.width/2-player.width/2
            delayInvencible=180
            TomeiDano=False
        
        # Desenho os inimigos
        enemy.draw(matrizDeInimigos)
            
        # Perco o jogo
        if (vidas <= 0):
            mixer.music.stop()
            ranking.fimDoJogoDerrota(score) 
        for i in range(len(matrizDeInimigos)-1,-1,-1):
            for j in matrizDeInimigos[i]:
                if j[0].collided(player) or j[0].y>=player.y:
                    mixer.music.stop()
                    ranking.fimDoJogoDerrota(score)
         
        # Desenho a pontuação
        janela.draw_text(("Score: "), janela.width-130, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(score), janela.width-50, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Desenho a vida
        janela.draw_text(("Vidas: "), 0, 0, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(vidas), 75, 0, size=24, font_name="Arial", bold=True,color=[255, 0, 0])

        # Instancio o titulo da janela  
        janela.set_title("Space Invaders")
        
        # Finalizo o Gameloop
        janela.update()