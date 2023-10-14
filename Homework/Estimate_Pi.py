# Estimating the value of Pi using Monte Carlo

import random
import matplotlib.pyplot as plt
import numpy as np

def MonteCarlo_Pi(interval):
    circle_points = 0
    
    center_point_x = 0
    center_point_y = 0
    
    pi = 0
    
    inside_x = []
    inside_y = []
    outside_x = []
    outside_y = []
    
    for i in range(interval):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        position = (x - center_point_x)**2 + (y - center_point_y)**2
        
        if position <= 1:
            circle_points += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)
        
    pi = 4 * (circle_points / interval)
    
    return pi, inside_x, inside_y, outside_x, outside_y

def Draw_2D_Plot(inside_x, inside_y, outside_x, outside_y):
    square_x = [1, -1, -1, 1, 1]
    square_y = [1, 1, -1, -1, 1]
    
    circle_x = []
    circle_y = []
    
    for i in range(361):
        circle_x.append(np.cos(np.pi * i / 180))
        circle_y.append(np.sin(np.pi * i / 180))
    
    plt.plot(square_x, square_y, color = 'black')
    plt.plot(circle_x, circle_y, color = 'blue')
    plt.scatter(inside_x, inside_y, color = 'green', marker = '.')
    plt.scatter(outside_x, outside_y, color = 'red', marker = '.')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    return

pi, inside_x, inside_y, outside_x, outside_y = MonteCarlo_Pi(500)
Draw_2D_Plot(inside_x, inside_y, outside_x, outside_y)

print('Estimation of Pi =', pi)