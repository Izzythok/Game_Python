from settings import *

class Plataforma(pygame.sprite.Sprite):

    def __init__(self,position: tuple,size: tuple,sprite) -> None:
        super().__init__()
        self.position = position
        self.size = size
        self.sprite = sprite
        self.image = pygame.image.load(self.sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
    
    

        
