from ursina import *
from ursina.shaders import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import time
Game = Ursina()
Sky()
window.borderless = False
window.cog_button.disable()
#window.fps_counter.disable()
window.exit_button.disable()
def input(key):
    if key == "left mouse down":
        if Pistol.visible == True:
            Audio("Assets/Pistol_Gunshot.mp3")
        if Enemy1.hovered:
            destroy(Enemy1)
    if key == "tab":
        EditorCamera()
    if key == "escape":
        mouse.locked = not mouse.locked
    if key == "e":
        Pistol.visible = not Pistol.visible
        Shotgun.visible = not Shotgun.visible
        if Pistol.visible == True:
            Pistol_cursor.color = color.gray
            Shotgun_cursor.color = color.light_gray
        if Shotgun.visible == True:
            Pistol_cursor.color = color.light_gray
            Shotgun_cursor.color = color.gray
def update():
    try:
        Enemy1.look_at(Player)
    except:
        print("Error: Enemy cannot look at player")
    if held_keys["left mouse"]:
        Pistol.rotation = (10,25,0)
        Shotgun.rotation = (-6, -10, -10)
    else:
        Pistol.rotation = (5,25,0)
        Shotgun.rotation = (-5, -10, -10)
#Enemy
x = random.randint(-25,25)
z = random.randint(-25,25)
Enemy1 = Button(parent=scene,model="Assets/Running.fbx", texture="white_cube", position=(x,1,z), scale = 0.01, collider="mesh",color=color.gray,highlight_color=color.gray)
#MAP
for i in range(150):
    x = random.randint(-25,25)
    z = random.randint(-25,25)
    rocks = Entity(model="Assets/Rocks.obj", scale = .005, color=color.gray, position=(x, 0, z),shader=basic_lighting_shader, rotation=(0,random.randint(1,180),0))
arch = Entity(model="Assets/arch.obj", scale = .1, color=color.rgb(112, 112, 112), position=(4,4,4),shader=basic_lighting_shader, collider="mesh")
#MAP
Floor = Entity(collider="box", model="plane", position=(0,0,0), scale=(50,0,50), texture="Assets/download.jpg", texture_scale=(10,10), color=color.lime)
Player = FirstPersonController(position=(0,1,0))
#GUNS
Shotgun = Entity(model="Assets/shotgun.obj", parent = camera.ui, scale = .3, color=color.gray, position=(.7, -.5), rotation=(-5, -10, -10))
Pistol = Entity(model="Assets/pistol.obj", parent = camera.ui, scale = .01, color=color.gray, position=(.7, -.5, 1.1),rotation=(5,25,0))
Shotgun.visible = False
Shotgun_cursor = Entity(model="cube", parent = camera.ui, scale = .1,texture="Assets/shotgun-icon.png", position=(0.6,-0.4,0))
Pistol_cursor = Entity(model="cube", parent = camera.ui, scale = .1,texture="Assets/pistol-icon.png", position=(0.72,-0.4,0), color=color.cyan)
#GUNS
Cursor = Entity(model="cube", parent = camera.ui, scale = .05, color=color.white, position=(0,0), texture="Assets/gun-pointer.png")
destroy(Player.cursor)
Game.run()
