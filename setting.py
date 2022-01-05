#%%
import pygame,os
#%%
title='Shooting'
scale=3
screen_size=screen_width,screen_height=224*scale,288*scale
FPS=60
#%%
current_path=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(current_path,'image')
sound_path=os.path.join(current_path,'sound')