#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from pylab import *
import random as rnd

# declare global arrays and objects
file_obj = open('phase_plot.dat', 'r')
graph_titles = []
clust_coeffs = []
path_lengths = []


# funtion to read (known) data file
def read_datafile(file):
    file.readline()
    for line in file:
        title = str(line.split()[0])
        graph_titles.append(title)
        avg_clust = float(line.split()[1])
        clust_coeffs.append(avg_clust)
        avg_path = float(line.split()[2])
        path_lengths.append(avg_path)

def plot_data():
    fig, ax = plt.subplots()
    colours = []
    for i in range(len(clust_coeffs)):
        colours.append(rnd.randint(0,1000))
    ax.scatter(clust_coeffs, path_lengths, c=colours, s=100, alpha=0.5)
    for i in range(len(graph_titles)):
        xy = (clust_coeffs[i], path_lengths[i])
        xynew = (clust_coeffs[i]+rnd.uniform(-0.1,0.1), path_lengths[i]+rnd.uniform(-0.1,0.1))
        plt.annotate(
            graph_titles[i], xy, xynew,
            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'green', alpha = 0.5),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0')
        )
    plt.ylabel("Average Shortest Path")
    plt.xlabel("Average Clustering Coefficient")
    grid(True)
    plt.show()

def main():
    read_datafile(file_obj)
    plot_data()
if __name__ == "__main__":
    main()