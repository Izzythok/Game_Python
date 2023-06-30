from settings import *

class Puntuacion:
    def __init__(self,name_font: str,size_font: int) -> None:
        self.name_font = name_font
        self.value = 0
        self.size_font = size_font
        self.font = pygame.font.Font(self.name_font,self.size_font)
    
    def show_font(self, position: tuple,text: str,color: tuple, surface: pygame.Surface):
        score = self.font.render(text,True,color)
        surface.blit(score,position)

    def increase(self,value: int):
        self.value += value

