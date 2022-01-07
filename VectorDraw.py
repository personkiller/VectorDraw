from Vector2 import Vector2
from time import sleep
from math import atan2, degrees, dist, sqrt
import turtle


def InitializeCanvas(windowWidth: float, windowHeight: float) -> None:
    wn = turtle.Screen()  # Creates turtle window
    # Sets height and width of window
    wn.setup(width=windowWidth, height=windowHeight)
    wn.title("VectorDraw 1.0.0")
    turtle.color("black", "black")  # Sets fill and outline to black
    turtle.hideturtle()
    turtle.begin_fill()
    turtle.speed("fastest")


def EndDrawing(delay: float = 0) -> None:
    sleep(delay)
    turtle.done()


def DrawLine(initialPosition: Vector2, endPosition: Vector2) -> None:
    # Raw distance between the start and endpoint
    # Could also be thought of as lengths of a triangle
    distanceToTravel = Vector2(
        endPosition.x - initialPosition.x, endPosition.y - initialPosition.y
    )

    # Gets angle in radians between the start and end
    angleOfLineRad: float = atan2(
        endPosition.x - initialPosition.x, endPosition.y - initialPosition.y
    )
    # Converts angle of line to degrees
    angleOfLineDeg: float = degrees(angleOfLineRad)

    t = turtle.Turtle()  # initializes new turtle

    t.penup()
    t.goto(initialPosition.x, initialPosition.y)
    t.pendown()

    t.left(
        angleOfLineDeg
    )  # rotate turtle so that it that it matches the angle of the line
    t.forward(
        sqrt(distanceToTravel.x ** 2 + distanceToTravel.y ** 2)
    )  # length of line using a ** 2 + b ** 2 = c ** 2
