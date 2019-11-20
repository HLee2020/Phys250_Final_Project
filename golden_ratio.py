import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rng
from ant_walks import *
from ant_measurements import *

def golden_ratio(lattice, x_init, y_init, steps, state, orient):
    x = x_init
    y = y_init
    x_list = [x]
    y_list = [y]
    lattice_y = len(lattice)
    lattice_x =len(lattice[0])
    edge = True
    count = 0
    while count <= steps and edge == True:
        if state == 0:
            if lattice[y][x] == -1:
                lattice[y][x] *= -1
                if orient == 0:
                    orient = 3
                else:
                    orient -= 1
                edge = edge_check(lattice, x, y, orient)
                x, y = orientated_step(orient, x, y)
                x_list.append(x)
                y_list.append(y)
                state = 1
            else:
                if orient == 0:
                    orient = 3
                else:
                    orient -= 1
                edge = edge_check(lattice, x, y, orient)
                x, y = orientated_step(orient, x, y)
                x_list.append(x)
                y_list.append(y)
                state = 1
        else:
            if lattice[y][x] == -1:
                lattice[y][x] *= -1
                if orient == 3:
                    orient = 0
                else:
                    orient += 1
                edge = edge_check(lattice, x, y, orient)
                x, y = orientated_step(orient, x, y)
                x_list.append(x)
                y_list.append(y)
                state = 1
            else:
                lattice[y][x] *= -1
                edge = edge_check(lattice, x, y, orient)
                x, y = orientated_step(orient, x, y)
                x_list.append(x)
                y_list.append(y)
                state = 0
        # plt.imshow(lattice)
        # plt.pause(0.00001)
        # plt.clf()
        count += 1
    return (lattice, x, y, count, state, x_list, y_list)

def plotlattice_golden(lattice, x, y, count, state):
    plt.imshow(lattice, origin="lower", cmap='Blues', vmin=-1, vmax=1)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Golden Ratio Variation of Langton's Ant, Iteration Number: {}".format(count))
    plt.colorbar()
    plt.savefig("ant_walk_golden_"+str(count)+".svg")
    plt.show()

lattice = normal_lattice(90, 90, -1)
lattice, x, y, count, state, x_list, y_list = golden_ratio(lattice, 40, 40, 5000, 0, 0)
plotlattice_golden(lattice, x, y, count, state)
#
# lattice = normal_lattice(350, 350, -1)
# lattice, x, y, count, state, x_list, y_list = golden_ratio(lattice, 150, 150, 4000, 0, 0)
# plotlattice_golden(lattice, x, y, count, state)

# lattice, x, y, count, state, x_list, y_list = spiral(lattice, 25, 25, 1000, 0, 0)
# plotlattice_spiral(lattice, x, y, count, state)

# lattice, x, y, count, state, x_list, y_list = spiral(lattice, 101, 101, 2000, 0, 0)
# plotlattice_spiral(lattice, x, y, count, state)

# distance_list = [distance(150, 150, i, j) for i,j in zip(x_list, y_list)]
# plt.plot(range(len(distance_list)), distance_list)
# plt.title("Distance to Number of Steps, Golden Ratio Pattern with "+str(count)+" Steps")
# plt.ylabel("Distance")
# plt.xlabel("Number of Steps")
# plt.savefig("golden_ratio_distance_"+str(count)+".svg")
# plt.show()
