import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rng
from ant_walks import *

def distance(x_init, y_init, x_final, y_final):
    delta_x = (x_final-x_init)**2
    delta_y = (y_final-y_init)**2
    return (np.sqrt(delta_x+delta_y))

def distance_trend(x_init, y_init, lattice_init, steps):
    orient_final = 0
    lattice_final, x_final, y_final, orient_final, count, x_list, y_list = ant_walk_history(lattice_init, x_init, y_init, 0, steps)
    distance_list = [distance(x_init, y_init, i, j) for i,j in zip(x_list, y_list)]
    count_list = range(len(distance_list))
    # plotlattice(lattice_final, x_final, y_final, orient_final, count)
    return count_list, distance_list

lattice = normal_lattice(101, 101, -1)
steps = 5000
counts, distance = distance_trend(50, 50, lattice, steps)
plt.plot(counts, distance, marker=".")
plt.title("Quantifying Langton's Ant Behavior Up to {}".format(steps))
plt.ylabel("Distance from Starting Origin")
plt.xlabel("Number of Steps Taken")
plt.savefig("counts_distance_"+str(steps)+".svg")
plt.show()

# lattice = normal_lattice(101, 101, -1)
# lattice, x, y, orient, count = ant_walk(lattice, 50, 50, 0, 970)
# plotlattice(lattice, x, y, orient, count)

# lattice = normal_lattice(21, 21, -1)
# lattice, x, y, orient, count = ant_walk(lattice, 10, 10, 0, 50)
# plotlattice(lattice, x, y, count, orient)
#
# lattice = normal_lattice(41, 41, -1)
# lattice, x, y, orient, count = ant_walk(lattice, 20, 20, 0, 1000)
# plotlattice(lattice, x, y, count, orient)
#
# lattice = normal_lattice(60, 55, -1)
# lattice, x, y, orient, count = ant_walk(lattice, 30, 30, 0, 10100)
# plotlattice(lattice, x, y, count, orient)
#
# lattice = normal_lattice(101, 101, -1)
# lattice, x, y, orient, count = ant_walk(lattice, 50, 50, 0, 100000)
# plotlattice(lattice, x, y, count, orient)
#
# lattice = normal_lattice(101, 101, 1)
# lattice, x, y, orient, count = ant_walk(lattice, 50, 50, 0, 100000)
# plotlattice(lattice, x, y, count, orient)
