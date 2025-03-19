import matplotlib.pyplot as plt


def visualize_maze_with_path(maze, path, visit_maze):
    plt.figure(figsize=(len(maze[0]), len(maze)))  # 设置图形大小
    plt.imshow(maze, cmap='Greys', interpolation='nearest')  # 使用灰度色图，并关闭插值

    # 绘制路径
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, marker='o',
                 markersize=8, color='red', linewidth=3)

    for node in visit_maze:
        plt.text(node[1], node[0], '■', color='yellow', alpha=0.5,
                 fontsize=73, ha='center', va='center')
    # 设置坐标轴刻度和边框
    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))
    plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=2)

    plt.axis('on')  # 显示坐标轴
    plt.show()


if __name__ == "__main__":
    # 提供迷宫的二维数组
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]

    # 假设给定路径的坐标列表
    path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2),
            (2, 3), (2, 4), (3, 4), (4, 4)]
    visit_list = [
        (0, 0)
    ]
    # 可视化迷宫及路径
    visualize_maze_with_path(maze, path, visit_list)
