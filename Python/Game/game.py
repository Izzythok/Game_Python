from settings import *
from level_surface import Level_Surface

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level_surface = Level_Surface()

    def run(self):
        while True:
            self.clock.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level_surface.run()
            pygame.display.flip()
