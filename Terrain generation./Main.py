from ursina import *
from perlin_noise import PerlinNoise
import random
app = Ursina()
window.borderless = False #adding normal window controls
window.exit_button.enabled = False #removing default exit button
seed = random.randint(1,100)
noise = PerlinNoise(octaves=3, seed=seed)
for x in range(50): 
    for z in range(50):
        y = .25 + noise([x/50, z/50])
        Voxel = Entity(position=(x,y,z), model="cube", texture="white_cube") #Create voxels
EditorCamera() #Simple camera
app.run()
