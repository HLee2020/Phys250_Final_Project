import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rng

# Define 1 as 'black' and -1 as 'white'
# Define orientation as 0 for north, 1 for east, 2 for south, 3 for west
# lattice[y][x] coordinate system

def normal_lattice(y, x, value):
    # N as x, M as y
    return np.full((y, x), value)

def random_lattice(y, x):
    return rng.choice((-1, 1), (y, x))

def plotlattice(lattice, x, y, orient, count):
    plt.imshow(lattice, origin="lower", cmap='Blues', vmin=-1, vmax=1)
    if orient == 0:
        plt.arrow(x, y-0.5, 0, 0.1, head_width=0.5, color="red")
    elif orient == 1:
        plt.arrow(x-0.5, y, 0.1, 0, head_width=0.5, color="red")
    elif orient == 2:
        plt.arrow(x, y+0.5, 0, -0.1, head_width=0.5, color="red")
    elif orient == 3:
        plt.arrow(x+0.5, y, -0.1, 0, head_width=0.5, color="red")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Lattice Visualization, Iteration Number: {}".format(count))
    plt.colorbar()
    plt.savefig("ant_walk_"+str(count)+".svg")
    plt.show()

def orientated_step(orient, x, y):
    if orient == 0:
        y += 1
    elif orient == 1:
        x += 1
    elif orient == 2:
        y -= 1
    elif orient == 3:
        x -= 1
    return (x, y)

def edge_check(lattice, x, y, orient):
    if orient == 0:
        if y == (len(lattice)-1):
            return False
    elif orient == 1:
        if x == (len(lattice[0])-1):
            return False
    elif orient == 2:
        if y == 0:
            return False
    elif orient == 3:
        if x == 0:
            return False
    return True

def ant_step(lattice, x, y, orient):
    if lattice[y][x] == -1:
        if orient == 3:
            orient = 0
        else:
            orient += 1
        if edge_check(lattice, x, y, orient) == False:
            print("Reached the Edge")
            return (lattice, x, y, None)
        lattice[y][x] *= -1
        x, y, = orientated_step(orient, x, y)
    else:
        if orient == 0:
            orient = 3
        else:
            orient -= 1
        if edge_check(lattice, x, y, orient) == False:
            print("Reached the Edge")
            return (lattice, x, y, None)
        lattice[y][x] *= -1
        x, y, = orientated_step(orient, x, y)
    return (lattice, x, y, orient)

def ant_walk(lattice, x, y, orient, iter):
    count = 0
    while count < iter and orient != None:
        past_lattice = lattice.copy()
        past_x = x
        past_y = y
        past_orient = orient
        lattice, x, y, orient = ant_step(lattice, x, y, orient)
        # plotlattice(lattice, x, y, count, orient)
        count += 1
    if orient == None:
        return lattice, x, y, past_orient, count
    else:
        return lattice, x, y, orient, count

def ant_walk_history(lattice, x, y, orient, iter):
    x_history = [x]
    y_history = [y]
    count = 0
    while count < iter and orient != None:
        lattice, x, y, orient = ant_step(lattice, x, y, orient)
        x_history.append(x)
        y_history.append(y)
        count += 1
    return lattice, x, y, orient, count, x_history, y_history
