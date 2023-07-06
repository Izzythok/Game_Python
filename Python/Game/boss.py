from settings import *
from sprite import Sprite
from sprites_object import Proyectil, Vidas
import time

class Boss(pygame.sprite.Sprite):
    def __init__(self,position: tuple,folder_sprites,size: tuple) -> None:
        super().__init__()
        self.sprite_boss = Sprite(folder_sprites)
        self.size = size
        self.position = position
        self.load_sprites()
        self.status = "Idle"
        self.index_status = 0
        self.image: pygame.Surface = self.animations[self.status][self.index_status]
        self.rect = self.image.get_rect(topleft = self.position)
        self.direction = pygame.math.Vector2()
        self.speed = -10
        self.status_gravity = 3
        self.increase_index = 0.5
        self.one_jump = False
        self.flag_move = False
        self.time_shoot = None
        self.interval_shoot = 5
        self.value_die = 0
        self.life = 7
        self.dead_time = None
        self.song_hit = None
        self.song_die = None

    def load_sprites(self):
        self.animations = self.sprite_boss.load_all_sprites(self.size)

    def gravity(self):
        self.rect.y +=self.status_gravity
        self.direction.y = 1
    
    def move(self):
        if(self.flag_move):
            if(self.speed != 0):
                self.rect.x +=  self.speed
                self.status = "Walk"
                if(self.speed > 0):
                    self.direction.x = 1
                elif(self.speed < 0):
                    self.direction.x = -1
    
    def animation(self):
        self.index_status += self.increase_index
        if(self.index_status >= len(self.animations[self.status])):
            self.index_status = 0
        self.image = self.animations[self.status][int(self.index_status)]

    def reverse_image(self):
        if(self.speed < 0):
            self.image = pygame.transform.flip(self.image,True,False)

    def reverse(self):
        self.speed *= -1
    
    def play_song_hit(self,song_path):
        self.song_hit = pygame.mixer.Sound(song_path)
        self.song_hit.play()
    
    def play_song_die(self,song_path):
        self.song_die = pygame.mixer.Sound(song_path)
        self.song_die.play()

    def reset(self):
        self.speed = -10
        self.status_gravity = 3
        self.increase_index = 0.5
        self.dead_time = None
    
    def stop(self):
        self.speed = 0
        self.status_gravity = 0
    
    def die(self):
        self.status = "Hit"
        self.stop()
        self.play_song_hit("./audios/song/hitBoss.wav")
        if(not self.dead_time):
            self.dead_time = time.time()
    
    def is_dead(self):
        return self.dead_time and time.time() - self.dead_time > 0.3
    
    def lifes(self,x: int,y: int,life_group: pygame.sprite.Group):
        while (self.life > 0):
            self.life_b = Vidas((x,y),(50,50),"./Images/Items/heart")
            life_group.add(self.life_b)
            x += 60
            self.life -= 1

    def collision_vertical(self,sprite_group):
        self.move()
        for sprite in sprite_group.sprites():
            if(sprite.rect.colliderect(self.rect)):
                if(self.direction.x > 0):
                    self.rect.right = sprite.rect.left
                    self.reverse()
                elif(self.direction.x < 0):
                    self.rect.left = sprite.rect.right
                    self.reverse()
                

    def collision_horizontal(self,sprite_group):
        self.gravity()
        for sprite in sprite_group.sprites():
            if(sprite.rect.colliderect(self.rect)):
                if(self.direction.y > 0):
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.flag_move = True

    def collide(self,other_object):
        other_object.collide_with_boss(self)
    
    def update(self):
        self.animation()
        self.reverse_image()