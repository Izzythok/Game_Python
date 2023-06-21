from settings import *
from plataforma import Plataforma
from player import Player
from enemigo import Enemigo

class Terreno:
    def __init__(self,level_surface ,map_terrain) -> None:
        self.display_surface = level_surface
        self.setup_terrain(map_terrain)

    def setup_terrain(self,data):
        self.platforms = pygame.sprite.Group()
        self.block_clear = pygame.sprite.Group()
        self.player_1 = pygame.sprite.GroupSingle()
        self.enemy_1 = pygame.sprite.GroupSingle()
        for index_fil,fila in enumerate(data):
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
                    self.block_clear.add(self.block)
                elif (columna == "p"):
                    self.player = Player((x,y),"./Images/Character")
                    self.player_1.add(self.player)
                elif (columna == "E"):
                    self.enemy = Enemigo((x,y),"./Images/Enemies/AngryPing")
                    self.enemy_1.add(self.enemy)

                self.platforms.add(self.block_platform)
        
    
    # def collision_vertical_enemy(self):
    #     ob_enemy: Enemigo = self.enemy_1.sprite
    #     ob_enemy.move()
    #     for sprite in self.platforms.sprites():
    #         if(sprite.rect.colliderect(ob_enemy.rect)):   
    #             ob_enemy.flag_move = True
    
    def collion_reverse_enemy(self):
        enemy = self.enemy_1.sprite
        if(pygame.sprite.spritecollide(enemy,self.block_clear,False)):
            enemy.reverse()


    def collision_vertical(self,sprite_single,sprite_group):
        objet = sprite_single.sprite
        objet.move()
        for sprite in sprite_group.sprites():
            if(sprite.rect.colliderect(objet.rect)):
                if(objet.direction.x > 0):
                    objet.rect.right = sprite.rect.left
                elif(objet.direction.x < 0):
                    objet.rect.left = sprite.rect.right
                

    def collision_horizontal(self,sprite_single,sprite_group):
        object = sprite_single.sprite
        object.gravity()
        for sprite in sprite_group.sprites():
            if(sprite.rect.colliderect(object.rect)):
                if(object.direction.y > 0):
                    object.rect.bottom = sprite.rect.top
                    object.direction.y = 0
                    object.one_jump = True
                    object.flag_move = True
                elif(object.direction.y < 0):
                    object.rect.top = sprite.rect.bottom
        
        if (object.one_jump and object.direction.y < 0 or object.direction.y > 0):
            object.one_jump = False
        

    
    def run(self):
        # self.collision_vertical_enemy()
        self.collision_vertical(self.enemy_1,self.platforms)
        self.collision_horizontal(self.enemy_1,self.platforms)

        self.collision_vertical(self.player_1,self.platforms)
        self.collision_horizontal(self.player_1,self.platforms)

        self.block_clear.draw(self.display_surface)
        self.platforms.draw(self.display_surface)
        self.collion_reverse_enemy()
        self.enemy_1.draw(self.display_surface)
        self.enemy.update()

        self.player_1.draw(self.display_surface)
        self.player.update()
        