#!/bin/env python3
'''
Draw a labyrinth
'''
import matplotlib.pyplot as plt
import numpy as np
import math
import solid2


def draw_circle_svg(r,**kwargs):
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
def draw_circle_scad(r,**kwargs):
    print("kwargs", kwargs)
    cuts = []
    if 'cuts' in kwargs:
        cuts = kwargs['cuts']
    retval = solid2.circle(r=r)
    retval -= solid2.circle(r=r-.1)
    
    for cut in cuts:
        re = 2*r
        xa = re*np.cos(np.pi*cut[0]/180.) 
        ya = re*np.sin(np.pi*cut[0]/180.)
        xb = re*np.cos(np.pi*cut[1]/180.) 
        yb = re*np.sin(np.pi*cut[1]/180.)
        retval -= solid2.polygon([(0,0),(xa,ya),(xb,yb)])
    return retval

        
                     
    return rtval

def draw_labyrinth_svg(n_circ):
    solid2.set_global_fn(500);
    for i in range(1, n_circ):
        cut_ang =  180*math.atan2(1,i)/np.pi;
        if i % 2:
            draw_circle_scad(i, cuts=[(0, 2*cut_ang)])
        else:
            draw_circle_scad(i, cuts=[(0, cut_ang), (360-cut_ang,360)])
    plt.plot([1,n_circ-1],[0,0])
    plt.plot([2,n_circ-1],[1,1])
    
    plt.gca().set_aspect('equal')
    plt.savefig('foo.svg')


def draw_labyrinth_scad(n_circ):
    #retval = solid2.down(-.5)(solid2.circle(r=n_circ+1))
    retval = solid2.union()
    for i in range(1, n_circ):
        cut_ang =  180*math.atan2(1,i)/np.pi;
        if i % 2:
            retval += draw_circle_scad(i, cuts=[(0, 2*cut_ang)])
        else:
            retval += draw_circle_scad(i, cuts=[(0, cut_ang), (360-cut_ang,360)])
    retval += solid2.down(.5)(solid2.right(1)(solid2.cube([n_circ-2,.1,1])))
    retval += solid2.down(.5)(solid2.right(1.8)(solid2.forward(1)(solid2.cube([n_circ-3,.1,1]))))
    #plt.plot([2,n_circ-1],[1,1])
    return retval
    #plt.gca().set_aspect('equal')
    #plt.savefig('foo.svg')
if __name__ == '__main__':
    print('hello')
    solid2.minkowski()(draw_labyrinth_scad(7),solid2.sphere(.1)).save_as_scad()