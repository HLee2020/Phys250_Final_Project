import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rng
from ant_walks import *

def distance(x_init, y_init, x_final, y_final):
    delta_x = (x_final-x_init)**2
    delta_y = (y_final-y_init)**2
    return (np.sqrt(delta_x+delta_y))

lattice = normal_lattice(101, 101, -1)
lattice, x, y, orient, count = ant_walk(lattice, 50, 50, 0, 10100)
plotlattice(lattice, x, y, count, orient)

lattice = normal_lattice(101, 101, -1)
lattice, x, y, orient, count = ant_walk(lattice, 50, 50, 0, 100000)
plotlattice(lattice, x, y, count, orient)
