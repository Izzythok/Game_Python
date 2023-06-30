from settings import *
from sprite import Sprite
from sprites_object import Vidas
import time

class Player(pygame.sprite.Sprite):
    def __init__(self, position,folder_sprites,size: tuple) -> None:
        super().__init__()
        self.init_position = position
        self.size = size
        self.sprite_player = Sprite(folder_sprites)
        self.load_sprites()
        self.status = "Right_idle"
        self.index_status = 0
        self.image: pygame.Surface = self.animations[self.status][self.index_status]
        self.rect = self.image.get_rect(topleft = self.init_position)
        self.direction = pygame.math.Vector2()
        self.speed = SPEED
        self.status_gravity = 2.5
        self.jump_speed = -28
        self.increase_index = 0.50
        self.flag_direct = True
        self.one_jump = False
        self.stop_status = True
        self.stop_controllers = True
        self.dead_time = None
        self.life = 3
        
        
        
    def input(self):
        if(self.stop_controllers == True):
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_RIGHT]):
                self.direction.x = 1
                self.flag_direct = True
            elif(keys[pygame.K_LEFT]):
                self.direction.x = -1
                self.flag_direct = False
            else:
                self.direction.x = 0

            if(keys[pygame.K_UP] and self.one_jump):
                self.jump()
                self.play_song_jump("./audios/song/Jump.wav")
                


    def get_status(self):
        if(self.stop_status == True):
            if(self.direction.x > 0):
                self.status = "Right"
            elif(self.direction.x < 0):
                self.status = "Right"
            else:
                if(self.direction.y > 0):
                    self.status = "Fall"
                elif(self.direction.y < 0):
                    self.status = "Jump"
                else:
                    self.status = "Right_idle"



    def gravity(self):
        self.direction.y +=self.status_gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y = self.jump_speed


    def animation(self):
        self.index_status += self.increase_index
        if(self.index_status >= len(self.animations[self.status])):
            self.index_status = 0
        self.image = self.animations[self.status][int(self.index_status)]
        if(not self.flag_direct):
            self.image = pygame.transform.flip(self.image,True,False)
    
    
    def load_sprites(self):
        self.animations = self.sprite_player.load_all_sprites(self.size)
    
    def move(self):
        self.rect.x += self.direction.x * self.speed
    
    def lifes(self,x: int,y: int,life_group: pygame.sprite.Group):
        while (self.life > 0):
                self.life_p = Vidas((x,y),(50,50),"./Images/Items/heart")
                life_group.add(self.life_p)
                x += 60
                self.life -= 1

    def play_song_jump(self,song_path: str):
        self.song = pygame.mixer.Sound(song_path)
        self.song.play()

    def play_song_die(self,song_path: str):
        self.song = pygame.mixer.Sound(song_path)
        self.song.play()
    

    def reset_player(self):
        self.rect.topleft = self.init_position
        self.speed = SPEED
        self.status_gravity = 2.5
        self.jump_speed = -28
        self.increase_index = 0.5
        self.stop_status = True
        self.stop_controllers = True
        self.dead_time = None
    
    def stop_player(self):
        self.speed = 0
        self.status_gravity = 0
        self.jump_speed = 0
        self.stop_status = False
        self.stop_controllers = False

    def die(self):
        self.status = "Hit"
        self.stop_player()
        if(not self.dead_time):
            self.dead_time = time.time()
    
    def is_dead(self):
        return self.dead_time and time.time() - self.dead_time > 0.3

    def collision_vertical(self,sprite_group):
        self.move()
        for sprite in sprite_group.sprites():
            if(sprite.rect.colliderect(self.rect)):
                if(self.direction.x > 0):
                    self.rect.right = sprite.rect.left
                elif(self.direction.x < 0):
                    self.rect.left = sprite.rect.right
        

    def collision_horizontal(self,sprite_group):
        self.gravity()
        for sprite in sprite_group.sprites():
            if(sprite.rect.colliderect(self.rect)):
                if(self.direction.y > 0):
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.one_jump = True
                elif(self.direction.y < 0):
                    self.rect.top = sprite.rect.bottom
        
        if (self.one_jump and self.direction.y < 0 or self.direction.y > 0):
            self.one_jump = False
    
    def collide(self,other_object):
        other_object.collide_with_player(self)
        
    def update(self):
        self.input()
        self.get_status()
        self.animation()

        
    