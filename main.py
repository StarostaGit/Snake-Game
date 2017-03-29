from classSnake import *
from graphics import *
import random

width = 600
height = 600
gridWidth = 10

rows = height // gridWidth
cols = width // gridWidth

window = GraphWin("Snake Game", width, height, autoflush=False)

textX = 20
textY = 15
text = Text(Point(textX, textY), "")
text.setTextColor("white")
text.setSize(10)
text.setStyle("bold")
text.draw(window)

gameoverMessage = Text(Point(width/2, height/2), "GAME OVER")
gameoverMessage.setSize(30)
gameoverMessage.setTextColor("white")
gameoverMessage.setStyle("bold")

def displayScore (snakeObject, textObject):
    textObject.setText(str(snakeObject.getScore()))


def detectCollision (snakeObject):
    # check edges
    if snakeObject.getX() > width:
        return True;
    if snakeObject.getX() < 0:
        return True;
    if snakeObject.getY() > height:
        return True;
    if snakeObject.getY() < 0:
        return True;
    if snakeObject.hasCrashed():
        return True;

    return False;

def generateFruit (fruitObject):
    fruitObject.undraw()
    fruitX = random.randint(0, cols - 1)
    fruitY = random.randint(0, rows - 1)
    fruitObject = Circle(Point(fruitX * gridWidth + gridWidth / 2, fruitY * gridWidth + gridWidth / 2), gridWidth / 2)
    fruitObject.setFill("red")
    fruitObject.draw(window)
    return fruitObject;


def main ():

    window.setBackground("black")

    snake = Snake(cols//2 * gridWidth + gridWidth/2, rows//2 * gridWidth + gridWidth/2, gridWidth, window)

    fruit = Circle(Point(0, 0), 0)

    displayScore(snake, text)

    fruit = generateFruit(fruit)

    while not window.isClosed():
        keyPressed = window.checkKey()
        if keyPressed:
            snake.setDirection(keyPressed)

        if snake.update(fruit):
            fruit = generateFruit(fruit)

        if detectCollision(snake):
            gameoverMessage.draw(window)
            window.getKey()
            gameoverMessage.undraw()
            snake.clear()
            snake = Snake(cols//2 * gridWidth + gridWidth/2, rows//2 * gridWidth + gridWidth/2, gridWidth, window)
            fruit = generateFruit(fruit)

        displayScore(snake, text)
        update(10)


if __name__ == "__main__":
    main()