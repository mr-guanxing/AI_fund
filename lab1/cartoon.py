import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate_maze_with_path(maze, path, visit_maze, interval=100):
    fig, ax = plt.subplots(figsize=(len(maze[0]), len(maze)))
    ax.set_xticks(range(len(maze[0])))
    ax.set_yticks(range(len(maze)))
    ax.set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    ax.imshow(maze, cmap='Greys', interpolation='nearest')

    visited_texts = []
    path_line, = ax.plot([], [], marker='o', markersize=8, color='red', linewidth=3)

    def update(frame):
        if frame < len(visit_maze):
            node = visit_maze[frame]
            t = ax.text(node[1], node[0], '■', color='yellow', alpha=0.5,
                        fontsize=73, ha='center', va='center')
            visited_texts.append(t)
        else:
            index = frame - len(visit_maze)
            if index < len(path):
                partial_path = path[:index + 1]
                path_x, path_y = zip(*partial_path)
                path_line.set_data(path_y, path_x)

        return visited_texts + [path_line]

    total_frames = len(visit_maze) + len(path)
    ani = animation.FuncAnimation(
        fig, update, frames=total_frames, interval=interval, blit=True, repeat=False
    )

    plt.axis('on')
    plt.show()

if __name__ == "__main__":
    maze = np.array([
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
])

    visit_maze = [(0,0), (1,0), (2,0), (2,1), (2,2), (3,2), (3,3)]
    path = [(0,0), (1,0), (2,0), (2,1), (2,2), (3,2), (3,3)]

    animate_maze_with_path(maze, path, visit_maze)
