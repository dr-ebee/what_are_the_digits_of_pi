# What are the digits of $\pi$?

## Tasks (34 points total)

1. [ ] TODO 1: In `drawing.py`, modify the `draw_point` function so that it moves the turtle to the appropriate place before drawing the dot. **(3 points)** Test your code by running the file `drawing.py`. You should see 3 black dots and some pink text that says, "Hello, World!"
2. [ ] TODO 2: In `drawing.py`, modify the `write` function to change the color, font, or size of the text on the screen. **(3 points)** Test your code by running the file `drawing.py`.
3. [ ] TODO 3: In `simulation.py`, modify the `get_random_point` function so that the `x` and `y` values of the point are random. **(5 points)** Test your code by running the `simulation.py` file. You should see a randomly positioned point.
4. [ ] TODO 4: In `simulation.py`, modify the `main.py` function to draw 10 random points instead of just 1. **(5 points)** Test your code by running the `simulation.py` file. You should see 10 randomly positioned points.
5. [ ] TODO 5: In `geometry.py`, fix the bug. **(2 points)** Test by running the file `geometry.py`.
6. [ ] TODO 6: In `geometry.py`, modify the `calculate_pi` function so that once we finish the simulation and we know how many points were inside the circle, then we can estimate the value of pi. **(10 points)**
7. [ ] In `drawing.py` modify the `draw_point` function so that it takes an additional parameter `in_circle`. Change the color of the dot so that if `in_circle` is `True`, the dot is one color, but if `in_circle` is `False`, it's another color. **(3 points)** Modify the doc string for the `draw_point` function to explain the new parameter. **(1 point)** In the `main` function in `drawing.py`, there are 3 calls to the function `draw_point`. Update the function calls to include either `True` or `False` as the argument. Test your code by running the file `drawing.py`. **(2 points)**
8. [ ] In `main.py` modify the `main` function so that it uses all of the functions you made to estimate `pi` and draw the points in the simulation. **(8 points)** Test your code by running the file `main.py`.

## Extra credit

* [ ] Modify the code in this project so that we recalculate our estimate of $pi$ every 100 iterations. Run a total of at least 2000 iterations, which will print out at least 20 consecutive estimates of $pi$. Is your estimate getting closer to 3.14159? **(5 points)**
* [ ] Instead of printing out the *estimate* every 100 iterations, print out the *difference* between the correct value of $pi$ (you can use `math.pi` for this) and your estimate. Is the error getting smaller as you sample more points? **(2 points)**
* [ ] Look up `matplotlib` and try to make a graph where the x-axis is the number of iterations and the y-axis is the error. **(5 points)** I'm not sure how `matplotlib` and `turtle` interact, so feel free to disable the `turtle` drawing. One extra point if you use a variable and/or user `input` to determine whether the program should draw the points using turtle.