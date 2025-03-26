from maze_visualization import cost_for_swamp,visualize_maze_with_path,generate_path,wall_representation,way_representation,swamp_representation
from generate_maze import generate_maze_with_path
import heapq


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def a_star(maze):
    direction_map = {(-1, 0): "u", (1, 0): "d", (0, -1): "l", (0, 1): "r"}
    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    goal = (rows - 1, cols - 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    priority_queue = [(manhattan_distance(start, goal), start, "")]
    cost_dic = {start: manhattan_distance(start, goal)}

    while priority_queue:
        current_cost, (x, y), path = heapq.heappop(priority_queue)
        if (x, y) in visited:
            continue
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
                new_cost = (
                    current_cost
                    + 1
                    - manhattan_distance((x, y), goal)
                    + manhattan_distance((nx, ny), goal)
                )
                if (nx, ny) not in cost_dic or new_cost < cost_dic[(nx, ny)]:
                    cost_dic[(nx, ny)] = new_cost
                    heapq.heappush(
                        priority_queue,
                        (new_cost, (nx, ny), path + direction_map[(dx, dy)]),
                    )
            elif (
                0 <= nx < rows
                and 0 <= ny < cols
                and maze[nx][ny] == swamp_representation()
                and 0 <= nx + dx < rows
                and 0 <= ny + dy < cols
                and maze[nx + dx][ny + dy] == way_representation()
                and (nx + dx, ny + dy) not in visited
            ):
                new_cost = (
                    current_cost
                    + cost_for_swamp()
                    - manhattan_distance((x, y), goal)
                    + manhattan_distance((nx + dx, ny + dy), goal)
                )
                if (nx + dx, ny + dy) not in cost_dic or new_cost < cost_dic[
                    (nx + dx, ny + dy)
                ]:
                    cost_dic[(nx + dx, ny + dy)] = new_cost
                    heapq.heappush(
                        priority_queue,
                        (
                            new_cost,
                            (nx + dx, ny + dy),
                            path + "j" + direction_map[(dx, dy)],
                        ),
                    )


maze = generate_maze_with_path(10, 10)
# maze = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0],
#     [0, 1, 0, 2, 0],
#     [0, 0, 0, 1, 0],
# ]

result = a_star(maze)
path_list = generate_path(result[1])
visited = result[2]
length = len(result[1]) - result[1].count("j")
print(length)
visualize_maze_with_path(maze, path_list, visited)

