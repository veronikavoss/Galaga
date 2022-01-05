#%%
from setting import *
#%%
class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((5,10))
        self.image.fill('white')
        self.rect=self.image.get_rect(midtop=pos)
        self.speed=-10
    
    def update(self):
        self.rect.y+=self.speed