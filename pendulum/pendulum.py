"""
Contains the Pendulum class.

Classes:
    Pendulum: A pendulum object made using VPython.
"""


import math
from vpython import vector, color, box, sphere, cylinder


class Pendulum:
    """ A pendulum object made using VPython.

    Instance Attributes:
        theta: Starting angle of pendulum from rest in degrees (default is 45).
        omega: Starting angular velocity of the pendulum in degrees/second (default is 0).
        dt: Change in time in seconds; must be very small (default is 0.001).
        rod_length: Length of rod in meters; end of rod to center of bob (default is 3).
        dampening_coeff: The damping coefficient (default is 0.0).
        acceleration_from_gravity: The acceleration due to gravity on the pendulum in meters/second**2 (default is 9.8).
        trail: Shows the path of the moving bob (default is False).

    Properties:
        angular_acceleration: The angular acceleration of the pendulum bob.
        position: The cartesian coordinates of the pendulum bob.
    """

    def __init__(self, theta=45, omega=0, dt=0.001, rod_length=3, dampening_coeff=0.5, acceleration_from_gravity=9.8,
                 trail=False):
        """
        :param theta: Starting angle of pendulum from rest in degrees (default is 45).
        :param omega: Starting angular velocity of the pendulum in degrees/second (default is 0).
        :param dt: Change in time in seconds; must be very small (default is 0.001).
        :param rod_length: Length of rod in meters; end of rod to center of bob (default is 3).
        :param dampening_coeff: The damping coefficient; must be greater than 0 (default is 0.5).
        :param acceleration_from_gravity: The acceleration due to gravity that the pendulum feels in meters/second**2
        (default is 9.8).
        :param trail: Shows the path of the moving bob (default is False).
        """
        
        self.theta = math.radians(theta)
        self.omega = math.radians(omega)
        self.dt = dt
        self._rod_length = rod_length
        self._dampening_coeff = dampening_coeff
        self.acceleration_from_gravity = acceleration_from_gravity
        self.trail = trail

    @property
    def rod_length(self):
        if self._rod_length > 0:
            return self._rod_length
        else:
            raise ValueError('rod_length must be greater than 0')

    @rod_length.setter
    def rod_length(self, value):
        self._rod_length = value

    @property
    def dampening_coeff(self):
        if self._dampening_coeff >= 0:
            return self._dampening_coeff
        else:
            raise ValueError('dampening_coeff must be greater than 0')

    @dampening_coeff.setter
    def dampening_coeff(self, value):
        self._dampening_coeff = value

    @property
    def angular_acceleration(self):
        """ Calculates angular acceleration. """

        return -(self.acceleration_from_gravity/self.rod_length)*math.sin(self.theta) - self.dampening_coeff*self.omega

    def angular_velocity(self):
        """ Calculates the updated angular velocity after some small time dt. """

        self.omega += self.angular_acceleration*self.dt
        return self.omega

    def angular_position(self):
        """ Calculates the updated angular position after some small time dt. """

        self.theta += self.omega*self.dt
        return self.theta

    @property
    def position(self):
        """ Finds the center position of the bob in cartesian coordinates. """

        return vector(self.rod_length*math.sin(self.theta), -self.rod_length*math.cos(self.theta), 0)

    @staticmethod
    def shelf():
        """ Creates a shelf for the pendulum to hang from. """

        return box(pos=vector(0, 0.1/2, 0), size=vector(2, 0.1, 2), color=color.white)

    @staticmethod
    def rod(axis):
        """ Creates the pendulum rod. """

        return cylinder(pos=vector(0, 0, 0), axis=axis, radius=0.02, color=color.red)

    def bob(self, position):
        """ Creates the pendulum bob. """

        if self.trail:
            return sphere(pos=position, radius=0.3, color=color.red, make_trail=True, trail_color=color.white,
                          retain=20)
        else:
            return sphere(pos=position, radius=0.3, color=color.red)
