#!/usr/bin/env python

import matplotlib.pyplot as plt
import networkx as nx
from networkx import *
import time
import sys

t0 = time.clock()


def compute_clustering_coefficient(Directed_G, Undirected_G):
    return nx.average_clustering(Undirected_G)
    
def average_shortest_path(Directed_G, Undirected_G):
    t1 = time.clock()
    path_sum = 0
    num_paths = 0
    no_paths = 0
    counter = 0
    for node0 in Undirected_G:
        print("Computing average path length for node %i" % counter)
        counter += 1
        for node1 in Undirected_G:
            if (nx.has_path(Undirected_G, node0, node1) and node0 != node1):
                num_paths += 1
                sp = nx.shortest_path_length(Undirected_G, node0, node1)
                path_sum += sp
            else:
                no_paths += 1
        print("Node %i done:" % counter), "| Average path length:", path_sum / float(num_paths)
    t2 = time.clock()
    if (num_paths != 0):
        return (path_sum / float(num_paths))

def report_final_stats():
    t6 = time.clock()
    print '%f seconds elapsed in total\n' % (t6-t0)

def run_main():
    file = str(sys.argv[1])
    f = open(file, 'r')
    print "\nReading inputfile:", file, "..."
    
    edgelist = []
    for line in f.readlines():
        edgelist.append((int(line.split()[0]), int(line.split()[1])))
    
    
    Directed_G = nx.DiGraph(edgelist)
    Undirected_G = Directed_G.to_undirected()
    #plt.figure(figsize=(8,8))
    #nx.draw(Directed_G,pos=nx.spring_layout(Directed_G))
    #plt.draw()
    #time.sleep(0.1)

    # compute other things
    print "Number of nodes involved in network:", nx.number_of_nodes(Undirected_G)
    print "Number of edges:", nx.number_of_edges(Undirected_G)
    print "Average degree:", nx.number_of_edges(Undirected_G) / float(nx.number_of_nodes(Undirected_G))
    t0 = time.clock()
    print "Average clustering coefficient:", compute_clustering_coefficient(Directed_G, Undirected_G)
    print "Took:", time.clock() - t0, "seconds"
    t1 = time.clock()
    print "Average path length:", average_shortest_path(Directed_G, Undirected_G)
    print "Took:", time.clock() - t1, "seconds"
    print "Total time:", time.clock() - t0, "seconds"
           
    report_final_stats()
    counter += 1
    second_counter += 1
    
def main():
    run_main()
if __name__ == "__main__":
    main()
