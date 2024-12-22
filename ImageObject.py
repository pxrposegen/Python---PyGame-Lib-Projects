import pygame 
from os.path import join 

class ImageObject: 
    def __init__(self,filepath):
        store = tuple(filepath.split("/"))
        self.image = pygame.image.load(join(*store)).convert_alpha()
        
    
    def scale(self,w = None, h = None):
        self.image = pygame.transform.scale(self.image,(w,h))
    
    def frectposition(self, position, x, y):
        self.frect = self.image.get_frect(**{position: (x, y)})
