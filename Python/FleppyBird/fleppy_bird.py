import pygame
import os
import random
import neat

ia_jogando = True
geracao = 0

# Inicializar pygame
pygame.init()

# Configurações da tela
TELA_LARGURA = 500
TELA_ALTURA = 800
TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("Flappy Bird")

# Carregar imagens
BASE_DIR = os.path.dirname(__file__)
IMG_DIR = os.path.join(BASE_DIR, "imgs")

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "pipe.png")))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "base.png")))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "bg.png")))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "bird3.png")))
]

# Fonte
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont("Arial", 40)

# FPS
FPS = 30


# Classe Pássaro
class Passaro:
    IMGS = IMAGENS_PASSARO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.imagem = self.IMGS[0]
        self.contagem_imagem = 0

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo ** 2) + self.velocidade * self.tempo

        if deslocamento > 16:
            deslocamento = 16
        if deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # Rotação
        if deslocamento < 0 or self.y < self.altura + 50:
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        self.contagem_imagem += 1

        # Animação das asas
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]
        else:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # Não bater asa quando estiver caindo
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO * 2

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


# Classe Cano
class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        topo_offset = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        base_offset = (self.x - passaro.x, self.pos_base - round(passaro.y))

        b_point = passaro_mask.overlap(base_mask, base_offset)
        t_point = passaro_mask.overlap(topo_mask, topo_offset)

        if b_point or t_point:
            return True
        return False


# Classe Chão
class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))
 

# Função desenhar tela
def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    for cano in canos:
        cano.desenhar(tela)

    texto = FONTE_PONTOS.render(f"Pontos:  {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))

    if ia_jogando:
        texto = FONTE_PONTOS.render(f"Geração: {geracao}", 1, (255, 255, 255))
        tela.blit(texto, (10, 10))

    chao.desenhar(tela)

    for passaro in passaros:
        passaro.desenhar(tela)

    pygame.display.update()


# Função principal
def main():
    global geracao
    geracao += 1
    if ia_jogando:
        redes = []
        lista_genomas = []
        passaros = []

    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = TELA
    relogio = pygame.time.Clock()
    pontos = 0

    rodando = True
    while rodando:
        relogio.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()

        # Movimento
        for passaro in passaros:
            passaro.mover()

        chao.mover()

        adicionar_cano = False
        remover_canos = [] 
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    rodando = False

                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True

            cano.mover()
            if cano.x + cano.CANO_BASE.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))

        for cano in remover_canos:
            canos.remove(cano)

        for passaro in passaros:
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                rodando = False

        desenhar_tela(tela, passaros, canos, chao, pontos)


if __name__ == "__main__":
    main()