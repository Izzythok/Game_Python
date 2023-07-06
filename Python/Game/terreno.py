from settings import *
from plataforma import Plataforma
from player import Player
from enemigo import Enemigo
from sprites_object import Items
from boss import Boss
import time

class Terreno:
    def __init__(self,map_terrain) -> None:
        self.map_terrain = map_terrain
        self.platforms_group = pygame.sprite.Group()
        self.block_clear_group = pygame.sprite.Group()
        self.player_group_single = pygame.sprite.GroupSingle()
        self.enemys_group = pygame.sprite.Group()
        self.enemys_group_T = pygame.sprite.Group()
        self.coins_group = pygame.sprite.Group()

        self.cup_win_group = pygame.sprite.Group()

        self.projectile_group = pygame.sprite.Group()
        self.life_group = pygame.sprite.Group()

        self.boss_group = pygame.sprite.GroupSingle()
        self.life_boss_group = pygame.sprite.Group()
        self.this_moment = time.time()

    def load_objets_map_terrain_2(self):
        for index_fil,fila in enumerate(self.map_terrain):
            for index_col,columna in enumerate(fila):
                x = index_col * size_plataforma
                y = index_fil * size_plataforma
                match columna:
                    case "A":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/A.png")
                        self.platforms_group.add(self.block_platform)
                    case "1":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/1.png")
                        self.platforms_group.add(self.block_platform)
                    case "X":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/X.png")
                        self.platforms_group.add(self.block_platform)
                    case "8":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/8.png")
                        self.platforms_group.add(self.block_platform)
                    case "p":
                        self.player = Player((x,y),"./Images/Character",(35,35))
                        self.player_group_single.add(self.player)
                    case "B":
                        self.boss = Boss((x,y),"./Images/Boss",(120,120))
                        self.boss_group.add(self.boss)


    def load_objets_map_terrain_1(self):

        for index_fil,fila in enumerate(self.map_terrain):
            for index_col,columna in enumerate(fila):
                x = index_col * size_plataforma
                y = index_fil * size_plataforma
                match columna:
                    case "A":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/A.png")
                        self.platforms_group.add(self.block_platform)
                    case "F":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/F.png")
                        self.platforms_group.add(self.block_platform)
                    case "D":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/D.png")
                        self.platforms_group.add(self.block_platform)
                    case "1":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/1.png")
                        self.platforms_group.add(self.block_platform)
                    case "X":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/X.png")
                        self.platforms_group.add(self.block_platform)
                    case "I":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/I.png")
                        self.platforms_group.add(self.block_platform)
                    case "J":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/J.png")
                        self.platforms_group.add(self.block_platform)
                    case "9":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/9.png")
                        self.platforms_group.add(self.block_platform)
                    case "8":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/8.png")
                        self.platforms_group.add(self.block_platform)
                    case "7":
                        self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/7.png")
                        self.platforms_group.add(self.block_platform)
                    case "S":
                        self.block_platform = Plataforma((x,y),(64,20),"./Images/tile_space/S.png")
                        self.platforms_group.add(self.block_platform)
                    case "Q":
                        self.block_platform = Plataforma((x,y),(size_plataforma,29),"./Images/tile_space/Q.png")
                        self.block_platform.image = pygame.transform.flip(self.block_platform.image,False,True)
                        self.platforms_group.add(self.block_platform)
                    case "p":
                        self.player = Player((x,y),"./Images/Character",(35,35))
                        self.player_group_single.add(self.player)
                    case "W":
                        self.items = Items((x,y),(30,30),"./Images/Items/End","./audios/song/Winner.wav")
                        self.items.rect.topleft = (x,y)
                        self.cup_win_group.add(self.items)
                    

    


    def load_objets_map_terrain(self):

        for index_fil,fila in enumerate(self.map_terrain):
            for index_col,columna in enumerate(fila):
                x = index_col * size_plataforma
                y = index_fil * size_plataforma
                if (columna == "0"):
                    self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/0.png")
                elif (columna == "1"):
                    self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/1.png")
                elif (columna == "2"):
                    self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/2.png")
                elif (columna == "3"):
                    self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/3.png")
                elif (columna == "4"):
                    self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/4.png")
                elif (columna == "5"):
                    self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/5.png")
                elif (columna == "6"):
                    self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/6.png")
                elif (columna == "X"):
                    self.block_platform = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/tile_space/X.png")
                elif (columna == "R"):
                    self.block = Plataforma((x,y),(size_plataforma,size_plataforma),"./Images/Surface/E.png")
                    self.block_clear_group.add(self.block)
                elif (columna == "p"):
                    self.player = Player((x,y),"./Images/Character",(35,35))
                    self.player_group_single.add(self.player)
                elif (columna == "E"):
                    self.enemy = Enemigo((x,y),"./Images/Enemies/AngryPing",(35,35),"./audios/song/Angry.wav")
                    self.enemys_group.add(self.enemy)
                elif (columna == "N"):
                    self.enemy_1 = Enemigo((x,y),"./Images/Enemies/Trunk",(35,35),"./audios/song/Trunk.wav")
                    self.enemys_group_T.add(self.enemy_1)
                elif (columna == "M"):
                    self.items = Items((x,y),(20,20),"./Images/Items/coins","./audios/song/coins.wav")
                    self.coins_group.add(self.items)
                elif (columna == "W"):
                    self.items = Items((x,y),(30,30),"./Images/Items/End","./audios/song/Winner.wav")
                    self.items.rect.topleft = (x,y)
                    self.cup_win_group.add(self.items)

                self.platforms_group.add(self.block_platform)
    
    def collion_reverse_enemy(self):
        for enemy in self.enemys_group.sprites():
            if(pygame.sprite.spritecollide(enemy,self.block_clear_group,False)):
                enemy.reverse()
    
    def collide_with_player(self,player: Player):
        player.collision_vertical(self.platforms_group)
        player.collision_horizontal(self.platforms_group)

    def collide_with_enemy(self,enemy: Enemigo):
        enemy.collision_vertical(self.platforms_group)
        enemy.collision_horizontal(self.platforms_group)

    def collide_with_projectile(self, projectile):
        projectile.collide_with_platfomr(self.platforms_group)
    
    def time_generate_enemy(self,timer: int):
        return time.time() - self.this_moment > timer
    
    def collide_with_boss(self, boss: Boss):
        boss.collision_vertical(self.platforms_group)
        boss.collision_horizontal(self.platforms_group)
        
    def generate_enemys(self,pisition: tuple, size: tuple):
        self.this_moment = time.time()
        self.enemy = Enemigo(pisition,"./Images/Enemies/Toro",size,"./audios/song/Angry.wav")
        self.enemys_group.add(self.enemy)