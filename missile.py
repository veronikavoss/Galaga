#%%
from setting import *
#%%
class Missile(pygame.sprite.Sprite):
    def __init__(self,asset,midtop):
        pygame.sprite.Sprite.__init__(self)
        self.asset=asset
        self.missile_images=asset.missile_images
        self.image=self.missile_images[1]
        self.rect=self.image.get_rect(midtop=midtop)
        self.speed=-10
    
    def update(self):
        self.rect.y+=self.speed
        if self.rect.bottom<0:
            self.kill()

class Enemy_Missile(pygame.sprite.Sprite):
    def __init__(self,asset,midbottom):
        pygame.sprite.Sprite.__init__(self)
        self.asset=asset
        self.missile_images=asset.missile_images
        self.image=self.missile_images[4]
        self.rect=self.image.get_rect(midbottom=midbottom)
        self.speed=5
    
    def update(self):
        self.rect.y+=self.speed
        if self.rect.top>stage_height:
            self.kill()
        print(self.rect)
    
    # def draw(self,screen):
    #     screen.blit(self.image,self.rect)