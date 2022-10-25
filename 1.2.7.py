import numpy as np
import matplotlib.pyplot as plt

def save_plot(function, x_min, x_max, dots = 1000):
    x = np.arange(x_min, x_max, (x_max - x_min)/dots)
    plt.plot(x, eval(function))
    plt.savefig("output.png")
