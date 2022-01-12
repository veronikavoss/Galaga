#%%
from setting import *
#%%
class Asset:
    def __init__(self):
        self.game_sheet=pygame.image.load(os.path.join(image_path,'General_Sprites.png')).convert_alpha()
        self.start_screen=pygame.image.load(os.path.join(image_path,'start_screen.png')).convert_alpha()
        self.start_screen=pygame.transform.scale(self.start_screen,screen_size)
        self.start_screen.set_colorkey((0,0,0))
        self.get_background_image()
        self.get_player_images()
        self.get_enemies_images()
        self.get_missile_images()
    
    def get_background_image(self):
        background=pygame.image.load(os.path.join(image_path,'background.png'))
        self.background_image=pygame.transform.scale(background,(320*scale,256*scale))
    
    def get_player_images(self):
        self.player_images={'normal':[],'capture':[]}
        self.player_destroy_images=[]
        
        for y,key in enumerate(self.player_images.keys()):
            for x in range(7):
                surface=pygame.Surface(surface_size)
                surface.blit(self.game_sheet,(0,0),(18*x+1,18*y+1,surface_width,screen_height))
                surface=pygame.transform.scale(surface,surface_scale)
                surface.set_colorkey((0,0,0))
                self.player_images[key].append(surface)
        
        for x in range(4):
            surface=pygame.Surface((32,32))
            surface.blit(self.game_sheet,(0,0),(34*x+145,1,32,32))
            surface.set_colorkey((64,64,64))
            surface=pygame.transform.scale(surface,(32*scale,32*scale))
            surface.set_colorkey((0,0,0))
            self.player_destroy_images.append(surface)
    
    def get_enemies_images(self):
        self.enemies_images={'boss_galaga1':[],'boss_galaga2':[],'butterfly':[],'bee':[]}
        self.transform_enemies_images={'sasori':[],'midori':[],'galboss':[]}
        self.bonuses_enemies_images={'tonbo':[],'momiji':[],'enterprise':[]}
        self.enemy_destroy_images=[]
        
        for y,key in enumerate(self.enemies_images.keys()):
            for x in range(8):
                surface=pygame.Surface(surface_size)
                surface.blit(self.game_sheet,(0,0),(18*x+1,18*y+37,surface_width,screen_height))
                surface=pygame.transform.scale(surface,surface_scale)
                surface.set_colorkey((0,0,0))
                self.enemies_images[key].append(surface)
        for y,key in enumerate(self.transform_enemies_images.keys()):
            for x in range(7):
                surface=pygame.Surface(surface_size)
                surface.blit(self.game_sheet,(0,0),(18*x+1,18*y+109,surface_width,screen_height))
                surface=pygame.transform.scale(surface,surface_scale)
                surface.set_colorkey((0,0,0))
                self.transform_enemies_images[key].append(surface)
        for y,key in enumerate(self.bonuses_enemies_images.keys()):
            for x in range(7):
                surface=pygame.Surface(surface_size)
                surface.blit(self.game_sheet,(0,0),(18*x+1,18*y+163,surface_width,screen_height))
                surface=pygame.transform.scale(surface,surface_scale)
                surface.set_colorkey((0,0,0))
                self.bonuses_enemies_images[key].append(surface)
        del self.bonuses_enemies_images['momiji'][6]
        
        for x in range(5):
            surface=pygame.Surface((32,32))
            surface.blit(self.game_sheet,(0,0),(34*x+289,1,32,32))
            surface.set_colorkey((64,64,64))
            surface=pygame.transform.scale(surface,(32*scale,32*scale))
            surface.set_colorkey((0,0,0))
            self.enemy_destroy_images.append(surface)
    
    def get_missile_images(self):
        self.missile_images=[]
        for y in range(3):
            for x in range(3):
                surface=pygame.Surface(surface_size)
                surface.blit(self.game_sheet,(0,0),(18*x+289,18*y+118,surface_width,screen_height))
                surface=pygame.transform.scale(surface,surface_scale)
                surface.set_colorkey((0,0,0))
                self.missile_images.append(surface)