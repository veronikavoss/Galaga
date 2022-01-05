#%%
from setting import *
from player import *
#%%
class Controller:
    def __init__(self,screen):
        self.screen=screen
        self.player_sprite=pygame.sprite.GroupSingle(Player())
    
    def update(self):
        self.player_sprite.sprite.bullet.update()
        self.player_sprite.update()
    
    def draw(self):
        self.screen.fill('black')
        self.player_sprite.sprite.bullet.draw(self.screen)
        self.player_sprite.draw(self.screen)