import os,sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

from PPlay.window import*
from PPlay.animation import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.gameobject import*
from PPlay.collision import*
from PPlay.keyboard import*
from PPlay.mouse import*
from PPlay.sound import*
import menu
import Player
import enemy
import shooting
import EndOfGame

################################################################################################################################
################################################ Inicializações / Start() ######################################################
################################################################################################################################

def game(vidas,vidasInimigo,movimento,movimentoInimigo,velProjetil,velProjetilInimigo,delay,delayInimigo):
    # Instancio o tamanho da janela
    janela = Window(1280,720)
    
    # Inicializo o teclado
    teclado = janela.get_keyboard()
    
    # Inicializo o mouse
    mouseClick = janela.get_mouse()
    
    # Adiciono a variavel q trocará de musica
    musica=0
    
    # Instancio os cenários
    cenarioFloresta = GameImage("Images/Floresta.jpg")
    chaoFloresta = Sprite("Images/FlorestaChao.png",1)
    chaoFloresta.y = janela.height-chaoFloresta.height
    saidaFloresta = Sprite("Images/FlorestaSaida.png",1)
    saidaFloresta.x = janela.width/2+50
    saidaFloresta.y = janela.height-saidaFloresta.height-300
    
    cenarioCastelo = GameImage("Images/Castelo.jpg")
    chaoCastelo = Sprite("Images/CasteloChao.png",1)
    chaoCastelo.y = janela.height-chaoCastelo.height
    
    cenarioDungeon = GameImage("Images/Dungeon.jpg")
    chaoDungeon = Sprite("Images/DungeonChao.png",1) 
    chaoDungeon.y = 60
    trapDungeonOff = Sprite("Images/Dungeontrapmap.png",1)
    trapDungeonOn = Sprite("Images/Dungeontrapmaphit.png",1)
    
    cenario=1
     
    # Instancio os objetos
    sangue = Sprite("Images/sangue.png", 1)
    sangue.set_position(janela.width-sangue.width-10,janela.height-sangue.height-100)
    
    pop_up = Sprite("Images/popUp.png",1)
    pop_up.set_position(janela.width/2 - pop_up.width/2, janela.height/2 - pop_up.height/2)
    
    continueButton = Sprite("Images/Continue.png",1)
    continueButton.set_position(pop_up.x+135, pop_up.y+pop_up.height)
    
    objetivoFloresta = Sprite("Images/ObjetivoFloresta.png",1)
    objetivoFloresta.set_position(janela.width-objetivoFloresta.width,0)
    objetivoCastelo = Sprite("Images/ObjetivoCastelo.png",1)
    objetivoCastelo.set_position(janela.width-objetivoCastelo.width,0)
    objetivoDungeon = Sprite("Images/ObjetivoDungeon.png",1)
    objetivoDungeon.set_position(janela.width-objetivoDungeon.width,0)
    
    # Instancio a Emih
    player_Esq_Run = Sprite("Images/Emih_invertido.png", 8)
    player_Esq_Run.x = 0
    player_Esq_Run.y = janela.height-player_Esq_Run.height
    player_Esq_Run.set_total_duration(1000)
    
    player_Esq = Sprite("Images/Emih_invertido_Idle.png", 1)
    player_Esq.x = 0
    player_Esq.y = janela.height-player_Esq.height
    
    player_Clone_Esq = Sprite("Images/Emih_Back_Esq.png", 1)
    player_Clone_Esq.x = 0
    player_Clone_Esq.y = janela.height-player_Clone_Esq.height

    player_Dash_Esq=Sprite("Images/Emih_Dash_Esq.png", 1)
    player_Dash_Esq.x = 0
    player_Dash_Esq.y = janela.height-player_Dash_Esq.height
    
    player_Dir_Run = Sprite("Images/Emih.png", 8)
    player_Dir_Run.x = 0
    player_Dir_Run.y = janela.height-player_Dir_Run.height
    player_Dir_Run.set_total_duration(1000)
    
    player_Dir = Sprite("Images/Emih_Idle.png", 1)
    player_Dir.x = 0
    player_Dir.y = janela.height-player_Dir.height
    
    player_Clone_Dir = Sprite("Images/Emih_Back_Dir.png", 1)
    player_Clone_Dir.x = 0
    player_Clone_Dir.y = janela.height-player_Clone_Dir.height

    player_Dash_Dir = Sprite("Images/Emih_Dash.png", 1)
    player_Dash_Dir.x = 0
    player_Dash_Dir.y = janela.height-player_Dash_Dir.height

    player_Clone = player_Clone_Dir
    player = player_Dir
    hitBoxPlayer = player_Dir
    vidasPlayer = vidas

    # Instancio o minotauro
    minotauro_Esq_Run = Sprite("Images/MinotauroEsq.png", 8)
    minotauro_Esq_Run.x = janela.width-minotauro_Esq_Run.width
    minotauro_Esq_Run.y = janela.height-minotauro_Esq_Run.height
    minotauro_Esq_Run.set_total_duration(1000)
    
    minotauro_Dir_Run = Sprite("Images/MinotauroDir.png", 8)
    minotauro_Dir_Run.x = janela.width-minotauro_Dir_Run.width
    minotauro_Dir_Run.y = janela.height-minotauro_Dir_Run.height
    minotauro_Dir_Run.set_total_duration(1000)
    
    minotauro_Esq = Sprite("Images/Minotauro_Idle_Esq.png", 6)
    minotauro_Esq.x = janela.width-minotauro_Esq.width
    minotauro_Esq.y = janela.height-minotauro_Esq.height
    minotauro_Esq.set_total_duration(1000)

    minotauro_Dir = Sprite("Images/Minotauro_Idle_Dir.png", 6)
    minotauro_Dir.x = janela.width-minotauro_Dir.width
    minotauro_Dir.y = janela.height-minotauro_Dir.height
    minotauro_Dir.set_total_duration(1000)

    minotauro_Death_Dir = Sprite("Images/Minotauro_Death_Dir.png", 6)
    minotauro_Death_Dir.x = janela.width - minotauro_Death_Dir.width
    minotauro_Death_Dir.y = janela.height - minotauro_Death_Dir.height
    minotauro_Death_Dir.set_total_duration(1000)

    minotauro_Death_Esq = Sprite("Images/Minotauro_Death_Esq.png", 6)
    minotauro_Death_Esq.x = janela.width-minotauro_Death_Esq.width
    minotauro_Death_Esq.y = janela.height-minotauro_Death_Esq.height
    minotauro_Death_Esq.set_total_duration(1000)

    minotauro_attack = Sprite("Images/Minotauro_attack.png", 9) 
    minotauro_attack.x = janela.width - minotauro_attack.width
    minotauro_attack.y = janela.height - minotauro_attack.height
    minotauro_attack.set_total_duration(1000)

    minotauro_attack_Esq = Sprite("Images/Minotauro_attack_Esq.png", 9)
    minotauro_attack_Esq.x = janela.width-minotauro_attack_Esq.width
    minotauro_attack_Esq.y = janela.height-minotauro_attack_Esq.height
    minotauro_attack_Esq.set_total_duration(1000)

    minotauro_Rage_Dir = Sprite("Images/Minotaur_Rage_Dir.png", 1)
    minotauro_Rage_Dir.x = janela.width-minotauro_Rage_Dir.width
    minotauro_Rage_Dir.y = janela.height-minotauro_Rage_Dir.height

    minotauro_Rage_Esq = Sprite("Images/Minotaur_Rage_Esq.png", 1)
    minotauro_Rage_Esq.x = janela.width-minotauro_Rage_Esq.width
    minotauro_Rage_Esq.y = janela.height-minotauro_Rage_Esq.height

    minotauro = minotauro_Esq
    vidasMinotauro = vidasInimigo
    
    # Instancio o cultista
    cultista_Esq_Run = Sprite("Images/CultistaEsq.png", 10)
    cultista_Esq_Run.x = janela.width-minotauro_Esq_Run.width
    cultista_Esq_Run.y = janela.height-cultista_Esq_Run.height
    cultista_Esq_Run.set_total_duration(1000)
    
    cultista_Dir_Run = Sprite("Images/CultistaDir.png", 10)
    cultista_Dir_Run.x = janela.width-minotauro_Dir_Run.width
    cultista_Dir_Run.y = janela.height-cultista_Dir_Run.height
    cultista_Dir_Run.set_total_duration(1000)
    
    cultista_Esq = Sprite("Images/Cultista_Idle_Esq.png", 10)
    cultista_Esq.x = janela.width-minotauro_Esq.width
    cultista_Esq.y = janela.height-cultista_Esq.height
    cultista_Esq.set_total_duration(1000)

    cultista_Morte_Esq = Sprite("Images/Cultista_Morte_Esq.png", 10)
    cultista_Morte_Esq.x = janela.width-cultista_Morte_Esq.width
    cultista_Morte_Esq.y = janela.height-cultista_Morte_Esq.height
    cultista_Morte_Esq.set_total_duration(1000)
    
    cultista_Dir = Sprite("Images/Cultista_Idle_Dir.png", 10)
    cultista_Dir.x = janela.width-cultista_Dir.width
    cultista_Dir.y = janela.height-cultista_Dir.height
    cultista_Dir.set_total_duration(1000)
    
    cultista_Morte_Dir = Sprite("Images/Cultista_Morte_Dir.png", 10)
    cultista_Morte_Dir.x = janela.width-cultista_Morte_Dir.width
    cultista_Morte_Dir.y = janela.height-cultista_Dir.height
    cultista_Morte_Dir.set_total_duration(1000)

    cultista_Attack_Esq = Sprite("Images/cultista_Attack_Esq.png", 10)
    cultista_Attack_Esq.x = janela.width-cultista_Attack_Esq.width
    cultista_Attack_Esq.y = janela.height-cultista_Attack_Esq.height
    cultista_Attack_Esq.set_total_duration(1000)

    cultista = cultista_Esq
    vidasCultista = vidasInimigo
    
    # Instancio os guardas
    guardas_Esq_Run = Sprite("Images/GuardasEsq.png", 6)
    guardas_Esq_Run.x = janela.width-guardas_Esq_Run.width
    guardas_Esq_Run.y = janela.height-guardas_Esq_Run.height
    guardas_Esq_Run.set_total_duration(1000)
    
    guardas_Dir_Run = Sprite("Images/GuardasDir.png", 6)
    guardas_Dir_Run.x = janela.width-guardas_Dir_Run.width
    guardas_Dir_Run.y = janela.height-guardas_Dir_Run.height
    guardas_Dir_Run.set_total_duration(1000)
    
    guardas_Esq = Sprite("Images/Guardas_Idle_Esq.png", 6)
    guardas_Esq.x = janela.width-guardas_Esq.width
    guardas_Esq.y = janela.height-guardas_Esq.height
    guardas_Esq.set_total_duration(1000)

    guardas_Morte_Esq = Sprite("Images/Guardas_Morte_Esq.png", 6)
    guardas_Morte_Esq.x = janela.width-guardas_Morte_Esq.width
    guardas_Morte_Esq.y = janela.height-guardas_Morte_Esq.height
    guardas_Morte_Esq.set_total_duration(1000)

    guardas_Dir = Sprite("Images/Guardas_Idle_Dir.png", 6)
    guardas_Dir.x = janela.width-guardas_Dir.width
    guardas_Dir.y = janela.height-guardas_Dir.height
    guardas_Dir.set_total_duration(1000)
    
    guardas_Morte_Dir = Sprite("Images/Guardas_Morte_Dir.png", 6)
    guardas_Morte_Dir.x = janela.width-guardas_Morte_Dir.width
    guardas_Morte_Dir.y = janela.height-guardas_Morte_Dir.height
    guardas_Morte_Dir.set_total_duration(1000)

    guardas_Attack_Dir = Sprite("Images/Guardas_Attack_Direita.png", 6)
    guardas_Attack_Dir.x = janela.width-guardas_Attack_Dir.width
    guardas_Attack_Dir.y = janela.height-guardas_Attack_Dir.height
    guardas_Attack_Dir.set_total_duration(1000)

    guardas_Attack_Esq = Sprite("Images/Guardas_Attack_Esquerda.png", 6)
    guardas_Attack_Esq.x = janela.width-guardas_Attack_Esq.width
    guardas_Attack_Esq.y = janela.height-guardas_Attack_Esq.height
    guardas_Attack_Esq.set_total_duration(1000)
    
    guarda = guardas_Esq
    vidasGuarda = vidasInimigo
    
    # Instancio o Caebralum
    caebralum_Esq_Run = Sprite("Images/CaebralumEsq.png", 5)
    caebralum_Esq_Run.x = janela.width-caebralum_Esq_Run.width
    caebralum_Esq_Run.y = janela.height-caebralum_Esq_Run.height
    caebralum_Esq_Run.set_total_duration(1000)
    
    caebralum_Dir_Run = Sprite("Images/CaebralumDir.png", 5)
    caebralum_Dir_Run.x = janela.width-caebralum_Dir_Run.width
    caebralum_Dir_Run.y = janela.height-caebralum_Dir_Run.height
    caebralum_Dir_Run.set_total_duration(1000)
    
    caebralum_Esq = Sprite("Images/Caebralum_Idle_Esq.png", 1)
    caebralum_Esq.x = janela.width-caebralum_Esq.width
    caebralum_Esq.y = janela.height-caebralum_Esq.height
    
    caebralum_Dir = Sprite("Images/Caebralum_Idle_Dir.png", 1)
    caebralum_Dir.x = janela.width-caebralum_Dir.width
    caebralum_Dir.y = janela.height-caebralum_Dir.height
    
    caebralumFireCircle = Sprite("Images/CaebralumCircleFire.png", 2)
    caebralumFireCircle.x = janela.width-caebralumFireCircle.width
    caebralumFireCircle.y = janela.height-caebralumFireCircle.height
    caebralumFireCircle.set_total_duration(500)
    
    caebralumFireCircle_Idle = Sprite("Images/CaebralumCircleFire_Idle.png", 1)
    caebralumFireCircle_Idle.x = janela.width-caebralumFireCircle.width
    caebralumFireCircle_Idle.y = janela.height-caebralumFireCircle.height
    
    caebralum = caebralum_Esq
    hitBoxFireCircle = caebralumFireCircle_Idle
    vidasCaebralum = vidasInimigo * 2
    
    # Crio o vetor de projeteis aliados e sua direçao
    listaProjeteisE = []
    listaProjeteisD = []
    checkPos=0

    # Crio o vetor de projeteis inimigos
    listaProjeteisInimigos = []
    checkPosInim=0
    velProjetilInimigoNormal=velProjetilInimigo
    velProjetilInimigoRage=velProjetil*1.5
    
    # Crio as variaveis de estado dos mobs
    summon=False
    spawn=0
    delayRugido=1
    
    # Crio as variaveis de estado do player/mapa
    invencibility=0
    trapTime=1
    
    # Crio as variaveis de estado das habilidades
    clone=0
    delayClone=0
    checkDash=0
    dashTime=0
    delayDash=0
    delayDash2=0
    tempoDeRecargaTiro=0
    cargaDeDash=1
    tempoDeRecargaClone=0
    
    # Crios os diferentes movimentos para cada dificuldade
    movimentoNormal=movimentoInimigo
    if movimentoInimigo==200:
        dificuldade="facil"
        movimentoRage=400
    if movimentoInimigo==250:
        dificuldade="medio"
        movimentoRage=500
    if movimentoInimigo==300:
        dificuldade="dificil"
        movimentoRage=600
    movimentoInimigoBoss=movimentoInimigo/2 + 50
    movimentoRageBoss=movimentoRage/2 + 50
    
    # Defino o frame per second
    FPS = 60
    clock = pygame.time.Clock()

    ################################################################################################################################
    ##################################################### Game Loop / Update() #####################################################
    ################################################################################################################################
    while(True):
        # Limito o Framerate
        clock.tick(FPS)
        
        # Volto pro menu
        if (teclado.key_pressed("ESC")):
            pygame.mixer.music.stop()
            menu.menu()
        
        # Desenho o cenario desejado e a placa que indica o que precisa ser feito
        if cenario==1:
            cenarioFloresta.draw()
            chao = chaoFloresta
            saida = saidaFloresta
            objetivo = objetivoFloresta
            
            # Inicio a musica de batalha
            if musica==0:
                pygame.mixer.music.load("Music/ForestBattle.wav")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)
                musica+=1
            
            # Crio a movimentacao do minotauro
            checkPosInim = enemy.moveEnemy(janela,player,minotauro,movimentoInimigo,checkPosInim)
            if checkPosInim==0:
                if (vidasMinotauro>3):
                    if (minotauro.x<player.x and minotauro.x>0):
                        minotauro = enemy.SetEnemy(minotauro_Dir_Run,minotauro)
                        minotauro.update()
                    if minotauro.x==player.x and minotauro.y == player.y:
                        minotauro = enemy.SetEnemy(minotauro_Dir,minotauro)
                    if (invencibility>80):
                        minotauro = enemy.SetEnemyAttack(minotauro_attack,minotauro,cenario,invencibility)
                        minotauro.update()
                elif (vidasMinotauro<=3) and (vidasMinotauro>0):
                    minotauro = enemy.SetEnemy(minotauro_Rage_Dir,minotauro)
                    minotauro.draw()
            else:
                if (vidasMinotauro>3):
                    if (minotauro.x>player.x and minotauro.x<janela.width):
                        minotauro = enemy.SetEnemy(minotauro_Esq_Run,minotauro)
                        minotauro.update()
                    if minotauro.x==player.x and minotauro.y==player.y:
                        minotauro = enemy.SetEnemy(minotauro_Esq,minotauro)
                    if (invencibility>80):
                        minotauro = enemy.SetEnemyAttack(minotauro_attack_Esq,minotauro,cenario,invencibility)
                        minotauro.draw()
                elif (vidasMinotauro<=3) and (vidasMinotauro>0):
                    minotauro = enemy.SetEnemy(minotauro_Rage_Esq,minotauro)
                    minotauro.draw()
            
            if summon:
                if (vidasMinotauro>0):
                    minotauro.draw()
                    if (vidasMinotauro<=(vidasInimigo/2 + 0.5)):
                        #auraMinotauro.draw()
                        movimentoInimigo=movimentoRage
                    vidasMinotauro = enemy.hit(listaProjeteisE,listaProjeteisD,minotauro,vidasMinotauro)
                    enemy.lifeMobs(minotauro,minotauro_Dir,vidasMinotauro,dificuldade)
                    if invencibility ==0:
                        vidasPlayer,invencibility = enemy.enemy_melee_attack(minotauro,player,vidasPlayer,invencibility)
                else:
                    movimentoInimigo=movimentoNormal
            
            if ((player.collided(saida)) and vidasMinotauro<=0):
                clone=0
                cenario+=1
                player.set_position(0,janela.height-player.height)
                summon=False
                pygame.mixer.music.stop()
        
        elif cenario==2:
            cenarioCastelo.draw()
            sangue.draw()
            chao = chaoCastelo
            objetivo = objetivoCastelo
            
            # Inicio a musica de batalha
            if musica==1:
                pygame.mixer.music.load("Music/CastleBattle.wav")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)
                musica+=1
            
            # Crio a movimentacao do guarda
            checkPosInim = enemy.moveEnemy(janela,player,guarda,movimentoInimigo,checkPosInim)
            if checkPosInim==0:
                if (guarda.x<player.x and guarda.x>0):
                    guarda = enemy.SetEnemy(guardas_Dir_Run,guarda)
                    guarda.update()
                if guarda.x == player.x and guarda.y==player.y:
                    guarda = enemy.SetEnemy(guardas_Dir,guarda)
                if (invencibility>80):
                    guarda = enemy.SetEnemyAttack(guardas_Attack_Dir,guarda,cenario,invencibility)
                    guarda.update()
            else:
                if (guarda.x>player.x and minotauro.x<janela.width):
                    guarda = enemy.SetEnemy(guardas_Esq_Run,guarda)
                    guarda.update()
                if guarda.x == player.x and guarda.y==player.y:
                    guarda = enemy.SetEnemy(guardas_Esq,guarda)
                if (invencibility>80):
                    guarda = enemy.SetEnemyAttack(guardas_Attack_Esq,guarda,cenario,invencibility)
                    guarda.update()
            # Crio a movimentacao do cultista
            enemy.moveEnemyRanged(janela,player,cultista,movimentoInimigo)
            if (delayInimigo<30) or (delayInimigo>115):
                cultista = enemy.SetEnemy(cultista_Attack_Esq,cultista)
                cultista.update()
            else:
                if (cultista.x>player.x and cultista.x<janela.width and delayInimigo>10):
                    cultista = enemy.SetEnemy(cultista_Esq_Run,cultista)
                    cultista.update()
                if cultista.x == player.x and cultista.y == player.y and delayInimigo>10:
                    cultista = enemy.SetEnemy(cultista_Esq,cultista)
            
            if summon:
                # Desenho o cultista
                if (vidasCultista>0):
                    cultista.draw()
                    if (vidasCultista<=round(vidasInimigo/2 + 0.5)):
                        velProjetilInimigo=velProjetilInimigoRage
                    vidasCultista = enemy.hit(listaProjeteisE,listaProjeteisD,cultista,vidasCultista)
                    enemy.lifeMobs(cultista,cultista,vidasCultista,dificuldade)
                    if invencibility==0:
                        vidasPlayer,invencibility = enemy.enemy_ranged_attack(listaProjeteisInimigos,player,vidasPlayer,invencibility)
                    if (delayInimigo==0):
                        enemy.criaProjetilInimigo(cultista,listaProjeteisInimigos)
                        delayInimigo = shooting.recargaCultistaInimigo(dificuldade,delayInimigo)
                    
                else:
                    velProjetilInimigo=velProjetilInimigoNormal

                # Desenho o guarda
                if (vidasGuarda>0):
                    guarda.draw()
                    if (vidasGuarda<=round(vidasInimigo/2 - 0.5)):                    
                        movimentoInimigo=movimentoRage
                    vidasGuarda = enemy.hit(listaProjeteisE,listaProjeteisD,guarda,vidasGuarda)
                    enemy.lifeMobs(guarda,guarda,vidasGuarda,dificuldade)
                    if invencibility ==0:
                        vidasPlayer,invencibility = enemy.enemy_melee_attack(guarda,player,vidasPlayer,invencibility)
                else:
                    movimentoInimigo=movimentoNormal
            
            if ((player.collided(sangue)) and (vidasCultista<=0 and vidasGuarda<=0)):
                pop_up.draw()
                continueButton.draw()
                if mouseClick.is_button_pressed(1) and mouseClick.is_over_object(continueButton):
                    clone=0
                    cenario+=1
                    player.set_position(0,janela.height/2)
                    pygame.mixer.music.stop()     

        
        elif cenario==3:
            hitBoxPlayer.draw()
            hitBoxFireCircle.draw()
            cenarioDungeon.draw()
            chao = chaoDungeon
            objetivo = objetivoDungeon
            objetivo.draw()
            
            # Inicio a musica de batalha
            if musica==2:
                pygame.mixer.music.load("Music/FinalBattle.wav")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)
                musica+=1
            
            # Crio a movimentacao do Caebralum
            checkPosInim = enemy.moveEnemy(janela,player,caebralum,movimentoInimigoBoss,checkPosInim)
            if checkPosInim==0:
                if (caebralum.x<player.x and caebralum.x>0):
                    caebralum = enemy.SetEnemy(caebralum_Dir_Run,caebralum)
                    caebralum.update()
                if caebralum.x == player.x and caebralum.y == player.y:
                    caebralum = enemy.SetEnemy(caebralum_Dir,caebralum)
            else:
                if (caebralum.x>player.x and caebralum.x<janela.width):
                    caebralum = enemy.SetEnemy(caebralum_Esq_Run,caebralum)
                    caebralum.update()
                if caebralum.x == player.x and caebralum.y == player.y:
                    caebralum = enemy.SetEnemy(caebralum_Esq,caebralum)
            
            # Ativamos e desativamos as armadilhas
            hitBoxPlayer.x=player.x
            hitBoxPlayer.y=player.y
            if hitBoxPlayer.collided_perfect(trapDungeonOff) and invencibility==0:
                vidasPlayer-=1
                invencibility=120
                trapTime=60
            if trapTime>0:
                trapDungeonOn.draw()
                trapTime-=1
            
            if summon:
                # Desenho o Caebralum
                if (vidasCaebralum>0):
                    caebralum.draw()
                    if (vidasCaebralum<=vidasInimigo):
                        caebralumFireCircle.set_position(caebralum.x-50,caebralum.y-50)
                        caebralumFireCircle.update()
                        caebralumFireCircle.draw()
                        hitBoxFireCircle.x = caebralumFireCircle.x
                        hitBoxFireCircle.y = caebralumFireCircle.y
                        if hitBoxPlayer.collided_perfect(hitBoxFireCircle) and invencibility<=0:
                            vidasPlayer-=1
                            invencibility=120
                        movimentoInimigoBoss=movimentoRageBoss
                    vidasCaebralum = enemy.hit(listaProjeteisE,listaProjeteisD,caebralum,vidasCaebralum)
                    enemy.lifeBoss(janela,vidasCaebralum,dificuldade)
                    if invencibility ==0:
                        vidasPlayer,invencibility = enemy.enemy_melee_Boss_attack(caebralum,player,vidasPlayer,invencibility)
                    if delayRugido>0:
                        delayRugido-=1
                else:
                    movimentoInimigo=movimentoNormal
            
            # Crio o latido do Boss
            if delayRugido==0:
                rugido = pygame.mixer.Sound("Music/Rugido.wav")
                rugido.set_volume(0.1)
                pygame.mixer.find_channel().play(rugido)
                delayRugido=600
        
        # Checo o tempo de invencibilidade apos sofrer dano
        if invencibility>0:
            invencibility-=1
         
        # Crio a movimentacao do personagem principal
        checkPos = Player.movePlayer(janela,teclado,player,movimento,chao,checkPos)
        if checkPos==0:
            if (teclado.key_pressed("D") or teclado.key_pressed("RIGHT")):
                player = Player.SetPlayer(player_Dir_Run,player)
                player.update()
            elif (teclado.key_pressed("S") or teclado.key_pressed("DOWN")):
                player = Player.SetPlayer(player_Dir_Run,player)
                player.update()
            elif (teclado.key_pressed("W") or teclado.key_pressed("UP")):
                player = Player.SetPlayer(player_Dir_Run,player)
                player.update()
            else:
                player = Player.SetPlayer(player_Dir,player)
        elif checkPos==1:
            if (teclado.key_pressed("A") or teclado.key_pressed("LEFT")):
                player = Player.SetPlayer(player_Esq_Run,player)
                player.update()
            elif (teclado.key_pressed("S") or teclado.key_pressed("DOWN")):
                player = Player.SetPlayer(player_Esq_Run,player)
                player.update()
            elif (teclado.key_pressed("W") or teclado.key_pressed("UP")):
                player = Player.SetPlayer(player_Esq_Run,player)
                player.update()
            else:
                player = Player.SetPlayer(player_Esq,player)
        
        # Ativo e desativo a habilidade "Clone"
        player,clone,delayClone,tempoDeRecargaClone = Player.clone(teclado,player,player_Clone,player_Clone_Esq,player_Clone_Dir,clone,delayClone,tempoDeRecargaClone,checkPos)
        if delayClone>0:
            delayClone-=1
        if delayClone%60==0 and tempoDeRecargaClone>0:
            tempoDeRecargaClone-=1
        Player.BarraDeClone(tempoDeRecargaClone)
        
        # Ativo e desativo a habilidade "Dash"
        dashTime,delayDash,cargaDeDash,checkDash,delayDash2 = Player.dash(player,janela,teclado,dashTime,delayDash,cargaDeDash,checkPos,checkDash,delayDash2)
        if checkDash==1:
            player = Player.SetPlayer(player_Dash_Esq,player)
            if dashTime>0 and player.x>5:
                player.x -= movimento* 4 * janela.delta_time()
                dashTime-=1
            else:
                checkDash=0
        if checkDash==2:
            player = Player.SetPlayer(player_Dash_Dir,player)
            if dashTime>0:
                player.x += movimento* 4 * janela.delta_time()
                dashTime-=1
            else:
                checkDash=0
        
        if delayDash2>0:
            delayDash2-=1
        if delayDash<=0 and cargaDeDash<3:
            cargaDeDash+=1
            delayDash=180
        if delayDash>0:
            delayDash-=1
        Player.BarraDeDash(cargaDeDash)

        # Chamo a funçao que lidará com o desenho da barra de vida do player
        Player.life(vidasPlayer,dificuldade)
            
        # Chamo a funçao que irá lidar com a criaçao dos tiros
        if (teclado.key_pressed("SPACE") and delay==0):
            Player.criaProjetil(player,listaProjeteisE,listaProjeteisD,checkPos)
            delay = shooting.recarga(dificuldade,delay)
            tempoDeRecargaTiro= round(delay/60)
        Player.BarraDeTiro(tempoDeRecargaTiro)

        # Faço o movimento dos tiros aliados
        Player.magicAttack(janela,listaProjeteisE,listaProjeteisD,velProjetil)
        if delay>0:
            delay-=1
        if delay%60==0 and tempoDeRecargaTiro>0:
            tempoDeRecargaTiro-=1
        
        # Desenho o personagem principal
        if vidasPlayer>0:
            player.draw()
        else:
            EndOfGame.derrota()
        
        # Desenho as instruçoes
        if player.x>=80:
            if cenario==1:
                objetivo.draw()
                summon = True
                if spawn==0:
                    minotauro.set_position(janela.width-minotauro.width,janela.height/2)
                    spawn+=1
            elif cenario==2:
                objetivo.draw()
                summon = True
                if spawn==1:
                    cultista.set_position(janela.width-cultista.width,janela.height-cultista.height)
                    guarda.set_position(janela.width-guarda.width,janela.height/2+guarda.height)
                    spawn+=1
        
        # Faço o movimento dos tiros inimigos
        enemy.magicAttackInimigo(janela,player,vidasPlayer,listaProjeteisInimigos,velProjetil,invencibility)
        if delayInimigo>0:
            delayInimigo-=1
            
        # Termino o jogo se mato o boss final
        if vidasCaebralum<=0:
            EndOfGame.vitoria()

        # Desenho os tempos de recarga
        janela.draw_text("Magic Attack: ",0,75,size=24,font_name="Arial",bold=False,italic=False,color=[255,0,255])
        janela.draw_text("Dash: ",0,100,size=24,font_name="Arial",bold=False,italic=False,color=[255,0,255])
        janela.draw_text("Clone: ",0,125,size=24,font_name="Arial",bold=False,italic=False,color=[255,0,255])

        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Finaliza o Gameloop
        janela.update()