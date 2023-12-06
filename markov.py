import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def randomwalk1D(n):
    x, y = 0, 0
    timepoints = np.arange(n + 1)
    positions = [y]
    directions = [1, -1]
    for i in range(1, n + 1):
        y += random.choice(directions)
        positions.append(y)
    return timepoints, positions

def update_plot(num, time_data, pos_data, line, scatter):
    line.set_data(time_data[:num], pos_data[:num])
    scatter.set_offsets(np.column_stack((time_data[num-1], pos_data[num-1])))
    return line, scatter

n = 200
time_data, pos_data = randomwalk1D(n)

fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')
scatter = ax.scatter([], [], c='red', marker='o')

ax.set_xlim(0, max(time_data))
ax.set_ylim(min(pos_data) - 1, max(pos_data) + 1)
ax.set_title("Random Walk 1D - Dynamic Plot")

# Assign the animation to a variable
ani = animation.FuncAnimation(fig, update_plot, frames=len(time_data), fargs=(time_data, pos_data, line, scatter), blit=False, interval=10, repeat=False)

plt.show()