"""
Monte Carlo dart-throwing simulation
"""

import math as m
import numpy as np
import matplotlib.pyplot as plt

def draw_board(r=1, pts=100):
    plt.plot([-r, r, r, -r, -r], [-r, -r, r, r, -r], 'k-')
    theta = np.linspace(0, 2*m.pi, pts)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    plt.plot(x, y, 'r-')
    plt.axis('equal')
    
def throw_darts(r=1):
    xpos = np.random.uniform(-r, r)
    ypos = np.random.uniform(-r, r)
    return (xpos, ypos)
    
def plot_darts(x, y, color='b'):
    plt.figure(1)
    plt.plot(x, y, '.', mfc=color, mec=color)
    plt.draw()
    plt.pause(0.01)

def plot_est(nums, ests):
    plt.figure(2)
    plt.plot(nums, ests, 'ko')
    plt.plot(nums, m.pi*np.ones(len(nums)), 'g.')
    plt.draw()
    plt.pause(0.01)
    
if __name__ == '__main__':
    darts_to_throw = 10000
    darts_thrown = 0
    board_rad = 1
    do_plot = 0
    inside = 0
    pi_est = []
    x_i_vec = []
    y_i_vec = []
    x_o_vec = []
    y_o_vec = []

    plt.figure(1)
    plt.clf()
    draw_board(r=board_rad)

    plt.figure(2)
    plt.clf()

    while darts_thrown < darts_to_throw:
        darts_thrown += 1
        x_d, y_d = throw_darts(board_rad)
        r_d = m.sqrt(x_d**2 + y_d**2)
        color='m'
        if r_d < board_rad:
            inside += 1
            x_i_vec += [x_d]
            y_i_vec += [y_d]
            color='g'
        else:
            x_o_vec += [x_d]
            y_o_vec += [y_d]

        pi_est += [4*inside/darts_thrown]
        print('{:5d}'.format(darts_thrown) + 
               ' {:5d}'.format(inside) +
               ' {:0.3e}'.format(pi_est[-1]))
        
        if do_plot:
            plot_darts(x_d, y_d, color)
            plot_est(darts_thrown, pi_est[-1])

    if not do_plot:
        plot_darts(x_i_vec, y_i_vec, 'g')
        plot_darts(x_o_vec, y_o_vec, 'm')
        plot_est(np.linspace(1, darts_thrown, darts_thrown), pi_est)

    plt.figure(1)
    draw_board(board_rad)
