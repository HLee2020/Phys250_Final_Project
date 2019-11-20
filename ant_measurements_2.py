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

# lattice = random_lattice(201, 201)
# lattice, x, y, orient, count = ant_walk(lattice, 100, 100, 0, 100000000)
# plotlattice(lattice, x, y, orient, count)

def checker_lattice(y, x):
    '''only good with odd number of y and x'''
    lattice = normal_lattice(y, x, 1)
    # print(lattice)
    count = 0
    for i in range(y):
        for j in range(x):
            if count%2 == 0:
                lattice[i][j] *= -1
                # print("even")
                count += 1
            else:
                # print("odd")
                count += 1
    # print(lattice)
    return lattice


# lattice = checker_lattice(101, 101)
# steps = 5000
# counts, distance = distance_trend(50, 50, lattice, steps)
# plt.plot(counts, distance, marker=".")
# plt.title("Distance to Number of Steps for Checkered Initial Lattice")
# plt.ylabel("Distance from Starting Origin")
# plt.xlabel("Number of Steps Taken")
# plt.savefig("counts_distance_checker_"+str(counts)+".svg")
# plt.show()

lattice = random_lattice(101, 101)
steps = 5000
counts, distance = distance_trend(50, 50, lattice, steps)
plt.plot(counts, distance, marker=".")
plt.title("Distance to Number of Steps for Random Initial Lattice")
plt.ylabel("Distance from Starting Origin")
plt.xlabel("Number of Steps Taken")
plt.savefig("counts_distance_random_"+str(counts)+".svg")
plt.show()

# lattice = checker_lattice(101, 101)
# lattice, x, y, orient, count = ant_walk(lattice, 50, 50, 0, 10000)
# plotlattice(lattice, x, y, orient, count)
#
# lattice = checker_lattice(101, 101)
# lattice, x, y, orient, count = ant_walk(lattice, 20, 20, 0, 10000)
# plotlattice(lattice, x, y, orient, count)
#
# lattice = checker_lattice(100, 100)
# lattice, x, y, orient, count = ant_walk(lattice, 50, 50, 0, 10000)
# plotlattice(lattice, x, y, orient, count)
#
# lattice = checker_lattice(100, 100)
# lattice, x, y, orient, count = ant_walk(lattice, 50, 50, 1, 10000)
# plotlattice(lattice, x, y, orient, count)
