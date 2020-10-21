"""
Contains a demonstration of a swinging pendulum using VPython.

Functions:
    main: Pendulum demo built for use with VPython.
"""


import math
from vpython import canvas, vector, label, graph, gcurve, color, rate
from pendulum import Pendulum


def main(theta=45, omega=0, dt=0.001, rod_length=5, dampening_coeff=0.3, acceleration_from_gravity=9.8, trail=False,
         animation_rate=2000, time_limit=None, repeat=True, limits=(0.01, 0.001), labels=True, display_width=1900,
         display_height=950, plot=False):
    """ Pendulum demo built for use with VPython.

    :param theta: Starting angle of pendulum from rest in degrees (default is 45).
    :param omega: Starting angular velocity of the pendulum in degrees/second (default is 0).
    :param dt: Change in time in seconds; must be very small (default is 0.001).
    :param rod_length: Length of rod in meters; end of rod to center of bob (default is 5).
    :param dampening_coeff: The damping coefficient; a number between 0 and 1 (default is 0.3).
    :param acceleration_from_gravity: The acceleration due to gravity on the pendulum in meters/second**2
    (default is 9.8).
    :param trail: Shows the path of the moving bob (default is False).
    :param animation_rate: The maximum amount of loop executions per second (default is 2000).
    :param time_limit: A number that represents an ending time for the pendulum animation
    (t goes from 0 to time_limit with dt step sizes); if left as None the demo will run until it reaches its
    limit values (unless repeat is True) (default is None).
    :param repeat: If repeat is True and time_limit is None, repeats the demo after the pendulum has reached
    its limit values (default is True).
    :param limits: A tuple that when time_limit is None, will use +- the given theta (degrees) and
    omega (degrees/time) values to determine when to either reset the pendulum or stop (default is (0.01, 0.001)).
    :param labels: True if you want to display a box of the input values (default is True).
    :param display_width: The VPython canvas pixel width.
    :param display_height: The VPython canvas pixel height.
    :param plot: If True, will display a graph of the bob's angle vs. time; can cause performance issues
    (default is False).
    """

    _make_scene(plot, display_width, display_height)
    pen = Pendulum(theta=theta, omega=omega, dt=dt, rod_length=rod_length, dampening_coeff=dampening_coeff,
                   acceleration_from_gravity=acceleration_from_gravity, trail=trail)
    shelf = pen.shelf()
    rod = pen.rod(pen.position)
    bob = pen.bob(pen.position)

    if labels:
        _make_labels(theta, omega, dampening_coeff, acceleration_from_gravity, rod_length)

    t = 0
    if plot:
        f = _make_plot(pen.theta, display_width, display_height)

    if time_limit is None:
        while True:
            rate(animation_rate)
            angle = pen.angular_position()
            vel = pen.angular_velocity()

            if -limits[0] < angle < limits[0] and -limits[1] < vel < limits[1]:
                if repeat:
                    pen.theta = math.radians(theta)
                    pen.omega = math.radians(omega)
                    bob.clear_trail()

                    if plot:
                        f.delete()
                        t = 0
                else:
                    break

            rod.axis = pen.position
            bob.pos = pen.position

            if plot:
                f.plot(t, math.degrees(pen.theta))
                t += dt

    else:
        while t <= time_limit:
            while t < time_limit:
                rate(animation_rate)
                angle = pen.angular_position()
                vel = pen.angular_velocity()
                rod.axis = pen.position
                bob.pos = pen.position

                if plot:
                    f.plot(t, math.degrees(pen.theta))
                t += dt

            if repeat and t >= time_limit:
                pen.theta = math.radians(theta)
                pen.omega = math.radians(omega)
                bob.clear_trail()

                if plot:
                    f.delete()
                t = 0


def _make_scene(plot, display_width, display_height):
    """ Makes the VPython canvas. """

    if plot:
        canvas(width=display_width/2-10, height=display_height, align='left')
    else:
        canvas(width=display_width, height=display_height)


def _make_labels(theta, omega, dampening_coeff, acceleration_from_gravity, rod_length):
    """ Makes the VPython labels. """

    equation_label = 'Angular Acceleration (\u03b1): \n\u03b1 = - D\u03c9 - (g/L)sin(\u03b8)'
    theta_label = f'Starting Theta (\u03b8) = {theta} \u00b0'
    omega_label = f'Starting Omega (\u03c9) = {omega} \u00b0/s'
    dampening_label = f'Damping Coeff (D) = {dampening_coeff}'
    gravity_label = f'Gravity (g) = {acceleration_from_gravity} m/s\u00b2'
    rod_label = f'Rod Length (L) = {rod_length} m'
    combined_label = '\n'.join((equation_label, '', theta_label, omega_label, dampening_label, gravity_label,
                                rod_label))
    label(pos=vector(0, rod_length/2, 0), text=combined_label)


def _make_plot(theta, display_width, display_height):
    """ Makes the VPython graph.

    :return: The graph object.
    """

    graph(width=display_width/2 - 10, height=display_height, background=color.white, align='right', xtitle='Time (s)',
          ytitle='Angle (\u00b0)')
    f = gcurve(color=color.red, dot=True, interval=100)
    f.plot(0, math.degrees(theta))
    return f


if __name__ == '__main__':
    main(theta=45, omega=0, dampening_coeff=0.3, repeat=True, plot=True)
