from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from ursina.prefabs.first_person_controller import FirstPersonController
App = Ursina()
window.borderless = False
window.cog_button.disable()
window.fps_counter.disable()
window.exit_button.disable()
Sky()
def Cube():
    cube = Draggable(color=color.gray,parent=scene,model="cube",texture="white_cube",lock=(0,1,1))
def Sphere():
    Entity(model="shpere",texture="white_cube")
def Plane():
    Entity(model="plane",texture="white_cube")
def Player():
    moveablecamera.enabled = False
    FirstPersonController()
def camera():
    moveablecamera.enabled = not moveablecamera.enabled
addmenu = DropdownMenu('Menu', buttons=(
    DropdownMenu('Add Object', buttons=(
        DropdownMenuButton('Add New Cube', on_click=Cube),
        DropdownMenuButton('Add New Sphere', on_click=Sphere),
        DropdownMenuButton('Add New Plane', on_click=Plane),
        )),
    DropdownMenuButton('Toggle Moveable camera', on_click=camera),
    DropdownMenuButton('Run Game', on_click=Player),
    ))
moveablecamera = EditorCamera()
moveablecamera.enabled = False
App.run()
