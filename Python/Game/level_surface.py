from settings import *
from terreno import Terreno


class Level_Surface:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.terrain = Terreno(map_1)
    
    def run(self):
        self.display_surface.fill(CYAN)
        self.setup_surface_level_1()
        # self.display_surface.blit(self.load_background("./Surface/ground.png",),(0,450))
    
    def setup_surface_level_1(self):
        #Player
        sprite_player = self.terrain.player_group_single.sprite
        if(sprite_player):
            for platform in self.terrain.platforms_group.sprites():
                sprite_player.collide(platform)
                
            self.terrain.player_group_single.draw(self.display_surface)
            sprite_player.update()

        #Enemy
        for enemy in self.terrain.enemys_group.sprites():
            self.terrain.collision_vertical(enemy,self.terrain.platforms_group)
            self.terrain.collision_horizontal(enemy,self.terrain.platforms_group)
            if(sprite_player):
                sprite_player.collide(enemy)
            enemy.update()
        self.terrain.collion_reverse_enemy()
        self.terrain.enemys_group.draw(self.display_surface)

        #bloques
        self.terrain.block_clear_group.draw(self.display_surface)
        self.terrain.platforms_group.draw(self.display_surface)

    def scale(self,size):
        self.display_surface = pygame.transform.smoothscale(self.display_surface,size)

    def load_background(self, relative_path: str, width=None,height=None):
        back_ground = pygame.image.load(relative_path)
        if(width!=None and height!=None):
            back_ground = pygame.transform.scale(back_ground,(width,height))
        return back_ground
    
    def load_sound(self, relative_path: str):
        back_ground_sound = pygame.mixer.music.load(relative_path)
        return back_ground_sound