# bfs
from maze_visualization import visualize_maze_with_path,generate_path,wall_representation,way_representation,swamp_representation
from queue import Queue


def bfs(maze):
    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    goal = (rows - 1, cols - 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    queue = Queue()
    queue.put((start, ""))
    while not queue.empty():
        (x, y), path = queue.get()
        visited.add((x, y))
        if (x, y) == goal:
            return len(path), path, visited

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and maze[nx][ny] == way_representation()
                and (nx, ny) not in visited
            ):
                queue.put(
                    (
                        (nx, ny),
                        path
                        + {(-1, 0): "u", (1, 0): "d", (0, -1): "l", (0, 1): "r"}[
                            (dx, dy)
                        ],
                    )
                )


# n, m = map(int, input().split())
# maze = []

# for i in range(n):
#     input_list = input().strip().split()
#     maze.append([int(i) for i in input_list])

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

# len(path), path, visited
result = bfs(maze)
path_list = generate_path(result[1])
visited = result[2]

visualize_maze_with_path(maze, path_list, visited)
print(result[0])
