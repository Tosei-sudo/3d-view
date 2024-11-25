# encoding: UTF-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class ploter:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_zlim(-10, 10)
    
    def plot(self, surface):
        x = surface.points[:, 0]
        y = surface.points[:, 1]
        z = surface.points[:, 2]
        self.ax.plot_trisurf(x, y, z, color=surface.color, alpha=1)
        self.ax.scatter(x, y, z, color='red')
    
    def show(self):
        plt.show()

class Surface:
    def __init__(self, points, color = (1,1,1), perforated_points = None):
        self.points = points
        self.color = color
        self.perforated_points = perforated_points


surfaces = [
    Surface(np.array([
        [0, 0, 0],
        [5, 0, 0],
        [5, 1, 0],
        [0, 1, 0],
    ]), (1,1,1)),
    Surface(np.array([
        [0, 5, 0],
        [5, 5, 0],
        [5, 4, 0],
        [0, 4, 0],
    ]), (1,1,1)),
    Surface(np.array([
        [1, 1, 0],
        [1, 4, 0],
        [0, 4, 0],
        [0, 1, 0],
    ]), (1,1,1)),
    Surface(np.array([
        [4, 1, 0],
        [4, 4, 0],
        [5, 4, 0],
        [5, 1, 0],
    ]), (1,1,1)),
    Surface(np.array([
        [1, 1, 0],
        [4, 1, 0],
        [4, 4, 0],
        [1, 4, 0],
    ]), (.8, .8, .8, 1)),
]

p = ploter()

for s in surfaces:
    p.plot(s)

p.show()