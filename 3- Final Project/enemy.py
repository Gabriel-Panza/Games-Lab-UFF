from PPlay.window import*
from PPlay.animation import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.gameobject import*
from PPlay.collision import*
from PPlay.keyboard import*

def SetEnemy(EnemyState,EnemyAtual):
    Enemy = EnemyState
    Enemy.x = EnemyAtual.x
    Enemy.y = EnemyAtual.y
    return Enemy

def SetEnemyAttack(EnemyState,EnemyAtual,cenario,inv):
    if cenario==1:
        if inv==120:
            Enemy = EnemyState
            Enemy.x = EnemyAtual.x 
            Enemy.y = EnemyAtual.y - 45
        else:
            Enemy = EnemyState
            Enemy.x = EnemyAtual.x
            Enemy.y = EnemyAtual.y
        return Enemy
    if cenario==2:
        if inv==120:
            Enemy = EnemyState
            Enemy.x = EnemyAtual.x
            Enemy.y = EnemyAtual.y
        else:
            Enemy = EnemyState
            Enemy.x = EnemyAtual.x
            Enemy.y = EnemyAtual.y
        return Enemy
    

def moveEnemy(janela,player,enemy,movimento,checkPosInimigo):
    if (enemy.x<player.x and enemy.x>-5):
        enemy.x += (movimento*2/5) * janela.delta_time()
        checkPosInimigo=0
    elif (enemy.x>player.x and enemy.x<janela.width+5):
        enemy.x -= (movimento*2/5) * janela.delta_time()
        checkPosInimigo=1
    if (enemy.y>player.y - player.height/3):
        enemy.y-= (movimento/5) * janela.delta_time()
    elif (enemy.y<player.y - player.height/3):
        enemy.y+= (movimento/5) * janela.delta_time()
    return checkPosInimigo

def moveEnemyRanged(janela,player,enemy,movimento):
    if (enemy.y>player.y - player.height/3):
        enemy.y-= (movimento/5) * janela.delta_time()
    elif (enemy.y<player.y - player.height/3):
        enemy.y+= (movimento/5) * janela.delta_time()

def criaProjetilInimigo(cultista,listaProjeteisInimigo):
    projetil = Sprite("Images/MagiaCultista.png",1)
    projetil.x = cultista.x
    projetil.y = cultista.y+cultista.height/3
    listaProjeteisInimigo.append(projetil)

def magicAttackInimigo(janela, player, vidasPlayer, listaProjeteisInimigo, velProjetil, delayInv):
    for i,projetil in enumerate(listaProjeteisInimigo):
        projetil.x -= velProjetil*janela.delta_time()
        projetil.draw()
        if (projetil.x<0):
            listaProjeteisInimigo.pop(i)

def enemy_melee_attack(enemy,player,vidasPlayer,delayInv):
    if enemy.collided(player):
        vidasPlayer-=1
        delayInv= 120
    return vidasPlayer, delayInv

def enemy_ranged_attack(listaProjeteisInimigo,player,vidasPlayer,delayInv):
    for i,projetil in enumerate(listaProjeteisInimigo):
        if projetil.collided(player):
            vidasPlayer-=1
            delayInv= 120
            listaProjeteisInimigo.pop(i)
    return vidasPlayer, delayInv

def enemy_melee_Boss_attack(enemy,player,vidasPlayer,delayInv):
    if enemy.collided(player):
        vidasPlayer-=2
        delayInv= 120
    return vidasPlayer, delayInv

def hit(listaProjeteisE,listaProjeteisD,enemy,vidas):
    for i,projetil in enumerate(listaProjeteisE):
        if projetil.collided(enemy):
            vidas-=1
            listaProjeteisE.pop(i)
    for i,projetil in enumerate(listaProjeteisD):
        if projetil.collided(enemy):
            vidas-=1
            listaProjeteisD.pop(i)
    return vidas

