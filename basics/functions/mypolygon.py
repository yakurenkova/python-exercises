# -*- coding: utf-8 -*-
"""
This exercise is from the book "Think Python: How to Think Like a Computer 
Scientist" by Allen B. Downey
"""

import turtle
import math

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    """
    Draws n connected line segments with the given length 
    and angle (in degrees) between them. t is a Turtle object
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def square(t, length):
    """
    Draws a square with the given side length. 
    """
    polyline(t, 4, length, 90)


def polygon(t, sides, length):
    """
    Draws a polygon with the given side length and number of sides. 
    """
    polyline(t, sides, length, 360/sides)

def arc(t, r, angle):
    """
    Draws an arc with the given radius r and angle. 
    """    
    circumference = 2*math.pi*r
    n = int(circumference/3)+3 #number of line segments in the arc
    length = circumference/n
    polyline(t, int(n*angle/360), length, 360/n)

def circle(t, r):
    """
    Draws a circle with the given radius r. 
    """    
    arc(t, r, 360)


square(bob, 100)
polygon(bob, 5, -100)
circle(bob, 100)
arc(bob, 50, 180)
turtle.mainloop()
turtle.done()