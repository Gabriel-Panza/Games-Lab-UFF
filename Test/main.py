import random
import pygame
from pygame.locals import *
import os
import sys
from datetime import datetime

pygame.init()

# Inicializa janela redimensionável
screen = pygame.display.set_mode((1280, 720), RESIZABLE)
pygame.display.set_caption("Dungeon Generator")

# Fonte
font = pygame.font.SysFont("arial", 20)
tooltip_font = pygame.font.SysFont("arial", 16)

# Garante que o executável acesse o arquivo no mesmo diretório
base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
img_path = os.path.join(base_path, "SalaMasmorra.jpg")
original_bg = pygame.image.load(img_path).convert()

# Função para salvar o score
def salvar_score(score):
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    with open("pontuacoes.txt", "a") as f:
        f.write(f"{now} - {score}\n")

# Função para desenhar texto
def draw_text(text, x, y, font_obj, color=(255, 255, 255)):
    rendered = font_obj.render(text, True, color)
    screen.blit(rendered, (x, y))

# Botão
class Button:
    def __init__(self, x, y, text):
        self.text = text
        self.rel_x = x
        self.rel_y = y
        self.width = 180
        self.height = 50
        self.enabled = True
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def update_position(self, window_width, window_height):
        self.x = int(self.rel_x / 1280 * window_width)
        self.y = int(self.rel_y / 720 * window_height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        color = (0, 128, 0) if self.enabled else (100, 100, 100)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        draw_text(self.text, self.x + 10, self.y + 15, font)

        if not self.enabled and self.is_hovering():
            draw_text("Porta trancada", self.x, self.y - 20, tooltip_font, (255, 255, 0))

    def is_clicked(self):
        return self.enabled and self.is_hovering() and pygame.mouse.get_pressed()[0]

    def is_hovering(self):
        mx, my = pygame.mouse.get_pos()
        return self.rect.collidepoint(mx, my)

def fade_transition():
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((0, 0, 0))
    for alpha in range(0, 255, 15):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)

# Gerador de salas
def gerar_sala():
    descrições = [
        "O ar aqui é denso e úmido. Você pisa em ossos antigos enquanto\numa tocha solitária crepita em uma parede distante.",
        "Correntes balançam sozinhas no teto, fazendo um som metálico\ninquietante. Há marcas de garras na pedra.",
        "Uma estátua de guerreiro decapitado segura sua própria cabeça,\ncom os olhos ainda brilhando em púrpura.",
        "As paredes pulsantes estão cobertas de runas vivas, que se\ncontorcem sob seu olhar.",
        "Uma névoa esverdeada rasteja pelo chão, dificultando a visão.\nHá silhuetas imóveis à frente.",
        "Um altar sacrificial está coberto por sangue fresco... mas não\nhá ninguém por perto.",
        "Você ouve um sussurro vindo do teto — mas ao olhar para cima,\nsó há olhos brilhando na escuridão.",
        "Uma figura encapuzada desintegra-se diante de você,\ncomo se nunca tivesse existido.",
        "Estátuas de criaturas reptilianas circundam a sala,\ne todas estão apontando para você.",
        "A água escorre pelas paredes, mas não há umidade no chão.\nUm reflexo estranho aparece nas poças.",
        "Uma porta trancada vibra como se algo do outro lado\nestivesse tentando sair... ou entrar.",
        "Há uma fornalha acesa no centro, mas nenhum sinal de quem\na alimenta. Uma voz sussurra seu nome.",
        "Livros flutuam em círculos no ar, alguns sussurrando\nversos em línguas esquecidas.",
        "Cadeias arrebentadas e marcas de garras nas paredes\nindicam que algo grande esteve preso aqui.",
        "Um elmo flutuante gira lentamente no centro da sala,\ncoberto por sangue seco e ainda pingando.",
        "Você pisa em algo mole. Quando olha, é uma mão.\nEla se fecha lentamente e depois relaxa.",
        "Há um buraco no chão emitindo gemidos abafados.\nCorrentes quebradas pendem ao redor dele.",
        "Um espelho gigante ocupa a parede inteira. Seu reflexo\nestá sorrindo... mas você não está.",
        "Estátuas humanas deformadas pelas emoções que carregam: medo,\ndesespero e dor. Uma delas pisca.",
        "A escuridão parece viva nesta sala. Ela recua conforme você entra,\nmas permanece espreitando.",
    ]


    while True:
        portas = {
            "frente": random.choice([True, False]),
            "direita": random.choice([True, False]),
            "esquerda": random.choice([True, False])
        }
        if any(portas.values()):
            break

    return random.choice(descrições), portas

def draw_hearts(lives, x=20, y=20, spacing=30):
    total_hearts = 10
    for i in range(total_hearts):
        cx = x + i * spacing
        color = (255, 0, 0) if i < lives else (0, 0, 0)

        # Desenha os dois "lados" arredondados do coração
        pygame.draw.circle(screen, color, (cx - 5, y), 6)
        pygame.draw.circle(screen, color, (cx + 5, y), 6)

        # Desenha o triângulo inferior do coração
        pygame.draw.polygon(screen, color, [
            (cx - 11, y),
            (cx + 11, y),
            (cx, y + 14)
        ])

