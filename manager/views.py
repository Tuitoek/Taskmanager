# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.title("Clock")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def drawclock(pen):
    #Draw clock face
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("blue")
    pen.pendown()
    pen.circle(210)

    #Draw the lines for the hours
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for i in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)



drawclock(pen)


















wn.mainloop()

from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return  render(request, 'home.html')
