import geometry
from graphics import *

# The snake class

class Snake:

    def __init__ (self, x, y, snakeWidth, window):
        self.pos = Point(x, y)
        self.vel = Point(0, 0)
        self.window = window
        self.dir = None
        self.snakeWidth = snakeWidth
        self.score = 0
        self.tail = []
        self.hasEaten = 0

        leftCorner = Point(x - snakeWidth/2, y - snakeWidth/2)
        rightCorner = Point(x + snakeWidth/2, y + snakeWidth/2)
        head = Rectangle(leftCorner, rightCorner)
        head.setFill("white")
        head.draw(self.window)
        self.tail.append(head)


    def update (self, fruit):
        prev = self.tail[0].getCenter()
        self.pos = geometry.add(self.pos, self.vel)
        self.tail[0].move(self.vel.getX(), self.vel.getY())

        for i in range(1, len(self.tail) - self.hasEaten):
            temp = self.tail[i].getCenter()
            vector = geometry.sub(prev, temp)
            self.tail[i].move(vector.getX(), vector.getY())
            prev = temp

        self.hasEaten = 0

        if geometry.dist(self.pos, fruit.getCenter()) < self.snakeWidth:
            self.score += 100
            self.hasEaten = 1
            newSegment = self.tail[len(self.tail) - 1].clone()
            # newSegment.setFill(color_rgb(175, 175, 175))
            newSegment.setFill("white")
            self.tail.append(newSegment)
            self.tail[len(self.tail) - 1].draw(self.window)
            return True;

        return False;


    def setDirection (self, keyPressed):
        if self.isOpposite(keyPressed):
            return;
        self.dir = keyPressed
        if self.dir == "Right":
            self.vel = Point(self.snakeWidth, 0)
        elif self.dir == "Left":
            self.vel = Point(-self.snakeWidth, 0)
        elif self.dir == "Up":
            self.vel = Point(0, -self.snakeWidth)
        elif self.dir == "Down":
            self.vel = Point(0, self.snakeWidth)


    def clear (self):
        for i in self.tail:
            i.undraw()




    def getScore (self):
        return self.score;

    def getX (self):
        return self.pos.getX()

    def getY (self):
        return self.pos.getY()


    def isOpposite (self, keyPressed):
        if len(self.tail) == 1:
            return False;
        if keyPressed == "Right" and self.dir == "Left":
            return True;
        if keyPressed == "Left" and self.dir == "Right":
            return True;
        if keyPressed == "Down" and self.dir == "Up":
            return True;
        if keyPressed == "Up" and self.dir == "Down":
            return True;
        return False;


    def hasCrashed (self):

        for i in range(1, len(self.tail) - self.hasEaten):
            if geometry.dist(self.pos, self.tail[i].getCenter()) < self.snakeWidth:
                return True;

        return False;