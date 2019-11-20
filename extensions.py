import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rng
from ant_walks import *
from ant_measurements import *

def spiral(lattice, x_init, y_init, steps, state, orient):
    x = x_init
    y = y_init
    x_list = [x]
    y_list = [y]
    lattice_y = len(lattice)
    lattice_x =len(lattice[0])
    edge = False
    count = 0
    while count <= steps and edge == False:
        if state == 0:
            if lattice[y][x] == -1:
                lattice[y][x] *= -1
                x, y = orientated_step(orient, x, y)
                x_list.append(x)
                y_list.append(y)
                if y >= lattice_y:
                    edge = True
                state = 1
            elif lattice[y][x] == 1:
                if orient == 0:
                    orient = 3
                else:
                    orient -= 1
                x, y = orientated_step(orient, x, y)
                x_list.append(x)
                y_list.append(y)
                if x <= 0:
                    edge == True
                state = 0
        elif state == 1:
            if lattice[y][x] == -1:
                if orient == 3:
                    orient = 0
                else:
                    orient += 1
                lattice[y][x] *= -1
                x, y = orientated_step(orient, x, y)
                x_list.append(x)
                y_list.append(y)
                if x >= lattice_x:
                    edge = True
                state = 1
            elif lattice[y][x] == 1:
                lattice[y][x] *= -1
                x, y = orientated_step(orient, x, y)
                x_list.append(x)
                y_list.append(y)
                if y >= lattice_y:
                    edge = True
                state = 0
        # plt.imshow(lattice)
        # plt.pause(0.00001)
        # plt.clf()
        count += 1
    return (lattice, x, y, count, state, x_list, y_list)

def plotlattice_spiral(lattice, x, y, count, state):
    plt.imshow(lattice, origin="lower", cmap='Blues', vmin=-1, vmax=1)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Spiral Variation of Langton's Ant, Iteration Number: {}".format(count))
    plt.colorbar()
    plt.savefig("ant_walk_spiral_"+str(count)+".svg")
    plt.show()

lattice = normal_lattice(201, 201, -1)
lattice, x, y, count, state, x_list, y_list = spiral(lattice, 101, 101, 10000, 0, 0)
plotlattice_spiral(lattice, x, y, count, state)

# lattice, x, y, count, state, x_list, y_list = spiral(lattice, 25, 25, 1000, 0, 0)
# plotlattice_spiral(lattice, x, y, count, state)

# lattice, x, y, count, state, x_list, y_list = spiral(lattice, 101, 101, 2000, 0, 0)
# plotlattice_spiral(lattice, x, y, count, state)

distance_list = [distance(51, 51, i, j) for i,j in zip(x_list, y_list)]
plt.plot(range(len(distance_list)), distance_list)
plt.title("Distance to Number of Steps, Spiral Pattern with "+str(count)+" Steps")
plt.ylabel("Distance")
plt.xlabel("Number of Steps")
plt.savefig("spiral_distance_"+str(count)+".svg")
plt.show()
