"""
File : windmill.py
Description : Demonstration of basic python programming concepts (functions,
arguments, tupple) using turtle graphics.
Author : Archit Joshi
Language : Python 3.11
Version: 1.2

Revisions :
1.0 - Basic outline
1.1 - Added sleep() for uniform transitions
1.2 - Refactoring for code reuse

"""

import time
import turtle as t
from math import sqrt


def init() -> None:
    """
    Create Turtle window, set dimensions & other information.

    :return: None
    """

    # Initialise the window size
    t.setup(400, 400)
    # Initialise the world coordinates
    t.setworldcoordinates(-200, -200, 200, 200)
    # Pen-up
    t.up()
    # Turtle at max speed
    t.speed(6)
    # Hide the turtle
    t.hideturtle()
    # Window name
    t.title("WINDMILL")


def draw() -> None:
    """
    Driver function for drawing all elements.

    :return: None
    """

    # Blade colors
    color1 = "Green"
    color2 = "Red"

    # Loop to simulate rotation of blades
    for i in range(0, 20):
        try:
            draw_pattern(color1, color2)        # Draw pattern
            time.sleep(0.5)                     # Pause/sleep for 0.5 seconds
            color1, color2 = color2, color1     # Swap color values (tuples)
            draw_pattern(color1, color2)        # Draw pattern
            time.sleep(0.5)                     # Pause/sleep for 0.5 seconds
        except KeyboardInterrupt:
            print("Goodbye!!")

    # Helper to print exit message
    endthis()


def draw_stick() -> None:
    """
    Draw stick of the paper windmill and return to start position.

    :pre: Turtle at (0,0), tail up, facing east
    :post: Turtle at (0,0), tail up, facing east

    :return: None
    """

    t.down()
    t.right(90)
    t.color("black")
    t.forward(100)
    t.left(180)
    t.forward(100)
    t.right(90)
    t.up()


def draw_pattern(color1, color2) -> None:
    """
    Function to draw the windmill pattern.

    :pre: Turtle at (0,0), tail up, facing east
    :post: Turtle at (0,0), tail up, facing east

    :param color1: color 1 value as string
    :param color2: color 2 value as string
    :return: None
    """
    try:
        # Implementing tracer, so we don't have to wait for turtle to complete
        t.tracer(0, 0)
        draw_stick()
        draw_blade1(color1)     # Draw first 4 blades
        t.right(45)             # Tilt by 45
        draw_blade1(color2)     # Draw adjacent 4 blades
        t.left(45)              # Return to (0,0)
        # Update the screen after the drawing is completed
        t.update()
    except KeyboardInterrupt:
        print("Goodbye !!")


def draw_triangle(color) -> None:
    """
    Helper function to draw the individual triangles of the windmill.

    :pre: Turtle at (0,0), tail up, facing relative east
    :post: Turtle at (0,0), tail up, facing relative east

    :param color: color value for the blade as string
    :return: None
    """

    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.forward(50)
    t.left(135)
    side = 50 / sqrt(2)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.end_fill()
    t.left(135)


def draw_blade1(color) -> None:
    """
    Helper to draw the blades of the windmill.

    :pre: Turtle at (0,0), tail up, facing east
    :post: Turtle at (0,0), tail up, facing east

    :param color: color value for the blade as string
    :return: None
    """

    # Loop to draw 4 blades of the windmill.
    for i in range(4):
        draw_triangle(color)
        t.left(90)


def endthis() -> None:
    """
    Clear screen and print goodbye message.

    :return: None
    """

    t.clear()
    t.setpos(-100, 0)
    t.write("The windmill is closed now ! Goodbye !")


def main() -> None:
    # Initialise the window
    init()
    # Draw the graphic
    draw()
    # Keep window alive
    t.done()


if __name__ == "__main__":
    main()
