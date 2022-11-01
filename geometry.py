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

def main():
    print(f"{is_in_circle(1, 1, 1)} <---- This should be False")
    print(f"{is_in_circle(0, 1, 1)} <---- This should be True")
    print(f"{is_in_circle(0, 1, 0.5)} <---- This should be False")

if __name__ == "__main__":
    main()