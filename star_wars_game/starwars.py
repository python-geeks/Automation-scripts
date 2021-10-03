#This is the First Part:

import turtle
import math
import random

window = turtle.Screen()
window.setup(width=600, height=600)
window.title("Star Wars Game by Max Müller")
window.bgcolor("black")

window.tracer(0)

vertex = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18, 5),(15, 0))
window.register_shape("player", vertex)

asVertex = ((0, 10), (5, 7), (3,3), (10,0), (7, 4), (8, -6), (0, -10), (-5, -5), (-7, -7), (-10, 0), (-5, 4), (-1, 8))
window.register_shape("chattan", asVertex)

####################
#This is the Second Part:


class Max(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.speed(0)
        self.penup()


def max1(t1, t2):
    x1 = t1.xcor()
    y1 = t1.ycor()
    
    x2 = t2.xcor()
    y2 = t2.ycor()
    
    taauko = math.atan2(y1 - y2, x1 - x2)
    taauko = taauko * 180.0 / 3.14159
    
    return taauko


player = Max()
player.color("white")
player.shape("player")
player.score = 0

####################
#This is the Third Part

missiles = []
for _ in range(3):
    missile = Max()
    missile.color("red")
    missile.shape("arrow")
    missile.speed = 1
    missile.state = "ready"
    missile.hideturtle()
    missiles.append(missile)

pen = Max()
pen.color("white")
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0", False, align = "center", font = ("Arial", 24, "normal"))

####################
#This is the Fourth Part


chattans = []

for _ in range(5):   
    chattan = Max()
    chattan.color("brown")
    chattan.shape("arrow")

    chattan.speed  = random.randint(2, 3)/50
    chattan.goto(0, 0)
    taauko = random.randint(0, 260)
    distance = random.randint(300, 400)
    chattan.setheading(taauko)
    chattan.fd(distance)
    chattan.setheading(max1(player, chattan))
    chattans.append(chattan)

####################
#This is the Functions for Defence Part

def baanya():
    player.lt(20)
    
def daanya():
    player.rt(20)
    
def fire_missile():
    for missile in missiles:
        if missile.state == "ready":
            missile.goto(0, 0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state = "fire"
            break


window.listen()
window.onkey(baanya, "Left")
window.onkey(daanya, "Right")
window.onkey(fire_missile, "space")

####################
#This is the Functioning the Code Part-1

sakkyo = False
while True:

    window.update()
    player.goto(0, 0)
    

    for missile in missiles:
        if missile.state == "fire":
            missile.fd(missile.speed)
        
        if missile.xcor() > 300 or missile.xcor() < -300 or missile.ycor() > 300 or missile.ycor() < -300:
            missile.hideturtle()
            missile.state = "ready"

    for chattan in chattans:    
        chattan.fd(chattan.speed)
        
        for missile in missiles:
            if chattan.distance(missile) < 20:
                taauko = random.randint(0, 260)
                distance = random.randint(600, 800)
                chattan.setheading(taauko)
                chattan.fd(distance)
                chattan.setheading(max1(player, chattan))
                chattan.speed += 0.01
                
                missile.goto(600, 600)
                missile.hideturtle()
                missile.state = "ready"
                
                player.score += 10
                pen.clear()
                pen.write("Score: {}".format(player.score), False, align = "center", font = ("Arial", 24, "normal"))

        ####################
        #This is the Functioning the Code Part-2

        if chattan.distance(player) < 20:
            taauko = random.randint(0, 260)
            distance = random.randint(600, 800)
            chattan.setheading(taauko)
            chattan.fd(distance)
            chattan.setheading(max1(player, chattan))
            chattan.speed += 0.005
            sakkyo = True
            player.score -= 30
            pen.clear()
            pen.write("Score: {}".format(player.score), False, align = "center", font = ("Arial", 24, "normal"))
    if sakkyo == True:
        player.hideturtle()
        missile.hideturtle()
        for a in chattans:
            a.hideturtle()
        pen.clear()
        break

window.mainloop()
# This Game is build by Max Müller
