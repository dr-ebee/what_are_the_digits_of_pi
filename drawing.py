import turtle

def draw_point(x, y):
    """
    Draw a point at position x, y
    
    Parameters:
    * `x` (float): x-axis position
    * `y` (float): y-axis position
    """
    # Stop drawing lines where the turtle goes
    turtle.up()

    # Go to the position
    # TODO 1 ------> YOUR CODE HERE!!!
    turtle.goto(x,y)

    # Stamp a dot at the turtle's current location
    turtle.dot()

def write(text):
    """
    Draw text in large letters in the middle of the screen
    
    Parameters:
    * `text` (str): String to print on canvas
    """
    turtle.goto(0,0)
    turtle.down()

    # TODO 2 ------> Change color, font, or size of text

    turtle.color("magenta")
    turtle.write(
        text,
        font=("Courier", 64, "normal"),
        align = "center"
    )
    turtle.up()

def setup():
    """
    Setup turtle so that we only render at the end, rather than watching the
    animation.
    """
    turtle.tracer(0,0)

def finish():
    """
    End the turtle commands so that we render the image at the end and keep the
    screen open until the user clicks on it.
    """
    turtle.hideturtle()
    turtle.update()
    turtle.exitonclick()

if __name__ == "__main__":
    setup()

    # Draw a point at the origin
    draw_point(0, 0)
    # Draw a point at the upper right corner
    draw_point(100, 100)
    # Draw a point at the lower left corner
    draw_point(-100, -100)

    write("Hello, World!")

    finish()