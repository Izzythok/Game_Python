from settings import *
from sprite import Sprite

class Vidas(pygame.sprite.Sprite):
    def __init__(self,position: tuple,size: tuple,folder: str) -> None:
        super().__init__()
        self.position = position
        self.size = size
        self.folder = folder
        self.sprite_life = Sprite()
        self.load_sprites()
        self.index_status = 0
        self.increase_index = 0.2
        self.image: pygame.Surface = self.animations[self.index_status]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def load_sprites(self):
        self.animations = self.sprite_life.load_sprite_path(self.folder,self.size)
    
    def animation(self):
        self.index_status += self.increase_index
        if(self.index_status >= len(self.animations)):
            self.index_status = 0
        self.image = self.animations[int(self.index_status)]
    
    def update(self):
        self.animation()

class Items(Vidas):
    def __init__(self, position: tuple, size: tuple, folder: str,song_path: str) -> None:
        super().__init__(position, size, folder)
        self.song_path = song_path
        self.value_collide = 0
        self.cup_winner = None

    def play_song(self):
        self.song = pygame.mixer.Sound(self.song_path)
        self.song.play()
    
    def stop_music(self):
        self.song.stop()

    def collide_winner(self,player):
        if(pygame.sprite.collide_rect(self,player)):
            self.play_song()
            self.kill()
            self.cup_winner = 1

    def collide_with_player(self, player):
        if(pygame.sprite.collide_rect(self,player)):
            self.value_collide += 5
            self.play_song()
            self.kill()


class Proyectil(Vidas):
    def __init__(self, position: tuple, size: tuple, folder: str,speed: int,song_path: str) -> None:
        super().__init__(position, size, folder)
        self.speed = speed
        self.song_path = song_path
        self.direction = pygame.math.Vector2()
    
    def play_song(self):
        self.song = pygame.mixer.Sound(self.song_path)
        self.song.play()

    def move_positive_x(self):
        self.rect.x += self.speed
        self.direction.x = 1
    
    def move_negative_x(self):
        self.rect.x -= self.speed
        self.direction.x = -1
    
    def collide_with_player(self, player):
        if(pygame.sprite.collide_rect(self,player)):
            player.die()
            player.play_song_die("./audios/song/Die_Player.wav")
            self.kill()
    
    def collide_with_platfomr(self, sprite_group):
        for sprite in sprite_group.sprites():
            if(sprite.rect.colliderect(self.rect)):
                self.kill()
    
    def collide(self, other_object):
        other_object.collide_with_projectile(self)

    def update(self):
        self.move_negative_x()

