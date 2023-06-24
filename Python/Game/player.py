from settings import *
from sprite import Sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, position,folder_sprites) -> None:
        super().__init__()
        self.sprite_player = Sprite(folder_sprites)
        self.load_sprites()
        self.status = "Right_idle"
        self.index_status = 0
        self.image: pygame.Surface = self.animations[self.status][self.index_status]
        self.rect = self.image.get_rect(topleft = position)
        self.direction = pygame.math.Vector2()
        self.speed = SPEED
        self.status_gravity = 2
        self.jump_speed = -28
        self.flag_direct = True
        self.one_jump = False
        
        
    def input(self):
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
            


    def get_status(self):
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
        # if (self.one_jump and self.direction.y < 0 or self.direction.y > 0):
        #     self.one_jump = False


    def animation(self):
        self.index_status += 0.50
        if(self.index_status >= len(self.animations[self.status])):
            self.index_status = 0
        self.image = self.animations[self.status][int(self.index_status)]
        if(not self.flag_direct):
            self.image = pygame.transform.flip(self.image,True,False)
    
    
    def load_sprites(self):
        self.animations = self.sprite_player.load_all_sprites()
    
    def move(self):
        self.rect.x += self.direction.x * self.speed

    def collide(self,other):
        other.collide_with_player(self)
        
    def update(self):
        self.input()
        self.get_status()
        self.animation()

        
    