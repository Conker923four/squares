import pygame 

class Platform(pygame.sprite.Sprite):
    def __init__(self, x=90, y=400, w = 20, h = 50):
        super().__init__()
        self.x = x
        self.y = y
        self.surf = pygame.Surface((w, h))
        self.surf.fill((237, 107, 134))
        self.rect = self.surf.get_rect()
        self.image = self.surf

    def update(self, cX ,cY, collisions, delta):
        
        self.rect.center = (self.x - cX, self.y -cY)
        
