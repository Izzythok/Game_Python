from settings import *
import time

class Cronometro:
    def __init__(self,name_font: str,size_font: int,timer_seg: int) -> None:
        self.timer_seg = timer_seg
        self.size_font = size_font
        self.name_font = name_font
        self.font = pygame.font.Font(self.name_font,self.size_font)
        self.start = time.time() + self.timer_seg
    

    def play(self)->str:
        self.end = time.time()
        full_time = time.gmtime(self.start - self.end)
        minutes = time.strftime("%M:%S",full_time)
        return minutes
    
    def show_font(self,value: str,color: tuple, position, surface: pygame.Surface):
        score = self.font.render(value,True,color)
        surface.blit(score,position)

    def time_over(self,time: str)-> bool:
        return time == "00:00"


