import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
TITLE ="Shooting Game"
message="Loading..."

target=Actor('target') 
target.pos=50,50

def draw():
    screen.clear() 
    screen.fill('black') 
    target.draw()
    screen.draw.text(message, center =(200,20), fontsize=30, color="white") 

def moveTarget():
    target.x = randint(50,350)
    target.y = randint(50,350)

def on_mouse_down(pos):
    global message
    if target.collidepoint(pos):
        message= "Good shot"
        moveTarget()
    else:
        message= "Try again"
        moveTarget()

moveTarget()
pgzrun.go()

