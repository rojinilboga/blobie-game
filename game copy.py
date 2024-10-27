#importing the libraries
import pgzrun
from random import randint

TITLE = "BLOBFISH SHOT GAME!!!"
WIDTH = 600
HEIGHT = 600
R = randint(1,255)
G = randint(1,255)
B = randint(1,255)
#creating the blobfish
blobfish =Actor("blobfish")

msg = ""

def draw():
    screen.clear()
    screen.fill(color =(R,G,B))

    blobfish.draw()
    screen.draw.text(msg, center=(100,10), fontsize=30)

def place_blobfish():
   blobfish.x=randint(50,550)
   blobfish.y=randint(50,550) 

def on_mouse_down(pos):
    global msg
    if blobfish.collidepoint(pos):
        msg = 'Good shot'
        place_blobfish()
    else:
        msg = "You missed:("


place_blobfish()


  



pgzrun.go()

