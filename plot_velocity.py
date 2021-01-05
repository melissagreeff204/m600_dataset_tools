""" Simple plot of velocities along the path
"""
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits import mplot3d

def plot_velocity(timestamp, x_vel, y_vel, z_vel, results_folder):

    plt.figure()
  
    plt.plot(timestamp, x_vel,label='x velocity',color='b')
    plt.plot(timestamp, y_vel,label='y velocity',color='g')
    plt.plot(timestamp, z_vel,label='z velocity',color='r')

    plt.xlabel('timestamp (ns)', fontsize=16)
    plt.ylabel('velocity (m/s)', fontsize=16)
    plt.title('Velocity', fontsize=16, weight='bold')

    plt.legend()
    
    plt.savefig("{}/est_velocity.png".format(results_folder), format='png', bbox_inches='tight')
    plt.close()

if __name__=="__main__":

    data_folder = "/Users/melissagreeff/Documents/montreal_trial1/teach/"
    results_folder = "/Users/melissagreeff/Documents/montreal_trial1/teach/"

    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    vel_data = np.genfromtxt(data_folder + 'velocities.csv', delimiter=',')

    timestamp = vel_data[1:,0]
    x_vel = vel_data[1:,1]
    y_vel = vel_data[1:,2]
    z_vel = vel_data[1:,3]

    # Plot the 2d visual of path
    plot_velocity(timestamp, x_vel, y_vel, z_vel, results_folder)

