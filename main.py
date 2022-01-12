#%%
from asset import Asset
from setting import *
from controller import *
#%%
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen=pygame.display.set_mode(screen_size)
        self.asset=Asset()
        self.clock=pygame.time.Clock()
        self.playing=True
        self.set_start_screen()
    
    def set_start_screen(self):
        self.controller=Controller(self.screen,self.asset)
        start_screen=True
        while start_screen:
            self.clock.tick(FPS)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    start_screen=False
                if event.type==pygame.KEYUP:
                    start_screen=False
                    self.start()
            self.controller.update()
            self.controller.draw()
    
    def start(self):
        self.controller=Controller(self.screen,self.asset)
        self.controller.start_screen=False
        self.loop()
    
    def loop(self):
        while self.playing:
            self.dt=self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
    
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
    
    def update(self):
        self.controller.update()
    
    def draw(self):
        self.controller.draw()

galaga=Game()
pygame.quit()