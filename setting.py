#%%
import pygame,os
#%%
title='Galaga'
scale=3
screen_size=screen_width,screen_height=224*scale,288*scale # 14,18
stage_size=stage_width,stage_height=224*scale,256*scale
surface_size=surface_width,surface_height=16,16
surface_scale=surface_wscale,surface_hscale=16*scale,16*scale
FPS=60
#%%
current_path=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(current_path,'image')
sound_path=os.path.join(current_path,'sound')