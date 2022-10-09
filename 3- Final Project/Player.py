from PPlay.window import*
from PPlay.animation import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.gameobject import*
from PPlay.collision import*
from PPlay.keyboard import*

def SetPlayer(PlayerState,playerAtual):
    player = PlayerState
    player.x = playerAtual.x
    player.y = playerAtual.y
    return player

def movePlayer(janela,teclado,player,movimento,chao,checkPos):
    if ((teclado.key_pressed("A") or teclado.key_pressed("LEFT")) and player.x>0):
        player.x -= movimento * janela.delta_time()
        checkPos=1
    elif ((teclado.key_pressed("D") or teclado.key_pressed("RIGHT")) and player.x<janela.width-player.width):
        player.x += movimento * janela.delta_time()
        checkPos=0
    if ((teclado.key_pressed("W") or teclado.key_pressed("UP")) and player.y+player.height>=chao.y):
        player.y-= (movimento*4/5) * janela.delta_time()
    elif ((teclado.key_pressed("S") or teclado.key_pressed("DOWN")) and player.y+player.height<janela.height):
        player.y+= (movimento*4/5) * janela.delta_time()
    return checkPos

def criaProjetil(player,listaProjeteisE,listaProjeteisD, checkTiro):
    # Crio o projetil
    if (checkTiro==1):
        projetilEsq = Sprite("Images/MagiaEmih.png",1)
        projetilEsq.x = player.x
        projetilEsq.y = player.y+player.height/4
        listaProjeteisE.append(projetilEsq)

    elif (checkTiro==0):
        projetilDir = Sprite("Images/MagiaEmih_invertido.png",1)
        projetilDir.x = player.x
        projetilDir.y = player.y+player.height/4
        listaProjeteisD.append(projetilDir)

def magicAttack(janela, listaProjeteisE, listaProjeteisD, velProjetil):
    for i in listaProjeteisD:
        i.x += velProjetil*janela.delta_time()
        i.draw()
        if (i.x>janela.width or i.x<0):
            listaProjeteisD.remove(i)
    for j in listaProjeteisE:
        j.x -= (velProjetil*janela.delta_time())
        j.draw()
        if (j.x>janela.width or j.x<0):
            listaProjeteisE.remove(j)
def clone(teclado,player,player_Clone,player_Clone_Esq,player_Clone_Dir,clone,delayClone,tempoDeRecargaClone,checkPos):
    if (teclado.key_pressed("LEFT_CONTROL") and delayClone==0):
        clone+=1
        if clone==1 and delayClone==0:
            delayClone=180
            if checkPos==1:
                player_Clone=player_Clone_Esq
            if checkPos==2:
                player_Clone=player_Clone_Dir
            player_Clone.x=player.x
            player_Clone.y=player.y
    if clone==1:
        if delayClone<=0:
            clone+=1
        else:
            player_Clone.draw()
    if clone==2 and delayClone==0:
        player.x=player_Clone.x
        player.y=player_Clone.y
        clone=0
        delayClone=180
        tempoDeRecargaClone=3
    return player,clone,delayClone,tempoDeRecargaClone

def dash(player,janela,teclado,dashTime,delayDash,cargaDeDash,checkPos,checkDash,delayDash2):
    if (teclado.key_pressed("LEFT_SHIFT") and (cargaDeDash>0 and delayDash2<=0) and (player.x<janela.width-player.width or player.x>0)):
        dashTime=15
        cargaDeDash-=1
        delayDash=180
        delayDash2=16
        if checkPos==1:
            checkDash=1
        if checkPos==0:
            checkDash=2
    return dashTime,delayDash,cargaDeDash,checkDash,delayDash2

def BarraDeTiro(tempoDeRecarga):
    if tempoDeRecarga==3:
        barraDeRecargaEmpty = Sprite("Images/Emptybar.png",1)
        barraDeRecargaEmpty.set_position(150,79)
        barraDeRecargaEmpty.draw()
    if tempoDeRecarga==2:
        barraDeRecargaLow = Sprite("Images/ShootBarLow.png",1)
        barraDeRecargaLow.set_position(150,79)
        barraDeRecargaLow.draw()
    if tempoDeRecarga==1:
        barraDeRecargaMedium = Sprite("Images/ShootBarMedium.png",1)
        barraDeRecargaMedium.set_position(150,79)
        barraDeRecargaMedium.draw()
    if tempoDeRecarga==0:
        barraDeRecargaFull = Sprite("Images/ShootBarFull.png",1)
        barraDeRecargaFull.set_position(150,79)
        barraDeRecargaFull.draw()

def BarraDeClone(tempoDeRecarga):
    if tempoDeRecarga==3:
        barraDeRecargaEmpty = Sprite("Images/Emptybar.png",1)
        barraDeRecargaEmpty.set_position(75,129)
        barraDeRecargaEmpty.draw()
    if tempoDeRecarga==2:
        barraDeRecargaLow = Sprite("Images/CloneBarLow.png",1)
        barraDeRecargaLow.set_position(75,129)
        barraDeRecargaLow.draw()
    if tempoDeRecarga==1:
        barraDeRecargaMedium = Sprite("Images/CloneBarMedium.png",1)
        barraDeRecargaMedium.set_position(75,129)
        barraDeRecargaMedium.draw()
    if tempoDeRecarga==0:
        barraDeRecargaFull = Sprite("Images/CloneBarFull.png",1)
        barraDeRecargaFull.set_position(75,129)
        barraDeRecargaFull.draw()

def BarraDeDash(cargaDeDash):
    if cargaDeDash==0:
        barraDeRecargaEmpty = Sprite("Images/DashBarEmpty.png",1)
        barraDeRecargaEmpty.set_position(75,102)
        barraDeRecargaEmpty.draw()
    if cargaDeDash==1:
        barraDeRecargaLow = Sprite("Images/DashBarLow.png",1)
        barraDeRecargaLow.set_position(75,105)
        barraDeRecargaLow.draw()
    if cargaDeDash==2:
        barraDeRecargaMedium = Sprite("Images/DashBarMedium.png",1)
        barraDeRecargaMedium.set_position(75,105)
        barraDeRecargaMedium.draw()
    if cargaDeDash==3:
        barraDeRecargaFull = Sprite("Images/DashBarFull.png",1)
        barraDeRecargaFull.set_position(75,105)
        barraDeRecargaFull.draw()
    
def life(vidas,dificuldade):
    # Instancio as barras de vida
    healthBarFull = Sprite("Images/HealthBarFull.png", 1)
    healthBarFull.set_position(0,0)
    
    healthBarMedium1 = Sprite("Images/HealthBarMedium1.png", 1)
    healthBarMedium1.set_position(0,0)
    
    healthBarMedium2 = Sprite("Images/HealthBarMedium2.png", 1)
    healthBarMedium2.set_position(0,0)

    healthBarMedium3 = Sprite("Images/HealthBarMedium3.png", 1)
    healthBarMedium3.set_position(0,0)

    healthBarLow = Sprite("Images/HealthBarLow.png", 1)
    healthBarLow.set_position(0,0)
        
    # Desenho a barra de vida desejada
    if dificuldade=="dificil":
        if (vidas==3):
            healthBarFull.draw()
        if (vidas==2):
            healthBarMedium2.draw()
        if (vidas==1):
            healthBarLow.draw()
    else:
        if (vidas==5):
            healthBarFull.draw()
        if (vidas==4):
            healthBarMedium1.draw()
        if (vidas==3):
            healthBarMedium2.draw()
        if (vidas==2):
            healthBarMedium3.draw()
        if (vidas==1):
            healthBarLow.draw()