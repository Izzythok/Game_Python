from settings import *
from terreno import Terreno
from puntuacion import Puntuacion
from cronometro import Cronometro


class Level_Surface:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.terrain = Terreno(map_0)
        self.terrain.load_objets_map_terrain()
        self.terrain_1 = Terreno(map_1)
        self.terrain_1.load_objets_map_terrain_1()
        self.terrain_2 = Terreno(map_2)
        self.terrain_2.load_objets_map_terrain_2()
        self.score = Puntuacion("freesansbold.ttf",32)
        self.cronomet = Cronometro("freesansbold.ttf",32,120)
        self.finish_game = None
        self.finish_level = None
        self.finish_level_1 = None
        self.game_over = 0
        self.time = None
        self.load_music("./audios/song/Discord.mp3")

    def run(self):
        self.display_surface.blit(self.load_background("./Images/Surface/Fondos/0.png",SCREEN_WIDTH,SCREEN_HEIGHT),(0,0))
        if(not self.finish_level):
            self.setup_surface_level_0()
        elif(self.finish_level == 2):
            self.setup_surface_level_1()
        elif(self.finish_level == 3):
            self.setup_surface_level_2()
        self.time = self.cronomet.play()
        if(self.cronomet.time_over(self.time)):
            self.finish_game = self.game_over
        return self.finish_game
    
    def setup_surface_level_2(self):
        #Player
        sprite_player = self.terrain_2.player_group_single.sprite
        if(sprite_player):
            sprite_player.update()
            sprite_player.collide(self.terrain_2)
            sprite_player.lifes(150,25,self.terrain_2.life_group)
            if(sprite_player.is_dead()):
                sprite_player.reset_player()
                for life in self.terrain_2.life_group.sprites():
                    life.kill()
                    break
        self.terrain_2.player_group_single.draw(self.display_surface)
        #Boss
        boss = self.terrain_2.boss_group.sprite
        if(boss):
            boss.collide(self.terrain_2)
            boss.collide(sprite_player)
            boss.lifes(650,25,self.terrain_2.life_boss_group)
            if(boss.is_dead()):
                boss.reset()
                for life in self.terrain_2.life_boss_group.sprites():
                    life.kill()
                    break

        self.terrain_2.boss_group.draw(self.display_surface)
        self.terrain_2.boss_group.update()

        #Proyectil-Player
        for proyect in sprite_player.group_projectile.sprites():
            proyect.collide(self.terrain_2)
            boss.collide(proyect)
            for enemy in self.terrain_2.enemys_group.sprites():
                proyect.collide(enemy)
                self.score.increase(enemy.value_die)
        
        sprite_player.group_projectile.draw(self.display_surface)
        sprite_player.group_projectile.update()

        if(len(self.terrain_2.life_boss_group) == 0):
            boss.play_song_die("./audios/song/killboss.wav")
            self.finish_game = 1
        

        #bloques
        self.terrain_2.platforms_group.draw(self.display_surface)

        self.terrain_2.life_boss_group.update()
        self.terrain_2.life_boss_group.draw(self.display_surface)

        #life
        self.terrain_2.life_group.update()
        self.terrain_2.life_group.draw(self.display_surface)
        if(len(self.terrain_2.life_group) == 0):
            self.finish_game = self.game_over

        self.puntuacion()
        self.cronometro()



    
    def setup_surface_level_1(self): 
        #Player
        sprite_player = self.terrain_1.player_group_single.sprite
        if(sprite_player):
            sprite_player.update()
            sprite_player.collide(self.terrain_1)
            sprite_player.lifes(150,25,self.terrain_1.life_group)
            if(sprite_player.is_dead()):
                sprite_player.reset_player()
                for sprite in self.terrain_1.life_group.sprites():
                    sprite.kill()
                    break
        self.terrain_1.player_group_single.draw(self.display_surface)

        #Enemys
        if(self.terrain_1.time_generate_enemy(3.5)):
            self.terrain_1.generate_enemys((768,0),(50,28))
            self.terrain_1.generate_enemys((1152,0),(50,28))
        for enemy in self.terrain_1.enemys_group.sprites():
            if(enemy):
                enemy.collide(self.terrain_1)
                if(sprite_player):
                    sprite_player.collide(enemy)
                    self.score.increase(enemy.value_die)

        self.terrain_1.enemys_group.update()
        self.terrain_1.collion_reverse_enemy()
        self.terrain_1.enemys_group.draw(self.display_surface)
        
        #Proyectil-Player
        for proyect in sprite_player.group_projectile.sprites():
            proyect.collide(self.terrain_1)
            for enemy in self.terrain_1.enemys_group.sprites():
                proyect.collide(enemy)
                self.score.increase(enemy.value_die)
        
        sprite_player.group_projectile.draw(self.display_surface)
        sprite_player.group_projectile.update()

        self.terrain_1.platforms_group.draw(self.display_surface)

        #winner
        for win in self.terrain_1.cup_win_group.sprites():
            self.finish_level = win.collide_winner(sprite_player,3)
            if(self.finish_level == -1):
                self.finish_level = 2
        self.terrain_1.cup_win_group.update()
        self.terrain_1.cup_win_group.draw(self.display_surface)

        #life
        if(len(self.terrain_1.life_group) == 0):
            self.finish_game = self.game_over
        self.terrain_1.life_group.update()
        self.terrain_1.life_group.draw(self.display_surface)

        self.puntuacion()
        self.cronometro()

        
    #############################################################################################################################
    
    def setup_surface_level_0(self)->bool:
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

        #Proyectil-enemy_T
        for proyect in self.terrain.projectile_group.sprites():
            proyect.collide(self.terrain)
            sprite_player.collide(proyect)
        self.terrain.projectile_group.update()
        self.terrain.projectile_group.draw(self.display_surface)


        #Proyectil-Player
        for proyect in sprite_player.group_projectile.sprites():
            proyect.collide(self.terrain)
            for enemy in self.terrain.enemys_group.sprites():
                proyect.collide(enemy)
                self.score.increase(enemy.value_die)
                for enemy_T in self.terrain.enemys_group_T.sprites():
                    proyect.collide(enemy_T)
                    self.score.increase(enemy_T.value_die)

        
        sprite_player.group_projectile.draw(self.display_surface)
        sprite_player.group_projectile.update()

        #coins
        for coins in self.terrain.coins_group.sprites():
            sprite_player.collide(coins)
            self.score.increase(coins.value_collide)
        #winner
        for win in self.terrain.cup_win_group.sprites():
            self.finish_level = win.collide_winner(sprite_player,2)
            if(self.finish_level == -1):
                self.finish_level = None
            
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

        self.puntuacion()
        self.cronometro()

        
    


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
    
    def cronometro(self):
        #Cronometro
        self.cronomet.show_font("Time: " + str(self.time),CYAN,(550,20),self.display_surface)

    def puntuacion(self):
        #puntuacion
        self.score.show_font((350,20),"Score: " + str(self.score.value),CYAN,self.display_surface)

    
    def stop_music(self):
        pygame.mixer.music.stop()