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
        self.try_again = True
        self.flag_ranking = True

    def run(self):
        while True:
            if(self.try_again):
                self.is_game_over = self.play()
                self.try_again = None
            
            if(self.is_game_over == 0):
                self.over()
                self.try_again = True
            elif(self.is_game_over == 1):
                self.win()
                self.try_again = True
    
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
            value = self.score_total()
            self.show_score_total("Total Score: " + str(value),CYAN,CENTER,self.screen)
            if(self.flag_ranking):
                self.add_ranking(value)
                self.flag_ranking = False
            self.show_ranking(self.screen)
            
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
                        break
            
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
        
        value_total = self.level_surface.score.value + (int(lis[0])*60 + int(lis[1]))*100
        return value_total
    
    def show_ranking(self,surface: pygame.Surface):
        players = self.read_archive()
        count = 0
        Rank = pygame.font.Font("freesansbold.ttf",30)
        name_rank = Rank.render("RANKING:",True,BLUE)
        surface.blit(name_rank,(200,250))
        for player in players:
            count += 25
            font = pygame.font.Font("freesansbold.ttf",30)
            score = font.render(player,True,BLUE)
            surface.blit(score,(200,250 + count))



    def add_ranking(self, data_archive: int|float|str):
        count = 0
        lis_player = self.read_archive()
        lis_player_aux = self.read_archive()
        count = len(lis_player) + 1
        score = "Player_" + str(count) + ": " + str(data_archive)
        lis_player.append(score)
        lis_player_aux.append(score)
        self.ordenar_lista(lis_player,lis_player_aux)

        with open("Ranking.txt", "w") as file:
            for player in lis_player:
                player = player + "\n"
                file.write(player)
        
        return score

    def read_archive(self):
        list_players = []
        with open("Ranking.txt", "r") as file:
            for linea in file:
                linea = linea.replace("\n", "")
                list_players.append(linea)
        return list_players
    
    def get_value_string(self, lista: list):
        list_value = []
        for string in lista:
            lis = string.split(":")
            value = lis[1].replace(" ", "")
            list_value.append(int(value))
        return list_value
             

    def ordenar_lista(self,list_player: list,list_dismantle: list):
        tam = len(list_player)
        list_value = self.get_value_string(list_dismantle)
        for i in range(0,tam-1):
            for j in range(i+1,tam):
                if(list_value[i] < list_value[j]):
                    aux = list_player[i]
                    list_player[i] = list_player[j]
                    list_player[j] = aux 