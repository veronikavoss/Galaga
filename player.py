#%%
from setting import *
from missile import *
#%%
class Player(pygame.sprite.Sprite):
    def __init__(self,asset):
        pygame.sprite.Sprite.__init__(self)
        self.asset=asset
        self.player_images=self.asset.player_images
        self.player_destroy_images=self.asset.player_destroy_images
        self.status='normal'
        self.frame_index=0
        self.image=self.player_images[self.status][self.frame_index+6]
        self.rect=self.image.get_rect(midbottom=(screen_width//2,stage_height))
        self.speed=5
        self.launched=False
        
        self.player_missiles=pygame.sprite.Group()
    
    def key_input(self):
        key_input=pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            self.rect.x-=self.speed
        elif key_input[pygame.K_RIGHT]:
            self.rect.x+=self.speed
        
        if self.rect.left<=0:
            self.rect.left=0
        elif self.rect.right>=stage_width:
            self.rect.right=stage_width
        
        if key_input[pygame.K_SPACE]:
            if not self.launched:
                self.launch_missile()
        else:
            self.launched=False
    
    def launch_missile(self):
        self.player_missiles.add(Missile(self.asset,self.rect.midtop))
        self.launched=True
    
    def update(self):
        self.key_input()

class Destoy_Player(pygame.sprite.Sprite):
    def __init__(self,asset,center):
        super().__init__()
        self.asset=asset
        self.player_destroy_images=asset.player_destroy_images
        self.frame_index=0
        self.image=self.player_destroy_images[self.frame_index]
        self.rect=self.image.get_rect(center=center)
    
    def animation(self):
        animation=self.asset.player_destroy_images
        self.frame_index+=0.2
        if self.frame_index>=len(animation):
            self.frame_index=0
            self.kill()
        self.image=animation[int(self.frame_index)]
    
    def update(self):
        self.animation()