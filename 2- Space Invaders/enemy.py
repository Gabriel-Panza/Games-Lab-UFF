from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.sound import*
import ranking
import random

def spawn(linha,matrizDeInimigos):    
    for i in range(linha):
        linhas = []
        for j in range(10):
            if linha<6:
                if i==0:
                    inimigoAtras = Sprite("inimigo3.png",1)
                    inimigoAtras.x = 75 * j
                    inimigoAtras.y = 50 * i
                    linhas.append((inimigoAtras,1))
                elif i==linha-1:
                    inimigoFrente = Sprite("inimigo1.png",1)
                    inimigoFrente.x = 75 * j
                    inimigoFrente.y = 50 * i
                    linhas.append((inimigoFrente,1))
                else:
                    inimigoMeio = Sprite("inimigo2.png",1)
                    inimigoMeio.x = 75 * j
                    inimigoMeio.y = 50 * i
                    linhas.append((inimigoMeio,1))
            if linha>=6:
                if i==0:
                    inimigoAtras = Sprite("inimigo3.png",1)
                    inimigoAtras.x = 75 * j
                    inimigoAtras.y = 50 * i
                    linhas.append((inimigoAtras,1))
                elif i==linha-2:
                    inimigoFrente = Sprite("inimigo1.png",1)
                    inimigoFrente.x = 75 * j
                    inimigoFrente.y = 50 * i
                    linhas.append((inimigoFrente,1))
                elif i==linha-1:
                    inimigoBonus = Sprite("inimigoBonus.png",1)
                    inimigoBonus.x = 50
                    inimigoBonus.y = 50
                    break
                else:
                    inimigoMeio = Sprite("inimigo2.png",1)
                    inimigoMeio.x = 75 * j
                    inimigoMeio.y = 50 * i
                    linhas.append((inimigoMeio,1))
        matrizDeInimigos.append(linhas)
    
    i = random.randint(0,linha-1)
    j = random.randint(0,9)
    matrizDeInimigos[i][j] = (Sprite("inimigoBoss.png",1),3)
    matrizDeInimigos[i][j][0].x = 75 * j
    matrizDeInimigos[i][j][0].y = 50 * i
    
    if linha>=6:
        return inimigoBonus

def draw(matrizDeInimigos):
    for linha in range(len(matrizDeInimigos)-1,-1,-1):
        for alien in matrizDeInimigos[linha]:
            alien[0].draw()

def moveInimigos(janela, matrizDeInimigos, movimentoInimigo):
    bateu = False
    for i in matrizDeInimigos:
        for j in i:
            j[0].x += movimentoInimigo*janela.delta_time()
            if ((j[0].x >= janela.width - j[0].width - 5) or (j[0].x<-5)):
                bateu = True
    if (bateu):
        movimentoInimigo *= -1
        for i in matrizDeInimigos:
            for j in i:
                j[0].x += movimentoInimigo*janela.delta_time()
                j[0].y += 30
    return movimentoInimigo

def kill(listaProjeteis,matrizDeInimigos,score,linha,movimentoInimigo):
    for k,linhaDeInimigos in enumerate(matrizDeInimigos):
        for i,inimigo in enumerate(linhaDeInimigos):
            for j,projetil in enumerate(listaProjeteis):
                    if (projetil.collided(inimigo[0])):
                        listaProjeteis.pop(j)
                        linhaDeInimigos[i]=(inimigo[0],inimigo[1]-1)
                        if linhaDeInimigos[i][1]<=0:
                            linhaDeInimigos.pop(i)
                            if k==0:
                                score+=30
                            elif k==linha-1:
                                score+=10
                            else:
                                score+=20
                            movimentoInimigo*=1.01
    return score,movimentoInimigo
def killNavemae(listaProjeteis,score,naveMae):
    for i in listaProjeteis:
        if (i.collided(naveMae)):
            naveMae.y=-300
            score+=100
    return score

def hit(vidas,player,listaDeInimigos,listaProjeteisInimigos,listaProjeteisNavemae,score):
    for i,projetil in enumerate(listaProjeteisInimigos):
        if (projetil.collided(player)):
            listaProjeteisInimigos.pop(i)
            vidas-=1    
    for i,tiro in enumerate(listaProjeteisNavemae):
        if (tiro.collided(player)):
            listaProjeteisNavemae.pop(i)
            vidas-=1
    return vidas