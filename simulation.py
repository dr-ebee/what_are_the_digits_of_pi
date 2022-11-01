import random
import drawing

def get_random_point(max_distance_from_origin):
    """
    Sample a random (x,y) point

    Parameters:
    * `max_distance_from_origin` (int): maximum distance between the randomly
      simulated point and the origin (0, 0)
    
    Returns:
    * `x` (float): random number less than max distance away from origin
    * `y` (float): random number less than max distance away from origin
    """
    min_x = -max_distance_from_origin
    max_x = max_distance_from_origin
    min_y = -max_distance_from_origin
    max_y = max_distance_from_origin
    # TODO 3 ------> define variables x and y using `random.uniform` function
    # `x` should be between `min_x` and `max_x`. `y` should be between `min_y`
    # and `max_y`
    x = 0 # CHANGE THIS!
    y = 0 # CHANGE THIS!
    return x, y

def main():
    drawing.setup()
    # TODO 4 ------> Use a `for` loop and the `get_random_point` function to
    # sample and draw 10 random points instead of just 1.
    x, y = get_random_point(100)
    drawing.draw_point(x, y)
    drawing.finish()

if __name__ == "__main__":
    main()