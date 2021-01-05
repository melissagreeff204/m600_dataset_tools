""" Get closest GPS to images obtained
"""
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits import mplot3d

def search_closest_gps(im_data, gps_data, results_folder):

    im_stamps = im_data[1:,0]
    gps_stamps = gps_data[1:,0]

    im_gps_data = np.zeros((len(im_stamps),3))

    # Search closest gps stamp
    for i in range(0,len(im_stamps)):
        im_stamp = im_stamps[i]
        idx = np.argmin(np.abs(gps_stamps - im_stamp))
        im_gps_data[i,0] = im_data[i+1,1]
        im_gps_data[i,1] = gps_data[idx+1, 1]
        im_gps_data[i,2] = gps_data[idx+1, 2]

        np.savetxt(results_folder + 'im_gps.csv', im_gps_data, delimiter=',')

if __name__=="__main__":

    data_folder = "/Users/melissagreeff/Documents/montreal_trial1/teach/"
    results_folder = "/Users/melissagreeff/Documents/montreal_trial1/teach/"

    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    im_data = np.genfromtxt(data_folder + 'image_ids.csv', delimiter=',')
    gps_data = np.genfromtxt(data_folder + 'gps.csv', delimiter=',')

    search_closest_gps(im_data, gps_data, results_folder)


    



