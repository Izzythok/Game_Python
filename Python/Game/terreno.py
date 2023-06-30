from settings import *
from plataforma import Plataforma
from player import Player
from enemigo import Enemigo
from sprites_object import Items

class Terreno:
    def __init__(self,map_terrain) -> None:
        self.platforms_group = pygame.sprite.Group()
        self.block_clear_group = pygame.sprite.Group()
        self.player_group_single = pygame.sprite.GroupSingle()
        self.enemys_group = pygame.sprite.Group()
        self.enemys_group_T = pygame.sprite.Group()
        self.coins_group = pygame.sprite.Group()

        self.cup_win_group = pygame.sprite.Group()

        self.projectile_group = pygame.sprite.Group()
        self.life_group = pygame.sprite.Group()
        self.load_objets_map_terrain(map_terrain)

    
    
    def load_objets_map_terrain(self,map):
        for index_fil,fila in enumerate(map):
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
                    self.player_group_single.sprite
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
        
