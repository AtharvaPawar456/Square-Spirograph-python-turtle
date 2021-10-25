# ref: https://cppsecrets.com/users/5440112114971061011151044611511410511897115116971189795991154956641031089746979946105110/Python-turtle-Square-Spirograph-Project.php

import turtle
turtle.speed(0)
turtle.bgcolor("black")
for i in range(5):
    for colours in ("red" ,"magenta","white","cyan","green","yellow","blue","purple","pink"):
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
turtle.done()