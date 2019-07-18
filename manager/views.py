# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=400,height=400)
wn.title("Clock")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)



















wn.mainloop()

from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return  render(request, 'home.html')
