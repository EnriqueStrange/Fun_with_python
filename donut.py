# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:44:16 2023

@author: Strange
"""

import math
import os
import sys
import time

# Define constants and tables for pre-calculations
A, B = 0, 0
sintable, costable = [], []
for theta in range(0, 628):
    costable.append(math.cos(theta/100)) # pre-calculate cosines for each degree
    sintable.append(math.sin(theta/100)) # pre-calculate sines for each degree

# Clear the console screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Convert x, y coordinates to polar coordinates
def dot(r, a, b):
    x = int(r*a)
    y = int(r*b)
    return x, y

# Draw the donut using ASCII characters
def draw_donut(z):
    screen = [[' ' for _ in range(120)] for _ in range(30)]
    for theta in range(0, 628, 2):
        for phi in range(0, 628, 2):
            cosphi, sinphi = costable[phi], sintable[phi]
            costheta, sintheta = costable[theta], sintable[theta]
            ox, oy = dot(z, cosphi*costheta, cosphi*sintheta)
            x, y = dot(z, cosphi*costheta, cosphi*sintheta)
            xp, yp = x+60, y+15
            # Add a check to ensure that the index being accessed is within the bounds of the list
            if phi - z >= 0 and phi + z < 628 and theta - z >= 0 and theta + z < 628:
                luminance = max(0, int(8.0*(cosphi*costheta*sintable[phi-z]+cosphi*costheta*sintable[phi+z]+cosphi*sintheta*sintable[theta-z]+cosphi*sintheta*sintable[theta+z])))
            else:
                luminance = 0
            if yp >= 0 and yp < 30 and xp >= 0 and xp < 120 and z > 0 and luminance > 0:
                if luminance > 6:
                    screen[yp][xp] = '#'
                elif luminance > 4:
                    screen[yp][xp] = 'x'
                elif luminance > 2:
                    screen[yp][xp] = '.'
                else:
                    screen[yp][xp] = ' '
    for i in range(30):
        print(''.join(screen[i]))


# Continuously update the donut's position and redraw it
while True:
    cls()
    draw_donut(int(10*(1+math.sin(A)))) # update the z-coordinate based on a sine wave
    A += 0.07 # increase the angle of rotation
    B += 0.03 # increase the speed of rotation
    time.sleep(0.1) # pause for a short time to control the animation speed

