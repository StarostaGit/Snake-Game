from graphics import *
import math

def add (p1, p2):
    x = p1.getX() + p2.getX()
    y = p1.getY() + p2.getY()
    return Point(x, y);

def sub (p1, p2):
    x = p1.getX() - p2.getX()
    y = p1.getY() - p2.getY()
    return Point(x, y);

def dist (p1, p2):
    x = p1.getX() - p2.getX()
    y = p1.getY() - p2.getY()
    return math.hypot(x, y);