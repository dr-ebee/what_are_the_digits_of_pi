import simulation
import geometry
import drawing

def main():
    drawing.setup()
    num_points_in_circle = 0
    num_points_in_simulation = 10
    radius = 100
    for i in range(num_points_in_simulation):
        # randomly sample a point
        x, y = simulation.get_random_point(radius)
        # check if the point is in the circle
        # YOUR CODE HERE

        # update the number of points that are in the circle
        # YOUR CODE HERE

        # update the number of points in the simulation
        # YOUR CODE HERE

        # draw the point
        # YOUR CODE HERE

    pi_estimate = geometry.calculate_pi(
        num_points_in_circle,
        num_points_in_simulation,
        radius
    )
    drawing.draw_pi(pi_estimate)
    drawing.finish()

if __name__ == "__main__":
    main()