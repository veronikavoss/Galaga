#%%
from setting import *
from bullet import *
#%%
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bullet=pygame.sprite.Group()
        self.image=pygame.Surface((30,20))
        self.image.fill('blue')
        self.rect=self.image.get_rect(midbottom=(screen_width//2,screen_height))
        self.speed=3
        self.launch_cooldown=400
        self.launch_update=0
        self.launched=False
    
    def launch_bullet(self):
        self.bullet.add(Bullet(self.rect.midtop))
        self.launch_update=pygame.time.get_ticks()
        self.launched=True
    
    def launch_delay(self):
        self.current_time=pygame.time.get_ticks()
        if self.current_time-self.launch_update>=self.launch_cooldown:
            self.launched=False
    
    def key_input(self):
        key_input=pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            self.rect.x-=self.speed
        elif key_input[pygame.K_RIGHT]:
            self.rect.x+=self.speed
        if key_input[pygame.K_SPACE] and not self.launched:
            self.launch_bullet()
    
    def update(self):
        self.key_input()
        self.launch_delay()
        print(self.launched)