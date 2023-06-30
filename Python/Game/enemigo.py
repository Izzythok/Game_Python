from settings import *
from sprite import Sprite
from sprites_object import Proyectil
import time

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,position: tuple,folder_sprites,size: tuple,song_path: str) -> None:
        super().__init__()
        self.sprite_enemy = Sprite(folder_sprites)
        self.size = size
        self.position = position
        self.song_path = song_path
        self.load_sprites()
        self.status = "Idle"
        self.index_status = 0
        self.image: pygame.Surface = self.animations[self.status][self.index_status]
        self.rect = self.image.get_rect(topleft = self.position)
        
        self.direction = pygame.math.Vector2()
        self.speed = SPEED_ENEMY
        self.status_gravity = 3
        self.increase_index = 0.5
        self.one_jump = False
        self.flag_move = False
        self.time_shoot = None
        self.interval_shoot = 5
        self.value_die = 0
        # self.rect.midright

    def load_sprites(self):
        self.animations = self.sprite_enemy.load_all_sprites(self.size)

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
    
    def reverse_image(self):
        if(self.speed > 0):
            self.image = pygame.transform.flip(self.image,True,False)

    def reverse(self):
        self.speed *= -1

    def animation(self):
        self.index_status += self.increase_index
        if(self.index_status >= len(self.animations[self.status])):
            self.index_status = 0
        self.image = self.animations[self.status][int(self.index_status)]
    
    def stop_move(self):
        self.speed = 0

    def play_song_die(self):
        self.song = pygame.mixer.Sound(self.song_path)
        self.song.play()
    

    def shoot(self,state,pisition: tuple,size_bullet: tuple,path: str, speed_bullet: int,sprite_group: pygame.sprite.Group):
        self.status = state
        projec = Proyectil(pisition,size_bullet,path,speed_bullet,"./audios/song/shot.wav")
        self.time_shoot = time.time()
        projec.play_song()
        sprite_group.add(projec)
    
    def can_shoot(self):
            return not self.time_shoot or (time.time() - self.time_shoot > self.interval_shoot)

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

    def collide_with_player(self,player):
        if(pygame.sprite.collide_rect(self,player)):
            if(player.direction.x > 0):
                player.die()
                player.play_song_die("./audios/song/Die_Player.wav")
            elif(player.direction.x < 0):
                player.die()
                player.play_song_die("./audios/song/Die_Player.wav")
            elif(player.direction.y > 0):
                # self.status = "Hit"
                self.kill()
                self.play_song_die()
                self.value_die += 10
            else:
                player.die()
                player.play_song_die("./audios/song/Die_Player.wav")


    def collide(self,other_object):
        other_object.collide_with_enemy(self)

    def update(self):
        self.animation()
        self.reverse_image()