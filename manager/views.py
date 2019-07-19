# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import time
import math
# import turtle
# wn = turtle.Screen()
# wn.bgcolor("black")
# wn.setup(width=600,height=600)
# wn.title("Clock")
# wn.tracer(0)
#
# pen = turtle.Turtle()
# pen.hideturtle()
# pen.speed(0)
# pen.pensize(3)
#
# def drawclock(h,m,s,pen):
#     #Draw clock face
#     pen.up()
#     pen.goto(0,210)
#     pen.setheading(180)
#     pen.color("blue")
#     pen.pendown()
#     pen.circle(210)
#
#     #Draw the lines for the hours
#     pen.penup()
#     pen.goto(0,0)
#     pen.setheading(90)
#
#     for i in range(12):
#         pen.fd(190)
#         pen.pendown()
#         pen.fd(20)
#         pen.penup()
#         pen.goto(0,0)
#         pen.rt(30)
#
#     #Draw the hands
#     #Draw the hour hands
#     pen.penup()
#     pen.goto(0,0)
#     pen.color("white")
#     pen.setheading(90)
#     angle = (h/12) * 360
#     pen.rt(angle)
#     pen.pendown()
#     pen.fd(100)
#
#     #Draw the minute hands
#     pen.penup()
#     pen.goto(0,0)
#     pen.color("white")
#     pen.setheading(90)
#     angle = (m/60) * 360
#     pen.rt(angle)
#     pen.pendown()
#     pen.fd(180)
#
#     #Draw the second hands
#     pen.penup()
#     pen.goto(0,0)
#     pen.color("white")
#     pen.setheading(90)
#     angle = (s/60) * 360
#     pen.rt(angle)
#     pen.pendown()
#     pen.fd(60)
#
# while True:
#     h = int(time.strftime("%I"))
#     m = int(time.strftime("%M"))
#     s = int(time.strftime("%I"))
#
#     drawclock(h,m,s,pen)
#     wn.update()
#
#     time.sleep(1)
#
#     pen.clear()
#
# wn.mainloop()

from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return  render(request, 'home.html')

def startserver(request):
    return render(request,'home.html')    
