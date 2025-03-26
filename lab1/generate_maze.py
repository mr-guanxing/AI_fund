import random


def generate_maze(rows, cols, wall_ratio=0.3, swamp_ratio=0.3):
    """
    生成一个迷宫
    :param rows: 迷宫的行数
    :param cols: 迷宫的列数
    :param wall_ratio: 墙壁的比例
    :param swamp_ratio: 泥潭的比例
    :return: 迷宫的二维列表
    """
    maze = [[0 for _ in range(cols)] for _ in range(rows)]

    # 确保起点和终点是道路
    maze[0][0] = 0
    maze[rows - 1][cols - 1] = 0

    # 随机生成墙壁和泥潭
    for i in range(rows):
        for j in range(cols):
            if (i, j) != (0, 0) and (i, j) != (rows - 1, cols - 1):
                if random.random() < wall_ratio:
                    maze[i][j] = 1
                elif random.random() < swamp_ratio:
                    maze[i][j] = 2

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
                and maze[nx][ny] == 0
            ):
                visited.add((nx, ny))
                stack.append(((nx, ny), path + direction_map[(dx, dy)]))
    return False


def generate_maze_with_path(rows, cols):
    while True:
        maze = generate_maze(rows, cols)
        if dfs(maze):
            return maze


if __name__ == "__main__":
    # 设置迷宫的大小
    rows, cols = 10, 10

    # 生成迷宫
    maze = generate_maze_with_path(rows, cols)


    # 打印迷宫
    for row in maze:
        print(row)
