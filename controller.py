#%%
from enemy import Enemy, Destroy_Enemy
from setting import *
from player import *
#%%
class Controller:
    def __init__(self,screen,asset):
        self.screen=screen
        self.asset=asset
        self.get_background()
        self.start_screen=True
        
        self.player_sprite=pygame.sprite.GroupSingle(Player(self.asset))
        self.player_destroyed_sprite=pygame.sprite.GroupSingle()
        self.enemies_missile=pygame.sprite.Group()
        self.enemies_sprite=pygame.sprite.Group()
        self.enemies_destroyed_sprite=pygame.sprite.GroupSingle()
        self.enemy_spawn()
        self.update_time=0
    
    def get_background(self):
        self.background_image=self.asset.background_image
        self.background_image_rect1=self.background_image.get_rect(y=-256*scale)
        self.background_image_rect2=self.background_image.get_rect()
        
        self.background_scroll_speed=2
        self.background_flip=0
    
    def set_background(self):
        self.background_flip+=1
        if self.background_flip%50==0:
            self.background_image=pygame.transform.flip(self.background_image,True,False)
        else:
            self.background_image=pygame.transform.flip(self.background_image,False,False)
        
        self.background_image_rect1.y+=self.background_scroll_speed
        self.background_image_rect2.y+=self.background_scroll_speed
        if self.background_image_rect1.top>=stage_height:
            self.background_image_rect1.y=-256*scale
        elif self.background_image_rect2.top>=stage_height:
            self.background_image_rect2.y=-256*scale
    
    def background_draw(self):
        self.screen.blit(self.background_image,self.background_image_rect1)
        self.screen.blit(self.background_image,self.background_image_rect2)
        info_board=pygame.Rect(0,stage_height,stage_width,screen_height)
        pygame.draw.rect(self.screen,'black',info_board)
    
    def draw_start_screen(self):
        self.screen.blit(self.asset.start_screen,(0,0))
    
    def enemy_spawn(self):
        for y in range(2):
            for x in range(14):
                enemy1=Enemy(self.asset,x+1+(y*14),'boss_galaga1',x*48,y*48)
                enemy2=Enemy(self.asset,x+1+(y*14),'butterfly',x*48,(y+2)*48)
                enemy3=Enemy(self.asset,x+1+(y*14),'bee',x*48,(y+4)*48)
                self.enemies_sprite.add(enemy1,enemy2,enemy3)
    
    def enemy_missile_launch(self):
        current_time=pygame.time.get_ticks()
        if current_time-self.update_time>=1000:
            for enemy in self.enemies_sprite:
                if enemy.enemy_name=='bee':
                    if 26>=enemy.index>=17:
                        self.enemies_missile.add(Enemy_Missile(self.asset,enemy.rect.midbottom))
                        self.update_time=pygame.time.get_ticks()
    
    def collision(self):
        if self.player_sprite:
            for player in self.player_sprite:
                for enemy in self.enemies_sprite:
                    if pygame.sprite.collide_mask(player,enemy):
                        player.kill()
                        self.player_destroyed_sprite.add(Destoy_Player(self.asset,player.rect.center))
                for missile in self.enemies_missile:
                    if pygame.sprite.collide_mask(player,missile):
                        player.kill()
                        self.player_destroyed_sprite.add(Destoy_Player(self.asset,player.rect.center))
        
        if self.player_sprite:
            if self.player_sprite.sprite.player_missiles:
                for missile in self.player_sprite.sprite.player_missiles:
                    for enemy in self.enemies_sprite:
                        if pygame.sprite.collide_mask(missile,enemy):
                            if enemy.enemy_name=='boss_galaga1':
                                enemy.enemy_name='boss_galaga2'
                                missile.kill()
                            else:
                                self.enemies_destroyed_sprite.add(Destroy_Enemy(self.asset,enemy.rect.center))
                                missile.kill()
                                enemy.kill()
    
    def check_index(self):
        mouse_pos=pygame.mouse.get_pos()
        for enemy in self.enemies_sprite:
            if enemy.rect.collidepoint(mouse_pos):
                print(enemy.index)
    
    def update(self):
        if self.start_screen:
            self.set_background()
        else:
            self.set_background()
            if self.player_sprite.sprite:
                self.player_sprite.sprite.player_missiles.update()
            self.player_sprite.update()
            self.player_destroyed_sprite.update()
            self.enemies_missile.update()
            self.enemies_sprite.update()
            self.enemies_destroyed_sprite.update()
            self.collision()
            self.enemy_missile_launch()
            self.check_index()
    
    def draw(self):
        if self.start_screen:
            self.screen.fill('black')
            self.background_draw()
            self.draw_start_screen()
        else:
            self.screen.fill('black')
            self.background_draw()
            if self.player_sprite.sprite:
                self.player_sprite.sprite.player_missiles.draw(self.screen)
            self.player_sprite.draw(self.screen)
            self.player_destroyed_sprite.draw(self.screen)
            self.enemies_missile.draw(self.screen)
            self.enemies_sprite.draw(self.screen)
            self.enemies_destroyed_sprite.draw(self.screen)