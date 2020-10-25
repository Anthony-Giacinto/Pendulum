# pendulum
This project allows the user to animate a swinging pendulum using VPython.

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [How to Use](#how-to-use)

## General Info
The motion of the pendulum is calculated by using this differential equation:  
alpha = -(g/L) x sin(theta) - dampeningCoeff x omega ,  

where alpha is angular acceleration, omega is angular velocity, and theta is the angular position.  

This program takes starting values of theta and omega (along with other constant values like g, L and dampeningCoeff) and with them, determines alpha, which in turn calculates the next theta and omega after a given amount of time, dt.  

next_theta = previous_theta + previous_omega x dt  
next_omega = previous_omega + previous_alpha x dt  

The program then repeats this process to track the path of the pendulum  object created using vypthon. Different types of limits can be imposed onto the pendulum to determine when to stop calculating these values or when to reset the process to the original given values.  

There is also an option to plot the angle of the pendulum vs. time alongside the pendulum as it moves (this can cause the program to chug, however).

## Technologies
Project is created with:
* Python 3.6

## Features
* Can add a dampening coefficient to the pendulum.
* Can change the acceleration due to gravity on the pendulum.
* Can generate a real-time graph of angle vs. time.

## How to Use
All you need to do is 'from pendulum import pendulum pendulum.main()'.  
Here are the arguments for main:  
* theta: (float) Starting angle of pendulum from rest in degrees (default is 45.0).
* omega: (float) Starting angular velocity of the pendulum in degrees/second (default is 0).
* dt: (float) Change in time in seconds; must be very small (default is 0.001).
* rod_length: (float) Length of rod in meters; end of rod to center of bob (default is 5.0).
* dampening_coeff: (float) The damping coefficient; a number between 0 and 1 (default is 0.3).
* acceleration_from_gravity: (float) The acceleration due to gravity on the pendulum in meters/second^2 (default is 9.8).
* trail: (bool) Shows the path of the moving bob (default is False).
* animation_rate: (int) The maximum amount of loop executions per second (default is 2000).
* time_limit: (float) A number that represents an ending time for the pendulum animation (t goes from 0 to time_limit with dt step sizes); if left as None the demo will run until it reaches its limit values (unless repeat is True) (default is None).
* repeat: (bool) If repeat is True and time_limit is None, repeats the demo after the pendulum has reached its limit values (default is True).
* limits: (list) A tuple that when time_limit is None, will use +- the given theta (degrees) and omega (degrees/time) values to determine when to either reset the pendulum or stop (default is (0.01, 0.001)).
* labels: (bool) True if you want to display a box of the input values (default is True).
* display_width: (int) The VPython canvas pixel width.
* display_height: (int) The VPython canvas pixel height.
* plot: (bool) If True, will display a graph of the bob's angle vs. time; can cause performance issues (default is False).
