# https://strategywiki.org/wiki/Galaga/Gameplay
#%%
from missile import Enemy_Missile
from setting import *
#%%
class Enemy(pygame.sprite.Sprite):
    def __init__(self,asset,index,enemy_name,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.asset=asset
        self.enemies_images=self.asset.enemies_images
        self.index=index
        self.enemy_name=enemy_name
        self.frame_index=6
        self.image=self.enemies_images[self.enemy_name][self.frame_index]
        self.rect=self.image.get_rect(x=x,y=y)
        
        # self.enemies_missile=pygame.sprite.Group()
        # self.enemies_missile.add(Enemy_Missile(self.asset,self.rect.center))
    
    def animation(self):
        self.frame_index+=0.02
        animation=self.enemies_images[self.enemy_name]
        if self.frame_index>=len(animation):
            self.frame_index=6
        
        self.image=animation[int(self.frame_index)]
    
    def update(self):
        self.rect.y+=2
        self.animation()

class Destroy_Enemy(pygame.sprite.Sprite):
    def __init__(self,asset,center):
        super().__init__()
        self.asset=asset
        self.enemy_destroy_images=self.asset.enemy_destroy_images
        self.frame_index=0
        self.image=self.enemy_destroy_images[self.frame_index]
        self.rect=self.image.get_rect(center=center)
        
    def animation(self):
        self.frame_index+=0.2
        animation=self.enemy_destroy_images
        if self.frame_index>=len(animation):
            self.frame_index=0
            self.kill()
        self.image=animation[int(self.frame_index)]
    
    def update(self):
        self.animation()