from settings import *

class Plataforma(pygame.sprite.Sprite):

    def __init__(self,position: tuple,size,sprite) -> None:
        super().__init__()
        self.position = position
        self.size = size
        self.sprite = sprite
        self.image = pygame.image.load(self.sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size,self.size))
        self.rect = self.image.get_rect(topleft = self.position)

    def collision_vertical(self,object_sprite):
        pass
        # object_sprite.move()
        # if(pygame.sprite.collide_rect(object_sprite,self)):
        #     if(object_sprite.direction.x > 0):
        #         object_sprite.rect.right = self.rect.left
        #     elif(object_sprite.direction.x < 0):
        #         object_sprite.rect.left = self.rect.right
                

    def collision_horizontal(self,object_sprite):
        object_sprite.gravity()
        # if(pygame.sprite.collide_rect(object_sprite,self)):
        #     if(object_sprite.direction.y > 0):
        #         object_sprite.rect.bottom = self.rect.top
        #         object_sprite.direction.y = 0
        #         object_sprite.one_jump = True
        #     elif(object_sprite.direction.y < 0):
        #         object_sprite.rect.top = self.rect.bottom
        
        # if (object_sprite.one_jump and object_sprite.direction.y < 0 or object_sprite.direction.y > 0):
        #     object_sprite.one_jump = False

    def collide_with_player(self,player):
        self.collision_vertical(player)
        self.collision_horizontal(player)


        
