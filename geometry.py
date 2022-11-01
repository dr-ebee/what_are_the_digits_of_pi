import math

def is_in_circle(x, y, radius):
    """
    Check if a particular (x,y) point is inside of a circle with a particular
    radius.

    Parameters:
    * `x` (float): coordinate on the x-axis
    * `y` (float): coordinate on the y-axis
    * `radius` (float): radius of circle
    """
    # TODO 5 ------> Fix bug!
    return sqrt(x**2 + y**2) <= radius

def calculate_pi(num_points_in_circle, num_points_total, radius):
    """
    Estimate `pi` based on simulation. In the simulation, we randomly sample
    points from a square and ask how many of those points were inside a circle
    inscribed in the square.

    Parameters:
    * `num_points_in_circle` (int): Number of points from the simulation that
      were inside the circle
    * `num_points_total` (int): Total number of points from the simulation.
    * `radius` (float): Radius of the inscribed circle
    """
    # TODO 6 Fill in this function by answering the following questions:

    # What is the total area of the square?
    square_area = 0 # CHANGE THIS

    # Based on this simulation, the circle's area is what fraction of the
    # square's area?
    fraction_circle = 0 # CHANGE THIS

    # What is the area of the circle?
    area_circle = 0 # CHANGE THIS

    # We know that the area of a circle = pi * radius^2.
    # That means that pi = area / radius^2.
    pi = area_circle / radius ** 2

    # Return the estimate for pi
    return pi

def main():
    print("======= Tests for TODO 5 =======")
    print(f"{is_in_circle(1, 1, 1)} <---- This should be False")
    print(f"{is_in_circle(0, 1, 1)} <---- This should be True")
    print(f"{is_in_circle(0, 1, 0.5)} <---- This should be False")

    print("======= Tests for TODO 6 =======")
    print(f"{get_pi(9, 12, 1)} <--- This should be 3")
    print(f"{get_pi(79, 100, 1)} <--- This should be 3.16")

if __name__ == "__main__":
    main()