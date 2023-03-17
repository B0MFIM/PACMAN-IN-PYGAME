import pygame
import constantes as const
import sprites


class Game:
    def __init__(self):
        #Criando a Tela do Jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((const.LARGURA, const.ALTURA))
        pygame.display.set_caption(const.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True

    def novo_jogo(self):
        #Instância as Classes das Sprites do Jogo
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        #Loop do Jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(const.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        #Define os Eventos do Jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        #Atualizar Sprites
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        #Desenhar Sprites
        self.tela.fill(const.PRETO)             #Limpando a Tela
        self.todas_as_sprites.draw(self.tela)   #Desenhando as Sprites
        pygame.display.flip()

    def mostrar_tela_start(self):
        pass

    def mostrar_tela_game_over(self):
        pass


#CÓDIGO PRINCIPAL, INSTANCIANDO O OBJETO GAME!
g = Game()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()