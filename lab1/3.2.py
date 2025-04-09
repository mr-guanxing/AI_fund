from maze_visualization import visualize_maze_with_path,generate_path,wall_representation,way_representation,swamp_representation
from cartoon import animate_maze_with_path
from generate_maze import generate_maze_with_path

def dfs(maze):
    direction_map = {(-1, 0): "u", (1, 0): "d", (0, -1): "l", (0, 1): "r"}

    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    goal = (rows - 1, cols - 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    visit_record = []
    stack = [(start, "")]
    visited.add(start)

    while stack:
        (x, y), path = stack.pop()
        visit_record.append((x, y))
        if (x, y) == goal:
            return len(path), path, visited ,visit_record
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



# n, m = map(int, input().split())
# maze = []

# for i in range(n):
#     input_list = input().strip().split()
#     maze.append([int(i) for i in input_list])

# maze = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0]
# ]
maze = generate_maze_with_path(10, 10, 0.3, 0.1)
result = dfs(maze)
path_list = generate_path(result[1])
visited = result[2]
visualize_maze_with_path(maze, path_list, visited)
visit_list= result[3]
animate_maze_with_path(maze, path_list, visit_list)
print(result[0])
