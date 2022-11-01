# What are the digits of $\pi$?

## Tasks

1. [ ] TODO 1: In `drawing.py`, modify the `draw_point` function so that it moves the turtle to the appropriate place before drawing the dot. **(3 points)** Test your code by running the file `drawing.py`. You should see 3 black dots and some pink text that says, "Hello, World!"
2. [ ] TODO 2: In `drawing.py`, modify the `write` function to change the color, font, or size of the text on the screen. **(3 points)** Test your code by running the file `drawing.py`.
3. [ ] TODO 3: In `simulation.py`, modify the `get_random_point` function so that the `x` and `y` values of the point are random.
4. [ ] TODO 4: In `simulation.py`, modify the `main.py` function to draw 10 random points instead of just 1.

[ ] In `drawing.py` modify the `draw_point` function so that it takes an additional parameter `in_circle`. Change the color of the dot so that if `in_circle` is `True`, the dot is one color, but if `in_circle` is `False`, it's another color. **(3 points)** Modify the doc string for the `draw_point` function to explain the new parameter. **(1 point)** In the `main` function in `drawing.py`, there are 3 calls to the function `draw_point`. Update the function calls to include either `True` or `False` as the argument. Test your code by running the file `drawing.py`. **(2 points)**