def lifeMobs(enemy,enemyatual,vidas,dificuldade):
    # Instancio as barras de vida
    healthBarFull = Sprite("Images/MobsLifeFull.png", 1)
    healthBarFull.set_position(enemy.x+enemy.width/2, enemy.y+(enemy.height-enemyatual.height)/2-20)
    
    healthBarMedium1 = Sprite("Images/MobsLifeMedium1.png", 1)
    healthBarMedium1.set_position(enemy.x+enemy.width/2, enemy.y+(enemy.height-enemyatual.height)/2-20)
    
    healthBarMedium2 = Sprite("Images/MobsLifeMedium2.png", 1)
    healthBarMedium2.set_position(enemy.x+enemy.width/2, enemy.y+(enemy.height-enemyatual.height)/2-20)

    healthBarMedium3 = Sprite("Images/MobsLifeMedium3.png", 1)
    healthBarMedium3.set_position(enemy.x+enemy.width/2, enemy.y+(enemy.height-enemyatual.height)/2-20)

    healthBarLow = Sprite("Images/MobsLifeLow.png", 1)
    healthBarLow.set_position(enemy.x+enemy.width/2, enemy.y+(enemy.height-enemyatual.height)/2-20)
    
    healthBarEmpty = Sprite("Images/MobsLifeEmpty.png", 1)
    healthBarEmpty.set_position(enemy.x+enemy.width/2, enemy.y+(enemy.height-enemyatual.height)/2-20)
    
    # Desenho a barra de vida desejada
    if dificuldade=="facil":
        if (vidas==3):
            healthBarFull.draw()
        if (vidas==2):
            healthBarMedium2.draw()
        if (vidas==1):
            healthBarLow.draw()
        if (vidas==0):
            healthBarEmpty.draw()
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
        if (vidas==0):
            healthBarEmpty.draw()

def lifeBoss(janela,vidas,dificuldade):
    # Instancio as barras de vida
    healthBarFull = Sprite("Images/CaebralumLifeFull.png", 1)
    healthBarFull.set_position(janela.width/2 - healthBarFull.width/2+50, 0)
    
    healthBarMedium1 = Sprite("Images/CaebralumLifeMedium1.png", 1)
    healthBarMedium1.set_position(janela.width/2 - healthBarMedium1.width/2+50, 0)
    
    healthBarMedium2 = Sprite("Images/CaebralumLifeMedium2.png", 1)
    healthBarMedium2.set_position(janela.width/2 - healthBarMedium2.width/2+50, 0)

    healthBarMedium3 = Sprite("Images/CaebralumLifeMedium3.png", 1)
    healthBarMedium3.set_position(janela.width/2 - healthBarMedium3.width/2+50, 0)

    healthBarMedium4 = Sprite("Images/CaebralumLifeMedium4.png", 1)
    healthBarMedium4.set_position(janela.width/2 - healthBarMedium4.width/2+50, 0)
    
    healthBarMedium5 = Sprite("Images/CaebralumLifeMedium5.png", 1)
    healthBarMedium5.set_position(janela.width/2 - healthBarMedium5.width/2+50, 0)

    healthBarMedium6 = Sprite("Images/CaebralumLifeMedium6.png", 1)
    healthBarMedium6.set_position(janela.width/2 - healthBarMedium6.width/2+50, 0)
    
    healthBarMedium7 = Sprite("Images/CaebralumLifeMedium7.png", 1)
    healthBarMedium7.set_position(janela.width/2 - healthBarMedium7.width/2+50, 0)

    healthBarMedium8 = Sprite("Images/CaebralumLifeMedium8.png", 1)
    healthBarMedium8.set_position(janela.width/2 - healthBarMedium8.width/2+50, 0)

    healthBarLow = Sprite("Images/CaebralumLifeLow.png", 1)
    healthBarLow.set_position(janela.width/2 - healthBarLow.width/2+50, 0)
    
    healthBarEmpty = Sprite("Images/CaebralumLifeEmpty.png", 1)
    healthBarEmpty.set_position(janela.width/2 - healthBarEmpty.width/2+50, 0)
    
    # Desenho a barra de vida desejada
    if dificuldade=="facil":
        if (vidas==6):
            healthBarFull.draw()
        if (vidas==5):
            healthBarMedium2.draw()
        if (vidas==4):
            healthBarMedium4.draw()
        if (vidas==3):
            healthBarMedium6.draw()
        if (vidas==2):
            healthBarMedium8.draw()
        if (vidas==1):
            healthBarLow.draw()
        if (vidas==0):
            healthBarEmpty.draw()
    else:
        if (vidas==10):
            healthBarFull.draw()
        if (vidas==9):
            healthBarMedium1.draw()
        if (vidas==8):
            healthBarMedium2.draw()
        if (vidas==7):
            healthBarMedium3.draw()
        if (vidas==6):
            healthBarMedium4.draw()
        if (vidas==5):
            healthBarMedium5.draw()
        if (vidas==4):
            healthBarMedium6.draw()
        if (vidas==3):
            healthBarMedium7.draw()
        if (vidas==2):
            healthBarMedium8.draw()
        if (vidas==1):
            healthBarLow.draw()
        if (vidas==0):
            healthBarEmpty.draw()