def draw_menu():
    screen.fill((20, 20, 20))
    window_width, window_height = screen.get_size()

    title_font = pygame.font.SysFont("arial", 60, bold=True)
    subtitle_font = pygame.font.SysFont("arial", 24)

    draw_text("Gerador de Dungeons", window_width // 2 - 300, 120, title_font, (255, 255, 255))
    draw_text("Um gerador de dungeons divertido!", window_width // 2 - 200, 200, subtitle_font, (200, 200, 200))

    btn_start_game.update_position(window_width, window_height)
    btn_start_game.draw()

    pygame.display.update()

# Estado inicial
descricao_atual, portas_ativas = gerar_sala()
is_combat = random.random() < 0.3
enemy_name = random.choice(["imp", "goblin", "morto-vivo", "esqueleto", "kobold"]) if is_combat else ""
combat_result = None
player_roll = None
enemy_roll = None
combat_finished = False
combat_end_time = 0
score = 0
lives = 10
game_state = "menu"
window_width, window_height = screen.get_size()

# Criar botões
btn_frente = Button(560, 420, "Seguir em frente")
btn_direita = Button(770, 500, "Ir para a direita")
btn_esquerda = Button(350, 500, "Ir para a esquerda")
btn_rolar_dado = Button(540, 360, "Rolar d20")
btn_start_game = Button(550, 320, "Iniciar Jogo")
buttons = [btn_frente, btn_direita, btn_esquerda]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, RESIZABLE)

    if game_state == "menu":
        draw_menu()
        if btn_start_game.is_clicked():
            game_state = "jogo"
            pygame.time.wait(300)  # pequena pausa para não clicar duas vezes

    elif game_state == "jogo":
        screen.fill((10, 10, 10))
        window_width, window_height = screen.get_size()
        resized_bg = pygame.transform.scale(original_bg, (window_width, window_height))
        screen.blit(resized_bg, (0, 0))

        if lives <= 0:
            salvar_score(score)
            score = 0
            lives = 10
            descricao_atual, portas_ativas = gerar_sala()
            is_combat = False
            combat_result = None
            player_roll = None
            enemy_roll = None
            combat_finished = False
            game_state = "menu"
            pygame.time.wait(500)



        # Atualiza botões
        for button in buttons:
            button.update_position(window_width, window_height)

        btn_frente.enabled = portas_ativas["frente"]
        btn_direita.enabled = portas_ativas["direita"]
        btn_esquerda.enabled = portas_ativas["esquerda"]

        # Pontuação
        draw_text(f"Pontos: {score}", window_width - 150, 20, font)
        # Vidas
        draw_hearts(lives)
        
        # Descrição da sala
        for i, linha in enumerate(descricao_atual.split('\n')):
            draw_text(linha, window_width / 4 + 20, 200 + (i * 25), font)

        # Combate
        if is_combat:
            btn_rolar_dado.update_position(window_width, window_height)
            font_inimigo = pygame.font.SysFont("arial", 20, bold=True)
            draw_text(f"Um {enemy_name} aparece!", btn_rolar_dado.x - 10, btn_rolar_dado.y - 30, font_inimigo, (255, 0, 0))
            btn_rolar_dado.draw()

            if not combat_finished and btn_rolar_dado.is_clicked():
                player_roll = random.randint(1, 20)
                enemy_roll = random.randint(1, 20)
                combat_result = "Você venceu!" if player_roll >= enemy_roll else "Você perdeu!"
                combat_end_time = pygame.time.get_ticks() + 1500
                combat_finished = True
                if combat_result == "Você venceu!":
                    score+=100
                else:
                    lives-=1
            
            if combat_result:
                if player_roll == 1:
                    draw_text(f"Você rolou: {player_roll}", 520, 430, font, (255, 0, 0))
                elif player_roll == 20:
                    draw_text(f"Você rolou: {player_roll}", 520, 430, font, (0, 255, 0))
                else:
                    draw_text(f"Você rolou: {player_roll}", 520, 430, font)
                if enemy_roll == 1:
                    draw_text(f"Inimigo rolou: {enemy_roll}", 520, 450, font, (255, 0, 0))
                elif enemy_roll == 20:
                    draw_text(f"Inimigo rolou: {enemy_roll}", 520, 450, font, (0, 255, 0))
                else:
                    draw_text(f"Inimigo rolou: {enemy_roll}", 520, 450, font)
                draw_text(f"{combat_result}", 520, 470, font, (0, 255, 0) if combat_result == "Você venceu!" else (255, 0, 0))

            if combat_finished and pygame.time.get_ticks() > combat_end_time:
                fade_transition()
                descricao_atual, portas_ativas = gerar_sala()
                is_combat = random.random() < 0.3
                enemy_name = random.choice(["esqueleto", "ghoul", "kobold"]) if is_combat else ""
                combat_result = None
                player_roll = None
                enemy_roll = None
                combat_finished = False
                pygame.time.wait(200)

        # Sala comum
        else:
            for button in buttons:
                button.draw()

            if btn_frente.is_clicked() or btn_direita.is_clicked() or btn_esquerda.is_clicked():
                fade_transition()
                descricao_atual, portas_ativas = gerar_sala()
                is_combat = random.random() < 0.3
                enemy_name = random.choice(["esqueleto", "ghoul", "kobold"]) if is_combat else ""
                combat_result = None
                player_roll = None
                enemy_roll = None
                combat_finished = False
                score += 10
                pygame.time.wait(200)

    pygame.display.update()