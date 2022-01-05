#%%
from setting import *
from controller import *
#%%
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen=pygame.display.set_mode(screen_size)
        self.clock=pygame.time.Clock()
        self.playing=True
        self.start_screen()
    
    def start_screen(self):
        self.start()
    
    def start(self):
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
        pass
    
    def draw(self):
        self.screen.fill('black')
galaga=Game()
pygame.quit()