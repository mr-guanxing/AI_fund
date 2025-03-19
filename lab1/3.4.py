from maze_visualization import visualize_maze_with_path
import heapq


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def a_star(maze):
    direction_map = {
        (-1, 0): 'u',
        (1, 0): 'd',
        (0, -1): 'l',
        (0, 1): 'r'
    }
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
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                new_cost = current_cost + 1 - \
                    manhattan_distance((x, y), goal) + \
                    manhattan_distance((nx, ny), goal)
                if (nx, ny) not in cost_dic or new_cost < cost_dic[(nx, ny)]:
                    cost_dic[(nx, ny)] = new_cost
                    heapq.heappush(priority_queue, (new_cost,
                                   (nx, ny), path + direction_map[(dx, dy)]))


def generate_path(path_str):
    last = (0, 0)
    res_list = []
    res_list.append(last)
    direction_map = {
        'u': (-1, 0),
        'd': (1, 0),
        'l': (0, -1),
        'r': (0, 1)
    }

    for i in path_str:
        if i in direction_map:
            dx, dy = direction_map[i]
            last = (last[0] + dx, last[1] + dy)
            res_list.append(last)

    return res_list


maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

result = a_star(maze)
path_list = generate_path(result[1])
visited = result[2]

visualize_maze_with_path(maze, path_list, visited)
print(result[0])
