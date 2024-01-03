#!/bin/env python3
'''
Draw a labyrinth
'''
import matplotlib.pyplot as plt
import numpy as np
import math

def draw_circle(r,**kwargs):
    print("kwargs", kwargs)
    cuts = []
    if 'cuts' in kwargs:
        cuts = kwargs['cuts']
    
    theta_range = [v for v in np.arange(0, 360, .01)]
    for cut in cuts:
        theta_range = [v for v in theta_range if v < cut[0] or v > cut[1]]
                       
    x = [r*np.cos(np.pi*theta/180.) for theta in theta_range]
    y = [r*np.sin(np.pi*theta/180.) for theta in theta_range]
    plt.plot(x,y)        
def draw_labyrinth(n_circ):
    for i in range(1, n_circ):
        cut_ang =  180*math.atan2(1,i)/np.pi;
        if i % 2:
            draw_circle(i, cuts=[(0, 2*cut_ang)])
        else:
            draw_circle(i, cuts=[(0, cut_ang), (360-cut_ang,360)])
    plt.plot([1,n_circ-1],[0,0])
    plt.plot([2,n_circ-1],[1,1])
    
    plt.gca().set_aspect('equal')
    plt.savefig('foo.svg')
if __name__ == '__main__':
    print('hello')
    draw_labyrinth(32)