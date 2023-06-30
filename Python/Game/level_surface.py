from settings import *
from terreno import Terreno
from puntuacion import Puntuacion
from cronometro import Cronometro


class Level_Surface:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.terrain = Terreno(map_1)
        self.score = Puntuacion("freesansbold.ttf",32)
        self.cronomet = Cronometro("freesansbold.ttf",32,60)
        self.finish_game = None
        self.game_over = 0
        self.time = None
        self.load_music("./audios/song/Discord.mp3")

    def run(self):
        self.display_surface.blit(self.load_background("./Images/Surface/Fondos/0.png",SCREEN_WIDTH,SCREEN_HEIGHT),(0,0))
        game_over = self.setup_surface_level_1()
        self.time = self.cronomet.play()
        if(self.cronomet.time_over(self.time)):
            self.finish_game = self.game_over   
        return game_over
    
    def setup_surface_level_1(self)->bool:

        #Player
        sprite_player = self.terrain.player_group_single.sprite
        if(sprite_player):
            sprite_player.update()
            sprite_player.collide(self.terrain)
            sprite_player.lifes(150,25,self.terrain.life_group)
            if(sprite_player.is_dead()):
                sprite_player.reset_player()
                for sprite in self.terrain.life_group.sprites():
                    sprite.kill()
                    break
                    
        self.terrain.player_group_single.draw(self.display_surface)

        #Enemys
        for enemy in self.terrain.enemys_group.sprites():
            if(enemy):
                enemy.collide(self.terrain)
                if(sprite_player):
                    sprite_player.collide(enemy)
                    self.score.increase(enemy.value_die)

        self.terrain.enemys_group.update()
        self.terrain.collion_reverse_enemy()
        self.terrain.enemys_group.draw(self.display_surface)

        for enemy_T in self.terrain.enemys_group_T.sprites():
            if(enemy_T):
                enemy_T.stop_move()
                enemy_T.collide(self.terrain)
                if(sprite_player):
                    sprite_player.collide(enemy_T)
                    self.score.increase(enemy_T.value_die)
                if(enemy_T.can_shoot()):
                    enemy_T.shoot("Attack",enemy_T.rect.center,(20,20),"./Images/Enemies/Trunk/Bullet",5,self.terrain.projectile_group)
                enemy_T.update()
        
        self.terrain.enemys_group_T.draw(self.display_surface)

        #Proyectil
        for proyect in self.terrain.projectile_group.sprites():
            proyect.collide(self.terrain)
            sprite_player.collide(proyect)
        self.terrain.projectile_group.update()
        self.terrain.projectile_group.draw(self.display_surface)
        #coins
        for coins in self.terrain.coins_group.sprites():
            sprite_player.collide(coins)
            self.score.increase(coins.value_collide)
        #winner
        for win in self.terrain.cup_win_group.sprites():
            win.collide_winner(sprite_player)
            self.finish_game = win.cup_winner
            
        if(len(self.terrain.life_group) == 0):
                self.finish_game = self.game_over

        #bloques
        self.terrain.coins_group.update()
        self.terrain.coins_group.draw(self.display_surface)
        self.terrain.cup_win_group.update()
        self.terrain.cup_win_group.draw(self.display_surface)
        self.terrain.block_clear_group.draw(self.display_surface)
        self.terrain.platforms_group.draw(self.display_surface)
        #life
        self.terrain.life_group.update()
        self.terrain.life_group.draw(self.display_surface)

        #puntuacion
        self.score.show_font((350,20),"Score: " + str(self.score.value),CYAN,self.display_surface)

        #Cronometro
        self.cronomet.show_font("Time: " + str(self.time),CYAN,(550,20),self.display_surface)
    
        return self.finish_game


    def scale(self,size):
        self.display_surface = pygame.transform.smoothscale(self.display_surface,size)

    def load_background(self, relative_path: str, width=None,height=None):
        back_ground = pygame.image.load(relative_path)
        if(width!=None and height!=None):
            back_ground = pygame.transform.scale(back_ground,(width,height))
        return back_ground
    
    def load_music(self, relative_path: str):
        pygame.mixer.music.load(relative_path)
        pygame.mixer.music.play()
    
    def stop_music(self):
        pygame.mixer.music.stop()