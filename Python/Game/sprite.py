from os import walk
import pygame

class Sprite:
    def __init__(self,path_folder) -> None:
        self.path_folder = path_folder

    def load_sprite_path(self,path)-> list:
        """Carga los sprite de una carpeta donde estan alojadas

        Args:
            path (_type_): Recibe la direccion de la carpeta

        Returns:
            _type_: Devuelve una lista con los sprite
        """
        surfece_list = []
        for _,_,folder in walk(path):
            for i in range(len(folder)):
                full_path = path + "/" + folder[i]
                picture = pygame.image.load(full_path).convert_alpha()
                picture = pygame.transform.scale(picture, (35,35))
                surfece_list.append(picture)
        
        return surfece_list
    
    def load_all_sprites(self):
        dict_sprites = {}
        for _,folder_name,_ in walk(self.path_folder):
            for i in range(len(folder_name)):
                path = self.path_folder + "/" + folder_name[i]
                dict_sprites[folder_name[i]] = self.load_sprite_path(path)
        
        return dict_sprites
