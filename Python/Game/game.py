from settings import *
from sprite import Sprite
from level_surface import Level_Surface

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        # self.surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.level_surface = Level_Surface()
        self.sprites_game = Sprite()
        self.load_sprites()
        self.is_game_over = None
        self.flag_creem_game_over = False

    def run(self):
        while True:
            self.is_game_over = self.play()
            if(self.is_game_over == 0):
                self.over()
            elif(self.is_game_over == 1):
                self.win()
    
    def win(self):
        rtn = 1
        while True:
            self.clock.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if(evento.key == pygame.K_s):
                        pygame.quit()
                        sys.exit()
                    elif evento.key == pygame.K_r:
                        self.is_game_over = None
                        rtn = 0
            
            if(rtn == 0):
                break

            self.screen.blit(self.images["Winner"][0],(0,0))
            self.show_score_total("Total Score: " + str(self.score_total()),CYAN,CENTER,self.screen)
            
            pygame.display.flip()
            
        return rtn


    def play(self):
        while True:
            self.clock.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            is_game_over = self.level_surface.run()
            if(is_game_over != None):
                self.level_surface.stop_music()
                break
            pygame.display.flip()
        
        return is_game_over

    def over(self):
        rtn = 1
        while True:
            self.clock.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if(evento.key == pygame.K_s):
                        pygame.quit()
                        sys.exit()
                    elif evento.key == pygame.K_r:
                        self.is_game_over = None
                        rtn = 0
            
            if(rtn == 0):
                break

            self.screen.blit(self.images["GameOver"][0],(0,0))
            
            pygame.display.flip()
            
        return rtn


    def load_sprites(self):
        self.images = {}
        self.images["Close"] = self.sprites_game.load_sprite_path("./Images/Game_Over/Close",(100,100))
        self.images["GameOver"] = self.sprites_game.load_sprite_path("./Images/Game_Over/GameOver",(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.images["Restart"] = self.sprites_game.load_sprite_path("./Images/Game_Over/Restart",(100,100))
        self.images["Winner"] = self.sprites_game.load_sprite_path("./Images/Winner",(SCREEN_WIDTH,SCREEN_HEIGHT))

    def show_score_total(self,value: str,color: tuple, position, surface: pygame.Surface):
        self.font = pygame.font.Font("freesansbold.ttf",50)
        score = self.font.render(value,True,color)
        surface.blit(score,position)

    def score_total(self):
        value_total = None
        lis = self.level_surface.time.split(":")
        value_total = self.level_surface.score.value + int(lis[1])*100
        return value_total
