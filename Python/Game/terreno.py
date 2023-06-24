from settings import *
from plataforma import Plataforma
from player import Player
from enemigo import Enemigo

class Terreno:
    def __init__(self,map_terrain) -> None:
        self.platforms_group = pygame.sprite.Group()
        self.block_clear_group = pygame.sprite.Group()
        self.player_group_single = pygame.sprite.GroupSingle()
        self.enemys_group = pygame.sprite.Group()
        self.load_objets_map_terrain(map_terrain)

    

    def load_objets_map_terrain(self,map):
        for index_fil,fila in enumerate(map):
            for index_col,columna in enumerate(fila):
                x = index_col * size_plataforma
                y = index_fil * size_plataforma
                if (columna == "0"):
                    self.block_platform = Plataforma((x,y),size_plataforma,"./Images/tile_space/0.png")
                elif (columna == "1"):
                    self.block_platform = Plataforma((x,y),size_plataforma,"./Images/tile_space/1.png")
                elif (columna == "2"):
                    self.block_platform = Plataforma((x,y),size_plataforma,"./Images/tile_space/2.png")
                elif (columna == "3"):
                    self.block_platform = Plataforma((x,y),size_plataforma,"./Images/tile_space/3.png")
                elif (columna == "4"):
                    self.block_platform = Plataforma((x,y),size_plataforma,"./Images/tile_space/4.png")
                elif (columna == "5"):
                    self.block_platform = Plataforma((x,y),size_plataforma,"./Images/tile_space/5.png")
                elif (columna == "6"):
                    self.block_platform = Plataforma((x,y),size_plataforma,"./Images/tile_space/6.png")
                elif (columna == "X"):
                    self.block_platform = Plataforma((x,y),size_plataforma,"./Images/tile_space/X.png")
                elif (columna == "R"):
                    self.block = Plataforma((x,y),size_plataforma,"./Images/Surface/E.png")
                    self.block_clear_group.add(self.block)
                elif (columna == "p"):
                    self.player = Player((x,y),"./Images/Character")
                    self.player_group_single.add(self.player)
                elif (columna == "E"):
                    self.enemy = Enemigo((x,y),"./Images/Enemies/AngryPing")
                    self.enemys_group.add(self.enemy)

                self.platforms_group.add(self.block_platform)
    
    def collion_reverse_enemy(self):
        for enemy in self.enemys_group.sprites():
            if(pygame.sprite.spritecollide(enemy,self.block_clear_group,False)):
                enemy.reverse()


    def collision_vertical(self,object_sprite,sprite_group):
        object_sprite.move()
        for sprite in sprite_group.sprites():
            if(sprite.rect.colliderect(object_sprite.rect)):
                if(object_sprite.direction.x > 0):
                    object_sprite.rect.right = sprite.rect.left
                elif(object_sprite.direction.x < 0):
                    object_sprite.rect.left = sprite.rect.right
                

    def collision_horizontal(self,object_sprite,sprite_group):
        object_sprite.gravity()
        for sprite in sprite_group.sprites():
            if(sprite.rect.colliderect(object_sprite.rect)):
                if(object_sprite.direction.y > 0):
                    object_sprite.rect.bottom = sprite.rect.top
                    object_sprite.direction.y = 0
                    object_sprite.one_jump = True
                    object_sprite.flag_move = True
                elif(object_sprite.direction.y < 0):
                    object_sprite.rect.top = sprite.rect.bottom
        
        if (object_sprite.one_jump and object_sprite.direction.y < 0 or object_sprite.direction.y > 0):
            object_sprite.one_jump = False
    
    def collide_with_player(self,player):
        self.collision_vertical(player,self.platforms_group)
        self.collision_horizontal(player,self.platforms_group)
