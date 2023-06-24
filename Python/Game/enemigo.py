from settings import *
from sprite import Sprite

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,position,folder_sprites) -> None:
        super().__init__()
        self.sprite_enemy = Sprite(folder_sprites)
        self.load_sprites()
        self.status = "Idle"
        self.index_status = 0
        self.image: pygame.Surface = self.animations[self.status][self.index_status]
        self.rect = self.image.get_rect(topleft = position)
        self.direction = pygame.math.Vector2()
        self.speed = SPEED_ENEMY
        self.status_gravity = 3
        self.one_jump = False
        self.flag_move = False

    def load_sprites(self):
        self.animations = self.sprite_enemy.load_all_sprites()

    def gravity(self):
        self.rect.y +=self.status_gravity
        self.direction.y = 1
    
    def move(self):
        if(self.flag_move):
            self.rect.x +=  self.speed
            self.status = "Walk"
            self.direction.x = 1
    
    def reverse_image(self):
        if(self.speed > 0):
            self.image = pygame.transform.flip(self.image,True,False)
            self.direction.x = -1

    def reverse(self):
        self.speed *= -1

    def animation(self):
        self.index_status += 0.50
        if(self.index_status >= len(self.animations[self.status])):
            self.index_status = 0
        self.image = self.animations[self.status][int(self.index_status)]

    def update(self):
        self.animation()
        self.reverse_image()

    def collide_with_player(self,player):
        if(pygame.sprite.collide_rect(self,player)):
            player.kill