""" Example of using tools to read GPS data from pose graph. Then plot latitude
    and longitude.
"""
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits import mplot3d

def plot_path_2d(lat, lon, results_folder):

    plt.figure()
  
    plt.plot(lat, lon)  
    plt.ylabel('latitude', fontsize=16)
    plt.xlabel('longitude', fontsize=16)
    plt.title('GPS latitude, longitude', fontsize=16, weight='bold')
    
    plt.savefig("{}/path_gps_2d.png".format(results_folder), format='png', bbox_inches='tight')
    plt.close()

def plot_path_3d(lat, lon, alt, results_folder):

    plt.figure()
    ax = plt.axes(projection="3d")
  
    ax.plot3D(lat, lon, alt)  
    ax.set_ylabel('latitude', fontsize=16)
    ax.set_xlabel('longitude', fontsize=16)
    ax.set_zlabel('altitude', fontsize=16)
    ax.set_title('GPS latitude + longitude and altitude (WGS 84)', fontsize=16, weight='bold')
    
    plt.savefig("{}/path_gps_3d.png".format(results_folder), format='png', bbox_inches='tight')
    plt.close()

if __name__=="__main__":

    data_folder = "/Users/melissagreeff/Documents/montreal_trial1/teach/"
    results_folder =  "/Users/melissagreeff/Documents/montreal_trial1/teach/"

    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    gps_data = np.genfromtxt(data_folder + 'gps.csv', delimiter=',')

    lat = gps_data[1:,1]
    lon = gps_data[1:,2]
    alt = gps_data[1:,3]

    # Plot the 2d visual of path
    plot_path_2d(lat, lon, results_folder)

    # Plot the 3d visual of path
    plot_path_3d(lat, lon, alt, results_folder)

