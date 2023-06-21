from settings import *
from terreno import Terreno


class Level_Surface:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.terrain = Terreno(self.display_surface,map_1)
    
    def run(self):
        self.display_surface.fill(CYAN)
        self.terrain.run()
        # self.display_surface.blit(self.load_background("./Surface/ground.png",),(0,450))
    
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