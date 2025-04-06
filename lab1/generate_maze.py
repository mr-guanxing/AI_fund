import random
from maze_visualization import (
    cost_for_swamp,
    visualize_maze_with_path,
    generate_path,
    wall_representation,
    way_representation,
    swamp_representation,
)


def generate_maze(rows, cols, wall_ratio=0.2, swamp_ratio=0.2):

    assert wall_ratio+swamp_ratio<1
    maze = [[way_representation() for _ in range(cols)] for _ in range(rows)]

    maze[0][0] = way_representation()
    maze[rows - 1][cols - 1] = way_representation()

    for i in range(rows):
        for j in range(cols):
            if (i, j) != (0, 0) and (i, j) != (rows - 1, cols - 1):
                random_number = random.random()
                if random_number < wall_ratio:
                    maze[i][j] = wall_representation()
                elif wall_ratio < random.random() < wall_ratio + swamp_ratio:
                    maze[i][j] = swamp_representation()

    return maze


def dfs(maze):
    direction_map = {(-1, 0): "u", (1, 0): "d", (0, -1): "l", (0, 1): "r"}
    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    goal = (rows - 1, cols - 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    stack = [(start, "")]
    visited.add(start)

    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and (nx, ny) not in visited
                and maze[nx][ny] == way_representation()
            ):
                visited.add((nx, ny))
                stack.append(((nx, ny), path + direction_map[(dx, dy)]))
    return False


def generate_maze_with_path(rows, cols, wall_ratio=0.2, swamp_ratio=0.2):
    while True:
        maze = generate_maze(rows, cols, wall_ratio, swamp_ratio)
        if dfs(maze):
            return maze


if __name__ == "__main__":
    rows, cols = 10, 10

    maze = generate_maze_with_path(rows, cols)

    for row in maze:
        print(row)
